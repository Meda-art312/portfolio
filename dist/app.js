const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navigation');

function closeMenu() {
  menuButton.setAttribute('aria-expanded', 'false');
  navigation.dataset.open = 'false';
}
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.dataset.open = String(open);
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});
window.matchMedia('(min-width: 561px)').addEventListener('change', event => {
  if (event.matches) closeMenu();
});

const filters = document.querySelectorAll('[data-filter]');
const projects = document.querySelectorAll('[data-category]');
filters.forEach(button => {
  button.addEventListener('click', () => {
    const filter = button.dataset.filter;
    filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    let count = 0;
    projects.forEach(project => {
      const visible = filter === 'all' || project.dataset.category === filter;
      project.hidden = !visible;
      if (visible) count++;
    });
    document.querySelector('#project-count').textContent = `${count} PROJECT${count === 1 ? '' : 'S'}`;
  });
});

document.querySelector('#year').textContent = new Date().getFullYear();
const email = 'mohamedmedhat.dev2232@gmail.com';
const copyButton = document.querySelector('#copy-email');
copyButton.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(email);
    copyButton.textContent = 'Copied';
    document.querySelector('#copy-feedback').textContent = 'Email address copied to clipboard.';
  } catch {
    copyButton.textContent = 'Select email';
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('.contact-email > a'));
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    document.querySelector('#copy-feedback').textContent = 'Email address selected. Use your device’s copy command.';
  }
});

if ('IntersectionObserver' in window) {
  const links = [...navigation.querySelectorAll('a')];
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      links.forEach(link => {
        if (link.hash === `#${entry.target.id}`) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    });
  }, { rootMargin: '-15% 0px -65% 0px' });
  document.querySelectorAll('main > section[id]').forEach(section => observer.observe(section));
}
