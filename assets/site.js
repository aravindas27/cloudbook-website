/* Cloudbook Associates LLP — small site script: mobile menu and the enquiry form.
   The form sends nothing to a server: it opens WhatsApp or the visitor's email app
   with the message filled in, so no personal data is stored by this website. */
(() => {
  'use strict';
  const PHONE = '919447249439';
  const EMAIL = 'info@cloudbookassociates.com';

  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', (e) => { if (e.target.closest('a')) { nav.classList.remove('open'); toggle.setAttribute('aria-expanded', 'false'); } });
  }

  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = String(new Date().getFullYear()); });

  const form = document.getElementById('enquiry');
  if (!form) return;
  const err = form.querySelector('.err');
  const val = (name) => (form.elements[name] ? String(form.elements[name].value || '').trim() : '');
  const build = () => {
    const name = val('name'), phone = val('phone'), service = val('service'), type = val('type'), msg = val('message');
    if (!name || !phone) { err.textContent = 'Please add your name and a phone number so we can call you back.'; return null; }
    if (!/^[+\d][\d\s-]{6,}$/.test(phone)) { err.textContent = 'Please check the phone number.'; return null; }
    err.textContent = '';
    return [
      'Hello Cloudbook Associates,',
      '',
      `Name: ${name}`,
      `Phone: ${phone}`,
      type ? `Business type: ${type}` : '',
      service ? `I need help with: ${service}` : '',
      msg ? `\n${msg}` : '',
    ].filter(Boolean).join('\n');
  };
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const text = build(); if (!text) return;
    const via = (e.submitter && e.submitter.value) || 'whatsapp';
    if (via === 'email') {
      window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent('Enquiry from ' + val('name'))}&body=${encodeURIComponent(text)}`;
    } else {
      window.open(`https://wa.me/${PHONE}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
    }
    form.querySelector('.note').textContent = 'Thank you. If nothing opened, call us on +91 94472 49439.';
  });
})();
