# university house style

version 1.2, september 2026. the on-screen reference is house-style-specimen.html.

This governs the curriculum and university documents I produce and share through this project: proposals, committee papers, assessment reports, and handbooks. The course projects use their own style. The Cascade website pocket uses none of this one.

## palette

Reference these by name. Hex is the source of truth.

- paper (#FFFFFF): document background
- canvas (#F2F2F0): the surrounding preview surface only, never inside the document
- ink (#1B1C1E): primary text
- ink-soft (#5E6166): labels, metadata, captions, secondary text
- rule (#E6E6E3): hairline rules and borders
- accent (#6E1F2A, oxblood): the record rule, section markers, table header rule, defined-term underline, links, the note border
- accent-tint (#F7ECED): the wash behind the note block

One accent only.

## type

Two families, fixed roles.

- body: Source Serif 4, 17px, line-height 1.7. Carries prose, table cells, defined-term text, note text. Word fallback: Georgia.
- chrome and headings: Courier Prime, weights 400 and 700. Carries the eyebrow, the title, section headings, field labels, the table header, the metadata line, the note label, the footer. Word fallback: Courier New.

## structure

record header. The document opens with a labeled grid (committee, document, effective term, status) set in mono, closed by a 1.5px oxblood rule.

title. Mono, 700, around 26px, lowercase.

metadata line. Mono, ink-soft, with any routing id set in ink.

section headings. Mono, 700, around 17px, lowercase, preceded by a two-digit mono section number in oxblood. Number sections in formal proposals and other ordered documents.

body. Serif, generous leading.

defined terms. An oxblood underline on the term, followed by a short mono gloss in parentheses, ink-soft.

tables. Mono header row, lowercase, closed by a 1.5px oxblood bottom rule. Serif cells, 1px hairline row rules, the rightmost column right-aligned. Unit changes set in mono (3 → 4).

note block. A faint oxblood tint, a 3px oxblood left border, a mono label, serif text. Square corners.

footer. A top hairline, then mono ink-soft: document id on the left, page on the right.

## links

Every link opens in a new tab, set with `target="_blank" rel="noopener noreferrer"`. This covers external URLs, links to other documents in the repository, and mailto links. An anchor to a section of the same document takes no target and no rel.

## restraint

Lowercase headings throughout, no title case, no all caps. Flat surfaces: hairline rules, no shadow, white page. Whitespace generous by default and tighter in multi-page proposals.

## channels

This file is canonical; source-of-truth points here. The screen reference is house-style-specimen.html. For Word or PDF submissions, the matching template applies these same tokens, and the document either uses Courier Prime and Source Serif 4 where installed or falls back to Courier New and Georgia. The Cascade website pocket does not use this style.
