from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "screenshots" / "cardputer"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 240, 135
SCALE = 5
BG = (4, 2, 0)
PANEL = (18, 9, 0)
AMBER = (255, 176, 0)
HOT = (255, 211, 106)
DIM = (155, 106, 32)
LINE = (93, 58, 0)
RED = (255, 90, 54)


def font(size=8, bold=False):
    candidates = [
        "C:/Windows/Fonts/consolab.ttf" if bold else "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size * SCALE)
    return ImageFont.load_default()


F_TINY = font(5)
F_SMALL = font(6)
F_BODY = font(7)
F_BODY_B = font(7, True)
F_BIG = font(11, True)
F_HUGE = font(15, True)


def xy(v):
    if isinstance(v, tuple):
        return tuple(int(x * SCALE) for x in v)
    return int(v * SCALE)


def text(draw, pos, value, fill=AMBER, f=F_BODY, anchor=None):
    draw.text(xy(pos), value, font=f, fill=fill, anchor=anchor)


def rect(draw, box, outline=LINE, fill=None, width=1):
    draw.rectangle(tuple(xy(v) for v in box), outline=outline, fill=fill, width=width * SCALE)


def line(draw, points, fill=LINE, width=1):
    draw.line([xy(p) for p in points], fill=fill, width=width * SCALE)


def base():
    img = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    d = ImageDraw.Draw(img)
    for y in range(0, H, 3):
        d.line([(0, y * SCALE), (W * SCALE, y * SCALE)], fill=(9, 5, 0), width=1)
    return img, d


def finish(img):
    glow = Image.new("RGB", img.size, (0, 0, 0))
    mask = Image.new("L", img.size, 0)
    mp = mask.load()
    pix = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pix[x, y]
            if r > 80 and g > 40:
                mp[x, y] = 80
    glow = Image.composite(Image.new("RGB", img.size, AMBER), glow, mask.filter(ImageFilter.GaussianBlur(3 * SCALE)))
    img = Image.blend(glow, img, 0.82)
    return img


def header(d, title, battery="92%"):
    text(d, (4, 3), title, HOT, F_SMALL)
    text(d, (218, 3), battery, HOT, F_SMALL)
    line(d, [(3, 14), (237, 14)], LINE)


def footer(d, value=";/ . MOVE   OK SELECT   ` BACK"):
    line(d, [(3, 121), (237, 121)], LINE)
    text(d, (5, 124), value, DIM, F_TINY)


def menu_screen(title, items, selected=0, footer_text=";/ . MOVE   OK SELECT   ` BACK"):
    img, d = base()
    header(d, title)
    count = len(items)
    step = 22 if count <= 4 else 18 if count <= 5 else 17
    box_h = 18 if count <= 4 else 16
    y = 23 if count <= 4 else 22
    for i, item in enumerate(items):
        fill = PANEL if i == selected else None
        outline = AMBER if i == selected else LINE
        rect(d, ((11, y - 3), (229, y - 3 + box_h)), outline=outline, fill=fill)
        prefix = ">" if i == selected else " "
        text(d, (18, y), f"{prefix} {item}", HOT if i == selected else AMBER, F_BODY_B if i == selected else F_BODY)
        y += step
    footer(d, footer_text)
    return finish(img)


def opening():
    img, d = base()
    text(d, (120, 36), "Mise_Deck", HOT, F_HUGE, anchor="mm")
    text(d, (120, 64), '"A pocket mise en place"', AMBER, F_BODY, anchor="mm")
    text(d, (120, 78), "for the Cardputer", AMBER, F_BODY, anchor="mm")
    text(d, (208, 119), "OK ENTER", DIM, F_TINY, anchor="mm")
    return finish(img)


def recipe_overview():
    img, d = base()
    header(d, "FOCACCIA DO ANDRE")
    text(d, (9, 21), "INGREDIENT 4 / 6", DIM, F_SMALL)
    rect(d, ((8, 35), (232, 96)), outline=AMBER, fill=PANEL)
    text(d, (120, 48), "WHEAT FLOUR", HOT, F_BIG, anchor="mm")
    text(d, (120, 73), "366.0 g", AMBER, F_HUGE, anchor="mm")
    text(d, (12, 104), "TOTAL 700.3 g", DIM, F_SMALL)
    text(d, (229, 104), "DOUGHS", DIM, F_SMALL, anchor="ra")
    footer(d, ", / PREV NEXT   SPACE ACTIONS")
    return finish(img)


def recipe_actions():
    return menu_screen(
        "RECIPE ACTIONS",
        ["CHANGE TOTAL", "INGREDIENTS", "DUPLICATE", "TIMER", "SHARE", "DELETE"],
        selected=4,
        footer_text=";/ . MOVE   OK OPEN   ` BACK",
    )


def timer_screen():
    img, d = base()
    header(d, "TIMER")
    text(d, (120, 42), "03:00", HOT, F_HUGE, anchor="mm")
    rect(d, ((25, 65), (215, 76)), outline=LINE, fill=None)
    rect(d, ((27, 67), (121, 74)), outline=None, fill=AMBER)
    text(d, (120, 91), "CUSTOM  1 MIN  3 MIN  5 MIN", AMBER, F_SMALL, anchor="mm")
    footer(d, "OK START   ` BACK")
    return finish(img)


def wifi_screen():
    img, d = base()
    header(d, "WIFI PORTAL")
    rect(d, ((8, 25), (232, 103)), outline=LINE, fill=PANEL)
    text(d, (18, 34), "STATUS: CONNECTED", HOT, F_BODY_B)
    text(d, (18, 51), "HOST: misedeck.local", AMBER, F_BODY)
    text(d, (18, 68), "IP: 192.168.0.42", AMBER, F_BODY)
    text(d, (18, 88), "OPEN THE PORTAL", DIM, F_SMALL)
    footer(d, "SYNC REFRESH   ` BACK")
    return finish(img)


def battery_screen():
    img, d = base()
    header(d, "BATTERY")
    text(d, (120, 34), "86%", HOT, F_HUGE, anchor="mm")
    rect(d, ((31, 60), (209, 77)), outline=AMBER, fill=None)
    rect(d, ((34, 63), (185, 74)), outline=None, fill=AMBER)
    text(d, (120, 94), "4.05 V", AMBER, F_BIG, anchor="mm")
    footer(d, "` BACK")
    return finish(img)


def save_all():
    screens = {
        "01_opening.png": opening(),
        "02_main_menu.png": menu_screen("MISE_DECK v1.5.0", ["RECIPES", "TOOLS", "WIFI", "SYSTEM"], 0),
        "03_library.png": menu_screen("LIBRARY", ["FAVORITES", "MAINS", "DOUGHS", "SWEETS", "DRINKS"], 2),
        "04_recipe_overview.png": recipe_overview(),
        "05_recipe_actions.png": recipe_actions(),
        "06_timer.png": timer_screen(),
        "07_wifi_portal.png": wifi_screen(),
        "08_battery.png": battery_screen(),
    }
    for name, img in screens.items():
        img.save(OUT / name)

    card_w, card_h = W * SCALE, H * SCALE
    pad = 46
    title_h = 90
    cols = 2
    rows = 4
    sheet = Image.new("RGB", (cols * card_w + (cols + 1) * pad, rows * card_h + (rows + 1) * pad + title_h), BG)
    sd = ImageDraw.Draw(sheet)
    sd.text((pad, 22), "Mise_Deck v1.5.0 // Cardputer UI preview", font=F_BIG, fill=HOT)
    sd.text((pad, 58), "Generated interface previews for release notes and README media.", font=F_BODY, fill=DIM)
    for idx, (name, img) in enumerate(screens.items()):
        c = idx % cols
        r = idx // cols
        x = pad + c * (card_w + pad)
        y = title_h + pad + r * (card_h + pad)
        sheet.paste(img, (x, y))
        sd.rectangle((x - 2, y - 2, x + card_w + 2, y + card_h + 2), outline=LINE, width=2)
        label = name.replace(".png", "").replace("_", " ").upper()
        sd.text((x, y + card_h + 8), label, font=F_SMALL, fill=DIM)
    sheet.save(ROOT / "media" / "screenshots" / "mise_deck_v1.5_cardputer_preview.png")


if __name__ == "__main__":
    save_all()
    print(f"Generated screenshots in {OUT}")


