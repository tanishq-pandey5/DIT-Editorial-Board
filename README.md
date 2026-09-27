# Pratibimb '25 — DIT University Editorial Board
> **Reflection of Innovation** · 27th Annual University Magazine · Established 1998 · Dehradun, Uttarakhand

An interactive, high-performance 3D web publication built for the **DIT University Editorial Board** showcasing all 135 pages of *Pratibimb 2025*.

Powered by a curved-surface 3D paper simulation with physical lighting, cast shadows, and a draggable brass magnifying glass (loupe), adapted from the [MengTo/sketchbook](https://github.com/MengTo/sketchbook) architecture.

---

## 🌟 Features

- **Realistic 3D Page Turn Engine**: 18 nested curved strips mathematically sweeping through an arc (`transform-style: preserve-3d`), creating true physical page curvature instead of flat 2D hinges.
- **Draggable Brass Loupe (Magnifier)**: A physical magnifying glass sitting on the desk that can be picked up and dragged across pages to inspect fine typography and details with 2.3× magnification.
- **Complete 135-Page Magazine (68 Spreads)**:
  - Spread 0: Custom embossed leather/clothbound hardcover inner lining with DIT crest + Front Cover.
  - Spreads 1–67: All 135 pages paired in sequential order.
- **Interactive Scrubber & Page Jump**: Smooth range scrubber with live spread/page counter and direct "Go to Page" navigation.
- **Table of Contents Quick-Jump Drawer**: Curated slide-over directory covering all 11 major sections (From the Desk, Central News, Department News, Clubs, Placements, Alumni, Research Papers, Articles, and Creatives).
- **Editorial Board Showcase**: Dedicated section celebrating Editor-in-Chief Dr. Sakshi Semwal, Student Editor Mahika Maheshwari, and the student teams (Design, Social Media, Content, and Proof-reading).
- **Offline Archival PDF**: Direct download link to the complete 300 DPI high-resolution magazine PDF (49 MB).
- **Responsive & Touch Friendly**: Seamlessly runs across desktops, laptops, tablets, and mobile devices with touch swipe support.

---

## 🚀 Quick Start

To launch the website locally:

```bash
# Start a local HTTP server
python3 -m http.server 8080
```

Then open your browser to:
[http://localhost:8080](http://localhost:8080)

---

## 📂 Project Structure

```text
├── index.html                   # Main interactive 3D web application
├── assets/
│   ├── spreads/                 # 68 web-optimized 1760x1240 2-page spreads
│   │   ├── spread-000.jpg       # Hardcover inner lining + Front cover (Page 1)
│   │   ├── spread-001.jpg       # Pages 2 & 3 (Editor-in-Chief & Editorial Board)
│   │   └── ...                  # Spreads up to spread-067.jpg (Pages 134-135)
│   ├── magazine_data.js         # Metadata catalog, section index, and team data
│   ├── pratibimb2025.pdf        # Full high-res 135-page PDF for download (49MB)
│   ├── instrument-serif.woff2   # Serif display typography
│   ├── instrument-serif-italic.woff2
│   ├── newsreader.woff2         # Body typography
│   ├── dit-logo.png             # Official DIT University logo
│   ├── dit-logo-transparent.png # Transparent background logo variant
│   ├── favicon.png              # DIT University browser tab icon
│   ├── bg-wash.jpg              # Linen paper wash ground texture
│   ├── divider.png              # Brass engraved section rule
│   ├── bloom.png                # Editorial floral accent
│   ├── botany-left.png          # Left margin botanical etching
│   └── botany-right.png         # Right margin botanical etching
├── pratibimb2025_jpgs/          # Source 16MP raw pages (page-001.jpg to page-135.jpg)
├── scripts/
│   └── generate_spreads.py      # Automated PIL script to build 68 spreads from raw pages
└── sketchbook/                  # Original MengTo reference repository
```

---

## 👥 Editorial Board Roster (2024–25)

- **Editor-in-Chief**: Dr. Sakshi Semwal
- **Student Editor**: Mahika Maheshwari
- **Design Team**: Sanskriti (Head), Eklavya (Co-Head)
- **Social Media Team**: Daksh Walia (Head), Nayonika Dhuria (Co-Head), Tanishq Pandey, and team
- **Content Team**: Amandeep Kaur (Head), Apurva Chaudhary (Co-Head)
- **Proof-reading Team**: Martina (Head), Aviral (Co-Head)

---

## 📜 License & Copyright

© 2025 DIT University Editorial Board. All publication content and assets are intellectual property of DIT University, Dehradun.
Interactive 3D paper engine adapted from Meng To under open-source reference.
