#!/usr/bin/env python3
"""Regenerate assets/htb.svg from live Hack The Box telemetry.

The card in this repo is parametric output, not hand-authored XML -- every
coordinate below is computed. Edit this generator, never the emitted SVG.

Public endpoints (no auth) supply everything except two fields:
    country rank  and  the XP / player-level track.
Those come from the authenticated API when HTB_TOKEN is set in the
environment; without it the generator falls back to XP_RANK_FALLBACK /
XP_LEVEL_FALLBACK and simply omits the country line.

Usage:
    python3 scripts/htb_sync.py            # write assets/htb.svg + patch README
    python3 scripts/htb_sync.py --dry-run  # print the telemetry, write nothing
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

UID = 212766
API = "https://labs.hackthebox.com/api/v4"
PROFILE_URL = f"https://app.hackthebox.com/users/{UID}"
UA = "Mozilla/5.0 (compatible; Aviral2642-profile-sync/1.0)"
BACKOFF = 15  # seconds; doubles per retry

# Used only when the authenticated API is unavailable.
XP_RANK_FALLBACK = "Prodigy III"
XP_LEVEL_FALLBACK = 89

ROOT = Path(__file__).resolve().parent.parent
SVG_PATH = ROOT / "assets" / "htb.svg"
README_PATH = ROOT / "README.md"

# ---------------------------------------------------------------- palette ---

BG = "#05070e"
CARD = "#0b0f1a"
EDGE = "#16203a"
GREEN = "#9fef00"          # Hack The Box signature
CYAN = "#00f0ff"
PINK = "#ff2d95"
PURPLE = "#7b2dff"
LILAC = "#c084fc"
AMBER = "#f5b942"
TEXT = "#e6edf7"
DIM = "#6b7a99"
FAINT = "#33415e"

W = 1200
MONO = ("'JetBrains Mono','Fira Code','SFMono-Regular',ui-monospace,"
        "Menlo,Consolas,monospace")

# Difficulty and category accents, so the eye can group without reading.
DIFF_COLOR = {"Easy": GREEN, "Medium": AMBER, "Hard": PINK, "Insane": LILAC}


# ------------------------------------------------------------------ fetch ---

def get(path: str, token: str | None = None, quiet: bool = False, tries: int = 4):
    """GET a JSON endpoint, backing off through Cloudflare's rate limiter.
    Returns None once the retries are spent -- an endpoint that stays down
    degrades the card rather than failing the workflow."""
    req = urllib.request.Request(
        f"{API}/{path}",
        headers={"User-Agent": UA, "Accept": "application/json",
                 **({"Authorization": f"Bearer {token}"} if token else {})},
    )
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as exc:
            # 1015 is Cloudflare's rate limit and clears on its own.
            retryable = exc.code in (429, 500, 502, 503, 504)
            if not retryable or attempt == tries - 1:
                if not quiet:
                    print(f"  ! {path}: HTTP {exc.code}", file=sys.stderr)
                return None
        except (urllib.error.URLError, ValueError, OSError) as exc:
            if attempt == tries - 1:
                if not quiet:
                    print(f"  ! {path}: {exc}", file=sys.stderr)
                return None
        delay = BACKOFF * (2 ** attempt)
        print(f"  · {path}: retrying in {delay}s", file=sys.stderr)
        time.sleep(delay)
    return None


def dig(obj, *keys, default=None):
    for k in keys:
        if not isinstance(obj, dict) or k not in obj:
            return default
        obj = obj[k]
    return obj


def find_key(obj, *names):
    """Depth-first search for the first of `names` present anywhere in a
    nested structure. The authenticated HTB payloads move these fields
    around between API revisions, so we look rather than assume."""
    stack = [obj]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            for n in names:
                if n in cur and cur[n] not in (None, ""):
                    return cur[n]
            stack.extend(cur.values())
        elif isinstance(cur, list):
            stack.extend(cur)
    return None


def collect(token: str | None) -> dict:
    print("fetching live telemetry ...")
    prof = dig(get(f"profile/{UID}"), "profile", default={}) or {}
    if not prof:
        raise SystemExit("fatal: public profile endpoint returned nothing")

    machines = dig(get(f"profile/progress/machines/{UID}"), "profile", default={}) or {}
    chals = dig(get(f"profile/progress/challenges/{UID}"), "profile", default={}) or {}
    sherlocks = dig(get(f"profile/progress/sherlocks/{UID}"), "profile", default={}) or {}
    forts = dig(get(f"profile/progress/fortress/{UID}"), "profile", "fortresses", default=[]) or []
    badges = dig(get(f"profile/badges/{UID}"), "badges", default=[]) or []

    country_rank = None
    xp_rank = XP_RANK_FALLBACK
    xp_level = XP_LEVEL_FALLBACK

    if token:
        # Country rank has no per-user endpoint -- it only exists as a position
        # inside the country leaderboard, so fetch the board and find ourselves.
        cc = prof.get("country_code", "US")
        board = get(f"rankings/country/{cc}/members", token)
        for row in (dig(board, "data", "rankings", default=[]) or []):
            if isinstance(row, dict) and row.get("id") == UID:
                country_rank = row.get("rank")
                break
        print(f"  · country rank: {country_rank or 'not on the board'}")

        # The XP / player-level track is not on any v4 route we can reach.
        # Look for it anyway -- if HTB ever surfaces it, the card picks it up
        # with no code change.
        basic = get(f"user/profile/basic/{UID}", token) or {}
        lvl = find_key(basic, "level", "player_level", "current_level")
        lvl_name = find_key(basic, "level_title", "level_name", "player_rank",
                            "xp_rank", "tier_name")
        if isinstance(lvl, dict):
            lvl_name = lvl_name or lvl.get("name") or lvl.get("title")
            lvl = lvl.get("level") or lvl.get("grade") or lvl.get("value")
        if lvl:
            xp_level = lvl
        if lvl_name:
            xp_rank = str(lvl_name)

    # Environment overrides win -- lets the workflow pin a value HTB stops
    # exposing without editing this file.
    country_rank = os.environ.get("HTB_COUNTRY_RANK") or country_rank
    xp_rank = os.environ.get("HTB_XP_RANK") or xp_rank
    xp_level = os.environ.get("HTB_XP_LEVEL") or xp_level

    return {
        "handle": prof.get("name", "AviralxRoot"),
        "rank": prof.get("rank", "?"),
        "next_rank": prof.get("next_rank"),
        "rank_progress": prof.get("current_rank_progress", 0),
        "ownership": prof.get("rank_ownership", 0),
        "requirement": prof.get("rank_requirement", 0),
        "global_rank": prof.get("ranking"),
        "country_rank": country_rank,
        "country": prof.get("country_name", ""),
        "country_code": prof.get("country_code", ""),
        "points": prof.get("points", 0),
        "respects": prof.get("respects", 0),
        "user_owns": prof.get("user_owns", 0),
        "system_owns": prof.get("system_owns", 0),
        "joined": (prof.get("joined_date") or "")[:10],
        "xp_rank": xp_rank,
        "xp_level": xp_level,
        "machines": dig(machines, "machine_owns", default={}) or {},
        "difficulties": machines.get("machine_difficulties") or [],
        "chal_owns": dig(chals, "challenge_owns", default={}) or {},
        "categories": chals.get("challenge_categories") or [],
        "sherlock_tasks": sherlocks.get("solved_tasks", 0),
        "sherlock_owns": dig(sherlocks, "challenge_owns", default={}) or {},
        "fortresses": forts,
        "badges": len(badges),
        "synced": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
    }


# ------------------------------------------------------------------- draw ---

def esc(s) -> str:
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def tw(s, size, ls=0.0) -> float:
    """Advance width of a mono string. JetBrains Mono and every fallback in
    the stack are 0.6em-advance, so this is exact, not a guess."""
    return len(str(s)) * (0.6 * size + ls)


def txt(x, y, s, size=12, fill=TEXT, weight=400, anchor="start",
        ls=0, opacity=None, glow=None, cls=""):
    a = [f'x="{x:.1f}"', f'y="{y:.1f}"', f'class="m{(" " + cls) if cls else ""}"',
         f'font-size="{size}"', f'fill="{fill}"']
    if weight != 400:
        a.append(f'font-weight="{weight}"')
    if anchor != "start":
        a.append(f'text-anchor="{anchor}"')
    if ls:
        a.append(f'letter-spacing="{ls}"')
    if opacity is not None:
        a.append(f'opacity="{opacity}"')
    if glow:
        a.append(f'filter="url(#{glow})"')
    return f'<text {" ".join(a)}>{esc(s)}</text>'


def card(x, y, w, h, r=10, fill=CARD, stroke=EDGE, op=1.0):
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1" opacity="{op}"/>')


def corner(x, y, w, h, c=CYAN, n=13, op=0.75):
    """Four bracket ticks -- the HUD motif the other assets use."""
    o = []
    for (cx, cy, dx, dy) in ((x, y, 1, 1), (x + w, y, -1, 1),
                             (x, y + h, 1, -1), (x + w, y + h, -1, -1)):
        o.append(f'<path d="M{cx + dx * n:.1f} {cy:.1f} H{cx:.1f} V{cy + dy * n:.1f}" '
                 f'fill="none" stroke="{c}" stroke-width="1.4" opacity="{op}"/>')
    return "".join(o)


def bar(x, y, w, h, pct, grad="barG", delay=0.0, track=FAINT):
    """Horizontal meter that animates out from zero on load."""
    pct = max(0.0, min(100.0, float(pct)))
    fw = w * pct / 100.0
    return (
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h}" rx="{h/2:.1f}" '
        f'fill="{track}" opacity=".45"/>'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="0" height="{h}" rx="{h/2:.1f}" '
        f'fill="url(#{grad})">'
        f'<animate attributeName="width" from="0" to="{fw:.1f}" dur="1.3s" '
        f'begin="{delay:.2f}s" fill="freeze" calcMode="spline" '
        f'keySplines=".25 .1 .25 1" keyTimes="0;1" values="0;{fw:.1f}"/></rect>'
    )


def chip(x, y, label, value, accent):
    """Pill: dim label, bright value. Returns (svg, width)."""
    label, value = str(label), str(value)
    lw = tw(label, 10, 1.2)
    vw = tw(value, 12, 0.6)
    w = 14 + lw + 10 + vw + 14
    o = [f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="26" rx="13" '
         f'fill="{accent}" opacity=".10"/>',
         f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="26" rx="13" '
         f'fill="none" stroke="{accent}" stroke-width="1" opacity=".55"/>',
         txt(x + 14, y + 17.5, label, size=10, fill=DIM, ls=1.2),
         txt(x + 14 + lw + 10, y + 17.5, value, size=12, fill=accent,
             weight=700, ls=0.6)]
    return "".join(o), w


def layout(d: dict) -> dict:
    """Every y-coordinate in the card, derived once so the canvas can be
    sized to its content instead of the other way round."""
    cats = sorted((c for c in d["categories"] if c.get("total_flags")),
                  key=lambda c: (-c.get("owned_flags", 0), c["name"]))
    rows = -(-len(cats) // 2)          # ceil, two columns
    sy = 384                            # "CHALLENGE CATEGORIES" baseline
    by = sy + 34                        # first meter row
    rowh = 31
    fy = by + rows * rowh + 14          # footer rule
    return {"cats": cats, "rows": rows, "sy": sy, "by": by, "rowh": rowh,
            "rule_y": fy, "chip_y": fy + 22, "H": fy + 22 + 24 + 26}


def render(d: dict) -> str:
    L = layout(d)
    H = L["H"]
    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" '
        f'aria-label="Hack The Box live telemetry for {esc(d["handle"])}" '
        f'data-fp="{d["fp"]}">',
        "<defs>",
        # Double-merged glow for large type only.
        '<filter id="gM" x="-70%" y="-70%" width="240%" height="240%">'
        '<feGaussianBlur stdDeviation="4.5" result="b"/><feMerge>'
        '<feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/>'
        '</feMerge></filter>',
        # Single-merge, tighter radius: small mono text blooms into a bar
        # across the x-height with the double-merged filter.
        '<filter id="gT" x="-70%" y="-70%" width="240%" height="240%">'
        '<feGaussianBlur stdDeviation="1.5" result="b"/><feMerge>'
        '<feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>',
        f'<linearGradient id="barG" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{CYAN}"/><stop offset="60%" stop-color="{PURPLE}"/>'
        f'<stop offset="100%" stop-color="{PINK}"/></linearGradient>',
        f'<linearGradient id="htbG" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{GREEN}"/><stop offset="100%" stop-color="{CYAN}"/>'
        f'</linearGradient>',
        f'<linearGradient id="rule" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{W}" y2="0">'
        f'<stop offset="0%" stop-color="{GREEN}" stop-opacity="0"/>'
        f'<stop offset="22%" stop-color="{GREEN}" stop-opacity=".8"/>'
        f'<stop offset="55%" stop-color="{CYAN}" stop-opacity=".7"/>'
        f'<stop offset="80%" stop-color="{PINK}" stop-opacity=".6"/>'
        f'<stop offset="100%" stop-color="{PINK}" stop-opacity="0"/></linearGradient>',
        f'<radialGradient id="halo" cx="50%" cy="50%" r="50%">'
        f'<stop offset="0%" stop-color="{GREEN}" stop-opacity=".16"/>'
        f'<stop offset="100%" stop-color="{GREEN}" stop-opacity="0"/></radialGradient>',
        '<pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">'
        f'<path d="M34 0H0V34" fill="none" stroke="{EDGE}" stroke-width="1" opacity=".5"/>'
        '</pattern>',
        '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="1.3" fill="#000" opacity=".26"/></pattern>',
        f"<style>.m{{font-family:{MONO};}}"
        "@keyframes fin{from{opacity:0}to{opacity:1}}"
        ".fin{animation:fin .8s ease-out both;}"
        "</style>",
        "</defs>",
        f'<rect width="{W}" height="{H}" fill="{BG}"/>',
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity=".55"/>',
        f'<ellipse cx="150" cy="120" rx="420" ry="220" fill="url(#halo)"/>',
    ]

    # ---- header -------------------------------------------------------
    o.append(txt(30, 41, "HACK THE BOX", size=19, fill=GREEN, weight=700,
                 ls=6.5, glow="gM"))
    o.append(txt(268, 41, "// LIVE TELEMETRY", size=13, fill=DIM, ls=4))
    o.append(f'<circle cx="{W-262}" cy="36" r="4" fill="{GREEN}" filter="url(#gT)">'
             f'<animate attributeName="opacity" values="1;.15;1" dur="2.4s" '
             f'repeatCount="indefinite"/></circle>')
    o.append(txt(W - 248, 40, f"UPDATED {d['synced']}", size=11, fill=DIM, ls=1.4))
    o.append(f'<rect x="0" y="66" width="{W}" height="1.4" fill="url(#rule)"/>')
    o.append(f'<circle cy="66.7" r="3" fill="{GREEN}" filter="url(#gT)">'
             f'<animate attributeName="cx" values="-20;1220" dur="6s" repeatCount="indefinite"/>'
             f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.12;.88;1" '
             f'dur="6s" repeatCount="indefinite"/></circle>')

    # ---- hero row -----------------------------------------------------
    hy, hh = 86, 148
    ax, aw = 28, 452
    bx, bw = 496, 336
    cx, cw = 848, 324

    # identity
    o.append(card(ax, hy, aw, hh))
    o.append(corner(ax, hy, aw, hh, GREEN, 14, 0.5))
    mx, my = ax + 26, hy + 30
    o.append(f'<path d="M{mx+44:.1f} {my:.1f} L{mx+88:.1f} {my+25:.1f} '
             f'L{mx+88:.1f} {my+75:.1f} L{mx+44:.1f} {my+100:.1f} '
             f'L{mx:.1f} {my+75:.1f} L{mx:.1f} {my+25:.1f} Z" '
             f'fill="{GREEN}" opacity=".08" stroke="{GREEN}" stroke-width="1.4"/>')
    o.append(txt(mx + 44, my + 63, "A", size=44, fill=GREEN, weight=700,
                 anchor="middle", glow="gM"))
    tx = ax + 138
    o.append(txt(tx, hy + 52, d["handle"], size=29, fill=TEXT, weight=700, ls=0.5))
    o.append(txt(tx, hy + 74, f"joined {d['joined']}  ·  {d['respects']} respects",
                 size=11, fill=DIM, ls=0.8))
    c1, w1 = chip(tx, hy + 88, "POINT RANK", str(d["rank"]).upper(), GREEN)
    o.append(c1)
    c2, _ = chip(tx, hy + 120, "XP RANK",
                 f"{str(d['xp_rank']).upper()} · LVL {d['xp_level']}", LILAC)
    o.append(c2)

    # rank progress
    o.append(card(bx, hy, bw, hh))
    o.append(corner(bx, hy, bw, hh, AMBER, 14, 0.4))
    o.append(txt(bx + 22, hy + 30, "CLIMBING TO", size=10, fill=DIM, ls=3))
    o.append(txt(bx + 22, hy + 60, str(d["next_rank"] or "—").upper(), size=24,
                 fill=AMBER, weight=700, ls=1.6, glow="gM"))
    prog = float(d["rank_progress"] or 0)
    o.append(bar(bx + 22, hy + 78, bw - 44, 9, prog, delay=0.35))
    o.append(txt(bx + 22, hy + 108, f"{prog:g}% of the way there", size=11, fill=DIM))
    o.append(txt(bx + bw - 22, hy + 108,
                 f"ownership {float(d['ownership'] or 0):g}% / {float(d['requirement'] or 0):g}%",
                 size=11, fill=CYAN, anchor="end"))
    o.append(txt(bx + 22, hy + 130,
                 f"{d['user_owns']} user flags  ·  {d['system_owns']} root flags",
                 size=11, fill=DIM))

    # ranking
    o.append(card(cx, hy, cw, hh))
    o.append(corner(cx, hy, cw, hh, CYAN, 14, 0.45))
    o.append(txt(cx + 22, hy + 30, "GLOBAL", size=10, fill=DIM, ls=3))
    o.append(txt(cx + 22, hy + 74, f"#{d['global_rank']}", size=42, fill=CYAN,
                 weight=700, glow="gM"))
    o.append(f'<line x1="{cx+22}" y1="{hy+92}" x2="{cx+cw-22}" y2="{hy+92}" '
             f'stroke="{EDGE}" stroke-width="1"/>')
    if d["country_rank"]:
        o.append(txt(cx + 22, hy + 114, esc(d["country"] or d["country_code"]).upper(),
                     size=10, fill=DIM, ls=3))
        o.append(txt(cx + cw - 22, hy + 122, f"#{d['country_rank']}", size=28,
                     fill=PINK, weight=700, anchor="end", glow="gM"))
    else:
        o.append(txt(cx + 22, hy + 114, esc(d["country"] or d["country_code"]).upper(),
                     size=10, fill=DIM, ls=3))
        o.append(txt(cx + cw - 22, hy + 122, d["country_code"] or "—", size=24,
                     fill=PINK, weight=700, anchor="end"))
    # Two rank systems coexist on HTB; say which one this column is.
    o.append(txt(cx + 22, hy + 136, "points leaderboard  ·  live position",
                 size=10, fill=DIM, opacity=".75"))

    # ---- stat tiles ---------------------------------------------------
    ty, th = 252, 96
    tiles = [
        ("MACHINES", d["machines"].get("solved", 0),
         f"{d['machines'].get('total', 0)} live  ·  {d['machines'].get('completion_percentage', 0)}%", CYAN),
        ("CHALLENGES", d["chal_owns"].get("solved", 0),
         f"{d['chal_owns'].get('total', 0)} live  ·  {d['chal_owns'].get('percentage', 0)}%", PINK),
        ("SHERLOCK TASKS", d["sherlock_tasks"],
         f"{d['sherlock_owns'].get('solved', 0)} investigations closed", LILAC),
        ("FORTRESSES", f"{sum(1 for f in d['fortresses'] if f.get('completion_percentage') == 100)}/{len(d['fortresses'])}",
         "cleared to 100%", GREEN),
        ("POINTS", f"{d['points']:,}", "system + user", AMBER),
        ("BADGES", d["badges"], "unlocked", CYAN),
    ]
    n = len(tiles)
    gap = 12
    tilew = (W - 56 - gap * (n - 1)) / n
    for i, (label, value, sub, accent) in enumerate(tiles):
        x = 28 + i * (tilew + gap)
        o.append(card(x, ty, tilew, th))
        o.append(f'<rect x="{x:.1f}" y="{ty}" width="3" height="{th}" rx="1.5" '
                 f'fill="{accent}" opacity=".85"/>')
        o.append(txt(x + 18, ty + 26, label, size=10, fill=DIM, ls=2.2))
        o.append(txt(x + 18, ty + 62, value, size=29, fill=accent, weight=700,
                     glow="gT", cls="fin"))
        o.append(txt(x + 18, ty + 82, sub, size=10, fill=DIM))

    # ---- challenge categories ----------------------------------------
    sy = L["sy"]
    o.append(txt(30, sy, "CHALLENGE CATEGORIES", size=13, fill=GREEN, weight=700, ls=4))
    o.append(txt(272, sy, f"// {d['chal_owns'].get('solved', 0)} FLAGS ACROSS "
                          f"{len(d['categories'])} CATEGORIES", size=11, fill=DIM, ls=2))
    o.append(f'<line x1="30" y1="{sy+12}" x2="{W-30}" y2="{sy+12}" stroke="{EDGE}" '
             f'stroke-width="1"/>')

    cats, rows = L["cats"], L["rows"]
    colw = (W - 56 - 32) / 2
    rowh, by = L["rowh"], L["by"]
    for i, c in enumerate(cats):
        col, row = divmod(i, rows)
        x = 28 + col * (colw + 32)
        y = by + row * rowh
        pct = c.get("completion_percentage", 0)
        o.append(txt(x, y + 11, c["name"], size=12, fill=TEXT))
        meter_x = x + 128
        meter_w = colw - 128 - 96
        o.append(bar(meter_x, y + 3, meter_w, 8, pct, delay=0.5 + i * 0.05))
        o.append(txt(x + colw, y + 11,
                     f"{c.get('owned_flags', 0)}/{c.get('total_flags', 0)}",
                     size=11, fill=DIM, anchor="end"))
        o.append(txt(x + colw - 62, y + 11, f"{pct}%", size=11,
                     fill=GREEN if pct >= 50 else CYAN, anchor="end"))

    # ---- footer strip -------------------------------------------------
    o.append(f'<rect x="0" y="{L["rule_y"]:.1f}" width="{W}" height="1" '
             f'fill="url(#rule)" opacity=".7"/>')
    fy = L["chip_y"]

    o.append(txt(30, fy + 12, "FORTRESSES", size=10, fill=DIM, ls=2.4))
    fx = 138
    for f in d["fortresses"]:
        done = f.get("completion_percentage") == 100
        acc = GREEN if done else DIM
        label = f.get("name", "?")
        cw2 = 16 + tw(label, 11) + 16
        o.append(f'<rect x="{fx:.1f}" y="{fy:.1f}" width="{cw2:.1f}" height="24" rx="12" '
                 f'fill="{acc}" opacity="{".12" if done else ".05"}"/>')
        o.append(f'<rect x="{fx:.1f}" y="{fy:.1f}" width="{cw2:.1f}" height="24" rx="12" '
                 f'fill="none" stroke="{acc}" stroke-width="1" opacity="{".6" if done else ".25"}"/>')
        o.append(txt(fx + cw2 / 2, fy + 16, label, size=11,
                     fill=acc if done else DIM, weight=700 if done else 400,
                     anchor="middle"))
        fx += cw2 + 8

    o.extend(_right_align_legend(d["difficulties"], W - 30, fy))

    o.append(f'<rect width="{W}" height="{H}" fill="url(#scan)" opacity=".55"/>')
    o.append("</svg>")
    return "\n".join(o)


def _right_align_legend(diffs, right, fy):
    """Lay the difficulty legend out right-to-left with measured widths."""
    parts, x = [], right
    for diff in reversed(diffs):
        name = diff.get("name", "?")
        owned = diff.get("owned_machines", 0)
        total = diff.get("total_machines", 0)
        acc = DIFF_COLOR.get(name, CYAN)
        label = f"{name.upper()} {owned}/{total}"
        lw = tw(label, 11, 1)
        parts.append(txt(x, fy + 16, label, size=11, fill=acc, ls=1, anchor="end"))
        parts.append(f'<circle cx="{x - lw - 11:.1f}" cy="{fy+12:.1f}" r="3.4" '
                     f'fill="{acc}"/>')
        x -= lw + 30
    return parts


def fingerprint(d: dict) -> str:
    """Identity of a render: the telemetry, minus the wall clock, plus this
    generator's own source. Data moves -> new card. Layout code changes ->
    new card. Time passing on its own -> no commit."""
    payload = {k: v for k, v in d.items() if k not in ("synced", "fp")}
    h = hashlib.sha256(json.dumps(payload, sort_keys=True, default=str).encode())
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()[:12]


# ----------------------------------------------------------------- readme ---

START = "<!-- HTB:START -->"
END = "<!-- HTB:END -->"


def readme_block(d: dict, version: str) -> str:
    raw = ("https://raw.githubusercontent.com/Aviral2642/Aviral2642/main/"
           f"assets/htb.svg?v={version}")
    forts = sum(1 for f in d["fortresses"] if f.get("completion_percentage") == 100)
    country = (f" · **#{d['country_rank']}** in {d['country']}"
               if d["country_rank"] else "")
    return f"""{START}
<div align="center">
  <a href="{PROFILE_URL}"><img src="{raw}" alt="Hack The Box live telemetry — {esc(d['handle'])}" width="100%" /></a>
</div>

<div align="center">

<sub>`◈` <b>LIVE</b> — <a href="https://github.com/Aviral2642/Aviral2642/blob/main/.github/workflows/htb-sync.yml"><code>htb-sync.yml</code></a> re-reads the Hack The Box API every six hours and redraws this card whenever a number moves. Last change <b>{d['synced']}</b>.</sub>

</div>

> **{esc(d['handle'])}** — **{d['rank']}** on points, **{d['xp_rank']} · level {d['xp_level']}** on XP. Global **#{d['global_rank']}**{country}, **{d['points']:,}** points, **{d['user_owns']}** user and **{d['system_owns']}** root flags, **{d['chal_owns'].get('solved', 0)}** challenges, **{d['sherlock_tasks']}** Sherlock tasks, and **{forts}** fortresses cleared end to end. Nothing on this card is typed by hand.
{END}"""


def patch_readme(d: dict, version: str) -> bool:
    text = README_PATH.read_text()
    block = readme_block(d, version)
    if START in text and END in text:
        new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block,
                     text, flags=re.S)
    else:
        raise SystemExit(f"fatal: README is missing the {START} / {END} markers")
    if new == text:
        return False
    README_PATH.write_text(new)
    return True


# ------------------------------------------------------------------- main ---

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--out", default=None, help="write the SVG somewhere else")
    ap.add_argument("--force", action="store_true",
                    help="re-emit even when the fingerprint matches")
    args = ap.parse_args()

    d = collect(os.environ.get("HTB_TOKEN") or None)

    print(f"  {d['handle']}: {d['rank']} / {d['xp_rank']} lvl {d['xp_level']} · "
          f"global #{d['global_rank']} · country #{d['country_rank'] or '—'} · "
          f"{d['points']} pts")
    print(f"  machines {d['machines'].get('solved')} · "
          f"challenges {d['chal_owns'].get('solved')} · "
          f"sherlocks {d['sherlock_tasks']} · badges {d['badges']}")

    d["fp"] = fingerprint(d)
    out = Path(args.out) if args.out else SVG_PATH
    previous = out.read_text() if out.exists() else ""

    if args.dry_run:
        print(f"  (dry run) fp={d['fp']}, "
              f"{len(render(d)):,} bytes of SVG, nothing written")
        return 0

    if f'data-fp="{d["fp"]}"' in previous and not args.force:
        print(f"  unchanged (fp={d['fp']}) — nothing to commit")
        return 0

    svg = render(d)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg)

    # Cache-buster: GitHub's camo proxy keys on the full URL, so the README
    # link has to change or the old render is served for hours.
    version = hashlib.sha256(svg.encode()).hexdigest()[:8]
    changed_md = patch_readme(d, version)

    print(f"  wrote {out.relative_to(ROOT)} ({len(svg):,} bytes, "
          f"fp={d['fp']}, v={version}) readme_changed={changed_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
