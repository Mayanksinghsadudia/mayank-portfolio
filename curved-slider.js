/**
 * 3D Curved Slider Engine (Infinite Cylinder Arc - All 35 Projects)
 * Styled with Mayank's Signature Neon Amber & Tangerine Theme (#ff9d4d, #ff6b00)
 */

(function () {
  'use strict';

  // All 35 Portfolio Projects for Mayank Singh Sadudia
  const ALL_PROJECTS = [
  {
    "id": "amazon-sentiment-analysis",
    "category": "analytics",
    "tag": "NLP & SENTIMENT ANALYSIS \u00b7 PYTHON",
    "title": "Amazon Review System",
    "desc": "Classifies review text from Google Sheets as positive, neutral or negative with VADER, then explores the results with interactive charts.",
    "img": "assets/user_projects/amazon-project.svg",
    "url": "amazon-sentiment-analysis.html",
    "linkText": "View Project",
    "isExternal": false
  },
  {
    "id": "customer-management-system",
    "category": "analytics",
    "tag": "BUSINESS REPORTING \u00b7 PYTHON & SQLITE",
    "title": "Customer Management System",
    "desc": "Stores customer profiles and orders in SQLite, with SQL summaries for total customers, orders and revenue, plus customer-level charts.",
    "img": "assets/user_projects/customer-project.svg",
    "url": "cms-analysis.html",
    "linkText": "View Project",
    "isExternal": false
  },
  {
    "id": "lifecare-health-system",
    "category": "analytics",
    "tag": "HEALTHCARE DATABASE APP \u00b7 FLASK & SQLITE",
    "title": "Lifecare Health System",
    "desc": "An MCA academic prototype for patient and doctor registration, administrator approvals, appointment requests and profile management.",
    "img": "assets/user_projects/lifecare-project.svg",
    "url": "lifecare-health-system.html",
    "linkText": "View Project",
    "isExternal": false
  },
  {
    "id": "retail-sales-analysis",
    "category": "analytics",
    "tag": "DATA ANALYSIS \u00b7 PYTHON & SQL",
    "title": "Online Retail Sales Analysis",
    "desc": "A portfolio study of 541,909 historical UCI invoice lines: data preparation, monthly sales, country mix, and repeat purchasing, with documented definitions and limitations.",
    "img": "retail-analysis-preview.png",
    "url": "retail-analysis.html",
    "linkText": "View Analysis",
    "isExternal": false
  },
  {
    "id": "reva-3d-speaker",
    "category": "uiux",
    "tag": "INTERACTIVE 3D WEB APPLICATION",
    "title": "3D Exploding Speaker Web Application",
    "desc": "Interactive 3D audio hardware showcase featuring exploded view component animation, dynamic woofer mechanics, and audio visualizer.",
    "img": "assets/user_projects/reva_speaker.jpg",
    "url": "https://mayanksinghsadudia.github.io/reva-3d-speaker-website/",
    "linkText": "Visit Live Website",
    "isExternal": true
  },
  {
    "id": "ford-mustang-1968",
    "category": "uiux",
    "tag": "3D AUTOMOTIVE UI/UX WEB APPLICATION",
    "title": "Ford Mustang Fastback (1968 Edition)",
    "desc": "High-precision 3D automotive web showcase and interactive model study of the iconic 1968 Ford Mustang Fastback muscle car.",
    "img": "assets/user_projects/ford_mustang_1968.jpg",
    "url": "https://mayanksinghsadudia.github.io/ford-mustang-1968-showcase/",
    "linkText": "Visit Live Website",
    "isExternal": true
  },
  {
    "id": "artboard-1",
    "category": "uiux",
    "tag": "UI/UX & DASHBOARD",
    "title": "Creative Artboard & UI Layout 1",
    "desc": "High-resolution creative artboard layout for dashboard UI and interactive web templates.",
    "img": "assets/user_projects/artboard_1.jpg",
    "url": "assets/user_projects/artboard_1.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "broucher-mockup",
    "category": "branding",
    "tag": "PRINT & EDITORIAL",
    "title": "Corporate Tri-Fold Brochure Mockup",
    "desc": "Tri-fold corporate brochure showcase presenting grid layouts, typography hierarchy, and corporate imagery.",
    "img": "assets/user_projects/broucher_mockup.jpg",
    "url": "assets/user_projects/broucher_mockup.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "business-statinary-black",
    "category": "branding",
    "tag": "PREMIUM DARK BRANDING",
    "title": "Black Edition Stationery Kit",
    "desc": "Luxury dark obsidian stationery collection featuring metallic foil accenting and grid symmetry.",
    "img": "assets/user_projects/business_statinary_black.jpg",
    "url": "assets/user_projects/business_statinary_black.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "bussuness-statinary-mockup",
    "category": "branding",
    "tag": "BRAND IDENTITY & MOCKUP",
    "title": "Corporate Brand Stationery Suite Mockup",
    "desc": "Complete brand identity mockup suite including letterhead, notepad, envelope, and business cards.",
    "img": "assets/user_projects/bussuness_statinary_mockup.jpg",
    "url": "assets/user_projects/bussuness_statinary_mockup.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "bussuness-statinary",
    "category": "branding",
    "tag": "BRAND IDENTITY PRINT",
    "title": "Corporate Stationery Print Layout",
    "desc": "Clean print design layout for corporate letterheads, branded envelopes, and office stationery.",
    "img": "assets/user_projects/bussuness_statinary.jpg",
    "url": "assets/user_projects/bussuness_statinary.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "dobby-poly-art",
    "category": "digital-art",
    "tag": "GEOMETRIC POLYGON ART",
    "title": "HP7 Dobby Low-Poly Vector Art",
    "desc": "Detailed geometric low-poly vector portrait study of Dobby with dramatic high-contrast illumination.",
    "img": "assets/user_projects/dobby_poly_art.jpg",
    "url": "assets/user_projects/dobby_poly_art.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "energy-drink-mockup",
    "category": "packaging",
    "tag": "3D BEVERAGE PACKAGING",
    "title": "Dragon Energy Beverage 3D Render",
    "desc": "500 ML & 250 ML matte black aluminum energy drink can packaging with vibrant dragon graphics.",
    "img": "assets/user_projects/energy_drink_mockup.jpg",
    "url": "assets/user_projects/energy_drink_mockup.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "flag-day-poster",
    "category": "posters",
    "tag": "PATRIOTIC COMMEMORATIVE POSTER",
    "title": "Armed Forces Flag Day Commemorative Poster",
    "desc": "Patriotic commemorative poster honoring Indian Armed Forces with bold typography and national flag accents.",
    "img": "assets/user_projects/flag_day_15-01.jpg",
    "url": "assets/user_projects/flag_day_15-01.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "invitation-card",
    "category": "posters",
    "tag": "EVENT & STATIONERY ART",
    "title": "Luxury Event Invitation Card Design",
    "desc": "Elegant floral border invitation card design crafted with ornate golden accents and classic calligraphy.",
    "img": "assets/user_projects/invitataion_card_.jpg",
    "url": "assets/user_projects/invitataion_card_.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "logo-1",
    "category": "branding",
    "tag": "VECTOR LOGO SUITE",
    "title": "Brand Logo Mark Design #1",
    "desc": "Geometric logo mark explorations across multiple color variations and brand guidelines.",
    "img": "assets/user_projects/log0_1.jpg",
    "url": "assets/user_projects/log0_1.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "logo-3",
    "category": "branding",
    "tag": "VECTOR LOGO SUITE",
    "title": "Minimalist Emblem Mark #3",
    "desc": "High-impact visual monogram mark designed for modern tech and design agencies.",
    "img": "assets/user_projects/logo_3.jpg",
    "url": "assets/user_projects/logo_3.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "logo-4",
    "category": "branding",
    "tag": "VECTOR LOGO SUITE",
    "title": "Geometric Brand Symbol #4",
    "desc": "Symmetrical vector brand mark engineered for digital app icons and print stationery.",
    "img": "assets/user_projects/logo_4.jpg",
    "url": "assets/user_projects/logo_4.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "logo-5",
    "category": "branding",
    "tag": "VECTOR LOGO SUITE",
    "title": "Abstract Creative Mark #5",
    "desc": "Modern dynamic abstract icon designed for creative agencies and tech startups.",
    "img": "assets/user_projects/logo_5.jpg",
    "url": "assets/user_projects/logo_5.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "logo-2",
    "category": "branding",
    "tag": "VECTOR LOGO SUITE",
    "title": "Vector Logo Emblem #2",
    "desc": "Clean minimalist corporate logo design with geometric grid symmetry.",
    "img": "assets/user_projects/logo2.jpg",
    "url": "assets/user_projects/logo2.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "manplution",
    "category": "digital-art",
    "tag": "COMPOSITING & DIGITAL ART",
    "title": "Surreal Photo Manipulation Artwork",
    "desc": "Surreal digital composition blending multiple photographic elements, dramatic color grading, and lighting FX.",
    "img": "assets/user_projects/manplution.jpg",
    "url": "assets/user_projects/manplution.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "mate-painting-2",
    "category": "digital-art",
    "tag": "CONCEPT ART & ENVIRONMENT",
    "title": "Fantasy World Matte Painting",
    "desc": "Surreal environmental concept art depicting mystical architecture and dramatic natural lighting.",
    "img": "assets/user_projects/mate_painting_2.jpg",
    "url": "assets/user_projects/mate_painting_2.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "matte-painting",
    "category": "digital-art",
    "tag": "CONCEPT ART & ENVIRONMENT",
    "title": "Cinematic Environment Matte Painting",
    "desc": "Atmospheric digital landscape matte painting created with multi-layered photo bashing and digital painting.",
    "img": "assets/user_projects/matte_painting.jpg",
    "url": "assets/user_projects/matte_painting.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "milk-mockup",
    "category": "packaging",
    "tag": "PRODUCT CARTON & BOTTLE",
    "title": "Pure Dairy Packaging Suite Mockup",
    "desc": "Organic milk bottle and box package mockup with clean minimalist typography and cow motif.",
    "img": "assets/user_projects/milk_mockup.jpg",
    "url": "assets/user_projects/milk_mockup.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "mockup-package-desgin",
    "category": "packaging",
    "tag": "COMMERCIAL PACKAGING",
    "title": "Retail Display Box Package Mockup",
    "desc": "3D retail box display mockup highlighting structural folds, embossing, and product branding.",
    "img": "assets/user_projects/mockup_package_desgin.jpg",
    "url": "assets/user_projects/mockup_package_desgin.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "music-website-landing-page",
    "category": "uiux",
    "tag": "DARK MODE WEB DESIGN",
    "title": "Music Streaming Web UI Landing Page",
    "desc": "Modern dark mode web landing page for music discovery, featuring hero player visuals and glassmorphism elements.",
    "img": "assets/user_projects/music_website_landing_page.jpg",
    "url": "assets/user_projects/music_website_landing_page.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "package-desgin-1",
    "category": "packaging",
    "tag": "RETAIL PRODUCT PACKAGING",
    "title": "Luxury Box & Pouch Packaging Design",
    "desc": "Premium product box and foil pouch packaging design rendered with realistic lighting.",
    "img": "assets/user_projects/package_desgin_1.jpg",
    "url": "assets/user_projects/package_desgin_1.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "poster-2-01",
    "category": "posters",
    "tag": "ADVERTISING & PROMOTIONAL POSTER",
    "title": "High-Impact Advertising Poster Design",
    "desc": "Bold advertising poster layout engineered for maximum visual contrast and instant audience engagement.",
    "img": "assets/user_projects/poster_2-01.jpg",
    "url": "assets/user_projects/poster_2-01.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "potrait-01",
    "category": "digital-art",
    "tag": "DIGITAL ILLUSTRATION",
    "title": "Vector Digital Portrait Study",
    "desc": "Hand-crafted vector digital portrait emphasizing contour shading, skin highlights, and hair texturing.",
    "img": "assets/user_projects/potrait-01.jpg",
    "url": "assets/user_projects/potrait-01.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "raksha-bandhan",
    "category": "posters",
    "tag": "FESTIVE SOCIAL MEDIA ART",
    "title": "Raksha Bandhan Cultural Festival Poster",
    "desc": "Vibrant Indian cultural festival banner celebrating traditional Rakhi ties with ornate vector graphics.",
    "img": "assets/user_projects/raksha_bandhan.jpg",
    "url": "assets/user_projects/raksha_bandhan.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "sc-png",
    "category": "uiux",
    "tag": "UI/UX & COMPOSITING",
    "title": "Screen Composition & UI Showcase",
    "desc": "Screen composition showcase demonstrating user interface layout, typography, and visual hierarchy.",
    "img": "assets/user_projects/sc.png",
    "url": "assets/user_projects/sc.png",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "visting-card-mockup",
    "category": "branding",
    "tag": "CORPORATE CARD MOCKUP",
    "title": "Minimalist Visiting Card Mockup",
    "desc": "Dual-sided clean business card layout with rounded edges and tactile paper texture rendering.",
    "img": "assets/user_projects/visting_card_mockup.jpg",
    "url": "assets/user_projects/visting_card_mockup.jpg",
    "linkText": "View Project",
    "isExternal": true
  },
  {
    "id": "video-1",
    "category": "motion",
    "tag": "MOTION GRAPHICS & VIDEO",
    "title": "Motion Design Video Reel 1",
    "desc": "Dynamic motion graphics video showcase displaying animated visual effects, transitions, and motion editing.",
    "img": "assets/user_projects/video1_poster.jpg",
    "url": "assets/user_projects/video1.mp4",
    "linkText": "Watch Video",
    "isExternal": true
  },
  {
    "id": "video-2",
    "category": "motion",
    "tag": "MOTION GRAPHICS & VIDEO",
    "title": "Motion Graphics Reel 2",
    "desc": "High-energy motion graphic reel presenting typography animation, visual compositing, and creative transitions.",
    "img": "assets/user_projects/video2_poster.jpg",
    "url": "assets/user_projects/video2.mp4",
    "linkText": "Watch Video",
    "isExternal": true
  },
  {
    "id": "web-template-pdf",
    "category": "uiux",
    "tag": "WEB DESIGN DOCUMENTATION",
    "title": "Web Template Specification (PDF)",
    "desc": "Comprehensive web template design specification document containing full website wireframes and component layouts.",
    "img": "assets/user_projects/sc.png",
    "url": "assets/user_projects/web_template.pdf",
    "linkText": "Download PDF",
    "isExternal": true
  }
];

  class CurvedSlider {
    constructor() {
      this.viewport = document.getElementById('curvedSliderViewport');
      this.stage = document.getElementById('curvedSliderStage');
      this.cursor = document.getElementById('curvedSliderCursor');
      this.prevBtn = document.getElementById('sliderPrevBtn');
      this.nextBtn = document.getElementById('sliderNextBtn');
      this.counterCurrent = document.getElementById('sliderCounterCurrent');
      this.counterTotal = document.getElementById('sliderCounterTotal');
      this.progressBar = document.getElementById('sliderProgressBar');

      if (!this.viewport || !this.stage) return;

      this.projects = ALL_PROJECTS;
      this.total = this.projects.length;

      // Continuous offset for infinite looping
      this.currentOffset = 0;
      this.targetOffset = 0;

      // Interaction state
      this.isDragging = false;
      this.startX = 0;
      this.dragStartOffset = 0;
      this.hasDraggedSignificantly = false;

      // Cursor follower state
      this.cursorX = window.innerWidth / 2;
      this.cursorY = window.innerHeight / 2;
      this.targetCursorX = this.cursorX;
      this.targetCursorY = this.cursorY;

      // Autoplay
      this.autoplayTimer = null;
      this.isHovered = false;

      // Initialize
      this.initCards();
      this.initCounter();
      this.bindEvents();
      this.startLoop();
      this.startAutoplay();
    }

    initCards() {
      this.cards = [];
      this.stage.innerHTML = '';

      this.projects.forEach((proj, idx) => {
        const card = document.createElement('div');
        card.className = 'curved-slider-card';
        card.setAttribute('data-index', idx);
        card.setAttribute('data-category', proj.category);

        card.innerHTML = `
          <div class="curved-slider-card-media">
            <img src="${proj.img}" alt="${proj.title}" class="curved-slider-card-img" loading="lazy" />
          </div>
          <div class="curved-slider-card-overlay">
            <div class="curved-slider-card-top">
              <span class="curved-slider-tag">${proj.tag}</span>
            </div>
            <div class="curved-slider-card-body">
              <h3 class="curved-slider-card-title">${proj.title}</h3>
              <p class="curved-slider-card-desc">${proj.desc}</p>
              <a href="${proj.url}" ${proj.isExternal ? 'target="_blank" rel="noopener noreferrer"' : ''} class="curved-slider-card-link">
                ${proj.linkText}
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="7" y1="17" x2="17" y2="7"></line>
                  <polyline points="7 7 17 7 17 17"></polyline>
                </svg>
              </a>
            </div>
          </div>
        `;

        // Card click handling: click side card brings to center, click center card opens link
        card.addEventListener('click', (e) => {
          if (this.hasDraggedSignificantly) return;
          const activeIdx = this.getWrappedIndex(Math.round(this.targetOffset));
          if (idx !== activeIdx) {
            e.preventDefault();
            this.goToNearest(idx);
          }
        });

        this.stage.appendChild(card);
        this.cards.push(card);
      });
    }

    initCounter() {
      if (this.counterTotal) {
        this.counterTotal.textContent = String(this.total).padStart(2, '0');
      }
      this.updateCounter();
    }

    getWrappedIndex(idx) {
      return ((idx % this.total) + this.total) % this.total;
    }

    bindEvents() {
      // Prev / Next buttons
      if (this.prevBtn) {
        this.prevBtn.addEventListener('click', () => {
          this.targetOffset -= 1;
          this.updateCounter();
          this.resetAutoplay();
        });
      }
      if (this.nextBtn) {
        this.nextBtn.addEventListener('click', () => {
          this.targetOffset += 1;
          this.updateCounter();
          this.resetAutoplay();
        });
      }

      // Pointer drag interaction
      this.viewport.addEventListener('pointerdown', (e) => this.onPointerDown(e));
      window.addEventListener('pointermove', (e) => this.onPointerMove(e));
      window.addEventListener('pointerup', () => this.onPointerUp());
      window.addEventListener('pointercancel', () => this.onPointerUp());

      // Cursor follower hover
      this.viewport.addEventListener('mouseenter', () => {
        this.isHovered = true;
        if (this.cursor) this.cursor.classList.add('is-visible');
        this.stopAutoplay();
      });

      this.viewport.addEventListener('mouseleave', () => {
        this.isHovered = false;
        if (this.cursor && !this.isDragging) this.cursor.classList.remove('is-visible');
        this.startAutoplay();
      });

      // Keyboard navigation
      window.addEventListener('keydown', (e) => {
        const rect = this.viewport.getBoundingClientRect();
        const isInView = rect.top < window.innerHeight && rect.bottom > 0;
        if (!isInView) return;

        if (e.key === 'ArrowLeft') {
          this.targetOffset -= 1;
          this.updateCounter();
          this.resetAutoplay();
        } else if (e.key === 'ArrowRight') {
          this.targetOffset += 1;
          this.updateCounter();
          this.resetAutoplay();
        }
      });
    }

    onPointerDown(e) {
      this.isDragging = true;
      this.hasDraggedSignificantly = false;
      this.startX = e.clientX;
      this.dragStartOffset = this.targetOffset;
      this.viewport.classList.add('is-dragging');
      if (this.cursor) this.cursor.classList.add('is-active');
      this.stopAutoplay();
    }

    onPointerMove(e) {
      this.targetCursorX = e.clientX;
      this.targetCursorY = e.clientY;

      if (!this.isDragging) return;

      const diffX = e.clientX - this.startX;
      if (Math.abs(diffX) > 6) {
        this.hasDraggedSignificantly = true;
      }

      const stepWidth = window.innerWidth < 768 ? 260 : 330;
      const deltaIndex = -diffX / stepWidth;
      this.targetOffset = this.dragStartOffset + deltaIndex;
      this.updateCounter();
    }

    onPointerUp() {
      if (!this.isDragging) return;
      this.isDragging = false;
      this.viewport.classList.remove('is-dragging');
      if (this.cursor) this.cursor.classList.remove('is-active');

      // Snap smoothly to nearest integer
      this.targetOffset = Math.round(this.targetOffset);
      this.updateCounter();
      this.startAutoplay();
    }

    goToNearest(targetIdx) {
      const currentNorm = this.getWrappedIndex(Math.round(this.targetOffset));
      let diff = targetIdx - currentNorm;
      // Shortest circular path
      if (diff > this.total / 2) diff -= this.total;
      if (diff < -this.total / 2) diff += this.total;

      this.targetOffset = Math.round(this.targetOffset) + diff;
      this.updateCounter();
      this.resetAutoplay();
    }

    updateCounter() {
      const activeIdx = this.getWrappedIndex(Math.round(this.targetOffset));
      if (this.counterCurrent) {
        this.counterCurrent.textContent = String(activeIdx + 1).padStart(2, '0');
      }
      if (this.progressBar) {
        const pct = ((activeIdx + 1) / this.total) * 100;
        this.progressBar.style.width = `${pct.toFixed(1)}%`;
      }
    }

    startAutoplay() {
      this.stopAutoplay();
      this.autoplayTimer = setInterval(() => {
        if (!this.isHovered && !this.isDragging) {
          this.targetOffset += 1;
          this.updateCounter();
        }
      }, 4500);
    }

    stopAutoplay() {
      if (this.autoplayTimer) {
        clearInterval(this.autoplayTimer);
        this.autoplayTimer = null;
      }
    }

    resetAutoplay() {
      this.stopAutoplay();
      this.startAutoplay();
    }

    startLoop() {
      const render = () => {
        const lerpFactor = this.isDragging ? 0.22 : 0.12;
        this.currentOffset += (this.targetOffset - this.currentOffset) * lerpFactor;

        this.renderCards();

        if (this.cursor) {
          this.cursorX += (this.targetCursorX - this.cursorX) * 0.25;
          this.cursorY += (this.targetCursorY - this.cursorY) * 0.25;
          this.cursor.style.left = `${this.cursorX}px`;
          this.cursor.style.top = `${this.cursorY}px`;
        }

        requestAnimationFrame(render);
      };

      requestAnimationFrame(render);
    }

    renderCards() {
      const isMobile = window.innerWidth < 768;
      const radius = isMobile ? 650 : 960;
      const stepAngleDeg = isMobile ? 22 : 18;
      const stepAngleRad = (stepAngleDeg * Math.PI) / 180;

      // Current fractional offset normalized to [0, total)
      const normOffset = ((this.currentOffset % this.total) + this.total) % this.total;

      this.cards.forEach((card, idx) => {
        // Compute circular distance between idx and normOffset in [-total/2, total/2]
        let delta = idx - normOffset;
        if (delta > this.total / 2) delta -= this.total;
        if (delta < -this.total / 2) delta += this.total;

        const absDelta = Math.abs(delta);

        // Cull cards that are beyond visible panoramic arc
        if (absDelta > 3.4) {
          card.style.display = 'none';
          return;
        }

        card.style.display = 'block';

        // Concave cylinder 3D math
        const theta = delta * stepAngleRad;
        const transX = radius * Math.sin(theta);
        const transZ = radius * (Math.cos(theta) - 1);
        const rotY = -delta * stepAngleDeg;

        const scale = Math.max(0.72, 1 - absDelta * 0.055);
        const opacity = Math.max(0, 1 - absDelta * 0.24);
        const zIndex = Math.round(100 - absDelta * 10);

        card.style.transform = `translate3d(${transX.toFixed(1)}px, 0px, ${transZ.toFixed(1)}px) rotateY(${rotY.toFixed(1)}deg) scale(${scale.toFixed(3)})`;
        card.style.opacity = opacity.toFixed(3);
        card.style.zIndex = zIndex;

        if (absDelta < 0.45) {
          card.classList.add('is-center');
        } else {
          card.classList.remove('is-center');
        }
      });
    }
  }

  // Auto-initialize
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => new CurvedSlider());
  } else {
    new CurvedSlider();
  }
})();
