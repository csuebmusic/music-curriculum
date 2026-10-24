# University house style

Version 2.0, September 2026. The on-screen reference is house-style-specimen.html.

This governs the curriculum and university documents I produce and share through this project: proposals, committee papers, assessment reports, and handbooks. It follows CSUEB visual identity, published at https://www.csueastbay.edu/universitycommunications/brand/fonts-and-colors.html. The course projects use their own style. The Cascade website pocket uses none of this one.

This spec covers document form. Prose style and register follow the "how I want you to communicate" section of Inés Thiebaut's profile.

## Palette

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

## Type

Two families, fixed roles.

- body: Roboto Serif, 16.5px, line-height 1.65. Carries prose, table cells, defined-term text, note text. Word fallback: Georgia.
- chrome and headings: Montserrat, weights 400, 600, and 700. Carries the eyebrow, the title, section headings, field labels, the table header, the metadata line, the note label, the footer. Word fallback: Arial.

Both are open source and load from Google Fonts on screen.

## Structure

Record header. The document opens with a labeled grid (committee, document, effective term, status) set in Montserrat, closed by a 1.5px brand red rule.

Title. Montserrat, 700, around 26px.

Metadata line. Montserrat, ink-soft, with any routing id set in ink.

Section headings. Montserrat, 700, around 17px, preceded by a two-digit Montserrat section number in brand red. Number sections in formal proposals and other ordered documents.

Body. Roboto Serif, generous leading.

Defined terms. A brand red underline on the term, followed by a short Montserrat gloss in parentheses, ink-soft.

Tables. Montserrat header row, closed by a 1.5px brand red bottom rule. Roboto Serif cells, 1px hairline row rules, the rightmost column right-aligned. Unit changes set in Montserrat (3 → 4).

Note block. A faint brand red tint, a 3px brand red left border, a Montserrat label, Roboto Serif text. Square corners.

Footer. A top hairline, then Montserrat ink-soft: document id on the left, page on the right.

## Links

Every link opens in a new tab, set with `target="_blank" rel="noopener noreferrer"`. This covers external URLs, links to other documents in the repository, and mailto links. An anchor to a section of the same document takes no target and no rel.

## Capitalization

Sentence case throughout: capitalize the first word and any proper noun. Set capitalization in the markup rather than through `text-transform`.

## Restraint

Flat surfaces: hairline rules, no shadow, white page. Whitespace generous by default and tighter in multi-page proposals.

## Channels

This file is canonical, and the screen reference is house-style-specimen.html. Documents match the spec as written. When the spec changes, the template, the specimen, and the stylesheets change with it.

Committee papers, proposals, and assessment reports go out as Word or PDF from templates/house-style-template.docx, which applies these same tokens. The document uses Montserrat and Roboto Serif where installed and falls back to Arial and Georgia. PDFs are exported from Word so the fonts embed.

Student-facing documents are screen-first and ship as finished HTML. The handbooks and guides apply this style through `documents/handbooks/handbooks.css`, and the Theory and Musicianship set through `curriculum/undergraduate-theory-musicianship/theory-musicianship.css`. The roadmaps layer `documents/roadmaps/roadmaps.css` on top for the general-education color and for print. The posted semester syllabi use `documents/syllabi/assets/syllabus.css`. These pages load the house fonts as web fonts. The handbooks add a fixed sidebar table of contents, anchored sections, and inline office popovers, and they're published as finished HTML on GitHub Pages, with Cascade linking to them.

The printed handouts in `documents/print/` are HTML rendered to PDF with WeasyPrint through `documents/print/print.css`.

The admissions email templates carry inline styles only, with no stylesheet, no tables, and no fixed widths, and the Salesforce wrapper controls layout. The page that presents them is house-styled through `documents/handbooks/handbooks.css`.

The Cascade website takes structural markup only (headings, paragraphs, tables, links), and Cascade supplies the appearance. The markup is given in chat for pasting into Cascade and isn't kept in this repository. When Cascade strips or changes a tag, the markup is adjusted.
