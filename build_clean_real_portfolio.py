import os
import re

# Load current index.html
with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build clean project cards for ALL 28 items in D:\PROJECTS GRAPHIC DESGIN
real_projects = [
    # 1. Artboard 1
    {
        "id": "artboard-1",
        "category": "uiux",
        "title": "Creative Artboard & UI Layout 1",
        "subtitle": "UI/UX & DASHBOARD",
        "img": "assets/user_projects/artboard_1.jpg",
        "desc": "High-resolution creative artboard layout for dashboard UI and interactive web templates.",
        "tools": "Photoshop & UI/UX"
    },
    # 2. Broucher Mockup
    {
        "id": "broucher-mockup",
        "category": "branding",
        "title": "Corporate Tri-Fold Brochure Mockup",
        "subtitle": "PRINT & EDITORIAL",
        "img": "assets/user_projects/broucher_mockup.jpg",
        "desc": "Tri-fold corporate brochure showcase presenting grid layouts, typography hierarchy, and corporate imagery.",
        "tools": "Photoshop & InDesign"
    },
    # 3. Business Stationary Black
    {
        "id": "business-statinary-black",
        "category": "branding",
        "title": "Black Edition Stationery Kit",
        "subtitle": "PREMIUM DARK BRANDING",
        "img": "assets/user_projects/business_statinary_black.jpg",
        "desc": "Luxury dark obsidian stationery collection featuring metallic foil accenting and grid symmetry.",
        "tools": "Photoshop Branding"
    },
    # 4. Bussuness Statinary Mockup
    {
        "id": "bussuness-statinary-mockup",
        "category": "branding",
        "title": "Corporate Brand Stationery Suite Mockup",
        "subtitle": "BRAND IDENTITY & MOCKUP",
        "img": "assets/user_projects/bussuness_statinary_mockup.jpg",
        "desc": "Complete brand identity mockup suite including letterhead, notepad, envelope, and business cards.",
        "tools": "Photoshop & Illustrator"
    },
    # 5. Bussuness Statinary
    {
        "id": "bussuness-statinary",
        "category": "branding",
        "title": "Corporate Stationery Print Layout",
        "subtitle": "BRAND IDENTITY PRINT",
        "img": "assets/user_projects/bussuness_statinary.jpg",
        "desc": "Clean print design layout for corporate letterheads, branded envelopes, and office stationery.",
        "tools": "Illustrator & Print"
    },
    # 6. Dobby Poly Art
    {
        "id": "dobby-poly-art",
        "category": "digital-art",
        "title": "HP7 Dobby Low-Poly Vector Art",
        "subtitle": "GEOMETRIC POLYGON ART",
        "img": "assets/user_projects/dobby_poly_art.jpg",
        "desc": "Detailed geometric low-poly vector portrait study of Dobby with dramatic high-contrast illumination.",
        "tools": "Photoshop & Vector Art"
    },
    # 7. Energy Drink Mockup
    {
        "id": "energy-drink-mockup",
        "category": "packaging",
        "title": "Dragon Energy Beverage 3D Render",
        "subtitle": "3D BEVERAGE PACKAGING",
        "img": "assets/user_projects/energy_drink_mockup.jpg",
        "desc": "500 ML & 250 ML matte black aluminum energy drink can packaging with vibrant dragon graphics.",
        "tools": "3D Render & Photoshop"
    },
    # 8. Flag Day 15-01
    {
        "id": "flag-day-poster",
        "category": "posters",
        "title": "Armed Forces Flag Day Commemorative Poster",
        "subtitle": "PATRIOTIC COMMEMORATIVE POSTER",
        "img": "assets/user_projects/flag_day_15-01.jpg",
        "desc": "Patriotic commemorative poster honoring Indian Armed Forces with bold typography and national flag accents.",
        "tools": "Photoshop & Vector"
    },
    # 9. Invitation Card
    {
        "id": "invitation-card",
        "category": "posters",
        "title": "Luxury Event Invitation Card Design",
        "subtitle": "EVENT & STATIONERY ART",
        "img": "assets/user_projects/invitataion_card_.jpg",
        "desc": "Elegant floral border invitation card design crafted with ornate golden accents and classic calligraphy.",
        "tools": "Photoshop Print Design"
    },
    # 10. Log0 1
    {
        "id": "logo-1",
        "category": "branding",
        "title": "Brand Logo Mark Design #1",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/log0_1.jpg",
        "desc": "Geometric logo mark explorations across multiple color variations and brand guidelines.",
        "tools": "Adobe Illustrator"
    },
    # 11. Logo 3
    {
        "id": "logo-3",
        "category": "branding",
        "title": "Minimalist Emblem Mark #3",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo_3.jpg",
        "desc": "High-impact visual monogram mark designed for modern tech and design agencies.",
        "tools": "Adobe Illustrator"
    },
    # 12. Logo 4
    {
        "id": "logo-4",
        "category": "branding",
        "title": "Geometric Brand Symbol #4",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo_4.jpg",
        "desc": "Symmetrical vector brand mark engineered for digital app icons and print stationery.",
        "tools": "Adobe Illustrator"
    },
    # 13. Logo 5
    {
        "id": "logo-5",
        "category": "branding",
        "title": "Abstract Creative Mark #5",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo_5.jpg",
        "desc": "Modern dynamic abstract icon designed for creative agencies and tech startups.",
        "tools": "Adobe Illustrator"
    },
    # 14. Logo 2
    {
        "id": "logo-2",
        "category": "branding",
        "title": "Vector Logo Emblem #2",
        "subtitle": "VECTOR LOGO SUITE",
        "img": "assets/user_projects/logo2.jpg",
        "desc": "Clean minimalist corporate logo design with geometric grid symmetry.",
        "tools": "Adobe Illustrator"
    },
    # 15. Manplution
    {
        "id": "manplution",
        "category": "digital-art",
        "title": "Surreal Photo Manipulation Artwork",
        "subtitle": "COMPOSITING & DIGITAL ART",
        "img": "assets/user_projects/manplution.jpg",
        "desc": "Surreal digital composition blending multiple photographic elements, dramatic color grading, and lighting FX.",
        "tools": "Photoshop Compositing"
    },
    # 16. Mate Painting 2
    {
        "id": "mate-painting-2",
        "category": "digital-art",
        "title": "Fantasy World Matte Painting",
        "subtitle": "CONCEPT ART & ENVIRONMENT",
        "img": "assets/user_projects/mate_painting_2.jpg",
        "desc": "Surreal environmental concept art depicting mystical architecture and dramatic natural lighting.",
        "tools": "Photoshop Digital Painting"
    },
    # 17. Matte Painting
    {
        "id": "matte-painting",
        "category": "digital-art",
        "title": "Cinematic Environment Matte Painting",
        "subtitle": "CONCEPT ART & ENVIRONMENT",
        "img": "assets/user_projects/matte_painting.jpg",
        "desc": "Atmospheric digital landscape matte painting created with multi-layered photo bashing and digital painting.",
        "tools": "Photoshop Matte Painting"
    },
    # 18. Milk Mockup
    {
        "id": "milk-mockup",
        "category": "packaging",
        "title": "Pure Dairy Packaging Suite Mockup",
        "subtitle": "PRODUCT CARTON & BOTTLE",
        "img": "assets/user_projects/milk_mockup.jpg",
        "desc": "Organic milk bottle and box package mockup with clean minimalist typography and cow motif.",
        "tools": "Photoshop Packaging"
    },
    # 19. Mockup Package Desgin
    {
        "id": "mockup-package-desgin",
        "category": "packaging",
        "title": "Retail Display Box Package Mockup",
        "subtitle": "COMMERCIAL PACKAGING",
        "img": "assets/user_projects/mockup_package_desgin.jpg",
        "desc": "3D retail box display mockup highlighting structural folds, embossing, and product branding.",
        "tools": "Photoshop 3D Mockup"
    },
    # 20. Music Website Landing Page
    {
        "id": "music-website-landing-page",
        "category": "uiux",
        "title": "Music Streaming Web UI Landing Page",
        "subtitle": "DARK MODE WEB DESIGN",
        "img": "assets/user_projects/music_website_landing_page.jpg",
        "desc": "Modern dark mode web landing page for music discovery, featuring hero player visuals and glassmorphism elements.",
        "tools": "UI/UX & Photoshop"
    },
    # 21. Package Desgin 1
    {
        "id": "package-desgin-1",
        "category": "packaging",
        "title": "Luxury Box & Pouch Packaging Design",
        "subtitle": "RETAIL PRODUCT PACKAGING",
        "img": "assets/user_projects/package_desgin_1.jpg",
        "desc": "Premium product box and foil pouch packaging design rendered with realistic lighting.",
        "tools": "Illustrator & Photoshop"
    },
    # 22. Poster 2-01
    {
        "id": "poster-2-01",
        "category": "posters",
        "title": "High-Impact Advertising Poster Design",
        "subtitle": "ADVERTISING & PROMOTIONAL POSTER",
        "img": "assets/user_projects/poster_2-01.jpg",
        "desc": "Bold advertising poster layout engineered for maximum visual contrast and instant audience engagement.",
        "tools": "Photoshop & Illustrator"
    },
    # 23. Potrait-01
    {
        "id": "potrait-01",
        "category": "digital-art",
        "title": "Vector Digital Portrait Study",
        "subtitle": "DIGITAL ILLUSTRATION",
        "img": "assets/user_projects/potrait-01.jpg",
        "desc": "Hand-crafted vector digital portrait emphasizing contour shading, skin highlights, and hair texturing.",
        "tools": "Illustrator & Photoshop"
    },
    # 24. Raksha Bandhan
    {
        "id": "raksha-bandhan",
        "category": "posters",
        "title": "Raksha Bandhan Cultural Festival Poster",
        "subtitle": "FESTIVE SOCIAL MEDIA ART",
        "img": "assets/user_projects/raksha_bandhan.jpg",
        "desc": "Vibrant Indian cultural festival banner celebrating traditional Rakhi ties with ornate vector graphics.",
        "tools": "Illustrator Festival Art"
    },
    # 25. SC PNG
    {
        "id": "sc-png",
        "category": "uiux",
        "title": "Screen Composition & UI Showcase",
        "subtitle": "UI/UX & COMPOSITING",
        "img": "assets/user_projects/sc.png",
        "desc": "Screen composition showcase demonstrating user interface layout, typography, and visual hierarchy.",
        "tools": "UI/UX & Photoshop"
    },
    # 26. Visting Card Mockup
    {
        "id": "visting-card-mockup",
        "category": "branding",
        "title": "Minimalist Visiting Card Mockup",
        "subtitle": "CORPORATE CARD MOCKUP",
        "img": "assets/user_projects/visting_card_mockup.jpg",
        "desc": "Dual-sided clean business card layout with rounded edges and tactile paper texture rendering.",
        "tools": "Illustrator & Photoshop"
    },
    # 27. Motion Video 1
    {
        "id": "video-1",
        "category": "motion",
        "title": "Motion Design Video Reel 1",
        "subtitle": "MOTION GRAPHICS & VIDEO",
        "isVideo": True,
        "video": "assets/user_projects/video1.mp4",
        "desc": "Dynamic motion graphics video showcase displaying animated visual effects, transitions, and motion editing.",
        "tools": "After Effects & Premiere"
    },
    # 28. Motion Video 2
    {
        "id": "video-2",
        "category": "motion",
        "title": "Motion Graphics Reel 2",
        "subtitle": "MOTION GRAPHICS & VIDEO",
        "isVideo": True,
        "video": "assets/user_projects/video2.mp4",
        "desc": "High-energy motion graphic reel presenting typography animation, visual compositing, and creative transitions.",
        "tools": "After Effects & Video FX"
    },
    # 29. Web Template Specification PDF
    {
        "id": "web-template-pdf",
        "category": "uiux",
        "title": "Web Template Specification (PDF)",
        "subtitle": "WEB DESIGN DOCUMENTATION",
        "isPdf": True,
        "pdf": "assets/user_projects/web_template.pdf",
        "img": "assets/user_projects/sc.png",
        "desc": "Comprehensive web template design specification document containing full website wireframes and component layouts.",
        "tools": "PDF & UI/UX Design"
    }
]

cards_html = []
for p in real_projects:
    if p.get("isVideo"):
        card = f'''          <!-- Card: {p['title']} -->
          <div class="project-card" data-category="{p['category']}" data-id="{p['id']}">
            <div class="project-img-wrapper" style="background: #000;">
              <video src="{p['video']}" controls muted loop style="width:100%; height:100%; object-fit:cover;"></video>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">{p['subtitle']}</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">{p['title']}</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                {p['desc']}
              </p>
              <div class="project-meta">
                <span>{p['tools']}</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">play_circle</span>
              </div>
            </div>
          </div>'''
    elif p.get("isPdf"):
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
                <a href="{p['pdf']}" target="_blank" style="color: var(--color-primary); text-decoration: none; font-weight: 600;">Download PDF Document</a>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">description</span>
              </div>
            </div>
          </div>'''
    else:
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

filter_buttons = '''        <!-- Category Filters -->
        <div class="filter-bar">
          <button class="filter-btn active" data-filter="all">ALL PROJECTS ({})</button>
          <button class="filter-btn" data-filter="branding">BRANDING & LOGOS</button>
          <button class="filter-btn" data-filter="packaging">PACKAGING</button>
          <button class="filter-btn" data-filter="digital-art">DIGITAL ART & MATTE</button>
          <button class="filter-btn" data-filter="uiux">UI/UX & WEB</button>
          <button class="filter-btn" data-filter="posters">POSTERS & MEDIA</button>
          <button class="filter-btn" data-filter="motion">MOTION & VIDEO</button>
        </div>'''.format(len(real_projects))

full_projects_section = f'''    <!-- 03 PROJECTS GALLERY SECTION -->
    <section class="page-section" id="projects">
      <div class="container">
        
        <div class="section-header">
          <div>
            <span class="text-label-caps text-accent">03 // FEATURED CREATIVE WORKS</span>
            <h2 class="text-headline-lg font-headline" style="margin-top: 4px;">Projects Gallery</h2>
          </div>
          <span class="section-num text-outlined">03</span>
        </div>

{filter_buttons}

        <!-- Projects Grid -->
        <div class="projects-grid">
{chr(10).join(cards_html)}
        </div>

      </div>
    </section>'''

# Clean replacement in index.html
start_marker = '<!-- 03 PROJECTS GALLERY SECTION -->'
end_marker = '<!-- 04 CONTACT SECTION -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + full_projects_section + '\n\n    ' + html[end_idx:]
    with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"SUCCESS: Cleanly wrote all {len(real_projects)} real project cards to index.html!")
else:
    print(f"ERROR: Markers not found in index.html! start_idx={start_idx}, end_idx={end_idx}")
