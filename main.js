// ===================================================================
// MAYANK SINGH SADUDIA · PORTFOLIO JAVASCRIPT ENGINE
// Interactive Audio, Filter Gallery, Modals & Communication
// ===================================================================

document.addEventListener('DOMContentLoaded', () => {

  // 1. Mobile Navigation Toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const desktopNav = document.getElementById('desktop-nav');
  const appHeader = document.getElementById('app-header');

  if (mobileBtn && desktopNav) {
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
        desktopNav.style.backgroundColor = '#111111';
        desktopNav.style.padding = '24px';
        desktopNav.style.borderBottom = '1px solid #242424';
        desktopNav.style.gap = '18px';
      }
    });

    // Close mobile nav on link click
    desktopNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        if (window.innerWidth <= 768) {
          desktopNav.style.display = 'none';
        }
      });
    });
  }

  // 2. Header Scrolled Glass Effect & Active Section Tracker
  const sections = document.querySelectorAll('section');
  const navLinks = document.querySelectorAll('.desktop-nav .nav-link');

  window.addEventListener('scroll', () => {
    // Header glass transition
    if (appHeader) {
      if (window.scrollY > 40) {
        appHeader.classList.add('scrolled');
      } else {
        appHeader.classList.remove('scrolled');
      }
    }

    // Nav active link tracker
    let current = '';
    const scrollPosition = window.scrollY + 180;

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

  // 3. 30-Second English Audio Player Engine
  const introAudio = document.getElementById('mayank-intro-audio');
  const heroAudioCard = document.getElementById('hero-audio-player');
  const heroAudioBtn = document.getElementById('hero-audio-btn');
  const heroAudioIcon = document.getElementById('hero-audio-icon');
  const navAudioBtn = document.getElementById('nav-audio-btn');
  const navAudioIcon = document.getElementById('nav-audio-icon');
  const audioTimeDisplay = document.getElementById('audio-time-display');

  function formatTime(sec) {
    if (isNaN(sec) || sec < 0) return '0:00';
    const m = Math.floor(sec / 60);
    const s = Math.floor(sec % 60);
    return `${m}:${s < 10 ? '0' : ''}${s}`;
  }

  function setAudioPlayingUI(isPlaying) {
    if (heroAudioCard) {
      heroAudioCard.classList.toggle('playing', isPlaying);
    }
    if (heroAudioIcon) {
      heroAudioIcon.textContent = isPlaying ? 'pause' : 'play_arrow';
    }
    if (navAudioBtn) {
      navAudioBtn.classList.toggle('playing', isPlaying);
    }
    if (navAudioIcon) {
      navAudioIcon.textContent = isPlaying ? 'pause' : 'volume_up';
    }
  }

  function toggleAudio() {
    if (!introAudio) return;
    if (introAudio.paused) {
      introAudio.play().then(() => {
        setAudioPlayingUI(true);
      }).catch(err => {
        console.warn('Audio play request blocked:', err);
      });
    } else {
      introAudio.pause();
      setAudioPlayingUI(false);
    }
  }

  if (heroAudioBtn) heroAudioBtn.addEventListener('click', toggleAudio);
  if (navAudioBtn) navAudioBtn.addEventListener('click', toggleAudio);

  if (introAudio) {
    introAudio.addEventListener('timeupdate', () => {
      if (audioTimeDisplay) {
        const cur = formatTime(introAudio.currentTime);
        const duration = introAudio.duration ? formatTime(introAudio.duration) : '0:27';
        audioTimeDisplay.textContent = `${cur} / ${duration}`;
      }
    });

    introAudio.addEventListener('ended', () => {
      setAudioPlayingUI(false);
      if (audioTimeDisplay) audioTimeDisplay.textContent = '0:00 / 0:27';
    });

    introAudio.addEventListener('loadedmetadata', () => {
      if (audioTimeDisplay && introAudio.duration) {
        audioTimeDisplay.textContent = `0:00 / ${formatTime(introAudio.duration)}`;
      }
    });
  }

  // 4. Project Gallery Filter & View All Toggle
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');
  const viewAllBtn = document.getElementById('view-all-projects-btn');
  const viewAllContainer = document.getElementById('view-all-container');

  let isExpanded = false;

  // Initial display setup: if not expanded, show first 8 items in 'all' mode
  function applyProjectVisibility(activeFilter) {
    projectCards.forEach((card, index) => {
      const category = card.getAttribute('data-category');
      const isMatch = (activeFilter === 'all' || category === activeFilter);

      if (activeFilter === 'all' && !isExpanded && index >= 8) {
        card.style.display = 'none';
        card.style.opacity = '0';
      } else if (isMatch) {
        card.style.display = 'flex';
        setTimeout(() => {
          card.style.opacity = '1';
          card.style.transform = 'scale(1)';
        }, 10);
      } else {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.96)';
        setTimeout(() => {
          if (card.style.opacity === '0') card.style.display = 'none';
        }, 150);
      }
    });
  }

  // View All Projects button click
  if (viewAllBtn) {
    viewAllBtn.addEventListener('click', () => {
      isExpanded = true;
      projectCards.forEach(card => {
        card.style.display = 'flex';
        card.style.opacity = '1';
        card.style.transform = 'scale(1)';
      });
      if (viewAllContainer) viewAllContainer.style.display = 'none';
    });
  }

  // Category filter tabs click
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

      applyProjectVisibility(filter);
    });
  });

  // Initial call
  applyProjectVisibility('all');

  // 5. Project Lightbox Modal
  const modalBackdrop = document.getElementById('project-modal');
  const modalImg = document.getElementById('modal-img');
  const modalTitle = document.getElementById('modal-title');
  const modalCategory = document.getElementById('modal-category');
  const modalDesc = document.getElementById('modal-desc');
  const modalTools = document.getElementById('modal-tools');
  const modalClose = document.getElementById('modal-close');

  projectCards.forEach(card => {
    card.addEventListener('click', (e) => {
      // Don't trigger modal if user clicks directly on links, buttons or video elements
      if (e.target.closest('a, button, video, input, textarea, select')) return;

      const media = card.querySelector('.project-img, video');
      const title = card.querySelector('h3');
      const category = card.querySelector('.text-accent');
      const desc = card.querySelector('p');
      const metaSpan = card.querySelector('.project-meta span');

      if (media && title) {
        const modalMediaWrapper = modalImg.parentElement;
        
        // Remove existing video if present
        const existingVideo = modalMediaWrapper.querySelector('video');
        if (existingVideo) existingVideo.remove();

        if (media.tagName === 'VIDEO') {
          modalImg.style.display = 'none';
          const videoElem = document.createElement('video');
          videoElem.src = media.src;
          videoElem.controls = true;
          videoElem.autoplay = true;
          videoElem.loop = true;
          videoElem.playsInline = true;
          videoElem.style.width = '100%';
          videoElem.style.maxHeight = '70vh';
          videoElem.style.objectFit = 'contain';
          modalMediaWrapper.appendChild(videoElem);
        } else {
          modalImg.style.display = 'block';
          modalImg.src = media.src;
        }

        modalTitle.textContent = title.textContent;
        modalCategory.textContent = category ? category.textContent : 'SELECTED PROJECT';
        modalDesc.textContent = desc ? desc.textContent : '';

        modalTools.innerHTML = '';
        if (metaSpan) {
          const tools = metaSpan.textContent.split('&').map(t => t.trim());
          tools.forEach(tool => {
            if (!tool) return;
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

  function closeModal() {
    if (!modalBackdrop) return;
    const modalVideo = modalBackdrop.querySelector('video');
    if (modalVideo) {
      modalVideo.pause();
      modalVideo.remove();
    }
    modalBackdrop.classList.remove('active');
    document.body.style.overflow = 'auto';
  }

  if (modalClose) modalClose.addEventListener('click', closeModal);
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) closeModal();
    });
  }

  // 6. Toast Notification Utility
  window.showToast = function(message) {
    const toast = document.getElementById('toast-msg');
    if (toast) {
      toast.textContent = message;
      toast.style.display = 'block';
      setTimeout(() => {
        toast.style.display = 'none';
      }, 4000);
    }
  };

  // Copy text helper
  window.copyText = function(text, label) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text).then(() => {
        window.showToast(`${label} copied to clipboard!`);
      });
    } else {
      window.showToast(`${label}: ${text}`);
    }
  };

  // 7. Contact Form Handler (Direct Delivery via FormSubmit)
  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const name = document.getElementById('name')?.value || 'Guest';
      const email = document.getElementById('email')?.value || '';
      const phone = document.getElementById('phone')?.value || 'Not provided';
      const projectType = document.getElementById('project-type')?.value || 'General Inquiry';
      const message = document.getElementById('message')?.value || '';

      window.showToast('Sending message directly to Mayank...');

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
          _subject: `Portfolio Message from ${name} [${projectType.toUpperCase()}]`
        })
      })
      .then(response => response.json())
      .then(() => {
        window.showToast('Thank you! Your message was delivered directly to Mayank’s Gmail.');
        contactForm.reset();
      })
      .catch(() => {
        // Fallback to mailto
        const subject = `Portfolio Inquiry from ${name} [${projectType.toUpperCase()}]`;
        const body = `Hi Mayank,\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nProject: ${projectType}\n\nMessage:\n${message}`;
        window.location.href = `mailto:mayanksadudia@gmail.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
        window.showToast('Opening your email client to send message to Mayank.');
        contactForm.reset();
      });
    });
  }

  // 8. 3D Reel Video Modal Logic
  const reelModal = document.getElementById('reel-modal');
  const openReelBtn = document.getElementById('open-reel-modal-btn');
  const closeReelBtn = document.getElementById('reel-modal-close');
  const reelVideo = document.getElementById('reel-modal-video');
  const switchEnBtn = document.getElementById('reel-switch-en-btn');
  const switchOrigBtn = document.getElementById('reel-switch-orig-btn');

  if (openReelBtn && reelModal && reelVideo) {
    openReelBtn.addEventListener('click', () => {
      reelModal.style.display = 'flex';
      reelVideo.currentTime = 0;
      reelVideo.play().catch(() => {});
    });

    const closeReel = () => {
      reelModal.style.display = 'none';
      reelVideo.pause();
    };

    if (closeReelBtn) closeReelBtn.addEventListener('click', closeReel);
    reelModal.addEventListener('click', (e) => {
      if (e.target === reelModal) closeReel();
    });

    if (switchEnBtn && switchOrigBtn) {
      switchEnBtn.addEventListener('click', () => {
        const time = reelVideo.currentTime;
        reelVideo.src = 'assets/reel_presenter_en.mp4';
        reelVideo.currentTime = time % 27;
        reelVideo.play().catch(() => {});
        switchEnBtn.className = 'btn-primary';
        switchOrigBtn.className = 'btn-secondary';
      });

      switchOrigBtn.addEventListener('click', () => {
        const time = reelVideo.currentTime;
        reelVideo.src = 'assets/reel_complete.mp4';
        reelVideo.currentTime = time % 16;
        reelVideo.play().catch(() => {});
        switchOrigBtn.className = 'btn-primary';
        switchEnBtn.className = 'btn-secondary';
      });
    }
  }

});
