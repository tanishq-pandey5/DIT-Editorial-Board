import os
import sys
from PIL import Image, ImageDraw, ImageFont

SOURCE_DIR = 'pratibimb2025_jpgs'
OUTPUT_DIR = 'assets/spreads'
PAGE_WIDTH = 880
PAGE_HEIGHT = 1240
SPREAD_WIDTH = PAGE_WIDTH * 2
SPREAD_HEIGHT = PAGE_HEIGHT

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_inner_cover_left(width, height):
    """
    Creates an elegant, rich clothbound inner cover facing page
    with deep royal navy / midnight blue texture and gold embossed typography.
    """
    img = Image.new('RGB', (width, height), (16, 24, 40))
    draw = ImageDraw.Draw(img)

    # Outer and inner gold decorative borders
    border_color = (205, 168, 105)
    faint_gold = (120, 95, 55)
    
    # Outer frame
    draw.rectangle([40, 40, width - 40, height - 40], outline=border_color, width=2)
    # Inner thin frame
    draw.rectangle([48, 48, width - 48, height - 48], outline=faint_gold, width=1)
    # Corner accents
    corner_len = 30
    for cx, cy in [(40, 40), (width - 40, 40), (40, height - 40), (width - 40, height - 40)]:
        sign_x = 1 if cx == 40 else -1
        sign_y = 1 if cy == 40 else -1
        draw.line([(cx, cy + sign_y * corner_len), (cx, cy), (cx + sign_x * corner_len, cy)], fill=border_color, width=3)

    # Center insignia / crest with official DIT University logo
    center_x = width // 2
    crest_y = 275

    logo_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'dit-logo.png')
    if os.path.exists(logo_path):
        logo_img = Image.open(logo_path)
        plaque_w, plaque_h = 170, 142
        pl_box = [center_x - plaque_w // 2, crest_y - plaque_h // 2, center_x + plaque_w // 2, crest_y + plaque_h // 2]
        # Gold frame
        draw.rounded_rectangle([pl_box[0] - 3, pl_box[1] - 3, pl_box[2] + 3, pl_box[3] + 3], radius=14, fill=border_color)
        draw.rounded_rectangle(pl_box, radius=12, fill=(255, 255, 255))
        # Inner logo
        logo_h = 112
        logo_w = int(logo_img.width * (logo_h / logo_img.height))
        logo_resized = logo_img.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
        img.paste(logo_resized, (center_x - logo_w // 2, crest_y - logo_h // 2))
    else:
        draw.ellipse([center_x - 55, crest_y - 55, center_x + 55, crest_y + 55], outline=border_color, width=2)
        draw.ellipse([center_x - 45, crest_y - 45, center_x + 45, crest_y + 45], outline=faint_gold, width=1)
        draw.polygon([
            (center_x, crest_y - 25),
            (center_x + 25, crest_y),
            (center_x, crest_y + 25),
            (center_x - 25, crest_y)
        ], outline=border_color, fill=(24, 34, 56))

    # Text elements
    try:
        # Try loading default system serif if available, else load default
        font_serif_lg = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 36)
        font_serif_md = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 24)
        font_serif_sm = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 15)
        font_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Bold.ttf", 52)
        font_sub = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia Italic.ttf", 22)
    except Exception:
        font_serif_lg = font_serif_md = font_serif_sm = font_title = font_sub = ImageFont.load_default()

    def draw_centered_text(y, text, font, fill):
        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        draw.text((center_x - text_w // 2, y), text, font=font, fill=fill)

    draw_centered_text(420, "DIT UNIVERSITY", font_serif_md, (220, 200, 160))
    draw_centered_text(465, "EDITORIAL BOARD", font_serif_sm, (180, 150, 100))

    # Divider line
    draw.line([(center_x - 120, 520), (center_x + 120, 520)], fill=border_color, width=1)
    draw.ellipse([center_x - 4, 520 - 4, center_x + 4, 520 + 4], fill=border_color)

    draw_centered_text(580, "PRATIBIMB '25", font_title, (245, 225, 180))
    draw_centered_text(655, "Reflection of Innovation", font_sub, (200, 180, 140))
    draw_centered_text(710, "ANNUAL UNIVERSITY MAGAZINE", font_serif_sm, (160, 140, 105))

    # Details
    draw.line([(center_x - 80, 780), (center_x + 80, 780)], fill=faint_gold, width=1)
    draw_centered_text(830, "DEHRADUN, UTTARAKHAND", font_serif_sm, (150, 135, 110))
    draw_centered_text(865, "ESTABLISHED 1998", font_serif_sm, (130, 115, 95))

    # Turning hint
    draw_centered_text(1080, "TURN PAGE TO BEGIN READING →", font_serif_sm, (180, 160, 120))
    draw.line([(center_x - 60, 1120), (center_x + 60, 1120)], fill=(60, 75, 105), width=1)

    return img

def resize_page(img_path):
    img = Image.open(img_path)
    return img.resize((PAGE_WIDTH, PAGE_HEIGHT), Image.Resampling.LANCZOS)

def generate_all_spreads():
    print("Generating Spread 000 (Inside cover + Front cover)...")
    left_0 = create_inner_cover_left(PAGE_WIDTH, PAGE_HEIGHT)
    right_0 = resize_page(os.path.join(SOURCE_DIR, 'page-001.jpg'))

    spread_0 = Image.new('RGB', (SPREAD_WIDTH, SPREAD_HEIGHT), (16, 24, 40))
    spread_0.paste(left_0, (0, 0))
    spread_0.paste(right_0, (PAGE_WIDTH, 0))
    spread_0.save(os.path.join(OUTPUT_DIR, 'spread-000.jpg'), 'JPEG', quality=88, optimize=True)

    total_pages = 135
    total_spreads = 68  # Spread 0 to 67

    # Spreads 1 through 67
    # Spread k has left = page-(2k), right = page-(2k+1)
    for spread_idx in range(1, total_spreads):
        p_left_num = spread_idx * 2
        p_right_num = spread_idx * 2 + 1

        left_file = os.path.join(SOURCE_DIR, f"page-{p_left_num:03d}.jpg")
        right_file = os.path.join(SOURCE_DIR, f"page-{p_right_num:03d}.jpg")

        left_im = resize_page(left_file)
        right_im = resize_page(right_file)

        spread = Image.new('RGB', (SPREAD_WIDTH, SPREAD_HEIGHT), (236, 231, 220))
        spread.paste(left_im, (0, 0))
        spread.paste(right_im, (PAGE_WIDTH, 0))

        out_name = f"spread-{spread_idx:03d}.jpg"
        out_path = os.path.join(OUTPUT_DIR, out_name)
        spread.save(out_path, 'JPEG', quality=88, optimize=True)

        if spread_idx % 10 == 0 or spread_idx == total_spreads - 1:
            print(f"Generated {out_name} (Pages {p_left_num}-{p_right_num})")

    print(f"Successfully generated all {total_spreads} spreads in {OUTPUT_DIR}/")

if __name__ == '__main__':
    generate_all_spreads()
