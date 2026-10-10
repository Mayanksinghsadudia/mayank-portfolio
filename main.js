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

  // Project Section Master Split Tabs & Category Filters
  const splitTabBtns = document.querySelectorAll('.split-tab-btn');
  const subsectionAnalytics = document.getElementById('subsection-data-analyst');
  const subsectionDesign = document.getElementById('subsection-graphic-design');
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  const viewAllBtn = document.getElementById('view-all-projects-btn');
  const viewAllContainer = document.getElementById('view-all-container');

  let isDesignExpanded = false;

  // 1. Master Split Tabs (All Projects vs Data Analyst vs Graphic Design)
  if (splitTabBtns.length > 0) {
    splitTabBtns.forEach(tab => {
      tab.addEventListener('click', () => {
        splitTabBtns.forEach(t => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        const tabType = tab.getAttribute('data-tab');

        if (tabType === 'analytics') {
          if (subsectionAnalytics) subsectionAnalytics.style.display = 'block';
          if (subsectionDesign) subsectionDesign.style.display = 'none';
        } else if (tabType === 'design') {
          if (subsectionAnalytics) subsectionAnalytics.style.display = 'none';
          if (subsectionDesign) subsectionDesign.style.display = 'block';
        } else {
          // 'all'
          if (subsectionAnalytics) subsectionAnalytics.style.display = 'block';
          if (subsectionDesign) subsectionDesign.style.display = 'block';
        }
      });
    });
  }

  // 2. View All Graphic Design Projects Button Click
  if (viewAllBtn) {
    viewAllBtn.addEventListener('click', () => {
      isDesignExpanded = true;
      const designCards = subsectionDesign ? subsectionDesign.querySelectorAll('.project-card') : [];
      designCards.forEach(card => {
        card.classList.add('show-extra');
        card.style.display = 'block';
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
      });
      if (viewAllContainer) viewAllContainer.style.display = 'none';
    });
  }

  // 3. Graphic Design Category Sub-Filters
  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');
      const designCards = subsectionDesign ? subsectionDesign.querySelectorAll('.project-card') : [];

      if (filter !== 'all-design' && filter !== 'all') {
        if (viewAllContainer) viewAllContainer.style.display = 'none';
      } else if (!isDesignExpanded) {
        if (viewAllContainer) viewAllContainer.style.display = 'block';
      }

      designCards.forEach((card, index) => {
        const category = card.getAttribute('data-category');
        const isMatch = (filter === 'all-design' || filter === 'all' || category === filter);

        if ((filter === 'all-design' || filter === 'all') && !isDesignExpanded && index >= 6) {
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
});
