// Portfolio Interactive JavaScript Engine

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const desktopNav = document.getElementById('desktop-nav');
  
  if (mobileBtn) {
    mobileBtn.addEventListener('click', () => {
      desktopNav.classList.toggle('active');
      if (desktopNav.style.display === 'flex') {
        desktopNav.style.display = 'none';
      } else {
        desktopNav.style.display = 'flex';
        desktopNav.style.flexDirection = 'column';
        desktopNav.style.position = 'absolute';
        desktopNav.style.top = '72px';
        desktopNav.style.left = '0';
        desktopNav.style.width = '100%';
        desktopNav.style.backgroundColor = '#131313';
        desktopNav.style.padding = '20px';
        desktopNav.style.borderBottom = '1px solid #262626';
      }
    });
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
        // Automatically show all matching projects when a specific category filter is clicked
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
      if (e.target.tagName === 'VIDEO' || e.target.tagName === 'A') return;

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

  // Toast Notification System
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

  // Contact Form Submission Handler with Direct FormSubmit Gmail Delivery
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;
      const projectType = document.getElementById('project-type').value;
      const message = document.getElementById('message').value;

      showToast('Sending your inquiry directly to Mayank...');

      fetch('https://formsubmit.co/ajax/mayanksadudia@gmail.com', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({
          name: name,
          email: email,
          project_type: projectType,
          message: message,
          _subject: `New Portfolio Design Inquiry from ${name} [${projectType.toUpperCase()}]`
        })
      })
      .then(response => response.json())
      .then(data => {
        showToast('Thank you! Your message has been delivered directly to Mayank’s Gmail.');
        contactForm.reset();
      })
      .catch(() => {
        // Fallback to mailto trigger
        const subject = `Design Inquiry from ${name} [${projectType.toUpperCase()}]`;
        const body = `Hi Mayank,\n\nName: ${name}\nEmail: ${email}\nProject Type: ${projectType}\n\nMessage:\n${message}\n\nSent from Portfolio Website`;
        window.location.href = `mailto:mayanksadudia@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        showToast('Opening your email client to send message to Mayank.');
        contactForm.reset();
      });
    });
  }
});
