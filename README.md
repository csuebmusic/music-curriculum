# music-curriculum

Curriculum, committee, assessment, and webmaster work for the Department of Music at California State University, East Bay, maintained by Inés Thiebaut. This repository is the canonical home for that work, outside of any single course.

The HTML documents are published at https://csuebmusic.github.io/music-curriculum/ and the links below open them there. Links to Markdown files open in the repository.

## handbooks and roadmaps

The [roadmaps README](documents/roadmaps/README.md) describes each plan and its status.

- [undergraduate handbook](https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html)
- [graduate handbook](https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html)
- [B.A. roadmap, 4-year entry](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html)
- [B.A. roadmap, 2-year transfer entry](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html)
- [FAST 4+1 B.A./M.A. roadmap](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html): both degrees in five years
- [FAST 4+1 with the music education certificate](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-certificate-roadmap.html): both degrees and the certificate in five years
- [FAST 2+1 transfer B.A./M.A. roadmap](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html): both degrees in three years from Music ADT transfer entry, proposed
- [FAST 2+1 transfer with the music education certificate](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-certificate-roadmap.html): both degrees and the certificate in three years from Music ADT transfer entry, proposed
- [music education certificate roadmap](https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html): the 31-unit certificate on its two-year course rotation

## admissions emails

The automated messages Salesforce sends to applicants, admits, and new students, with the flow that triggers them. Sixteen templates: one shared inquiry message, then five each for the B.A. and Additional Degree, the M.A., and the stand-alone certificate. The [pocket README](documents/admissions-emails/README.md) covers the build and the paste workflow.

- [admissions email templates](https://csuebmusic.github.io/music-curriculum/documents/admissions-emails/): the flow, the merge field, a rendered preview of every template, and a copy-source control for each

## student employment

- [equipment office student assistant guide](https://csuebmusic.github.io/music-curriculum/documents/handbooks/equipment-office-student-assistant-guide.html): position responsibilities, rounds, event setup, problem reporting, and the hour-tracking worksheet
- [ensemble manager student assistant guide](https://csuebmusic.github.io/music-curriculum/documents/handbooks/ensemble-manager-student-assistant-guide.html): the two ensemble assignments, weekly setup and strike, concert and recital work, and the hour-tracking worksheet

## website

Structural HTML pasted into Cascade, mirroring the live path under `/music/`. Cascade supplies the appearance.

- `website/current/index.html` &rarr; [student resources](https://www.csueastbay.edu/music/current/index.html)
- `website/prospective/how-to-apply/i-got-in-now-what.html` &rarr; [I got in! Now what?](https://www.csueastbay.edu/music/prospective/how-to-apply/i-got-in-now-what.html)

## theory and musicianship curriculum

Three framework documents and the twelve syllabi from MUS 108 through MUS 410. The [subsection README](curriculum/undergraduate-theory-musicianship/README.md) links every syllabus individually.

- [undergraduate curriculum guide](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/1_Theory-Musicianship-Undergraduate-Guide.html): sequence overview, content pacing, textbooks, workload classifications, benchmarks
- [instructor's companion](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/2_Theory-Musicianship-Undergraduate-Instructors-Companion.html): deadline schedules, class-structure guidance, grading and Canvas setup
- [syllabi index](https://csuebmusic.github.io/music-curriculum/curriculum/undergraduate-theory-musicianship/3_Theory-Musicianship-Undergraduate-Syllabi.html): all twelve syllabi in one place

## catalog audit

The MUS course inventory in the 2026-2027 catalog checked against the Curriculog proposal archive, the handbooks, the roadmaps, and the syllabi, with the revisions each course needs for the 2027-2028 catalog. The [subsection README](curriculum/catalog-audit/README.md) covers sources, columns, and open items.

- [course inventory](curriculum/catalog-audit/course-inventory.xlsx): 140 courses, their published values and teaching classification, and the technical and content findings for each

## semester syllabi

Posted syllabi for individual sections, one file per section per term, with a permanent link for Canvas. The [syllabi README](syllabi/README.md) covers naming, posting, and editing in the browser.

- [fall 2026](https://csuebmusic.github.io/music-curriculum/syllabi/fall-2026/)

## curriculum committee

Proposals under CLASS Curriculum Committee review, with review notes where feedback has been given, in `committee/ccc/`.

- [CCC README](committee/ccc/README.md), [Theatre Arts, B.A., revision](committee/ccc/proposals/theatre-arts-ba-revision-fall-2027.md), [review notes](committee/ccc/proposals/theatre-arts-ba-revision-fall-2027-review.md)
- [reference](committee/ccc/reference/README.md): the GEOC faculty guide, the GEOC alignment form required in Curriculog, the 25-26 CIC 1 syllabus policy, and the curricular deadlines

## graduate recruitment

Working documents for the graduate recruitment facilitator role, in `committee/grad-facilitator/`.

- [role.md](committee/grad-facilitator/role.md), [recruitment-plan.md](committee/grad-facilitator/recruitment-plan.md), [status.md](committee/grad-facilitator/status.md), [programs.md](committee/grad-facilitator/programs.md), [baseline.md](committee/grad-facilitator/baseline.md)

## conventions

- [house-style.md](conventions/house-style.md) is the canonical style spec, with [house-style-specimen.html](https://csuebmusic.github.io/music-curriculum/conventions/house-style-specimen.html) as its on-screen reference and [house-style-template.docx](conventions/templates/house-style-template.docx) as the document starting point.
- [grading-scheme.md](conventions/grading-scheme.md) is the canonical 0-4 grade-point model: the conversion chart, the student-facing text, and the Canvas setup that goes with it.

## layout

- `conventions/` holds the house style and the grading scheme.
- `syllabi/` holds the syllabi posted for individual sections, in one folder per term.
- `curriculum/` holds course and program proposals and curriculum documentation, organized into subsections, each with its own README: the undergraduate Theory and Musicianship sequence, and the catalog audit.
- `documents/` holds the handbooks, the roadmaps, the admissions email set, and program and policy material.
- `committee/` holds agendas, minutes, and papers for committee service: the CLASS Curriculum Committee in `committee/ccc/`, and the graduate recruitment facilitator role in `committee/grad-facilitator/`.
- `assessment/` holds program learning outcomes, assessment reports, and review cycles.
- `website/` holds structural HTML snippets that get pasted into Cascade, which supplies its own styling.

The repository is active, and the folders fill as each workstream produces material. `assessment/` is empty so far.

## channels

Committee papers, proposals, and assessment reports follow `conventions/house-style.md` and go out as Word or PDF from the template.

Student-facing documents are screen-first and ship as finished HTML rather than Word. The handbooks and roadmaps apply the same house style through `documents/handbooks/handbooks.css`, and the Theory and Musicianship set applies it through `curriculum/undergraduate-theory-musicianship/theory-musicianship.css`. Both stylesheets track house-style v1. The roadmaps layer `documents/roadmaps/roadmaps.css` on top for the general-education color and for print.

The website pocket is the one exception. Its markup is structural only, and Cascade supplies the appearance.

The admissions email templates are a third case. They carry inline styles only, with no stylesheet, no tables, and no fixed widths, so the Salesforce wrapper controls layout. The page that presents them is house-styled through `documents/handbooks/handbooks.css`.
