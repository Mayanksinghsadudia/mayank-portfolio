(() => {
  const progress = document.querySelector('.scroll-progress');
  let pending = false;
  const updateProgress = () => {
    const distance = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = `${distance > 0 ? window.scrollY / distance * 100 : 0}%`;
    pending = false;
  };
  window.addEventListener('scroll', () => {
    if (!pending) { pending = true; requestAnimationFrame(updateProgress); }
  }, { passive: true });
  window.addEventListener('resize', updateProgress);
  updateProgress();

  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  if (matchMedia('(pointer: fine)').matches && !reducedMotion.matches) {
    document.querySelectorAll('.project-card').forEach(card => {
      card.addEventListener('pointermove', event => {
        const bounds = card.getBoundingClientRect();
        card.style.setProperty('--spot-x', `${event.clientX - bounds.left}px`);
        card.style.setProperty('--spot-y', `${event.clientY - bounds.top}px`);
      });
    });
  }
})();
