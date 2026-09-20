/* ============================================================
   syllabus-tools.js
   download-to-PDF button for posted semester syllabi. the button
   and the back-link are hidden by the print stylesheet in
   syllabus.css, so the PDF carries the page alone.

   one include per syllabus, just before </body>:
     <script src="../assets/syllabus-tools.js" defer></script>

   instructor and section details are written into the file itself,
   so this script does not edit page content.
   ============================================================ */
(function () {
  function init() {
    if (document.querySelector('.syllabus-tools')) return;           // already built
    if (!document.querySelector('#contact')) return;                 // not a syllabus page

    var h1 = document.querySelector('h1');
    var title = h1 ? h1.textContent.trim() : 'Syllabus';

    var aside = document.createElement('aside');
    aside.className = 'syllabus-tools no-print';
    aside.innerHTML = '<button id="st-download" type="button">download pdf</button>';
    document.body.insertBefore(aside, document.body.firstChild);

    document.getElementById('st-download').addEventListener('click', function () {
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
