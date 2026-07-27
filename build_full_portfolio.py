import re

# Load index.html
with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Filter buttons HTML
filter_buttons = '''        <div class="filter-bar">
          <button class="filter-btn active" data-filter="all">ALL PROJECTS</button>
          <button class="filter-btn" data-filter="branding">BRANDING & LOGOS</button>
          <button class="filter-btn" data-filter="packaging">PACKAGING</button>
          <button class="filter-btn" data-filter="digital-art">DIGITAL ART & MATTE</button>
          <button class="filter-btn" data-filter="uiux">UI/UX & WEB</button>
          <button class="filter-btn" data-filter="posters">POSTERS & MEDIA</button>
        </div>'''

# Projects Cards List
projects_list = [
    # Branding & Logos
    {
        "id": "brand-stationery-suite",
        "category": "branding",
        "title": "Corporate Brand Stationery Suite",
        "subtitle": "BRAND IDENTITY & STATIONERY",
        "img": "assets/user_projects/bussuness_statinary_mockup.jpg",
        "desc": "Complete brand identity mockup suite including letterhead, notepad, envelope, and business cards.",
        "tools": "Photoshop & Illustrator"
    },
    {
        "id": "brand-stationery-black",
        "category": "branding",
        "title": "Black Edition Stationery Kit",
        "subtitle": "PREMIUM DARK BRANDING",
        "img": "assets/user_projects/business_statinary_black.jpg",
        "desc": "Luxury dark obsidian stationery collection featuring metallic foil accenting and grid symmetry.",
        "tools": "Photoshop Mockup"
    },
    {
        "id": "visiting-card-mockup",
        "category": "branding",
        "title": "Minimalist Business Card Suite",
        "subtitle": "CORPORATE CARD MOCKUP",
        "img": "assets/user_projects/visting_card_mockup.jpg",
        "desc": "Dual-sided clean business card layout with rounded edges and tactile paper texture rendering.",
        "tools": "Illustrator & Photoshop"
    },
    {
        "id": "brochure-mockup",
        "category": "branding",
        "title": "Corporate Tri-Fold Brochure",
        "subtitle": "PRINT & EDITORIAL DESIGN",
        "img": "assets/user_projects/broucher_mockup.jpg",
        "desc": "Tri-fold corporate brochure showcase presenting structured grid layouts, typography hierarchy, and imagery.",
        "tools": "Photoshop & InDesign"
    },
    {
        "id": "logo-identity-suite-1",
        "category": "branding",
        "title": "Modern Brand Mark Collection #1",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/log0_1.jpg",
        "desc": "Geometric logo mark explorations across multiple color variations and brand guidelines.",
        "tools": "Adobe Illustrator"
    },
    {
        "id": "logo-identity-suite-2",
        "category": "branding",
        "title": "Minimalist Emblem & Symbol #2",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo2.jpg",
        "desc": "Symmetrical vector brand mark engineered for digital app icons and print stationery.",
        "tools": "Adobe Illustrator"
    },
    {
        "id": "logo-identity-suite-3",
        "category": "branding",
        "title": "Creative Abstract Logo #3",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo_3.jpg",
        "desc": "High-impact visual monogram mark designed for modern tech and design agencies.",
        "tools": "Adobe Illustrator"
    },

    # Packaging
    {
        "id": "energy-drink-can",
        "category": "packaging",
        "title": "Dragon Energy Drink Cans",
        "subtitle": "3D BEVERAGE PACKAGING",
        "img": "assets/user_projects/energy_drink_mockup.jpg",
        "desc": "500 ML & 250 ML matte black aluminum energy drink can packaging with vibrant dragon graphics.",
        "tools": "3D Render & Photoshop"
    },
    {
        "id": "milk-package-mockup",
        "category": "packaging",
        "title": "Pure Dairy Packaging Suite",
        "subtitle": "PRODUCT CARTON & BOTTLE",
        "img": "assets/user_projects/milk_mockup.jpg",
        "desc": "Organic milk bottle and box package mockup with clean minimalist typography and cow motif.",
        "tools": "Photoshop Packaging"
    },
    {
        "id": "luxury-package-design-1",
        "category": "packaging",
        "title": "Luxury Box & Pouch Packaging",
        "subtitle": "RETAIL PRODUCT PACKAGING",
        "img": "assets/user_projects/package_desgin_1.jpg",
        "desc": "Premium product box and foil pouch packaging design rendered with realistic lighting.",
        "tools": "Illustrator & Photoshop"
    },
    {
        "id": "retail-box-mockup",
        "category": "packaging",
        "title": "Retail Display Box Package",
        "subtitle": "COMMERCIAL PACKAGING",
        "img": "assets/user_projects/mockup_package_desgin.jpg",
        "desc": "3D retail box display mockup highlighting structural folds, embossing, and product branding.",
        "tools": "Photoshop 3D Mockup"
    },

    # Digital Art & Matte Painting
    {
        "id": "dobby-poly-art",
        "category": "digital-art",
        "title": "HP7 Dobby Low-Poly Artwork",
        "subtitle": "GEOMETRIC VECTOR ART",
        "img": "assets/user_projects/dobby_poly_art.jpg",
        "desc": "Detailed geometric low-poly vector portrait study of Dobby with dramatic high-contrast lighting.",
        "tools": "Photoshop & Vector Art"
    },
    {
        "id": "photo-manipulation-art",
        "category": "digital-art",
        "title": "Surreal Photo Manipulation",
        "subtitle": "COMPOSITING & BLENDING",
        "img": "assets/user_projects/manplution.jpg",
        "desc": "Surreal digital composition blending multiple photographic elements, dramatic color grading, and lighting FX.",
        "tools": "Photoshop Compositing"
    },
    {
        "id": "matte-painting-landscape-1",
        "category": "digital-art",
        "title": "Cinematic Environment Matte Painting",
        "subtitle": "CONCEPT ART & ENVIRONMENT",
        "img": "assets/user_projects/matte_painting.jpg",
        "desc": "Atmospheric digital landscape matte painting created with multi-layered photo bashing and digital painting.",
        "tools": "Photoshop Matte Painting"
    },
    {
        "id": "matte-painting-landscape-2",
        "category": "digital-art",
        "title": "Fantasy World Matte Painting",
        "subtitle": "CONCEPT ART & ENVIRONMENT",
        "img": "assets/user_projects/mate_painting_2.jpg",
        "desc": "Surreal environmental concept art depicting mystical architecture and dramatic natural lighting.",
        "tools": "Photoshop Digital Painting"
    },
    {
        "id": "digital-portrait-vector",
        "category": "digital-art",
        "title": "Vector Digital Portrait Study",
        "subtitle": "DIGITAL ILLUSTRATION",
        "img": "assets/user_projects/potrait-01.jpg",
        "desc": "Hand-crafted vector digital portrait emphasizing contour shading, skin highlights, and hair texturing.",
        "tools": "Illustrator & Photoshop"
    },

    # UI/UX & Web Design
    {
        "id": "music-website-landing",
        "category": "uiux",
        "title": "Music Streaming Web UI Landing Page",
        "subtitle": "DARK MODE WEB DESIGN",
        "img": "assets/user_projects/music_website_landing_page.jpg",
        "desc": "Modern dark mode web landing page for music discovery, featuring hero player visuals and glassmorphism elements.",
        "tools": "UI/UX & Photoshop"
    },
    {
        "id": "web-dashboard-template",
        "category": "uiux",
        "title": "Creative Dashboard Web Template",
        "subtitle": "WEB APP & DASHBOARD UI",
        "img": "assets/user_projects/artboard_1.jpg",
        "desc": "Clean web application dashboard layout with modular widgets, navigation sidebar, and data charts.",
        "tools": "UI/UX Design"
    },

    # Posters & Media
    {
        "id": "poster-design-201",
        "category": "posters",
        "title": "High-Impact Promotional Poster",
        "subtitle": "ADVERTISING POSTER",
        "img": "assets/user_projects/poster_2-01.jpg",
        "desc": "Bold advertising poster layout engineered for maximum visual contrast and instant audience engagement.",
        "tools": "Photoshop & Illustrator"
    },
    {
        "id": "raksha-bandhan-poster",
        "category": "posters",
        "title": "Raksha Bandhan Cultural Poster",
        "subtitle": "FESTIVE SOCIAL MEDIA ART",
        "img": "assets/user_projects/raksha_bandhan.jpg",
        "desc": "Vibrant Indian cultural festival banner celebrating traditional Rakhi ties with ornate vector graphics.",
        "tools": "Illustrator Festival Art"
    },
    {
        "id": "flag-day-poster",
        "category": "posters",
        "title": "Armed Forces Flag Day Poster",
        "subtitle": "COMMEMORATIVE POSTER",
        "img": "assets/user_projects/flag_day_15-01.jpg",
        "desc": "Patriotic commemorative poster honoring Indian Armed Forces with bold typography and national flag accents.",
        "tools": "Photoshop & Vector"
    },
    {
        "id": "invitation-card-design",
        "category": "posters",
        "title": "Luxury Event Invitation Card",
        "subtitle": "EVENT STATIONERY",
        "img": "assets/user_projects/invitataion_card_.jpg",
        "desc": "Elegant floral border invitation card design crafted with ornate golden accents and classic calligraphy.",
        "tools": "Photoshop Print Design"
    }
]

cards_html = []
for p in projects_list:
    card = f'''          <!-- Card: {p['title']} -->
          <div class="project-card" data-category="{p['category']}" data-id="{p['id']}">
            <div class="project-img-wrapper">
              <img src="{p['img']}" alt="{p['title']}" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">{p['subtitle']}</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">{p['title']}</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                {p['desc']}
              </p>
              <div class="project-meta">
                <span>{p['tools']}</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>'''
    cards_html.append(card)

full_projects_grid = f'''        <!-- Category Filters -->
{filter_buttons}

        <!-- Projects Grid -->
        <div class="projects-grid">
{chr(10).join(cards_html)}
        </div>'''

# Replace in index.html
pattern = r'<!-- Category Filters -->.*?</div>\s*<!-- 04 CONTACT SECTION -->'
replacement = full_projects_grid + '\n\n      </div>\n    </section>\n\n    <!-- 04 CONTACT SECTION -->'

new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully updated index.html with all 22+ real graphic design portfolio projects from D:\\PROJECTS GRAPHIC DESGIN!")
