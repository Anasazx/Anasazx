#!/usr/bin/env python3
"""Generates the Minecraft-style SVGs used in the profile README.

Run from the repo root:  python3 scripts/generate.py
No dependencies. Edit the CONTENT section below and re-run.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "assets")

# ---------------------------------------------------------------- CONTENT

CHAT = [
    [("Anasazx joined the game", "yellow")],
    [("<Anasazx> hey, I'm Anas - a full-stack developer", "white")],
    [("<Anasazx> backend: Java + Spring Boot, frontend: Angular", "white")],
    [("<Anasazx> currently building ", "white"), ("timetable-ai", "aqua")],
    [("<Anasazx> (photos of schedules -> real timetables w/ local LLMs)", "white")],
    [("Anasazx has made the advancement ", "white"), ("[Full-Stack Developer]", "green")],
    [("<Anasazx> open to collabs - DM me on X", "white")],
]
CHAT_INPUT = "/msg Anasazx let's build something"

# (simple-icons slug, display name, colour)
HOTBAR = [
    ("openjdk", "Java", "#ED8B00"),
    ("springboot", "Spring Boot", "#6DB33F"),
    ("angular", "Angular", "#DD0031"),
    ("typescript", "TypeScript", "#3178C6"),
    ("postgresql", "PostgreSQL", "#4169E1"),
    ("docker", "Docker", "#2496ED"),
    ("nodedotjs", "Node.js", "#5FA04E"),
    ("git", "Git", "#F05032"),
    ("linux", "Linux", "#FCC624"),
]

# (file name, sprite, header kind, title, description)
TOASTS = [
    ("toast-timetable-ai", "clock", "challenge", "Timetable AI", "Schedule photos to timetables"),
    ("toast-reviewhood", "book", "advancement", "ReviewHood", "Product review platform"),
    ("toast-orphan-care", "heart", "advancement", "Orphan Care System", "Records for an orphan charity"),
    ("toast-bus-tickets", "minecart", "advancement", "Bus Ticket Booking", "Angular + Node.js booking"),
]

# ---------------------------------------------------------------- FONT
# Rows are bottom-aligned on the baseline; glyphs in DESCENDERS drop one row.

FONT = {
    "A": ".###.|#...#|#...#|#####|#...#|#...#|#...#",
    "B": "####.|#...#|####.|#...#|#...#|#...#|####.",
    "C": ".###.|#...#|#....|#....|#....|#...#|.###.",
    "D": "####.|#...#|#...#|#...#|#...#|#...#|####.",
    "E": "#####|#....|###..|#....|#....|#....|#####",
    "F": "#####|#....|###..|#....|#....|#....|#....",
    "G": ".####|#....|#..##|#...#|#...#|#...#|.###.",
    "H": "#...#|#...#|#####|#...#|#...#|#...#|#...#",
    "I": "###|.#.|.#.|.#.|.#.|.#.|###",
    "J": "....#|....#|....#|....#|....#|#...#|.###.",
    "K": "#...#|#..#.|###..|#..#.|#...#|#...#|#...#",
    "L": "#....|#....|#....|#....|#....|#....|#####",
    "M": "#...#|##.##|#.#.#|#...#|#...#|#...#|#...#",
    "N": "#...#|##..#|#.#.#|#..##|#...#|#...#|#...#",
    "O": ".###.|#...#|#...#|#...#|#...#|#...#|.###.",
    "P": "####.|#...#|####.|#....|#....|#....|#....",
    "Q": ".###.|#...#|#...#|#...#|#...#|#..#.|.##.#",
    "R": "####.|#...#|####.|#...#|#...#|#...#|#...#",
    "S": ".####|#....|.###.|....#|....#|#...#|.###.",
    "T": "#####|..#..|..#..|..#..|..#..|..#..|..#..",
    "U": "#...#|#...#|#...#|#...#|#...#|#...#|.###.",
    "V": "#...#|#...#|#...#|#...#|#...#|.#.#.|..#..",
    "W": "#...#|#...#|#...#|#...#|#.#.#|##.##|#...#",
    "X": "#...#|.#.#.|..#..|.#.#.|#...#|#...#|#...#",
    "Y": "#...#|.#.#.|..#..|..#..|..#..|..#..|..#..",
    "Z": "#####|....#|...#.|..#..|.#...|#....|#####",
    "a": ".###.|....#|.####|#...#|.####",
    "b": "#....|#....|#.##.|##..#|#...#|#...#|####.",
    "c": ".###.|#...#|#....|#...#|.###.",
    "d": "....#|....#|.##.#|#..##|#...#|#...#|.####",
    "e": ".###.|#...#|#####|#....|.####",
    "f": "..##|.#..|####|.#..|.#..|.#..|.#..",
    "g": ".####|#...#|#...#|.####|....#|####.",
    "h": "#....|#....|#.##.|##..#|#...#|#...#|#...#",
    "i": "#|.|#|#|#|#|#",
    "j": "...#|....|...#|...#|...#|...#|#..#|.##.",
    "k": "#...|#...|#..#|#.#.|##..|#.#.|#..#",
    "l": "#.|#.|#.|#.|#.|#.|.#",
    "m": "##.#.|#.#.#|#.#.#|#...#|#...#",
    "n": "####.|#...#|#...#|#...#|#...#",
    "o": ".###.|#...#|#...#|#...#|.###.",
    "p": "#.##.|##..#|#...#|####.|#....|#....",
    "q": ".##.#|#..##|#...#|.####|....#|....#",
    "r": "#.##.|##..#|#....|#....|#....",
    "s": ".####|#....|.###.|....#|####.",
    "t": ".#..|####|.#..|.#..|.#..|..##",
    "u": "#...#|#...#|#...#|#...#|.####",
    "v": "#...#|#...#|#...#|.#.#.|..#..",
    "w": "#...#|#...#|#.#.#|#.#.#|.####",
    "x": "#...#|.#.#.|..#..|.#.#.|#...#",
    "y": "#...#|#...#|#...#|.####|....#|####.",
    "z": "#####|...#.|..#..|.#...|#####",
    "0": ".###.|#...#|#..##|#.#.#|##..#|#...#|.###.",
    "1": "..#..|.##..|..#..|..#..|..#..|..#..|#####",
    "2": ".###.|#...#|....#|..##.|.#...|#...#|#####",
    "3": ".###.|#...#|....#|..##.|....#|#...#|.###.",
    "4": "...##|..#.#|.#..#|#...#|#####|....#|....#",
    "5": "#####|#....|####.|....#|....#|#...#|.###.",
    "6": "..##.|.#...|#....|####.|#...#|#...#|.###.",
    "7": "#####|#...#|....#|...#.|..#..|..#..|..#..",
    "8": ".###.|#...#|#...#|.###.|#...#|#...#|.###.",
    "9": ".###.|#...#|#...#|.####|....#|...#.|.##..",
    " ": "...",
    ".": "#",
    ",": "#|#",
    ":": "#|.|.|.|#",
    "!": "#|#|#|#|#|.|#",
    "?": ".###.|#...#|....#|...#.|..#..|.....|..#..",
    "'": "#|#|.|.|.|.|.",
    "-": "#####|.....|.....",
    "+": "..#..|..#..|#####|..#..|..#..|.....",
    "/": "....#|....#|...#.|..#..|.#...|#....|#....",
    "<": "...#|..#.|.#..|#...|.#..|..#.|...#",
    ">": "#...|.#..|..#.|...#|..#.|.#..|#...",
    "[": "###|#..|#..|#..|#..|#..|###",
    "]": "###|..#|..#|..#|..#|..#|###",
    "(": "..#|.#.|#..|#..|#..|.#.|..#",
    ")": "#..|.#.|..#|..#|..#|.#.|#..",
    "_": "#####",
}
DESCENDERS = set("gjpqy,_")
GLYPH_H = 8  # 7 rows above baseline + 1 descender row

# Minecraft chat colours and their drop-shadow colours (rgb / 4)
COLORS = {
    "white": "#FFFFFF",
    "gray": "#AAAAAA",
    "yellow": "#FFFF55",
    "green": "#55FF55",
    "aqua": "#55FFFF",
    "purple": "#FF55FF",
}


def shadow_of(hex_color):
    r, g, b = (int(hex_color[i:i + 2], 16) // 4 for i in (1, 3, 5))
    return f"#{r:02X}{g:02X}{b:02X}"


def glyph(ch):
    if ch not in FONT:
        raise ValueError(f"no glyph for {ch!r}")
    rows = FONT[ch].split("|")
    top = 7 - len(rows) + (1 if ch in DESCENDERS else 0)
    return rows, top, len(rows[0])


def text_width(text):
    """Width in font pixels, including the 1px gap after each glyph."""
    return sum(glyph(c)[2] + 1 for c in text)


def segments_width(segments):
    return sum(text_width(t) for t, _ in segments)


def text_rects(text, x, y, px):
    """Rect list (x, y, w, h) for text drawn at (x, y) with px-sized font pixels."""
    rects = []
    for ch in text:
        rows, top, w = glyph(ch)
        for r, row in enumerate(rows):
            c = 0
            while c < len(row):
                if row[c] == "#":
                    start = c
                    while c < len(row) and row[c] == "#":
                        c += 1
                    rects.append((x + start * px, y + (top + r) * px, (c - start) * px, px))
                else:
                    c += 1
        x += (w + 1) * px
    return rects


def draw_text(segments, x, y, px, shadow=True):
    """SVG for coloured text segments with Minecraft's 1px drop shadow."""
    fg, bg = [], []
    for text, color in segments:
        hex_color = COLORS.get(color, color)
        rects = text_rects(text, x, y, px)
        if shadow:
            bg.append(f'<g fill="{shadow_of(hex_color)}">' + rect_path(rects, px, px) + "</g>")
        fg.append(f'<g fill="{hex_color}">' + rect_path(rects) + "</g>")
        x += text_width(text) * px
    return "".join(bg + fg)


def rect_path(rects, dx=0, dy=0):
    d = "".join(f"M{x + dx:g} {y + dy:g}h{w:g}v{h:g}h{-w:g}z" for x, y, w, h in rects)
    return f'<path d="{d}"/>'


def sprite(rows, palette, x, y, px):
    """Pixel-art sprite from rows of palette keys ('.' is transparent)."""
    by_color = {}
    for r, row in enumerate(rows):
        for c, key in enumerate(row):
            if key != ".":
                by_color.setdefault(palette[key], []).append((x + c * px, y + r * px, px, px))
    return "".join(f'<g fill="{color}">{rect_path(rects)}</g>' for color, rects in by_color.items())


def svg(width, height, body, style=""):
    style = f"<style>{style}</style>" if style else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" shape-rendering="crispEdges">{style}{body}</svg>\n')


def write(name, content):
    path = os.path.join(ASSETS, name)
    with open(path, "w") as f:
        f.write(content)
    print(f"wrote assets/{name} ({len(content) // 1024} KB)")


# ---------------------------------------------------------------- SPRITES

SPRITES = {
    "heart": ([
        ".kkk.kkk.",
        "krrrkrrrk",
        "krwrrrrrk",
        "krrrrrrrk",
        ".krrrrrd.",
        "..krrrd..",
        "...krd...",
        "....k....",
    ], {"k": "#1A0000", "r": "#E01E1E", "w": "#FFFFFF", "d": "#9E0B0B"}),
    "hunger": ([
        "....kkkk.",
        "...kblbbk",
        "..kbbbbbk",
        "..kbbbbbk",
        "..kbbbbk.",
        ".kwkkkk..",
        "kwwk.....",
        "kwk......",
        ".k.......",
    ], {"k": "#2B1300", "b": "#B5651D", "l": "#E8A25A", "w": "#EDE6D3"}),
    "clock": ([
        "...kkkk...",
        ".kkyyyykk.",
        ".kyccccyk.",
        "kycccKccyk",
        "kycccKccyk",
        "kyccKKKcyk",
        "kycccccyk.",
        ".kyccccyk.",
        ".kkyyyykk.",
        "...kkkk...",
    ], {"k": "#3A2A00", "y": "#E8B923", "c": "#F4EED8", "K": "#222222"}),
    "book": ([
        "kkkkkkkkk.",
        "kbbbbbbwwk",
        "kbyyyybwwk",
        "kbbbbbbwwk",
        "kbyyyybwwk",
        "kbbbbbbwwk",
        "kbbbbbbwwk",
        "kbbbbbbwwk",
        "kdddddddwk",
        "kkkkkkkkk.",
    ], {"k": "#1E0E08", "b": "#8B3A2B", "d": "#5E2219", "y": "#E8B923", "w": "#EEEEEE"}),
    "minecart": ([
        "..........",
        "..........",
        "kkkkkkkkkk",
        "kgggggggGk",
        "kgGGGGGGGk",
        "kgggggggGk",
        ".kgggggGk.",
        ".kkkkkkkk.",
        ".kdk..kdk.",
        "..k....k..",
    ], {"k": "#1C1C1C", "g": "#A8A8A8", "G": "#6E6E6E", "d": "#4A4A4A"}),
}


# ---------------------------------------------------------------- CHAT

def chat():
    px = 2
    pad_x, line_h = 8, 22
    width = max(max(segments_width(line) for line in CHAT), text_width(CHAT_INPUT + "_")) * px + pad_x * 2
    input_h = 26
    height = len(CHAT) * line_h + 10 + input_h

    body = []
    for i, line in enumerate(CHAT):
        y = i * line_h
        body.append(
            f'<g class="ln" style="animation-delay:{0.4 + i * 0.7:.1f}s">'
            f'<rect width="{width}" height="{line_h}" y="{y}" fill="#000" fill-opacity=".72"/>'
            + draw_text(line, pad_x, y + 4, px) + "</g>")

    # chat input bar: the command types itself out, then the cursor blinks
    iy = height - input_h
    start = 0.4 + len(CHAT) * 0.7 + 0.6
    widths = [text_width(CHAT_INPUT[:n]) * px for n in range(len(CHAT_INPUT) + 1)]
    values = ";".join(str(w) for w in widths)
    cursor_x = ";".join(str(pad_x + w) for w in widths)
    dur = len(CHAT_INPUT) * 0.06
    body.append(
        f'<rect y="{iy}" width="{width}" height="{input_h}" fill="#000" fill-opacity=".72"/>'
        f'<clipPath id="typed"><rect x="{pad_x}" y="{iy}" width="0" height="{input_h}">'
        f'<animate attributeName="width" values="{values}" begin="{start:.1f}s" dur="{dur:.2f}s" '
        f'calcMode="discrete" fill="freeze"/></rect></clipPath>'
        f'<g clip-path="url(#typed)">{draw_text([(CHAT_INPUT, "white")], pad_x, iy + 6, px)}</g>'
        f'<g class="cur"><g>{draw_text([("_", "white")], 0, iy + 6, px)}'
        f'<animateTransform attributeName="transform" type="translate" values="{cursor_x}" '
        f'begin="{start:.1f}s" dur="{dur:.2f}s" calcMode="discrete" fill="freeze"/></g></g>')
    # translate before typing starts
    body[-1] = body[-1].replace('<g class="cur"><g>', f'<g class="cur"><g transform="translate({pad_x})">')

    style = (
        ".ln{opacity:0;animation:in .35s ease-out forwards}"
        "@keyframes in{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}"
        ".cur{animation:blink 1s steps(1) infinite}"
        "@keyframes blink{50%{opacity:0}}")
    write("chat.svg", svg(width, height, "".join(body), style))


# ---------------------------------------------------------------- HOTBAR

def hotbar():
    with open(os.path.join(ROOT, "scripts", "icons.json")) as f:
        icons = json.load(f)

    u = 3                       # screen pixels per Minecraft GUI pixel
    slots = len(HOTBAR)
    bar_w = (slots * 20 + 2) * u
    width = bar_w + 4 * u       # room for the selector to overhang
    ox = 2 * u                  # hotbar x offset
    name_h, hud_h, xp_h = 22, 9 * u, 5 * u
    hud_y = name_h + 4
    xp_y = hud_y + hud_h + 2 * u
    bar_y = xp_y + xp_h + 3 * u
    height = bar_y + 22 * u + 2 * u

    body = []

    # held item name (one per slot, shown while selected)
    cycle = 1.6 * slots
    for i, (_, name, _) in enumerate(HOTBAR):
        tw = text_width(name) * 2
        frac = lambda k: f"{k / slots:.4f}"
        if i == 0:
            vals, times = "1;0", f"0;{frac(1)}"
        elif i == slots - 1:
            vals, times = "0;1", f"0;{frac(i)}"
        else:
            vals, times = "0;1;0", f"0;{frac(i)};{frac(i + 1)}"
        body.append(
            f'<g opacity="{1 if i == 0 else 0}">'
            f'<rect x="{(width - tw) // 2 - 6}" y="0" width="{tw + 10}" height="{name_h}" fill="#000" fill-opacity=".6"/>'
            f'{draw_text([(name, "white")], (width - tw) // 2, 4, 2)}'
            f'<animate attributeName="opacity" values="{vals}" keyTimes="{times}" dur="{cycle:.1f}s" '
            f'calcMode="discrete" repeatCount="indefinite"/></g>')

    # hearts (left) and hunger (right)
    heart_rows, heart_pal = SPRITES["heart"]
    hunger_rows, hunger_pal = SPRITES["hunger"]
    for k in range(10):
        body.append(sprite(heart_rows, heart_pal, ox + k * 8 * u, hud_y, u))
        body.append(sprite(hunger_rows, hunger_pal, ox + bar_w - (k + 1) * 8 * u - u, hud_y - u, u))

    # xp bar fills up once
    xw = bar_w - 2 * u
    body.append(
        f'<rect x="{ox + u}" y="{xp_y}" width="{xw}" height="{xp_h}" fill="#1E1E1E"/>'
        f'<rect x="{ox + 2 * u}" y="{xp_y + u}" width="0" height="{xp_h - 2 * u}" fill="#80FF20">'
        f'<animate attributeName="width" from="0" to="{int(xw * 0.72)}" begin=".3s" dur="2s" fill="freeze"/></rect>')
    for k in range(1, 18):
        body.append(f'<rect x="{ox + u + k * xw // 18}" y="{xp_y}" width="{u}" height="{xp_h}" fill="#1E1E1E"/>')

    # hotbar frame + slots
    body.append(f'<rect x="{ox}" y="{bar_y}" width="{bar_w}" height="{22 * u}" fill="#1B1B1B"/>')
    for i, (slug, name, color) in enumerate(HOTBAR):
        sx, sy = ox + (1 + i * 20) * u, bar_y + u
        body.append(
            # inventory-style slot: dark top/left edge, light bottom/right edge
            f'<rect x="{sx + u}" y="{sy + u}" width="{18 * u}" height="{18 * u}" fill="#FFFFFF"/>'
            f'<rect x="{sx + u}" y="{sy + u}" width="{17 * u}" height="{17 * u}" fill="#373737"/>'
            f'<rect x="{sx + 2 * u}" y="{sy + 2 * u}" width="{16 * u}" height="{16 * u}" fill="#8B8B8B"/>'
            # icon (24x24 path) scaled into 14x14 gui px, centred
            f'<g transform="translate({sx + 3 * u} {sy + 3 * u}) scale({14 * u / 24:.4f})" '
            f'shape-rendering="geometricPrecision">'
            f'<path d="{icons[slug]}" fill="{shadow_of(color)}" transform="translate(1.2 1.2)"/>'
            f'<path d="{icons[slug]}" fill="{color}"/></g>')

    # selector frame steps across the slots
    sel = 24 * u
    steps = ";".join(f"{i * 20 * u},0" for i in range(slots))
    body.append(
        f'<g><g transform="translate({ox - u} {bar_y - u})">'
        f'<rect width="{sel}" height="{sel}" fill="none" stroke="#000" stroke-width="{u}" '
        f'x="{u / 2}" y="{u / 2}" transform="translate(0 0)"/>'
        f'<path d="M{u} {u}h{sel - 2 * u}v{sel - 2 * u}h{-(sel - 2 * u)}z'
        f'M{3 * u} {3 * u}v{sel - 6 * u}h{sel - 6 * u}v{-(sel - 6 * u)}z" fill="#FFFFFF" fill-rule="evenodd"/>'
        f'<path d="M{2 * u} {2 * u}h{sel - 4 * u}v{sel - 4 * u}h{-(sel - 4 * u)}z'
        f'M{3 * u} {3 * u}v{sel - 6 * u}h{sel - 6 * u}v{-(sel - 6 * u)}z" fill="#A0A0A0" fill-rule="evenodd"/>'
        f'</g><animateTransform attributeName="transform" type="translate" values="{steps}" '
        f'dur="{cycle:.1f}s" calcMode="discrete" repeatCount="indefinite"/></g>')

    write("hotbar.svg", svg(width, height, "".join(body)))


# ---------------------------------------------------------------- TOASTS

def toast(name, sprite_key, kind, title, desc):
    u = 2
    w, h = 210, 44
    header = ("Challenge Complete!", "purple") if kind == "challenge" else ("Advancement Made!", "yellow")
    frame = "#C46CC4" if kind == "challenge" else "#C6C6C6"

    body = [
        # rounded-corner pixel frame
        f'<path d="M{u} 0h{(w - 2) * u}v{u}h{u}v{(h - 2) * u}h{-u}v{u}h{-(w - 2) * u}v{-u}h{-u}v{-(h - 2) * u}h{u}z" fill="#000"/>',
        f'<rect x="{u}" y="{u}" width="{(w - 2) * u}" height="{(h - 2) * u}" fill="{frame}"/>',
        f'<rect x="{2 * u}" y="{2 * u}" width="{(w - 4) * u}" height="{(h - 4) * u}" fill="#212121"/>',
        f'<rect x="{2 * u}" y="{2 * u}" width="{(w - 4) * u}" height="{u}" fill="#3A3A3A"/>',
    ]
    rows, pal = SPRITES[sprite_key]
    sp = 2 * u  # sprite pixel size
    sx = 8 * u
    sy = (h * u - len(rows) * sp) // 2
    body.append(sprite(rows, pal, sx, sy, sp))

    tx = 34 * u
    body.append(draw_text([header], tx, 7 * u, u))
    body.append(draw_text([(title, "white")], tx, 18 * u, u))
    body.append(draw_text([(desc, "gray")], tx, 29 * u, u))
    if 34 + max(text_width(desc), text_width(title), text_width(header[0])) > w - 4:
        raise ValueError(f"toast text too wide: {title}")

    style = ".t{animation:slide .6s cubic-bezier(.2,.9,.3,1.2) both}@keyframes slide{from{transform:translateX(420px)}}"
    write(f"{name}.svg", svg(w * u, h * u, f'<g class="t">{"".join(body)}</g>', style))


if __name__ == "__main__":
    chat()
    hotbar()
    for t in TOASTS:
        toast(*t)
