"""Generate The Adversary banner and mascot emblem for paper-audit."""

from PIL import Image, ImageDraw, ImageFont
import math
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_font(size, bold=False):
    """Try system fonts, fall back to default."""
    candidates = [
        "C:/Windows/Fonts/impact.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_shield(draw, cx, cy, size, fill_color, border_color, border_width=3):
    """Draw a pointed shield shape centered at (cx, cy)."""
    w = size * 0.7
    h = size
    points = [
        (cx - w/2, cy - h*0.4),       # top-left
        (cx + w/2, cy - h*0.4),       # top-right
        (cx + w/2, cy + h*0.1),       # right shoulder
        (cx, cy + h*0.6),             # bottom point
        (cx - w/2, cy + h*0.1),       # left shoulder
    ]
    draw.polygon(points, fill=fill_color, outline=border_color, width=border_width)
    return points


def draw_gladius(draw, cx, cy, length, angle_deg=30):
    """Draw a stylized gladius (short sword) as red pen."""
    angle = math.radians(angle_deg)
    tip_x = cx + length * math.cos(angle)
    tip_y = cy - length * math.sin(angle)

    # Blade
    perp_angle = angle + math.pi/2
    bw = 4
    blade_pts = [
        (cx + bw*math.cos(perp_angle), cy - bw*math.sin(perp_angle)),
        (cx - bw*math.cos(perp_angle), cy + bw*math.sin(perp_angle)),
        (tip_x - 1*math.cos(perp_angle), tip_y + 1*math.sin(perp_angle)),
        (tip_x + 1*math.cos(perp_angle), tip_y - 1*math.sin(perp_angle)),
    ]
    draw.polygon(blade_pts, fill="#C0392B")

    # Guard (crosspiece)
    gw = 14
    draw.line(
        [(cx - gw*math.cos(perp_angle), cy + gw*math.sin(perp_angle)),
         (cx + gw*math.cos(perp_angle), cy - gw*math.sin(perp_angle))],
        fill="#F1C40F", width=4
    )

    # Grip
    grip_len = length * 0.25
    grip_x = cx - grip_len * math.cos(angle)
    grip_y = cy + grip_len * math.sin(angle)
    draw.line([(cx, cy), (grip_x, grip_y)], fill="#8B4513", width=6)

    # Pommel
    draw.ellipse([grip_x-5, grip_y-5, grip_x+5, grip_y+5], fill="#F1C40F")


def draw_magnifying_glass(draw, cx, cy, size):
    """Draw a magnifying glass icon."""
    r = size // 2
    # Glass circle
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline="#3498DB", width=3)
    draw.ellipse([cx-r+2, cy-r+2, cx+r-2, cy+r-2], outline="#3498DB", width=1)
    # Handle
    hx = cx + int(r * 0.7)
    hy = cy + int(r * 0.7)
    draw.line([(hx, hy), (hx + size//2, hy + size//2)], fill="#2C3E50", width=4)


def draw_helmet_crest(draw, cx, cy, width, height):
    """Draw a Roman centurion helmet crest (mohawk plume)."""
    # Helmet dome
    draw.arc([cx - width//2, cy - height//3, cx + width//2, cy + height//3],
             180, 0, fill="#8B7355", width=3)
    # Crest (red mohawk)
    crest_points = []
    for i in range(20):
        t = i / 19
        x = cx - width*0.3 + t * width*0.6
        base_y = cy - height//3
        peak = height * 0.4 * math.sin(t * math.pi)
        crest_points.append((x, base_y - peak))
    # Close the bottom
    crest_points.append((cx + width*0.3, cy - height//3))
    crest_points.append((cx - width*0.3, cy - height//3))
    if len(crest_points) >= 3:
        draw.polygon(crest_points, fill="#C0392B")


def generate_emblem(size=400):
    """Generate The Adversary emblem/mascot."""
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    cx, cy = size // 2, size // 2 + 20

    # Outer glow circle
    for i in range(40, 0, -1):
        alpha = int(3 * i)
        r = size//2 - 20 + i
        color = (192, 57, 43, alpha)
        draw.ellipse([cx-r, cy-20-r, cx+r, cy-20+r], outline=color)

    # Shield
    shield_size = size * 0.55
    draw_shield(draw, cx, cy, shield_size, "#1A1A2E", "#C0392B", 4)

    # Inner shield highlight
    inner_size = shield_size * 0.8
    draw_shield(draw, cx, cy, inner_size, "#16213E", "#E74C3C", 2)

    # "VII" on the shield
    font_vii = get_font(int(size * 0.14), bold=True)
    bbox = draw.textbbox((0, 0), "VII", font=font_vii)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((cx - tw//2, cy - th//2 - 10), "VII", fill="#F1C40F", font=font_vii)

    # Magnifying glass on shield (small, below VII)
    draw_magnifying_glass(draw, cx, cy + int(shield_size * 0.2), int(size * 0.06))

    # Gladius crossing behind shield (left)
    draw_gladius(draw, cx - int(shield_size*0.25), cy - int(shield_size*0.15),
                 int(size * 0.2), angle_deg=55)

    # Red pen crossing behind shield (right) — mirror
    draw_gladius(draw, cx + int(shield_size*0.25), cy - int(shield_size*0.15),
                 int(size * 0.2), angle_deg=125)

    # Helmet crest on top
    draw_helmet_crest(draw, cx, cy - int(shield_size * 0.35), int(size * 0.3), int(size * 0.2))

    # Angry eyes on helmet
    eye_y = cy - int(shield_size * 0.32)
    eye_spacing = int(size * 0.06)
    # Left eye
    draw.polygon([(cx - eye_spacing - 8, eye_y - 2), (cx - eye_spacing + 8, eye_y - 2),
                  (cx - eye_spacing + 6, eye_y + 6), (cx - eye_spacing - 6, eye_y + 6)],
                 fill="#F39C12")
    draw.ellipse([cx - eye_spacing - 3, eye_y, cx - eye_spacing + 3, eye_y + 5],
                 fill="#C0392B")
    # Right eye
    draw.polygon([(cx + eye_spacing - 8, eye_y - 2), (cx + eye_spacing + 8, eye_y - 2),
                  (cx + eye_spacing + 6, eye_y + 6), (cx + eye_spacing - 6, eye_y + 6)],
                 fill="#F39C12")
    draw.ellipse([cx + eye_spacing - 3, eye_y, cx + eye_spacing + 3, eye_y + 5],
                 fill="#C0392B")

    return img


def generate_banner(width=1280, height=640):
    """Generate The Adversary banner."""
    img = Image.new("RGB", (width, height), "#0D0D1A")
    draw = ImageDraw.Draw(img)

    # Gradient overlay — dark crimson from edges
    for x in range(width):
        for stripe in range(3):
            y_start = stripe * height // 3
            intensity = int(15 * (1 - abs(x - width/2) / (width/2)))
            if intensity > 0:
                draw.line([(x, y_start), (x, y_start + 2)],
                          fill=(intensity + 10, 0, 0))

    # Horizontal rule lines
    draw.line([(100, 160), (width - 100, 160)], fill="#C0392B", width=2)
    draw.line([(100, 480), (width - 100, 480)], fill="#C0392B", width=2)

    # Top text: "paper-audit presents"
    font_small = get_font(24)
    text_top = "paper-audit presents"
    bbox = draw.textbbox((0, 0), text_top, font=font_small)
    tw = bbox[2] - bbox[0]
    draw.text((width//2 - tw//2, 125), text_top, fill="#7F8C8D", font=font_small)

    # Main title: THE ADVERSARY
    font_title = get_font(96, bold=True)
    title = "THE ADVERSARY"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    # Shadow
    draw.text((width//2 - tw//2 + 3, 203), title, fill="#4A0000", font=font_title)
    # Main
    draw.text((width//2 - tw//2, 200), title, fill="#E74C3C", font=font_title)

    # Subtitle: trial names
    font_trials = get_font(20)
    trials = "I. CRUCIBLE   II. MIRROR   III. CHAIN   IV. EYE   V. TONGUE   VI. SCALE   VII. GATE"
    bbox = draw.textbbox((0, 0), trials, font=font_trials)
    tw = bbox[2] - bbox[0]
    draw.text((width//2 - tw//2, 330), trials, fill="#F1C40F", font=font_trials)

    # Tagline
    font_tag = get_font(28)
    tagline = "Seven trials. Zero mercy. Better papers."
    bbox = draw.textbbox((0, 0), tagline, font=font_tag)
    tw = bbox[2] - bbox[0]
    draw.text((width//2 - tw//2, 400), tagline, fill="#ECF0F1", font=font_tag)

    # Bottom: "Can your paper survive?"
    font_bot = get_font(22)
    bottom = "Can your paper go seven rounds?"
    bbox = draw.textbbox((0, 0), bottom, font=font_bot)
    tw = bbox[2] - bbox[0]
    draw.text((width//2 - tw//2, 500), bottom, fill="#95A5A6", font=font_bot)

    # Emblem on left side
    emblem = generate_emblem(280)
    # Paste emblem (with alpha) on left
    img.paste(emblem, (30, height//2 - 140), emblem)

    # Mirror emblem on right (smaller)
    emblem_small = emblem.resize((200, 200), Image.LANCZOS)
    img.paste(emblem_small, (width - 230, height//2 - 100), emblem_small)

    # Corner accents — small red diamonds
    diamond_size = 8
    for corner in [(90, 155), (width-90, 155), (90, 485), (width-90, 485)]:
        x, y = corner
        draw.polygon([(x, y-diamond_size), (x+diamond_size, y),
                       (x, y+diamond_size), (x-diamond_size, y)],
                      fill="#C0392B")

    return img


if __name__ == "__main__":
    print("Generating The Adversary emblem...")
    emblem = generate_emblem(400)
    emblem_path = os.path.join(OUT_DIR, "adversary-emblem.png")
    emblem.save(emblem_path)
    print(f"  -> {emblem_path}")

    print("Generating The Adversary banner...")
    banner = generate_banner(1280, 640)
    banner_path = os.path.join(OUT_DIR, "banner.png")
    banner.save(banner_path)
    print(f"  -> {banner_path}")

    print("Done.")
