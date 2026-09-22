# university house style

version 2.0, september 2026. the on-screen reference is house-style-specimen.html.

This governs the curriculum and university documents I produce and share through this project: proposals, committee papers, assessment reports, and handbooks. It follows CSUEB visual identity, published at https://www.csueastbay.edu/universitycommunications/brand/fonts-and-colors.html. The course projects use their own style. The Cascade website pocket uses none of this one.

## palette

Reference these by name. Hex is the source of truth.

- paper (#FFFFFF): document background
- canvas (#F2F2F0): the surrounding preview surface only, never inside the document
- ink (#000000, brand black): primary text
- ink-soft (#55575B): labels, metadata, captions, secondary text
- rule (#E4E4E6): hairline rules and borders
- accent (#D50032, brand red): the record rule, section markers, table header rule, defined-term underline, links, the note border
- gold (#FDC25A, brand gold): section numbers and dividers on a dark ground
- accent-tint (#FCE6EA): the wash behind the note block

Brand red reaches 5.4:1 on white and carries text there. Brand gold reaches 1.7:1 on white and 13:1 on brand black, so it appears only on a dark ground. Brand red on brand black reaches 3.9:1 and doesn't carry text.

## type

Two families, fixed roles.

- body: Roboto Serif, 16.5px, line-height 1.65. Carries prose, table cells, defined-term text, note text. Word fallback: Georgia.
- chrome and headings: Montserrat, weights 400, 600, and 700. Carries the eyebrow, the title, section headings, field labels, the table header, the metadata line, the note label, the footer. Word fallback: Arial.

Both are open source and load from Google Fonts on screen.

## structure

record header. The document opens with a labeled grid (committee, document, effective term, status) set in Montserrat, closed by a 1.5px brand red rule.

title. Montserrat, 700, around 26px.

metadata line. Montserrat, ink-soft, with any routing id set in ink.

section headings. Montserrat, 700, around 17px, preceded by a two-digit Montserrat section number in brand red. Number sections in formal proposals and other ordered documents.

body. Roboto Serif, generous leading.

defined terms. A brand red underline on the term, followed by a short Montserrat gloss in parentheses, ink-soft.

tables. Montserrat header row, closed by a 1.5px brand red bottom rule. Roboto Serif cells, 1px hairline row rules, the rightmost column right-aligned. Unit changes set in Montserrat (3 → 4).

note block. A faint brand red tint, a 3px brand red left border, a Montserrat label, Roboto Serif text. Square corners.

footer. A top hairline, then Montserrat ink-soft: document id on the left, page on the right.

## links

Every link opens in a new tab, set with `target="_blank" rel="noopener noreferrer"`. This covers external URLs, links to other documents in the repository, and mailto links. An anchor to a section of the same document takes no target and no rel.

## capitalization

Sentence case throughout: capitalize the first word and any proper noun, nothing else. No title case, no all caps, no lowercase styling. Set capitalization in the markup rather than through `text-transform`.

## restraint

Flat surfaces: hairline rules, no shadow, white page. Whitespace generous by default and tighter in multi-page proposals.

## channels

This file is canonical; source-of-truth points here. The screen reference is house-style-specimen.html.

Committee papers, proposals, and assessment reports go out as Word or PDF from templates/house-style-template.docx, which applies these same tokens. The document uses Montserrat and Roboto Serif where installed and falls back to Arial and Georgia.

Student-facing documents are screen-first and ship as finished HTML. The handbooks and guides apply this style through `documents/handbooks/handbooks.css`, and the Theory and Musicianship set through `curriculum/undergraduate-theory-musicianship/theory-musicianship.css`. The roadmaps layer `documents/roadmaps/roadmaps.css` on top for the general-education color and for print. The posted semester syllabi use `documents/syllabi/assets/syllabus.css`.

The admissions email templates carry inline styles only, with no stylesheet, no tables, and no fixed widths, and the Salesforce wrapper controls layout. The page that presents them is house-styled through `documents/handbooks/handbooks.css`.
