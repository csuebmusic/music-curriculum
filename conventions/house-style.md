# university house style

version 1, locked june 2026. the on-screen reference is house-style-specimen.html.

This governs the curriculum and university documents I produce and share through this project: proposals, committee papers, assessment reports, handbooks. It is distinct from the course projects' warm cream and rust pedagogical style, and distinct from the website pocket, which uses the styling Cascade gives me and carries none of this.

The character is a typed departmental memo: a monospace doing all the structural work, a serif carrying the prose, on a white page with one deep accent. The serif keeps long passages readable; the typewriter face keeps the document recognizably mine and sets it apart from the pedagogical look.

## palette

Reference these by name. Hex is the source of truth.

- paper (#FFFFFF): document background
- canvas (#F2F2F0): the surrounding preview surface only, never inside the document
- ink (#1B1C1E): primary text
- ink-soft (#5E6166): labels, metadata, captions, secondary text
- rule (#E6E6E3): hairline rules and borders
- accent (#6E1F2A, oxblood): the record rule, section markers, table header rule, defined-term underline, links, the note border
- accent-tint (#F7ECED): the wash behind the note block

One accent only. Oxblood does all the structural marking, and nothing competes with it.

## type

Two families, fixed roles.

- body: Source Serif 4, 17px, line-height 1.7. Carries prose, table cells, defined-term text, note text. Word fallback: Georgia.
- chrome and headings: Courier Prime, weights 400 and 700. Carries the eyebrow, the title, section headings, field labels, the table header, the metadata line, the note label, the footer. Word fallback: Courier New.

## structure

record header. The document opens with a labeled grid (committee, document, effective term, status) set in mono, closed by a 1.5px oxblood rule. This is the signature element, the routing slip every curriculum item already travels with.

title. Mono, 700, around 26px, lowercase.

metadata line. Mono, ink-soft, with any routing id set in ink.

section headings. Mono, 700, around 17px, lowercase, preceded by a two-digit mono section number in oxblood. Number sections only when the document is a real ordered sequence, which a formal proposal is.

body. Serif, generous leading.

defined terms. An oxblood underline on the term, followed by a short mono gloss in parentheses, ink-soft. This carries the glossing habit from the course readings into print.

tables. Mono header row, lowercase, closed by a 1.5px oxblood bottom rule. Serif cells, 1px hairline row rules, the rightmost column right-aligned. Unit changes set in mono (3 → 4).

note block. A faint oxblood tint, a 3px oxblood left border, a mono label, serif text. Square corners, since the border is single-sided.

footer. A top hairline, then mono ink-soft: document id on the left, page on the right.

## restraint

Lowercase headings throughout, no title case, no all caps. Flat surfaces: hairline rules, no shadow, white page. Whitespace generous by default, tightened for dense multi-page proposals where this spacing would run long.

## channels

This file is canonical; source-of-truth points here. The screen reference is house-style-specimen.html. For Word or PDF submissions, the matching template applies these same tokens, and the document either uses Courier Prime and Source Serif 4 where installed or falls back to Courier New and Georgia. The Cascade website pocket does not use this style.
