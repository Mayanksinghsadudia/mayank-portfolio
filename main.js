// Portfolio Interactive JavaScript Engine

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const desktopNav = document.getElementById('desktop-nav');
  
  if (mobileBtn && desktopNav) {
    const closeMenu = () => {
      desktopNav.classList.remove('active');
      mobileBtn.setAttribute('aria-expanded', 'false');
      mobileBtn.setAttribute('aria-label', 'Open navigation');
    };
    mobileBtn.addEventListener('click', () => {
      const open = desktopNav.classList.toggle('active');
      mobileBtn.setAttribute('aria-expanded', String(open));
      mobileBtn.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    });
    desktopNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
    document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(); });
  }

  // Active Section Scroll Tracker
  const sections = document.querySelectorAll('section.page-section, section.hero-section');
  const navLinks = document.querySelectorAll('nav.desktop-nav a');

  window.addEventListener('scroll', () => {
    let current = '';
    const scrollPosition = window.scrollY + 200;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

  // Project Gallery Filter & View All Toggle Logic
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  const viewAllBtn = document.getElementById('view-all-projects-btn');
  const viewAllContainer = document.getElementById('view-all-container');

  let isExpanded = false;

  // View All Projects Button Click
  if (viewAllBtn) {
    viewAllBtn.addEventListener('click', () => {
      isExpanded = true;
      projectCards.forEach(card => {
        card.classList.add('show-extra');
        card.style.display = 'block';
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
      });
      if (viewAllContainer) viewAllContainer.style.display = 'none';
    });
  }

  // Category Filter Buttons Click
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      if (filter !== 'all') {
        if (viewAllContainer) viewAllContainer.style.display = 'none';
      } else if (!isExpanded) {
        if (viewAllContainer) viewAllContainer.style.display = 'block';
      }

      projectCards.forEach((card, index) => {
        const category = card.getAttribute('data-category');
        const isMatch = (filter === 'all' || category === filter);

        if (filter === 'all' && !isExpanded && index >= 6) {
          card.style.display = 'none';
        } else if (isMatch) {
          card.style.display = 'block';
          card.style.opacity = '1';
          card.style.transform = 'scale(1)';
        } else {
          card.style.opacity = '0';
          card.style.transform = 'scale(0.95)';
          setTimeout(() => {
            if (card.style.opacity === '0') card.style.display = 'none';
          }, 200);
        }
      });
    });
  });

  // Lightbox Modal System
  const modalBackdrop = document.getElementById('project-modal');
  const modalImg = document.getElementById('modal-img');
  const modalTitle = document.getElementById('modal-title');
  const modalCategory = document.getElementById('modal-category');
  const modalDesc = document.getElementById('modal-desc');
  const modalTools = document.getElementById('modal-tools');
  const modalClose = document.getElementById('modal-close');

  const projectData = {
    'dobby': {
      title: 'HP7 Dobby Geometric Polygon Art',
      category: 'Illustration & Art Study',
      image: 'assets/dobby_lowpoly.jpg',
      desc: 'High-contrast low-poly geometric artwork depicting Dobby from Harry Potter (HP7). Built with meticulous polygon mesh placement, dramatic shadows, and high-chroma eye focal points.',
      tools: ['Photoshop', 'Illustrator', 'CorelDraw', 'Polygon Mesh']
    },
    'swastik': {
      title: 'Swastik Gifts Visual Identity',
      category: 'Branding & Logo Design',
      image: 'assets/swastik_gifts.jpg',
      desc: 'Minimalist brand identity for Swastik Gifts. Includes monochrome, inverted dark mode, and vibrant purple/orange butterfly gift box concept marks.',
      tools: ['Illustrator', 'Canva', 'Brand Guidelines']
    },
    'dragon': {
      title: 'Dragon Energy Beverage Packaging',
      category: 'Package Design & 3D Render',
      image: 'assets/dragon_energy.jpg',
      desc: 'High-impact packaging design for 500 ML Ultra Can & 250 ML Ultra Can. Rendered on realistic rustic wooden texture backdrop with frozen ice accents.',
      tools: ['Photoshop', '3D Mockup', 'CorelDraw', 'Illustrator']
    },
    'corporate': {
      title: 'Jhon Walker Corporate Identity Suite',
      category: 'Corporate Branding & Stationery',
      image: 'assets/corporate_identity.jpg',
      desc: 'Complete high-end corporate identity package featuring geometric M logo motif across leather notebook, letterhead, business cards, binder clips, and writing instruments on maroon paper texture.',
      tools: ['Illustrator', 'Photoshop', 'InDesign', 'Stationery Suite']
    },
    'samridhi': {
      title: 'Samridhi Haute Couture Poster',
      category: 'Posters & Event Banner',
      image: 'assets/samridhi_couture.jpg',
      desc: 'Sophisticated event banner and promotional poster for Samridhi Haute Couture Exhibition. Combines luxury typography with high-fashion model imagery.',
      tools: ['Photoshop', 'Canva', 'Typography Art']
    }
  };

  projectCards.forEach(card => {
    card.addEventListener('click', (e) => {
      // Don't trigger modal if user clicks directly on video controls or PDF download links
      if (e.target.closest('a, button, video')) return;

      const media = card.querySelector('.project-img, video');
      const title = card.querySelector('h3');
      const category = card.querySelector('.text-accent');
      const desc = card.querySelector('p');
      const toolsText = card.querySelector('.project-meta span');

      if (media && title) {
        const modalMediaWrapper = modalImg.parentElement;
        
        // Remove any previous modal video
        const existingVideo = modalMediaWrapper.querySelector('video');
        if (existingVideo) existingVideo.remove();

        if (media.tagName === 'VIDEO') {
          modalImg.style.display = 'none';
          const videoElem = document.createElement('video');
          videoElem.src = media.src;
          videoElem.controls = true;
          videoElem.autoplay = true;
          videoElem.loop = true;
          videoElem.muted = true;
          videoElem.playsInline = true;
          videoElem.style.width = '100%';
          videoElem.style.maxHeight = '70vh';
          videoElem.style.objectFit = 'contain';
          videoElem.style.borderRadius = '8px';
          modalMediaWrapper.appendChild(videoElem);
        } else {
          modalImg.style.display = 'block';
          modalImg.src = media.src;
        }

        modalTitle.textContent = title.textContent;
        modalCategory.textContent = category ? category.textContent : 'GRAPHIC DESIGN PROJECT';
        modalDesc.textContent = desc ? desc.textContent : '';

        modalTools.innerHTML = '';
        if (toolsText) {
          const tools = toolsText.textContent.split('&').map(t => t.trim());
          tools.forEach(tool => {
            const span = document.createElement('span');
            span.className = 'tool-tag highlight';
            span.textContent = tool;
            modalTools.appendChild(span);
          });
        }

        modalBackdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', closeModal);
  }

  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeModal();
    });
  }

  function closeModal() {
    const modalVideo = modalBackdrop.querySelector('video');
    if (modalVideo) {
      modalVideo.pause();
      modalVideo.remove();
    }
    modalBackdrop.classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  // Copy to Clipboard Utility
  window.copyText = function(text, label) {
    navigator.clipboard.writeText(text).then(() => {
      showToast(`${label} copied to clipboard!`);
    });
  };

  // =========================================================================
  // TOAST NOTIFICATION UTILITY
  // =========================================================================
  function showToast(message) {
    const toast = document.getElementById('toast-msg');
    if (toast) {
      toast.textContent = message;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 3500);
    }
  }
  window.showToast = showToast;

  // Contact Form Submission Handler
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const phone = document.getElementById('phone').value || 'Not provided';
      const projectType = document.getElementById('project-type').value;
      const message = document.getElementById('message').value;

      showToast('Sending your message directly to Mayank...');

      fetch('https://formsubmit.co/ajax/mayanksadudia@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          name: name,
          email: email,
          phone: phone,
          project_type: projectType,
          message: message,
          _subject: `New Portfolio Design Inquiry from ${name} [${projectType.toUpperCase()}]`
        })
      })
      .then(response => response.json())
      .then(data => {
        showToast('Thank you! Your inquiry was delivered directly to Mayank.');
        contactForm.reset();
      })
      .catch(() => {
        const subject = `Design Inquiry from ${name} [${projectType.toUpperCase()}]`;
        const body = `Hi Mayank,\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nProject: ${projectType}\n\nMessage:\n${message}`;
        window.location.href = `mailto:mayanksadudia@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        showToast('Opening email client to reach Mayank.');
        contactForm.reset();
      });
    });
  }

  // =========================================================================
  // 3D ORBIT: CARDS MOTION ENGINE (Jitter-Inspired Curved 3D Orbit Animation)
  // =========================================================================
  function initProjectOrbitAnimation() {
    const container = document.getElementById('orbit-showcase-section');
    const viewport = document.getElementById('orbit-viewport');
    const track = document.getElementById('orbit-track');
    const cards = document.querySelectorAll('.orbit-card');
    const prevBtn = document.getElementById('orbit-prev-btn');
    const nextBtn = document.getElementById('orbit-next-btn');
    const playBtn = document.getElementById('orbit-play-btn');
    const playIcon = document.getElementById('orbit-play-icon');
    const counter = document.getElementById('orbit-counter');

    if (!container || !viewport || !track || cards.length === 0) return;

    const totalCards = cards.length;
    let angle = 0; // Current global orbit rotation in radians
    let targetAngle = 0;
    let isAutoOrbiting = true;
    let isDragging = false;
    let startX = 0;
    let lastDragX = 0;
    let lastDragTime = 0;
    let dragVelocity = 0;
    let animId = null;

    // Dynamically calculate orbit geometry based on current viewport width
    function getRadii() {
      const w = viewport.clientWidth;
      if (w < 600) {
        return { rx: 210, rz: 110, ryCurve: 26, baseScale: 0.82 };
      } else if (w < 992) {
        return { rx: 320, rz: 145, ryCurve: 36, baseScale: 0.92 };
      } else {
        return { rx: 430, rz: 180, ryCurve: 46, baseScale: 1.0 };
      }
    }

    // Project each card onto the 3D cylindrical orbital arc
    function updateCards() {
      const { rx, rz, ryCurve, baseScale } = getRadii();
      const step = (Math.PI * 2) / totalCards;
      let closestIndex = 0;
      let maxCos = -2;

      cards.forEach((card, i) => {
        const phi = angle + (i * step);
        // Normalize angle to [-PI, PI] for smooth symmetric calculations
        const normPhi = ((phi + Math.PI) % (Math.PI * 2) + Math.PI * 2) % (Math.PI * 2) - Math.PI;

        const sinPhi = Math.sin(normPhi);
        const cosPhi = Math.cos(normPhi);

        if (cosPhi > maxCos) {
          maxCos = cosPhi;
          closestIndex = i;
        }

        // Curved 3D coordinates
        const x = sinPhi * rx;
        const z = cosPhi * rz;
        const y = (1 - cosPhi) * ryCurve; // Parabolic dip on flanks

        // Rotations matching Jitter Orbit: Cards perspective
        const rotY = -sinPhi * 36; // Yaw towards focal point
        const rotZ = -sinPhi * 9;  // Inward roll tilt
        const scale = (0.74 + 0.34 * ((cosPhi + 1) / 2)) * baseScale;
        
        // Z-Index ordering so front cards naturally overlap back cards
        const zIndex = Math.round((cosPhi + 1) * 100);
        // Fade out cards moving along the back of the orbit
        const opacity = cosPhi > -0.2 ? Math.min(1, ((cosPhi + 0.2) / 0.8) * 0.9 + 0.1) : 0;
        const brightness = 0.65 + 0.35 * Math.max(0, cosPhi);

        card.style.transform = `translate3d(${x.toFixed(1)}px, ${y.toFixed(1)}px, ${z.toFixed(1)}px) rotateY(${rotY.toFixed(1)}deg) rotateZ(${rotZ.toFixed(1)}deg) scale(${scale.toFixed(3)})`;
        card.style.zIndex = zIndex;
        card.style.opacity = opacity.toFixed(2);
        card.style.filter = `brightness(${brightness.toFixed(2)})`;
        card.style.pointerEvents = opacity > 0.45 ? 'auto' : 'none';

        if (cosPhi > 0.92) {
          card.classList.add('is-active-center');
        } else {
          card.classList.remove('is-active-center');
        }
      });

      if (counter) {
        counter.textContent = `0${closestIndex + 1} // 0${totalCards} FEATURED`;
      }
    }

    // 60fps RequestAnimationFrame Loop
    function tick() {
      if (isAutoOrbiting && !isDragging) {
        angle += 0.0035; // Silky-smooth constant orbital motion
        targetAngle = angle;
      } else if (!isDragging) {
        // Damped easing toward targetAngle
        angle += (targetAngle - angle) * 0.085;
      }
      updateCards();
      animId = requestAnimationFrame(tick);
    }

    tick();

    // Pointer Interaction (Mouse & Touch Drag Support)
    function onPointerDown(e) {
      isDragging = true;
      startX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      lastDragX = startX;
      lastDragTime = performance.now();
      dragVelocity = 0;
    }

    function onPointerMove(e) {
      if (!isDragging) return;
      const currentX = e.clientX || (e.touches && e.touches[0].clientX) || 0;
      const deltaX = currentX - lastDragX;
      lastDragX = currentX;
      const now = performance.now();
      const dt = now - lastDragTime;
      lastDragTime = now;
      if (dt > 0) {
        dragVelocity = deltaX / dt;
      }
      const moveFactor = (deltaX / (viewport.clientWidth || 800)) * 2.4;
      angle += moveFactor;
      targetAngle = angle;
    }

    function onPointerUp() {
      if (!isDragging) return;
      isDragging = false;
      const step = (Math.PI * 2) / totalCards;
      // Snap to nearest card step with gentle inertia
      targetAngle = Math.round((angle + dragVelocity * 0.14) / step) * step;
    }

    viewport.addEventListener('mousedown', onPointerDown);
    window.addEventListener('mousemove', onPointerMove);
    window.addEventListener('mouseup', onPointerUp);

    viewport.addEventListener('touchstart', onPointerDown, { passive: true });
    window.addEventListener('touchmove', onPointerMove, { passive: true });
    window.addEventListener('touchend', onPointerUp, { passive: true });

    // Hover pause auto-orbit
    viewport.addEventListener('mouseenter', () => {
      isAutoOrbiting = false;
    });

    viewport.addEventListener('mouseleave', () => {
      if (playBtn && playBtn.classList.contains('active')) {
        isAutoOrbiting = true;
      }
    });

    // Step Controls (Previous & Next Arrow Buttons)
    const cardStep = (Math.PI * 2) / totalCards;
    if (prevBtn) {
      prevBtn.addEventListener('click', () => {
        targetAngle += cardStep;
        isAutoOrbiting = false;
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => {
        targetAngle -= cardStep;
        isAutoOrbiting = false;
      });
    }

    // Auto-Orbit Play/Pause Toggle
    if (playBtn) {
      playBtn.addEventListener('click', () => {
        isAutoOrbiting = !isAutoOrbiting;
        if (isAutoOrbiting) {
          playBtn.classList.add('active');
          if (playIcon) playIcon.textContent = 'pause';
        } else {
          playBtn.classList.remove('active');
          if (playIcon) playIcon.textContent = 'play_arrow';
        }
      });
    }

    // Card Click: Rotate to Center or Open Full Project Modal
    cards.forEach((card, index) => {
      card.addEventListener('click', () => {
        const step = (Math.PI * 2) / totalCards;
        const phi = angle + (index * step);
        const normPhi = ((phi + Math.PI) % (Math.PI * 2) + Math.PI * 2) % (Math.PI * 2) - Math.PI;
        const cosPhi = Math.cos(normPhi);

        if (cosPhi > 0.90) {
          // Front center card: trigger the project lightbox modal
          const projectId = card.getAttribute('data-id');
          const gridCard = document.querySelector(`.projects-grid .project-card[data-id="${projectId}"]`);
          if (gridCard) {
            gridCard.click();
          }
        } else {
          // Flank card: smoothly spin that card to front center
          isAutoOrbiting = false;
          targetAngle = angle - normPhi;
        }
      });
    });

    window.addEventListener('resize', updateCards);
  }

  // Initialize 3D Orbit Cards Showcase
  initProjectOrbitAnimation();
});
