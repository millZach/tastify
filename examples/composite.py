"""Composite matched captures into pair images and a 2x3 grid.

Run: python3 composite.py   (expects captures/ beside this file)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).parent
CAP = HERE / "captures"
OUT = HERE
PAIRS = [("ember", "Ember"), ("foldline", "Foldline"), ("orrery", "Orrery")]
# Pairs that get pair images but stay out of the 2x3 grid.
EXTRA = [("redrising", "Red Rising"), ("pip", "Pip")]
LEFT, RIGHT = "Without skill", "With Tastify"
BG = (250, 249, 246)
INK = (28, 28, 26)
MUTED = (110, 108, 102)
RULE = (220, 218, 212)


def font(size, bold=False):
    for name in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/TTF/DejaVuSans.ttf",
    ):
        if Path(name).exists():
            return ImageFont.truetype(name, size)
    return ImageFont.load_default()


def fit(img, width):
    h = round(img.height * width / img.width)
    return img.resize((width, h), Image.LANCZOS)


def framed(img):
    """Thin rule around a capture so pale pages read as a screen."""
    out = Image.new("RGB", (img.width + 2, img.height + 2), RULE)
    out.paste(img, (1, 1))
    return out


def pair(slug, title, view):
    a = framed(fit(Image.open(CAP / f"{slug}-baseline-{view}.png").convert("RGB"), 1400 if view == "desktop" else 600))
    b = framed(fit(Image.open(CAP / f"{slug}-tastify-{view}.png").convert("RGB"), 1400 if view == "desktop" else 600))
    gap, pad, top, foot = 40, 40, 100, 90
    w = pad + a.width + gap + b.width + pad
    h = top + max(a.height, b.height) + foot
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    f_label, f_title = font(34, bold=True), font(24)
    d.text((pad, 34), LEFT, fill=INK, font=f_label)
    d.text((pad + a.width + gap, 34), RIGHT, fill=INK, font=f_label)
    sub = f"{title}  ·  GPT-6 Astra, same prompt, fresh context  ·  {'1440×900' if view == 'desktop' else '390×844'}"
    d.text((pad, h - foot + 30), sub, fill=MUTED, font=f_title)
    im.paste(a, (pad, top))
    im.paste(b, (pad + a.width + gap, top))
    path = OUT / f"{slug}-{view}-pair.png"
    im.save(path, optimize=True)
    print("saved", path, im.size)


def grid():
    cell_w = 900
    cells = {}
    for slug, _ in PAIRS:
        for cond in ("baseline", "tastify"):
            cells[(slug, cond)] = framed(fit(Image.open(CAP / f"{slug}-{cond}-desktop.png").convert("RGB"), cell_w))
    cell_h = max(c.height for c in cells.values())
    gap, pad, left, top = 36, 48, 400, 120
    w = left + 3 * cell_w + 2 * gap + pad
    h = top + 2 * cell_h + gap + pad
    im = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(im)
    f_col, f_row, f_sub = font(34, bold=True), font(36, bold=True), font(24)
    for i, (slug, title) in enumerate(PAIRS):
        x = left + i * (cell_w + gap)
        d.text((x, 48), title, fill=INK, font=f_col)
    for j, (cond, label) in enumerate((("baseline", LEFT), ("tastify", RIGHT))):
        y = top + j * (cell_h + gap)
        d.text((pad, y + 8), label, fill=INK, font=f_row)
        for i, (slug, _) in enumerate(PAIRS):
            im.paste(cells[(slug, cond)], (left + i * (cell_w + gap), y))
    note = "GPT-6 Astra, same brief per column, fresh context per cell, first screen at 1440×900"
    d.text((left, h - pad + 10), note, fill=MUTED, font=f_sub)
    path = OUT / "grid.png"
    im.save(path, optimize=True)
    print("saved", path, im.size)


if __name__ == "__main__":
    for slug, title in PAIRS + EXTRA:
        pair(slug, title, "desktop")
        pair(slug, title, "phone")
    grid()
