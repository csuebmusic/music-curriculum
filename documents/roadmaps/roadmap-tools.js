/* ============================================================
   roadmap-tools.js
   download pdf button for the roadmaps in documents/roadmaps/,
   and the entry-term switch on roadmaps with more than one plan.

   the button downloads the print sheet named by the page's
   <link rel="alternate" type="application/pdf" href="...">,
   which points into documents/print/. a page without that link
   gets no button.

   a page with entry options marks each plan
     <div class="entry-option" data-entry="fall-a">
   and gives each one its own alternate link with the same
   data-entry value. the switch shows one plan at a time and the
   button downloads that plan's sheet. the switch has the hidden
   attribute in the markup; without the script, it stays
   hidden and every plan shows.

   one include per roadmap, just before </body>, with the same
   ?v= value as the roadmaps.css link:
     <script src="roadmap-tools.js?v=20261008b" defer></script>
   ============================================================ */
(function () {
  function init() {
    if (document.querySelector('.roadmap-tools')) return;   // already built
    var links = [].slice.call(document.querySelectorAll('link[rel="alternate"][type="application/pdf"]'));
    if (!links.length) return;

    var aside = document.createElement('aside');
    aside.className = 'roadmap-tools';
    var a = document.createElement('a');
    a.href = links[0].getAttribute('href');
    a.setAttribute('download', '');
    a.textContent = 'download pdf';
    aside.appendChild(a);
    var main = document.querySelector('main');
    main.insertBefore(aside, main.firstChild);

    var options = [].slice.call(document.querySelectorAll('.entry-option'));
    if (!options.length) return;
    var buttons = [].slice.call(document.querySelectorAll('.entry-switch button'));
    var root = document.documentElement;

    function select(name) {
      root.setAttribute('data-entry', name);
      buttons.forEach(function (b) {
        b.setAttribute('aria-pressed', b.getAttribute('data-entry') === name ? 'true' : 'false');
      });
      var link = links.filter(function (l) { return l.getAttribute('data-entry') === name; })[0] || links[0];
      a.href = link.getAttribute('href');
    }

    function optionFor(el) {
      while (el && el !== document.body) {
        if (el.classList && el.classList.contains('entry-option')) return el.getAttribute('data-entry');
        el = el.parentNode;
      }
      return null;
    }

    function fromHash() {
      var id = decodeURIComponent(location.hash.slice(1));
      var target = id && document.getElementById(id);
      var name = target && optionFor(target);
      if (name) {
        select(name);
        target.scrollIntoView();
      }
      return name;
    }

    root.classList.add('has-entry-options');
    [].slice.call(document.querySelectorAll('.entry-switch')).forEach(function (el) { el.hidden = false; });
    buttons.forEach(function (b) {
      b.addEventListener('click', function () { select(b.getAttribute('data-entry')); });
    });
    document.addEventListener('click', function (e) {
      var a = e.target.closest && e.target.closest('a[href^="#"]');
      if (!a) return;
      var target = document.getElementById(decodeURIComponent(a.getAttribute('href').slice(1)));
      var name = target && optionFor(target);
      if (name) select(name);
    });
    window.addEventListener('hashchange', fromHash);
    if (!fromHash()) select(options[0].getAttribute('data-entry'));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
