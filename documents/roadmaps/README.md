# roadmaps

Student-facing HTML roadmaps for the B.A. in Music, the M.A. in Music, the FAST blended degrees, and the Certificate in Music Education, catalog 2027–2028, house-styled on
`../handbooks/handbooks.css`.

- [ba-roadmap-4-year.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html): first-year entry, 120 units.
- [ba-roadmap-2-year-transfer.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html): Music ADT transfer entry, 60 units in residence.
- [fast-ba-ma-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html): FAST 4+1 blended B.A. and M.A., ten semesters, 120 and 32 units.
- [fast-ba-ma-certificate-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-certificate-roadmap.html): FAST 4+1 with the Certificate in Music Education, 155 units across five years.
- [fast-transfer-ba-ma-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html): FAST 2+1 transfer entry through both degrees, with fall A and fall B entry plans, 81 units in residence.
- [fast-transfer-ba-ma-certificate-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-certificate-roadmap.html): FAST 2+1 transfer entry with the Certificate in Music Education, with fall A and fall B entry plans, 90 units in residence.
- [ba-composition-roadmap-2-year-transfer.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-composition-roadmap-2-year-transfer.html): Music ADT transfer entry with the music electives filled from composition, production, and music business courses, 60 units in residence.
- [ba-certificate-roadmap-4-year.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-certificate-roadmap-4-year.html): first-year B.A. entry with the Certificate in Music Education, 134 units across eight semesters.
- [ba-certificate-roadmap-2-year-transfer.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-certificate-roadmap-2-year-transfer.html): Music ADT transfer entry with the Certificate in Music Education, four semesters, 62 units in residence.
- [ma-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ma-roadmap.html): M.A. in Music, four semesters, with fall A and fall B entry plans, 32 units.
- [music-education-certificate-roadmap.html](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html): certificate course rotation across a two-year cycle, 31 units.
- [status.md](status.md): items on hold and open questions.

Keep course titles and units in sync with the University Catalog and the
undergraduate handbook (`../handbooks/undergraduate-handbook.html`). Each
semester has an anchored id (`sem1`, `sem2`, and so on) for deep linking.

Rows with the `petition` class are graduate courses taken for graduate credit
by petition in the last B.A. semester. They count toward the M.A. only.

A roadmap with more than one entry term wraps each plan in
`<div class="entry-option" data-entry="fall-a" id="fall-a">` (and `fall-b`), and
the fall B plan has the same semester and section ids with a `b` suffix
(`sem5b`, `blended-b`). Each plan has its own
`<link rel="alternate" type="application/pdf" data-entry="...">`.
`roadmap-tools.js` adds the entry switch, shows one plan at a time, and points
the download pdf button at that plan's sheet. A link to an id inside a plan
opens that plan. Without the script, both plans show.

Certificate rows have the `cert` class and an ochre tint. On the combined
roadmaps, certificate courses are in the Year A and Year B rotation slots the
certificate cycle allows: fall A semesters take Year A fall courses, spring A
semesters take Year A spring courses, and so on.

`roadmaps.css` layers row colors, a narrower centered column, and print rules
over the handbook style. It applies to the roadmaps alone: the handbooks keep
the single-accent house style.

Each roadmap has a download pdf button, built by `roadmap-tools.js` and
included once per roadmap just before `</body>`. The roadmaps link
`roadmaps.css` and `roadmap-tools.js` with a `?v=` value (`?v=20261008`). When
either file changes, change the value on every roadmap. The button downloads the print
sheet named in the roadmap's `<link rel="alternate" type="application/pdf">`,
which points to its PDF in `../print/`. A change to a roadmap's courses or units
goes into its print sheet too.

The print rules in `roadmaps.css` apply when a roadmap page is printed from the
browser: US Letter pages with the semesters two to a row (`div.sems` holding
one `div.sem` per semester), each semester's table kept on one page.
