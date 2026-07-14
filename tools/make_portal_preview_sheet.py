from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
PORTAL = ROOT / "media" / "screenshots" / "portal"
OUT = ROOT / "media" / "screenshots" / "mise_deck_v1.5_portal_preview.png"

BG = (4, 2, 0)
AMBER = (255, 176, 0)
HOT = (255, 211, 106)
DIM = (155, 106, 32)
LINE = (93, 58, 0)


def font(size=24, bold=False):
    candidates = [
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


F_TITLE = font(34, True)
F_BODY = font(18)
F_LABEL = font(15, True)


def fit(img, w, h):
    src = img.copy()
    src.thumbnail((w, h), Image.Resampling.LANCZOS)
    canvas = Image.new("RGB", (w, h), BG)
    x = (w - src.width) // 2
    y = (h - src.height) // 2
    canvas.paste(src, (x, y))
    return canvas


def main():
    desktop = Image.open(PORTAL / "portal_desktop_overview.png").convert("RGB")
    mobile_home = Image.open(PORTAL / "portal_mobile_home.png").convert("RGB")
    mobile_editor = Image.open(PORTAL / "portal_mobile_editor.png").convert("RGB")
    mobile_backup = Image.open(PORTAL / "portal_mobile_backup.png").convert("RGB")

    W, H = 1780, 1200
    pad = 34
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.text((pad, 24), "Mise_Deck v1.5.0 // Browser portal preview", font=F_TITLE, fill=HOT)
    d.text((pad, 66), "Mobile-friendly local portal with recipe editing, backup and sharing workflow.", font=F_BODY, fill=DIM)

    desktop_box = (pad, 115, 1000, 665)
    desktop_fit = fit(desktop, desktop_box[2] - desktop_box[0], desktop_box[3] - desktop_box[1])
    img.paste(desktop_fit, (desktop_box[0], desktop_box[1]))
    d.rectangle(desktop_box, outline=LINE, width=2)
    d.text((desktop_box[0], desktop_box[3] + 10), "DESKTOP OVERVIEW", font=F_LABEL, fill=DIM)

    mobile_w, mobile_h = 292, 632
    x0 = 1040
    y0 = 115
    mobiles = [
        ("MOBILE LIBRARY", mobile_home),
        ("MOBILE EDITOR", mobile_editor),
        ("BACKUP MODAL", mobile_backup),
    ]
    for i, (label, shot) in enumerate(mobiles):
        x = x0 + (i % 2) * (mobile_w + 24)
        y = y0 + (i // 2) * (mobile_h + 58)
        shot_fit = fit(shot, mobile_w, mobile_h)
        img.paste(shot_fit, (x, y))
        d.rectangle((x, y, x + mobile_w, y + mobile_h), outline=LINE, width=2)
        d.text((x, y + mobile_h + 8), label, font=F_LABEL, fill=DIM)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()


