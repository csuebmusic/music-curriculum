/* ============================================================
   syllabus-tools.js
   contact sidebar + print-to-PDF for the Theory & Musicianship
   syllabi. builds an "instructor details" panel from the Contact
   Information grid on the page, writes entries live into that grid,
   remembers them per course on the device, and prints the page as a
   PDF (the sidebar and back-link are hidden by the print stylesheet
   in theory-musicianship.css).

   one include per syllabus, just before </body>:
     <script src="syllabus-tools.js" defer></script>

   the script reads the contact rows it finds, so it adapts to each
   syllabus without per-page configuration. it does nothing on pages
   that have no contact grid.
   ============================================================ */
(function () {
  function slug(s) {
    return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  function init() {
    if (document.querySelector('.syllabus-tools')) return;          // already built
    var grid = document.querySelector('#contact .info-grid');
    if (!grid) return;                                              // not a syllabus page
    var rows = Array.prototype.slice.call(grid.querySelectorAll('.info-row'));
    if (!rows.length) return;

    var h1 = document.querySelector('h1');
    var title = h1 ? h1.textContent.trim() : 'Syllabus';
    var codeMatch = title.match(/^([A-Za-z]{2,4})\s?0*([0-9]{2,4})/);
    var code = codeMatch ? (codeMatch[1].toUpperCase() + codeMatch[2]) : 'syllabus';
    var KEY = 'syllabus-contact:' + code;

    var hints = {
      'instructor': 'name',
      'email': 'name@csueastbay.edu',
      'phone': '(000) 000-0000',
      'office': 'building / room',
      'office-hours': 'days / times'
    };

    var fields = [];
    rows.forEach(function (row) {
      var labelEl = row.querySelector('.info-label');
      var valueEl = row.querySelector('.info-value');
      if (!labelEl || !valueEl) return;
      var label = labelEl.textContent.trim();
      var key = slug(label);
      valueEl.setAttribute('data-placeholder', valueEl.textContent);
      valueEl.classList.add('is-empty');
      fields.push({ key: key, label: label, span: valueEl, hint: hints[key] || '' });
    });
    if (!fields.length) return;

    var aside = document.createElement('aside');
    aside.className = 'syllabus-tools no-print';
    aside.setAttribute('aria-label', 'instructor details');
    var html = '<h2>instructor details</h2>'
      + '<p class="st-hint">fill these in, then download a PDF. '
      + 'they stay on this device for next time.</p>';
    fields.forEach(function (f) {
      html += '<label for="st-' + f.key + '">' + f.label.toLowerCase() + '</label>'
        + '<input id="st-' + f.key + '" type="text" autocomplete="off"'
        + (f.hint ? ' placeholder="' + f.hint + '"' : '') + '>';
    });
    html += '<div class="st-actions">'
      + '<button id="st-download" type="button">download pdf</button>'
      + '<div class="st-saved" id="st-saved"></div></div>';
    aside.innerHTML = html;
    document.body.insertBefore(aside, document.body.firstChild);

    function inp(f) { return document.getElementById('st-' + f.key); }
    function apply(f) {
      var v = inp(f).value.trim();
      if (v) { f.span.textContent = v; f.span.classList.remove('is-empty'); }
      else {
        f.span.textContent = f.span.getAttribute('data-placeholder') || '';
        f.span.classList.add('is-empty');
      }
    }
    var flashTimer;
    function flash(msg) {
      var el = document.getElementById('st-saved');
      if (!el) return;
      el.textContent = msg;
      clearTimeout(flashTimer);
      flashTimer = setTimeout(function () { el.textContent = ''; }, 1600);
    }
    function save() {
      try {
        var data = {};
        fields.forEach(function (f) { data[f.key] = inp(f).value || ''; });
        localStorage.setItem(KEY, JSON.stringify(data));
        flash('saved on this device');
      } catch (e) { /* storage unavailable */ }
    }
    function load() {
      try {
        var raw = localStorage.getItem(KEY);
        if (!raw) return;
        var data = JSON.parse(raw);
        fields.forEach(function (f) { if (data[f.key] != null) inp(f).value = data[f.key]; });
      } catch (e) { /* storage unavailable */ }
    }

    load();
    fields.forEach(function (f) {
      apply(f);
      inp(f).addEventListener('input', function () { apply(f); save(); });
    });

    var btn = document.getElementById('st-download');
    if (btn) btn.addEventListener('click', function () {
      var prev = document.title;
      document.title = title + ' \u2014 Syllabus';
      window.print();
      setTimeout(function () { document.title = prev; }, 500);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
