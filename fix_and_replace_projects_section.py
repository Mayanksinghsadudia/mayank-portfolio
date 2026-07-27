import os

# Load current index.html
with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Build the complete Projects Section HTML
projects_section_html = '''    <!-- 03 PROJECTS GALLERY SECTION -->
    <section class="page-section" id="projects">
      <div class="container">
        
        <div class="section-header">
          <div>
            <span class="text-label-caps text-accent">03 // FEATURED CREATIVE WORKS</span>
            <h2 class="text-headline-lg font-headline" style="margin-top: 4px;">Projects Gallery</h2>
          </div>
          <span class="section-num text-outlined">03</span>
        </div>

        <!-- Category Filters -->
        <div class="filter-bar">
          <button class="filter-btn active" data-filter="all">ALL PROJECTS (29)</button>
          <button class="filter-btn" data-filter="branding">BRANDING & LOGOS</button>
          <button class="filter-btn" data-filter="packaging">PACKAGING</button>
          <button class="filter-btn" data-filter="digital-art">DIGITAL ART & MATTE</button>
          <button class="filter-btn" data-filter="uiux">UI/UX & WEB</button>
          <button class="filter-btn" data-filter="posters">POSTERS & MEDIA</button>
          <button class="filter-btn" data-filter="motion">MOTION & VIDEO</button>
        </div>

        <!-- Projects Grid -->
        <div class="projects-grid">

          <!-- Card: Corporate Brand Stationery Suite -->
          <div class="project-card" data-category="branding" data-id="bussuness-statinary-mockup">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/bussuness_statinary_mockup.jpg" alt="Corporate Brand Stationery Suite" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">BRAND IDENTITY & MOCKUP</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Corporate Brand Stationery Suite</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Complete brand identity mockup suite including letterhead, notepad, envelope, and business cards.
              </p>
              <div class="project-meta">
                <span>Photoshop & Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Black Edition Stationery Kit -->
          <div class="project-card" data-category="branding" data-id="business-statinary-black">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/business_statinary_black.jpg" alt="Black Edition Stationery Kit" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">PREMIUM DARK BRANDING</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Black Edition Stationery Kit</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Luxury dark obsidian stationery collection featuring metallic foil accenting and grid symmetry.
              </p>
              <div class="project-meta">
                <span>Photoshop Branding</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Corporate Stationery Print Layout -->
          <div class="project-card" data-category="branding" data-id="bussuness-statinary">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/bussuness_statinary.jpg" alt="Corporate Stationery Print Layout" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">BRAND IDENTITY PRINT</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Corporate Stationery Print Layout</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Clean print design layout for corporate letterheads, branded envelopes, and office stationery.
              </p>
              <div class="project-meta">
                <span>Illustrator & Print</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Minimalist Business Card Suite -->
          <div class="project-card" data-category="branding" data-id="visting-card-mockup">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/visting_card_mockup.jpg" alt="Minimalist Business Card Suite" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">CORPORATE CARD MOCKUP</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Minimalist Business Card Suite</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Dual-sided clean business card layout with rounded edges and tactile paper texture rendering.
              </p>
              <div class="project-meta">
                <span>Illustrator & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Corporate Tri-Fold Brochure Mockup -->
          <div class="project-card" data-category="branding" data-id="broucher-mockup">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/broucher_mockup.jpg" alt="Corporate Tri-Fold Brochure Mockup" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">PRINT & EDITORIAL</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Corporate Tri-Fold Brochure Mockup</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Tri-fold corporate brochure showcase presenting grid layouts, typography hierarchy, and corporate imagery.
              </p>
              <div class="project-meta">
                <span>Photoshop & InDesign</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Brand Logo Mark Design #1 -->
          <div class="project-card" data-category="branding" data-id="logo-1">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/log0_1.jpg" alt="Brand Logo Mark Design #1" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">VECTOR LOGO SUITE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Brand Logo Mark Design #1</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Geometric logo mark explorations across multiple color variations and brand guidelines.
              </p>
              <div class="project-meta">
                <span>Adobe Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Vector Logo Emblem #2 -->
          <div class="project-card" data-category="branding" data-id="logo-2">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/logo2.jpg" alt="Vector Logo Emblem #2" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">VECTOR LOGO SUITE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Vector Logo Emblem #2</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Clean minimalist corporate logo design with geometric grid symmetry.
              </p>
              <div class="project-meta">
                <span>Adobe Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Minimalist Emblem Mark #3 -->
          <div class="project-card" data-category="branding" data-id="logo-3">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/logo_3.jpg" alt="Minimalist Emblem Mark #3" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">VECTOR LOGO SUITE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Minimalist Emblem Mark #3</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                High-impact visual monogram mark designed for modern tech and design agencies.
              </p>
              <div class="project-meta">
                <span>Adobe Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Geometric Brand Symbol #4 -->
          <div class="project-card" data-category="branding" data-id="logo-4">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/logo_4.jpg" alt="Geometric Brand Symbol #4" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">VECTOR LOGO SUITE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Geometric Brand Symbol #4</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Symmetrical vector brand mark engineered for digital app icons and print stationery.
              </p>
              <div class="project-meta">
                <span>Adobe Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Abstract Creative Mark #5 -->
          <div class="project-card" data-category="branding" data-id="logo-5">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/logo_5.jpg" alt="Abstract Creative Mark #5" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">VECTOR LOGO SUITE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Abstract Creative Mark #5</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Modern dynamic abstract icon designed for creative agencies and tech startups.
              </p>
              <div class="project-meta">
                <span>Adobe Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Dragon Energy Beverage 3D Render -->
          <div class="project-card" data-category="packaging" data-id="energy-drink-mockup">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/energy_drink_mockup.jpg" alt="Dragon Energy Beverage 3D Render" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">3D BEVERAGE PACKAGING</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Dragon Energy Beverage 3D Render</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                500 ML & 250 ML matte black aluminum energy drink can packaging with vibrant dragon graphics.
              </p>
              <div class="project-meta">
                <span>3D Render & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Pure Dairy Packaging Suite Mockup -->
          <div class="project-card" data-category="packaging" data-id="milk-mockup">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/milk_mockup.jpg" alt="Pure Dairy Packaging Suite Mockup" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">PRODUCT CARTON & BOTTLE</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Pure Dairy Packaging Suite Mockup</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Organic milk bottle and box package mockup with clean minimalist typography and cow motif.
              </p>
              <div class="project-meta">
                <span>Photoshop Packaging</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Luxury Box & Pouch Packaging Design -->
          <div class="project-card" data-category="packaging" data-id="package-desgin-1">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/package_desgin_1.jpg" alt="Luxury Box & Pouch Packaging Design" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">RETAIL PRODUCT PACKAGING</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Luxury Box & Pouch Packaging Design</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Premium product box and foil pouch packaging design rendered with realistic lighting.
              </p>
              <div class="project-meta">
                <span>Illustrator & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Retail Display Box Package Mockup -->
          <div class="project-card" data-category="packaging" data-id="mockup-package-desgin">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/mockup_package_desgin.jpg" alt="Retail Display Box Package Mockup" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">COMMERCIAL PACKAGING</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Retail Display Box Package Mockup</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                3D retail box display mockup highlighting structural folds, embossing, and product branding.
              </p>
              <div class="project-meta">
                <span>Photoshop 3D Mockup</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: HP7 Dobby Low-Poly Vector Art -->
          <div class="project-card" data-category="digital-art" data-id="dobby-poly-art">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/dobby_poly_art.jpg" alt="HP7 Dobby Low-Poly Vector Art" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">GEOMETRIC POLYGON ART</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">HP7 Dobby Low-Poly Vector Art</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Detailed geometric low-poly vector portrait study of Dobby with dramatic high-contrast illumination.
              </p>
              <div class="project-meta">
                <span>Photoshop & Vector Art</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Surreal Photo Manipulation Artwork -->
          <div class="project-card" data-category="digital-art" data-id="manplution">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/manplution.jpg" alt="Surreal Photo Manipulation Artwork" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">COMPOSITING & DIGITAL ART</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Surreal Photo Manipulation Artwork</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Surreal digital composition blending multiple photographic elements, dramatic color grading, and lighting FX.
              </p>
              <div class="project-meta">
                <span>Photoshop Compositing</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Cinematic Environment Matte Painting -->
          <div class="project-card" data-category="digital-art" data-id="matte-painting">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/matte_painting.jpg" alt="Cinematic Environment Matte Painting" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">CONCEPT ART & ENVIRONMENT</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Cinematic Environment Matte Painting</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Atmospheric digital landscape matte painting created with multi-layered photo bashing and digital painting.
              </p>
              <div class="project-meta">
                <span>Photoshop Matte Painting</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Fantasy World Matte Painting -->
          <div class="project-card" data-category="digital-art" data-id="mate-painting-2">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/mate_painting_2.jpg" alt="Fantasy World Matte Painting" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">CONCEPT ART & ENVIRONMENT</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Fantasy World Matte Painting</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Surreal environmental concept art depicting mystical architecture and dramatic natural lighting.
              </p>
              <div class="project-meta">
                <span>Photoshop Digital Painting</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Vector Digital Portrait Study -->
          <div class="project-card" data-category="digital-art" data-id="potrait-01">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/potrait-01.jpg" alt="Vector Digital Portrait Study" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">DIGITAL ILLUSTRATION</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Vector Digital Portrait Study</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Hand-crafted vector digital portrait emphasizing contour shading, skin highlights, and hair texturing.
              </p>
              <div class="project-meta">
                <span>Illustrator & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Music Streaming Web UI Landing Page -->
          <div class="project-card" data-category="uiux" data-id="music-website-landing-page">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/music_website_landing_page.jpg" alt="Music Streaming Web UI Landing Page" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">DARK MODE WEB DESIGN</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Music Streaming Web UI Landing Page</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Modern dark mode web landing page for music discovery, featuring hero player visuals and glassmorphism elements.
              </p>
              <div class="project-meta">
                <span>UI/UX & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Creative Artboard & UI Layout 1 -->
          <div class="project-card" data-category="uiux" data-id="artboard-1">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/artboard_1.jpg" alt="Creative Artboard & UI Layout 1" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">UI/UX & DASHBOARD</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Creative Artboard & UI Layout 1</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                High-resolution creative artboard layout for dashboard UI and interactive web templates.
              </p>
              <div class="project-meta">
                <span>Photoshop & UI/UX</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Screen Composition & UI Showcase -->
          <div class="project-card" data-category="uiux" data-id="sc-png">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/sc.png" alt="Screen Composition & UI Showcase" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">UI/UX & COMPOSITING</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Screen Composition & UI Showcase</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Screen composition showcase demonstrating user interface layout, typography, and visual hierarchy.
              </p>
              <div class="project-meta">
                <span>UI/UX & Photoshop</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Web Template Design Documentation (PDF) -->
          <div class="project-card" data-category="uiux" data-id="web-template-pdf">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/artboard_1.jpg" alt="Web Template Design Documentation (PDF)" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">WEB DESIGN DOCUMENTATION</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Web Template Design Specification (PDF)</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Comprehensive web template design specification document containing full website wireframes and component layouts.
              </p>
              <div class="project-meta">
                <a href="assets/user_projects/web_template.pdf" target="_blank" style="color: var(--color-primary); text-decoration: none; font-weight: 600;">Download PDF Document</a>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">description</span>
              </div>
            </div>
          </div>

          <!-- Card: High-Impact Advertising Poster Design -->
          <div class="project-card" data-category="posters" data-id="poster-2-01">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/poster_2-01.jpg" alt="High-Impact Advertising Poster Design" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">ADVERTISING & PROMOTIONAL POSTER</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">High-Impact Advertising Poster Design</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Bold advertising poster layout engineered for maximum visual contrast and instant audience engagement.
              </p>
              <div class="project-meta">
                <span>Photoshop & Illustrator</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Raksha Bandhan Cultural Festival Poster -->
          <div class="project-card" data-category="posters" data-id="raksha-bandhan">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/raksha_bandhan.jpg" alt="Raksha Bandhan Cultural Festival Poster" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">FESTIVE SOCIAL MEDIA ART</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Raksha Bandhan Cultural Festival Poster</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Vibrant Indian cultural festival banner celebrating traditional Rakhi ties with ornate vector graphics.
              </p>
              <div class="project-meta">
                <span>Illustrator Festival Art</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Armed Forces Flag Day Commemorative Poster -->
          <div class="project-card" data-category="posters" data-id="flag-day-poster">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/flag_day_15-01.jpg" alt="Armed Forces Flag Day Commemorative Poster" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">PATRIOTIC COMMEMORATIVE POSTER</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Armed Forces Flag Day Commemorative Poster</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Patriotic commemorative poster honoring Indian Armed Forces with bold typography and national flag accents.
              </p>
              <div class="project-meta">
                <span>Photoshop & Vector</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Luxury Event Invitation Card Design -->
          <div class="project-card" data-category="posters" data-id="invitation-card">
            <div class="project-img-wrapper">
              <img src="assets/user_projects/invitataion_card_.jpg" alt="Luxury Event Invitation Card Design" class="project-img" />
              <div class="project-overlay"></div>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">EVENT & STATIONERY ART</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Luxury Event Invitation Card Design</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Elegant floral border invitation card design crafted with ornate golden accents and classic calligraphy.
              </p>
              <div class="project-meta">
                <span>Photoshop Print Design</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">arrow_forward</span>
              </div>
            </div>
          </div>

          <!-- Card: Motion Design Video Reel 1 -->
          <div class="project-card" data-category="motion" data-id="video-1">
            <div class="project-img-wrapper" style="background: #000;">
              <video src="assets/user_projects/video1.mp4" controls muted loop style="width:100%; height:100%; object-fit:cover;"></video>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">MOTION GRAPHICS & VIDEO</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Motion Design Video Reel 1</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                Dynamic motion graphics video showcase displaying animated visual effects, transitions, and motion editing.
              </p>
              <div class="project-meta">
                <span>After Effects & Premiere</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">play_circle</span>
              </div>
            </div>
          </div>

          <!-- Card: Motion Graphics Reel 2 -->
          <div class="project-card" data-category="motion" data-id="video-2">
            <div class="project-img-wrapper" style="background: #000;">
              <video src="assets/user_projects/video2.mp4" controls muted loop style="width:100%; height:100%; object-fit:cover;"></video>
            </div>
            <div class="project-card-content">
              <span class="text-label-caps text-accent">MOTION GRAPHICS & VIDEO</span>
              <h3 class="font-headline text-headline-md" style="margin-top: 4px;">Motion Graphics Reel 2</h3>
              <p style="color: var(--color-text-muted); font-size: 13px; margin-top: 6px;">
                High-energy motion graphic reel presenting typography animation, visual compositing, and creative transitions.
              </p>
              <div class="project-meta">
                <span>After Effects & Video FX</span>
                <span class="material-symbols-outlined" style="font-size: 18px; color: var(--color-primary);">play_circle</span>
              </div>
            </div>
          </div>

        </div>

      </div>
    </section>'''

# Replace Section 03 in index.html cleanly
start_marker = '<!-- 03 PROJECTS GALLERY SECTION -->'
end_marker = '<!-- 04 CONTACT SECTION -->'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + projects_section_html + '\n\n    ' + html[end_idx:]
    with open('C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("SUCCESS: Written complete Projects section with all 29 cards to index.html!")
else:
    print(f"ERROR: Markers not found. start_idx={start_idx}, end_idx={end_idx}")
