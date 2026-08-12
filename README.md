# music-curriculum

Curriculum, committee, assessment, and webmaster work for the Department of Music at California State University, East Bay, maintained by Inés Thiebaut. This repository is the canonical home for that work, outside of any single course.

The HTML documents are published at https://csuebmusic.github.io/music-curriculum/ and the links below open them there. Links to Markdown files open in the repository.

## handbooks and roadmaps

- [undergraduate handbook](https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html)
- [graduate handbook](https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html)
- [B.A. roadmap, 4-year entry](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html)
- [B.A. roadmap, 2-year transfer entry](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html)
- [music education certificate roadmap](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html): the 31-unit certificate on its two-year course rotation
- [FAST 4+1 B.A./M.A. roadmap](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html): both degrees in five years

## theory and musicianship curriculum

Three framework documents and the twelve syllabi from MUS 108 through MUS 410. The [subsection README](curriculum/undergraduate-theory-musicianship/README.md) links every syllabus individually.

- [undergraduate curriculum guide](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/1_Theory-Musicianship-Undergraduate-Guide.html): sequence overview, content pacing, textbooks, workload classifications, benchmarks
- [instructor's companion](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/2_Theory-Musicianship-Undergraduate-Instructors-Companion.html): deadline schedules, class-structure guidance, grading and Canvas setup
- [syllabi index](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/3_Theory-Musicianship-Undergraduate-Syllabi.html): all twelve syllabi in one place

## conventions

- [house-style.md](conventions/house-style.md) is the canonical style spec, with [house-style-specimen.html](https://csuebmusic.github.io/music-curriculum/conventions/house-style-specimen.html) as its on-screen reference and [house-style-template.docx](conventions/templates/house-style-template.docx) as the document starting point.
- [grading-scheme.md](conventions/grading-scheme.md) is the canonical 0-4 grade-point model: the conversion chart, the student-facing text, and the Canvas setup that goes with it.

## layout

- `conventions/` holds the house style and the grading scheme.
- `curriculum/` holds course and program proposals and curriculum documentation, organized into subsections, each with its own README. The first is the undergraduate Theory and Musicianship sequence.
- `documents/` holds the handbooks, the roadmaps, and program, admissions, and policy material.
- `committee/` holds agendas, minutes, and papers for the CLASS curriculum committee.
- `assessment/` holds program learning outcomes, assessment reports, and review cycles.
- `website/` holds structural HTML snippets that get pasted into Cascade, which supplies its own styling.

The repository is active, and the folders fill as each workstream produces material.

## channels

Committee papers, proposals, and assessment reports follow `conventions/house-style.md` and go out as Word or PDF from the template.

Student-facing documents are screen-first and ship as finished HTML rather than Word. The handbooks and roadmaps apply the same house style through `documents/handbooks/handbooks.css`, and the Theory and Musicianship set applies it through `curriculum/undergraduate-theory-musicianship/theory-musicianship.css`. Both stylesheets track house-style v1. The roadmaps layer `documents/roadmaps/roadmaps.css` on top for the general-education color and for print.

The website pocket is the one exception. Its markup is structural only, and Cascade supplies the appearance.
