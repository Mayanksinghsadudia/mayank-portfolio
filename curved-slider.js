/**
 * 3D Curved Slider Engine (Infinite Cylinder Arc)
 * Inspired by Dribbble Shot 27605260 (3D Curved Slider for Elementor by Devzeno Studio)
 * Implements concave cylinder 3D perspective, infinite continuous looping,
 * interactive DRAG cursor follower, momentum swipe, and keyboard controls.
 */

(function () {
  'use strict';

  // Curated Portfolio Projects for Mayank Singh Sadudia
  const PROJECTS = [
    {
      id: 'mustang-1968',
      tag: 'Interactive 3D Web',
      title: 'Ford Mustang 1968 3D Experience',
      desc: 'Real-time 3D automotive showcase with interactive camera orbit, lighting controls, and shaders.',
      img: 'assets/user_projects/ford_mustang_1968.jpg',
      url: 'https://mayanksinghsadudia.github.io/ford-mustang-1968-showcase/',
      isExternal: true
    },
    {
      id: 'reva-speaker',
      tag: '3D Hardware Web App',
      title: 'REVA 3D Exploding Speaker',
      desc: 'Interactive audio hardware visualization featuring exploded view component animation and sound mechanics.',
      img: 'assets/user_projects/reva_speaker.jpg',
      url: 'https://mayanksinghsadudia.github.io/reva-3d-speaker-website/',
      isExternal: true
    },
    {
      id: 'amazon-nlp',
      tag: 'NLP & Data Analytics',
      title: 'Amazon Review Sentiment Classifier',
      desc: 'Natural Language Processing pipeline classifying reviews with VADER & Google Sheets live integration.',
      img: 'assets/user_projects/amazon-project.svg',
      url: 'amazon-sentiment-analysis.html',
      isExternal: false
    },
    {
      id: 'retail-analysis',
      tag: 'Data Science · Python & SQL',
      title: 'Online Retail Sales Analysis',
      desc: 'Statistical portfolio study of 541,909 historical transactions: country sales distributions and metrics.',
      img: 'retail-analysis-preview.png',
      url: 'retail-analysis.html',
      isExternal: false
    },
    {
      id: 'customer-management',
      tag: 'Business Reporting',
      title: 'Customer Management System',
      desc: 'Relational SQLite architecture with customer profiling, SQL revenue aggregations, and business metrics.',
      img: 'assets/user_projects/customer-project.svg',
      url: 'cms-analysis.html',
      isExternal: false
    },
    {
      id: 'lifecare-health',
      tag: 'Healthcare Analytics',
      title: 'Lifecare Clinical Portal',
      desc: 'Medical triage prototype featuring patient and doctor indexing, appointment requests, and clinical workflow.',
      img: 'assets/user_projects/lifecare-project.svg',
      url: 'lifecare-health-system.html',
      isExternal: false
    },
    {
      id: 'red-chillies-vfx',
      tag: 'Digital Art & Matte',
      title: 'Red Chillies VFX Studio Matte Art',
      desc: 'Atmospheric digital landscape compositing and cinematic matte painting for visual storytelling.',
      img: 'assets/user_projects/matte_painting.jpg',
      url: 'assets/user_projects/matte_painting.jpg',
      isExternal: true
    },
    {
      id: 'motion-reel',
      tag: 'Motion Design & Video',
      title: 'Cinematic Motion Graphics Reel',
      desc: 'High-energy typography animation, dynamic visual compositing, and creative kinetic effects in After Effects.',
      img: 'assets/user_projects/video1_poster.jpg',
      url: 'assets/user_projects/video1.mp4',
      isExternal: true
    },
    {
      id: 'energy-drink',
      tag: 'Branding & Packaging',
      title: 'Torq Energy Drink Packaging Design',
      desc: '3D structural packaging mockup, typography hierarchy, and dynamic label branding for retail products.',
      img: 'assets/user_projects/energy_drink_mockup.jpg',
      url: 'assets/user_projects/energy_drink_mockup.jpg',
      isExternal: true
    },
    {
      id: 'music-web',
      tag: 'UI/UX & Web Design',
      title: 'BeatWave Music Streaming Platform',
      desc: 'Dark-mode audio interface design, artist spotlight components, and design system documentation.',
      img: 'assets/user_projects/music_website_landing_page.jpg',
      url: 'assets/user_projects/music_website_landing_page.jpg',
      isExternal: true
    }
  ];

  class CurvedSlider {
    constructor() {
      this.viewport = document.getElementById('curvedSliderViewport');
      this.stage = document.getElementById('curvedSliderStage');
      this.cursor = document.getElementById('curvedSliderCursor');
      this.prevBtn = document.getElementById('sliderPrevBtn');
      this.nextBtn = document.getElementById('sliderNextBtn');
      this.dotsContainer = document.getElementById('sliderDots');

      if (!this.viewport || !this.stage) return;

      this.projects = PROJECTS;
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
      this.initDots();
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
                View Project 
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                  <line x1="7" y1="17" x2="17" y2="7"></line>
                  <polyline points="7 7 17 7 17 17"></polyline>
                </svg>
              </a>
            </div>
          </div>
        `;

        // Card click handling
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

    initDots() {
      if (!this.dotsContainer) return;
      this.dotsContainer.innerHTML = '';
      this.dots = [];

      this.projects.forEach((_, idx) => {
        const dot = document.createElement('div');
        dot.className = `curved-slider-dot ${idx === 0 ? 'is-active' : ''}`;
        dot.setAttribute('data-index', idx);
        dot.addEventListener('click', () => this.goToNearest(idx));
        this.dotsContainer.appendChild(dot);
        this.dots.push(dot);
      });
    }

    getWrappedIndex(idx) {
      return ((idx % this.total) + this.total) % this.total;
    }

    bindEvents() {
      // Prev / Next buttons
      if (this.prevBtn) {
        this.prevBtn.addEventListener('click', () => {
          this.targetOffset -= 1;
          this.updateDots();
          this.resetAutoplay();
        });
      }
      if (this.nextBtn) {
        this.nextBtn.addEventListener('click', () => {
          this.targetOffset += 1;
          this.updateDots();
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
          this.updateDots();
          this.resetAutoplay();
        } else if (e.key === 'ArrowRight') {
          this.targetOffset += 1;
          this.updateDots();
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

      const stepWidth = window.innerWidth < 768 ? 260 : 340;
      const deltaIndex = -diffX / stepWidth;
      this.targetOffset = this.dragStartOffset + deltaIndex;
    }

    onPointerUp() {
      if (!this.isDragging) return;
      this.isDragging = false;
      this.viewport.classList.remove('is-dragging');
      if (this.cursor) this.cursor.classList.remove('is-active');

      // Snap smoothly to nearest integer
      this.targetOffset = Math.round(this.targetOffset);
      this.updateDots();
      this.startAutoplay();
    }

    goToNearest(targetIdx) {
      const currentNorm = this.getWrappedIndex(Math.round(this.targetOffset));
      let diff = targetIdx - currentNorm;
      // Shortest circular path
      if (diff > this.total / 2) diff -= this.total;
      if (diff < -this.total / 2) diff += this.total;

      this.targetOffset = Math.round(this.targetOffset) + diff;
      this.updateDots();
      this.resetAutoplay();
    }

    updateDots() {
      const activeIdx = this.getWrappedIndex(Math.round(this.targetOffset));
      if (this.dots) {
        this.dots.forEach((dot, idx) => {
          if (idx === activeIdx) {
            dot.classList.add('is-active');
          } else {
            dot.classList.remove('is-active');
          }
        });
      }
    }

    startAutoplay() {
      this.stopAutoplay();
      this.autoplayTimer = setInterval(() => {
        if (!this.isHovered && !this.isDragging) {
          this.targetOffset += 1;
          this.updateDots();
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
