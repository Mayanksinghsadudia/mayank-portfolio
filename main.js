// Portfolio Interactive JavaScript Engine & Instagram Portfolio Hub

document.addEventListener('DOMContentLoaded', () => {
  // Mobile Navigation Toggle
  const mobileBtn = document.getElementById('mobile-menu-btn');
  const desktopNav = document.getElementById('desktop-nav');
  
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
        desktopNav.style.backgroundColor = '#131313';
        desktopNav.style.padding = '20px';
        desktopNav.style.borderBottom = '1px solid #262626';
      }
    });
  }

  // Active Section Scroll Tracker
  const sections = document.querySelectorAll('section.page-section, section.hero-section, section.instagram-portfolio-hub');
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

  // Category Filter Function
  window.filterIgCategory = function(filter) {
    const targetBtn = document.querySelector(`.filter-btn[data-filter="${filter}"]`);
    if (targetBtn) targetBtn.click();
    const projectsSec = document.getElementById('projects');
    if (projectsSec) projectsSec.scrollIntoView({ behavior: 'smooth' });
  };

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

  // =========================================================================
  // INSTAGRAM PORTFOLIO HUB INTERACTIONS
  // =========================================================================

  // Instagram Tab Switcher
  const igTabs = document.querySelectorAll('.ig-tab');
  const igReelsPanel = document.getElementById('ig-reels-panel');
  const igReelVideo = document.getElementById('ig-reel-video');

  window.switchIgTab = function(tabKey) {
    igTabs.forEach(t => t.classList.toggle('active', t.getAttribute('data-tab') === tabKey));

    if (tabKey === 'reels') {
      if (igReelsPanel) igReelsPanel.classList.add('active');
      if (igReelVideo) {
        igReelVideo.play().catch(() => {});
      }
      igReelsPanel?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
      if (igReelsPanel) igReelsPanel.classList.remove('active');
      if (igReelVideo) igReelVideo.pause();

      if (tabKey === 'posts') {
        const targetBtn = document.querySelector('.filter-btn[data-filter="all"]');
        if (targetBtn) targetBtn.click();
        document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' });
      } else if (tabKey === 'insights') {
        const targetBtn = document.querySelector('.filter-btn[data-filter="analytics"]');
        if (targetBtn) targetBtn.click();
        document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' });
      } else if (tabKey === 'about') {
        document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  // Avatar Story Ring Click -> Trigger 3D Reel
  const avatarStoryTrigger = document.getElementById('ig-avatar-story-trigger');
  if (avatarStoryTrigger) {
    avatarStoryTrigger.addEventListener('click', () => {
      window.switchIgTab('reels');
      showToast('Opening 3D Presenter Story Reel ✨');
    });
  }

  // Instagram Follow Button Toggle
  const followBtn = document.getElementById('ig-follow-btn');
  const followersCount = document.getElementById('ig-followers-count');
  let isFollowing = false;
  let followerNum = 1420;

  if (followBtn) {
    followBtn.addEventListener('click', () => {
      isFollowing = !isFollowing;
      if (isFollowing) {
        followerNum += 1;
        followBtn.textContent = 'Following ✓';
        followBtn.classList.add('is-following');
        showToast('You are now following @mayanksinghsadudia');
      } else {
        followerNum -= 1;
        followBtn.textContent = 'Follow';
        followBtn.classList.remove('is-following');
        showToast('Unfollowed @mayanksinghsadudia');
      }
      if (followersCount) {
        followersCount.textContent = (followerNum / 1000).toFixed(1) + 'k';
      }
    });
  }

  // Instagram Profile Share Button
  const shareBtn = document.getElementById('ig-share-btn');
  if (shareBtn) {
    shareBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('Profile link copied to clipboard!');
      });
    });
  }

  // Reel Video Edition Switcher
  window.switchReelEdition = function(src, btn) {
    if (!igReelVideo) return;
    const wasPlaying = !igReelVideo.paused;
    igReelVideo.src = src;
    igReelVideo.load();
    igReelVideo.play().catch(() => {});
    document.querySelectorAll('.ig-edition-option').forEach(b => b.classList.remove('active'));
    if (btn) btn.classList.add('active');
  };

  // Reel Sound Toggle
  const reelSoundBtn = document.getElementById('ig-reel-sound-btn');
  const reelSoundIcon = document.getElementById('ig-reel-sound-icon');
  if (reelSoundBtn && igReelVideo) {
    reelSoundBtn.addEventListener('click', () => {
      igReelVideo.muted = !igReelVideo.muted;
      if (reelSoundIcon) {
        reelSoundIcon.textContent = igReelVideo.muted ? 'volume_off' : 'volume_up';
      }
      showToast(igReelVideo.muted ? 'Reel audio muted' : 'Reel audio unmuted 🔊');
    });
  }

  // Reel Like Button
  const reelLikeBtn = document.getElementById('ig-reel-like-btn');
  const reelLikeCount = document.getElementById('ig-reel-like-count');
  let reelLiked = false;
  let reelLikes = 582;

  if (reelLikeBtn) {
    reelLikeBtn.addEventListener('click', () => {
      reelLiked = !reelLiked;
      reelLikes += reelLiked ? 1 : -1;
      reelLikeBtn.classList.toggle('is-liked', reelLiked);
      if (reelLikeCount) reelLikeCount.textContent = reelLikes;
      if (reelLiked) showToast('Liked Mayank’s 3D Presenter Reel! ❤️');
    });
  }

  // Reel Share Button
  const reelShareBtn = document.getElementById('ig-reel-share-btn');
  if (reelShareBtn) {
    reelShareBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(window.location.origin + window.location.pathname + '#hero').then(() => {
        showToast('3D Reel link copied to clipboard!');
      });
    });
  }

  // =========================================================================
  // INSTAGRAM POST LIGHTBOX MODAL SYSTEM
  // =========================================================================
  const modalBackdrop = document.getElementById('ig-project-modal');
  const modalImg = document.getElementById('ig-modal-img');
  const modalMediaContainer = document.getElementById('ig-modal-media-container');
  const modalTitle = document.getElementById('ig-modal-title');
  const modalCategory = document.getElementById('ig-modal-category');
  const modalDesc = document.getElementById('ig-modal-desc');
  const modalTags = document.getElementById('ig-modal-tags');
  const modalLikesCount = document.getElementById('ig-modal-likes-count');
  const modalLikeBtn = document.getElementById('ig-modal-like-btn');
  const modalBookmarkBtn = document.getElementById('ig-modal-bookmark-btn');
  const modalShareBtn = document.getElementById('ig-modal-share-btn');
  const modalClose = document.getElementById('ig-modal-close');
  const commentInput = document.getElementById('ig-comment-input');
  const commentPostBtn = document.getElementById('ig-comment-post-btn');
  const commentsStream = document.getElementById('ig-comments-stream');
  const modalProjectLinks = document.getElementById('ig-modal-project-links');

  let currentPostLikes = 418;
  let currentPostLiked = false;
  let currentPostBookmarked = false;

  projectCards.forEach(card => {
    card.addEventListener('click', (e) => {
      // Don't trigger modal if user clicks directly on external links
      if (e.target.closest('a')) return;

      const media = card.querySelector('.project-img, video');
      const title = card.querySelector('h3');
      const category = card.querySelector('.text-accent');
      const desc = card.querySelector('p');
      const metaLinks = card.querySelectorAll('.project-meta a');
      const toolsText = card.querySelector('.project-meta span');

      if (media && title) {
        // Clear previous video if any
        const existingVideo = modalMediaContainer.querySelector('video');
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
          videoElem.style.maxHeight = '80vh';
          videoElem.style.objectFit = 'contain';
          modalMediaContainer.appendChild(videoElem);
        } else {
          modalImg.style.display = 'block';
          modalImg.src = media.src;
        }

        modalTitle.textContent = title.textContent;
        modalCategory.textContent = category ? category.textContent : 'PORTFOLIO SHOWCASE';
        modalDesc.textContent = desc ? desc.textContent : '';

        // Generate Hashtags
        modalTags.innerHTML = '';
        const catName = category ? category.textContent.toLowerCase() : '';
        const tags = ['#MayankSingh', '#Portfolio2026'];
        if (catName.includes('nlp') || catName.includes('sentiment') || catName.includes('analytics')) {
          tags.push('#DataAnalyst', '#Python', '#PowerBI', '#SQL', '#Streamlit', '#NLP');
        } else if (catName.includes('brand') || catName.includes('logo')) {
          tags.push('#GraphicDesign', '#BrandIdentity', '#LogoDesign', '#AdobeIllustrator');
        } else if (catName.includes('package') || catName.includes('3d')) {
          tags.push('#PackagingDesign', '#3DRender', '#Mockup', '#Photoshop');
        } else {
          tags.push('#CreativeDesign', '#VisualStorytelling', '#IndoreDesigner');
        }

        tags.forEach(t => {
          const badge = document.createElement('span');
          badge.className = 'ig-tag-badge';
          badge.textContent = t;
          modalTags.appendChild(badge);
        });

        // Setup Project Links
        modalProjectLinks.innerHTML = '';
        if (metaLinks.length > 0) {
          metaLinks.forEach(link => {
            const a = document.createElement('a');
            a.href = link.href;
            a.target = '_blank';
            a.rel = 'noopener noreferrer';
            a.className = 'ig-btn ig-btn-secondary';
            a.style.fontSize = '12px';
            a.innerHTML = link.innerHTML;
            modalProjectLinks.appendChild(a);
          });
        }

        // Randomize initial likes around 380 - 450
        currentPostLikes = Math.floor(Math.random() * 80) + 380;
        currentPostLiked = false;
        currentPostBookmarked = false;
        modalLikeBtn.classList.remove('is-liked');
        modalBookmarkBtn.classList.remove('is-liked');
        modalLikesCount.textContent = `Liked by ${currentPostLikes} creators and recruiters`;

        modalBackdrop.classList.add('active');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  // Modal Close
  function closeModal() {
    const modalVideo = modalMediaContainer.querySelector('video');
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

  // Modal Like Heart
  if (modalLikeBtn) {
    modalLikeBtn.addEventListener('click', () => {
      currentPostLiked = !currentPostLiked;
      currentPostLikes += currentPostLiked ? 1 : -1;
      modalLikeBtn.classList.toggle('is-liked', currentPostLiked);
      modalLikesCount.textContent = `Liked by ${currentPostLikes} creators and recruiters`;
      if (currentPostLiked) showToast('Liked project post! ❤️');
    });
  }

  // Modal Bookmark
  if (modalBookmarkBtn) {
    modalBookmarkBtn.addEventListener('click', () => {
      currentPostBookmarked = !currentPostBookmarked;
      modalBookmarkBtn.classList.toggle('is-liked', currentPostBookmarked);
      showToast(currentPostBookmarked ? 'Saved to your collection 🔖' : 'Removed from collection');
    });
  }

  // Modal Share
  if (modalShareBtn) {
    modalShareBtn.addEventListener('click', () => {
      navigator.clipboard.writeText(window.location.href).then(() => {
        showToast('Post link copied to clipboard! 📋');
      });
    });
  }

  // Modal Comment Focus
  const modalCommentFocusBtn = document.getElementById('ig-modal-comment-focus-btn');
  if (modalCommentFocusBtn && commentInput) {
    modalCommentFocusBtn.addEventListener('click', () => {
      commentInput.focus();
    });
  }

  // Add Comment Functionality
  function postComment() {
    if (!commentInput || !commentInput.value.trim()) return;
    const text = commentInput.value.trim();

    const item = document.createElement('div');
    item.className = 'ig-comment-item';
    item.innerHTML = `
      <div class="ig-comment-avatar" style="background: #ff6b00; color: #111;">YOU</div>
      <div class="ig-comment-content">
        <span class="ig-comment-user">you</span>
        <span class="ig-comment-text">${text}</span>
        <div class="ig-comment-meta">Just now • 1 like • Reply</div>
      </div>
    `;

    commentsStream.prepend(item);
    commentInput.value = '';
    showToast('Your comment was posted! 💬');
  }

  if (commentPostBtn) commentPostBtn.addEventListener('click', postComment);
  if (commentInput) {
    commentInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') postComment();
    });
  }

  // =========================================================================
  // TOAST NOTIFICATION UTILITY
  // =========================================================================
  function showToast(message) {
    const toast = document.getElementById('ig-toast') || document.getElementById('toast-msg');
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
