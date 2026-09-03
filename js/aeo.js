(function () {
  var ham = document.getElementById('hamburger');
  var mob = document.getElementById('mobileMenu');
  if (ham && mob) {
    ham.addEventListener('click', function () {
      mob.classList.toggle('open');
      document.body.style.overflow = mob.classList.contains('open') ? 'hidden' : '';
    });
  }
  document.querySelectorAll('.faq-item button').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var item = btn.parentElement;
      var open = item.classList.contains('open');
      document.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('open'); });
      if (!open) item.classList.add('open');
    });
  });
  var PAGE = document.body.getAttribute('data-page') || location.pathname;
  document.querySelectorAll('a[href*="wa.me"], a[href*="/evaluacion"]').forEach(function (link) {
    link.addEventListener('click', function () {
      var href = link.getAttribute('href') || '';
      var isWa = /wa\.me|whatsapp/.test(href);
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: 'contacto_web',
        cta_destination: isWa ? 'whatsapp' : 'evaluacion_form',
        cta_label: (link.textContent || '').trim().substring(0, 50),
        click_location: PAGE,
        clinica: 'lumina'
      });
      if (isWa && typeof fbq !== 'undefined') {
        fbq('track', 'Contact', { content_name: 'CTA - ' + PAGE, clinica: 'lumina', value: 5, currency: 'USD' });
      }
    });
  });
})();
