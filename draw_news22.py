#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: six world stories from Sunday
22 November 2026 in one 1024x1024 picture.

Pillow only, DejaVu fonts, no network, no clock: the same input always
renders the same bytes. Run: python3 draw_news22.py
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
NAVY = (12, 27, 46)
PANEL = (24, 46, 72)
INK = (238, 242, 247)
MUTED = (168, 184, 202)
GOLD = (232, 184, 66)
TICKER_BG = (10, 20, 34)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


BOLD = lambda s: font("DejaVuSans-Bold.ttf", s)
PLAIN = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Split text into lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def star_points(cx, cy, r_out, r_in, n=5):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = -math.pi / 2 + i * math.pi / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def draw_shield(d, x, y, s, color):
    d.polygon(
        [
            (x + s * 0.5, y),
            (x + s, y + s * 0.18),
            (x + s, y + s * 0.55),
            (x + s * 0.5, y + s),
            (x, y + s * 0.55),
            (x, y + s * 0.18),
        ],
        fill=color,
    )
    d.polygon(
        star_points(x + s * 0.5, y + s * 0.42, s * 0.22, s * 0.09),
        fill=(255, 255, 255),
    )


def draw_badge(d, x, y, s, color):
    d.polygon(star_points(x + s * 0.5, y + s * 0.5, s * 0.5, s * 0.21), fill=color)
    d.ellipse(
        [x + s * 0.36, y + s * 0.36, x + s * 0.64, y + s * 0.64],
        fill=(255, 255, 255),
    )
    d.text(
        (x + s * 0.5, y + s * 0.5),
        "!",
        font=BOLD(int(s * 0.34)),
        fill=color,
        anchor="mm",
    )


def draw_servers(d, x, y, s, color):
    for i in range(3):
        top = y + i * (s * 0.34)
        d.rounded_rectangle(
            [x, top, x + s, top + s * 0.28], radius=int(s * 0.05), fill=color
        )
        d.ellipse(
            [x + s * 0.08, top + s * 0.10, x + s * 0.16, top + s * 0.18],
            fill=(255, 255, 255),
        )
    d.polygon(
        [
            (x + s * 0.78, y + s * 0.62),
            (x + s * 1.02, y + s * 0.98),
            (x + s * 0.54, y + s * 0.98),
        ],
        fill=(232, 184, 66),
    )
    d.text(
        (x + s * 0.78, y + s * 0.88),
        "!",
        font=BOLD(int(s * 0.22)),
        fill=(12, 27, 46),
        anchor="mm",
    )


def draw_globe(d, x, y, s, color):
    d.ellipse([x, y, x + s, y + s], fill=color)
    d.ellipse([x + s * 0.08, y + s * 0.08, x + s * 0.92, y + s * 0.92], fill=NAVY)
    d.ellipse([x + s * 0.16, y + s * 0.16, x + s * 0.84, y + s * 0.84], fill=color)
    d.arc([x + s * 0.16, y + s * 0.16, x + s * 0.84, y + s * 0.84], 200, 340, fill=NAVY, width=4)
    d.line([x + s * 0.16, y + s * 0.5, x + s * 0.84, y + s * 0.5], fill=NAVY, width=4)
    d.ellipse(
        [x + s * 0.38, y + s * 0.16, x + s * 0.62, y + s * 0.84],
        outline=NAVY,
        width=4,
    )


def draw_ship(d, x, y, s, color):
    d.rectangle([x + s * 0.12, y + s * 0.10, x + s * 0.30, y + s * 0.34], fill=color)
    d.rectangle([x + s * 0.34, y + s * 0.10, x + s * 0.52, y + s * 0.34], fill=(255, 255, 255))
    d.rectangle([x + s * 0.56, y + s * 0.10, x + s * 0.74, y + s * 0.34], fill=color)
    d.polygon(
        [
            (x, y + s * 0.38),
            (x + s * 0.86, y + s * 0.38),
            (x + s * 0.72, y + s * 0.62),
            (x + s * 0.14, y + s * 0.62),
        ],
        fill=color,
    )
    for i, wx in enumerate((0.05, 0.38, 0.71)):
        d.arc(
            [x + s * wx, y + s * 0.72, x + s * (wx + 0.28), y + s * 0.98],
            180,
            360,
            fill=(255, 255, 255),
            width=5,
        )


def draw_ballot(d, x, y, s, color):
    d.polygon(
        [
            (x + s * 0.30, y),
            (x + s * 0.44, y),
            (x + s * 0.52, y + s * 0.30),
            (x + s * 0.38, y + s * 0.30),
        ],
        fill=(255, 255, 255),
    )
    d.rounded_rectangle(
        [x + s * 0.08, y + s * 0.30, x + s * 0.92, y + s * 0.92],
        radius=int(s * 0.06),
        fill=color,
    )
    d.line(
        [x + s * 0.30, y + s * 0.42, x + s * 0.70, y + s * 0.42],
        fill=(12, 27, 46),
        width=6,
    )
    d.text(
        (x + s * 0.5, y + s * 0.68),
        "✓",
        font=BOLD(int(s * 0.34)),
        fill=(255, 255, 255),
        anchor="mm",
    )


STORIES = [
    {
        "color": (62, 124, 177),
        "pic": draw_shield,
        "head": "NATO: 'Every inch of Poland'",
        "fact": "Rutte vows defence in Warsaw after Russian missiles and a drone land in Poland; Article 4 invoked.",
        "src": "THE TIMES · ASIATODAY · 22 NOV",
    },
    {
        "color": (192, 57, 43),
        "pic": draw_badge,
        "head": "'El Chapo Isidro' arrested",
        "fact": "Mexican drug lord on the FBI's 10 Most Wanted list captured in a shoot-out.",
        "src": "BBC · 22 NOV",
    },
    {
        "color": (230, 126, 34),
        "pic": draw_servers,
        "head": "FBI probes database hack",
        "fact": "Apparent breach of the National Crime Information Center under investigation.",
        "src": "BBC · 22 NOV",
    },
    {
        "color": (39, 174, 96),
        "pic": draw_globe,
        "head": "COP31 deadlocked on fossil fuels",
        "fact": "Nearly 200 nations stuck in Antalya as the fossil-fuel fight blocks a deal.",
        "src": "BBC · 21 NOV",
    },
    {
        "color": (22, 160, 133),
        "pic": draw_ship,
        "head": "Iran: Hormuz reopening in 2 days",
        "fact": "Tehran shortens its plan; IRGC claims strikes on two US Patriot radars.",
        "src": "ANI · WAITWHATNEWS · 22 NOV",
    },
    {
        "color": (142, 68, 173),
        "pic": draw_ballot,
        "head": "Democrats retake Congress",
        "fact": "Resurgent midterm win against the Republicans; milestone wins for African leaders.",
        "src": "C54 · 22 NOV",
    },
]

TICKER = (
    "ALSO TODAY  ·  Myanmar 4.1 quake  ·  TikTok launches deepfake detector  ·  "
    "Norway court voids disputed oil licences  ·  Kenya discharges last Ebola patient  ·  "
    "Japan–India defence pact"
)


def draw_panel(d, story, px, py, pw, ph):
    d.rounded_rectangle([px, py, px + pw, py + ph], radius=14, fill=PANEL)
    d.rounded_rectangle([px, py, px + pw, py + 10], radius=5, fill=story["color"])
    d.rectangle([px, py + 5, px + pw, py + 10], fill=story["color"])
    story["pic"](d, px + 18, py + 28, 104, story["color"])
    head_lines = wrap(d, story["head"], BOLD(29), pw - 158)[:2]
    hy = py + 30
    for line in head_lines:
        d.text((px + 138, hy), line, font=BOLD(29), fill=INK)
        hy += 36
    fact_lines = wrap(d, story["fact"], PLAIN(21), pw - 36)[:3]
    fy = py + 144
    for line in fact_lines:
        d.text((px + 18, fy), line, font=PLAIN(21), fill=MUTED)
        fy += 26
    d.text((px + 18, py + ph - 24), story["src"], font=PLAIN(15), fill=(120, 140, 164))


def main():
    img = Image.new("RGB", (W, H), NAVY)
    d = ImageDraw.Draw(img)

    # Masthead.
    d.rectangle([0, 0, W, 118], fill=(8, 18, 32))
    d.rectangle([0, 118, W, 124], fill=GOLD)
    d.text((28, 26), "THE WORLD IN ONE IMAGE", font=BOLD(44), fill=INK)
    d.text((28, 78), "SUNDAY · 22 NOVEMBER 2026", font=PLAIN(22), fill=MUTED)
    d.text((W - 28, 30), "make.fun · $100", font=BOLD(24), fill=GOLD, anchor="ra")
    d.text((W - 28, 66), "SIX STORIES · ONE PICTURE", font=PLAIN(18), fill=MUTED, anchor="ra")

    # Six panels: 2 columns x 3 rows.
    margin, gap = 16, 14
    pw = (W - 2 * margin - gap) // 2
    ph = 252
    top = 140
    for i, story in enumerate(STORIES):
        col, row = i % 2, i // 2
        px = margin + col * (pw + gap)
        py = top + row * (ph + gap)
        draw_panel(d, story, px, py, pw, ph)

    # Ticker.
    d.rectangle([0, 934, W, H], fill=TICKER_BG)
    d.rectangle([0, 934, W, 938], fill=GOLD)
    tick_lines = wrap(d, TICKER, PLAIN(20), W - 56)
    ty = 950
    for line in tick_lines:
        d.text((28, ty), line, font=PLAIN(20), fill=(200, 212, 226))
        ty += 26

    img.save(OUT, format="PNG")
    print("wrote {} ({} bytes)".format(OUT, os.path.getsize(OUT)))


if __name__ == "__main__":
    main()
