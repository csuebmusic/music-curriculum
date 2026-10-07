/* ============================================================
   roadmap-tools.js
   download-to-PDF button for the roadmaps in documents/roadmaps/.
   the button opens the browser's print dialog; "Save as PDF" there
   writes the file. the print rules in roadmaps.css hide the button
   and the sidebar and set the semesters two to a row.

   one include per roadmap, just before </body>:
     <script src="roadmap-tools.js" defer></script>
   ============================================================ */
(function () {
  function init() {
    if (document.querySelector('.roadmap-tools')) return;   // already built

    var h1 = document.querySelector('h1');
    var title = h1 ? h1.textContent.trim() : 'Roadmap';

    var aside = document.createElement('aside');
    aside.className = 'roadmap-tools';
    aside.innerHTML = '<button id="rt-download" type="button">download pdf</button>';
    var main = document.querySelector('main');
    main.insertBefore(aside, main.firstChild);

    document.getElementById('rt-download').addEventListener('click', function () {
      var prev = document.title;
      document.title = 'CSUEB Music, ' + title;
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
