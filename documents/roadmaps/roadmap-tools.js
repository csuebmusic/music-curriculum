/* ============================================================
   roadmap-tools.js
   download pdf button for the roadmaps in documents/roadmaps/.
   the button downloads the print sheet named by the page's
   <link rel="alternate" type="application/pdf" href="...">,
   which points into documents/print/. a page without that link
   gets no button.

   one include per roadmap, just before </body>:
     <script src="roadmap-tools.js" defer></script>
   ============================================================ */
(function () {
  function init() {
    if (document.querySelector('.roadmap-tools')) return;   // already built
    var pdf = document.querySelector('link[rel="alternate"][type="application/pdf"]');
    if (!pdf) return;

    var aside = document.createElement('aside');
    aside.className = 'roadmap-tools';
    var a = document.createElement('a');
    a.href = pdf.getAttribute('href');
    a.setAttribute('download', '');
    a.textContent = 'download pdf';
    aside.appendChild(a);
    var main = document.querySelector('main');
    main.insertBefore(aside, main.firstChild);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
