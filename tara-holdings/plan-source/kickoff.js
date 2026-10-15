(() => {
  const deck = document.querySelector('.deck');
  const slides = [...document.querySelectorAll('.slide')];
  const bar = document.querySelector('.bar i');
  let i = Math.min(Math.max(parseInt(location.hash.slice(1), 10) - 1 || 0, 0), slides.length - 1);

  const fit = () => {
    const s = Math.min(innerWidth / 1920, innerHeight / 1080);
    deck.style.transform = `translate(-50%, -50%) scale(${s})`;
  };
  const show = (n) => {
    i = Math.min(Math.max(n, 0), slides.length - 1);
    slides.forEach((el, k) => el.classList.toggle('on', k === i));
    bar.style.width = `${((i + 1) / slides.length) * 100}%`;
    history.replaceState(null, '', `#${i + 1}`);
  };

  addEventListener('resize', fit);
  addEventListener('keydown', (ev) => {
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(ev.key)) { ev.preventDefault(); show(i + 1); }
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(ev.key)) { ev.preventDefault(); show(i - 1); }
    else if (ev.key === 'Home') show(0);
    else if (ev.key === 'End') show(slides.length - 1);
    else if (ev.key === 'f') document.documentElement.requestFullscreen?.();
  });
  addEventListener('click', (ev) => show(ev.clientX < innerWidth / 3 ? i - 1 : i + 1));
  fit();
  show(i);
})();
