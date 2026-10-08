# print

Printed handouts for recruiting events and graduate fairs, US Letter, in the house style (`../../conventions/house-style.md`). Each sheet has an HTML source and the PDF rendered from it. Two-page sheets print front and back.

## files

Information sheets:

- [ba-infosheet.pdf](ba-infosheet.pdf), from [ba-infosheet.html](ba-infosheet.html): the B.A. in Music starting sheet for prospective first-year, transfer, and second-bachelor's students, two pages.
- [fast-infosheet.pdf](fast-infosheet.pdf), from [fast-infosheet.html](fast-infosheet.html): the FAST 4+1 B.A./M.A. starting sheet, two pages.
- [music-ed-infosheet.pdf](music-ed-infosheet.pdf), from [music-ed-infosheet.html](music-ed-infosheet.html): the Certificate in Music Education starting sheet, two pages.
- [ma-infosheet.pdf](ma-infosheet.pdf), from [ma-infosheet.html](ma-infosheet.html): the M.A. in Music starting sheet for prospective students, two pages.

Roadmaps, catalog 2027–2028:

- [ba-roadmap-4-year.pdf](ba-roadmap-4-year.pdf), from [ba-roadmap-4-year.html](ba-roadmap-4-year.html): the B.A. in Music from first-year entry in a fall A, eight semesters, with the music electives list, two pages.
- [ba-roadmap-4-year-fall-b.pdf](ba-roadmap-4-year-fall-b.pdf), from [ba-roadmap-4-year-fall-b.html](ba-roadmap-4-year-fall-b.html): the B.A. in Music from first-year entry in a fall B, eight semesters, with the music electives list, two pages.
- [ba-roadmap-transfer.pdf](ba-roadmap-transfer.pdf), from [ba-roadmap-transfer.html](ba-roadmap-transfer.html): the B.A. in Music from AA-T transfer entry in a fall A, four semesters, with the music electives list, two pages.
- [ba-roadmap-transfer-fall-b.pdf](ba-roadmap-transfer-fall-b.pdf), from [ba-roadmap-transfer-fall-b.html](ba-roadmap-transfer-fall-b.html): the B.A. in Music from AA-T transfer entry in a fall B, four semesters, with the music electives list, two pages.
- [fast-roadmap.pdf](fast-roadmap.pdf), from [fast-roadmap.html](fast-roadmap.html): FAST 4+1 from first-year entry in a fall A, ten semesters, three pages.
- [fast-roadmap-fall-b.pdf](fast-roadmap-fall-b.pdf), from [fast-roadmap-fall-b.html](fast-roadmap-fall-b.html): FAST 4+1 from first-year entry in a fall B, ten semesters, three pages.
- [fast-transfer-roadmap.pdf](fast-transfer-roadmap.pdf), from [fast-transfer-roadmap.html](fast-transfer-roadmap.html): FAST 2+1 from AA-T transfer entry in a fall A, six semesters, with the music electives list, two pages.
- [fast-transfer-roadmap-fall-b.pdf](fast-transfer-roadmap-fall-b.pdf), from [fast-transfer-roadmap-fall-b.html](fast-transfer-roadmap-fall-b.html): FAST 2+1 from AA-T transfer entry in a fall B, six semesters, with the music electives list, two pages.
- [music-ed-roadmap.pdf](music-ed-roadmap.pdf), from [music-ed-roadmap.html](music-ed-roadmap.html): the certificate's two-year course rotation, one page.
- [ma-roadmap.pdf](ma-roadmap.pdf), from [ma-roadmap.html](ma-roadmap.html): the M.A. in Music four-semester sequence from fall A entry, one page.
- [ma-roadmap-fall-b.pdf](ma-roadmap-fall-b.pdf), from [ma-roadmap-fall-b.html](ma-roadmap-fall-b.html): the M.A. in Music four-semester sequence from fall B entry, one page.
- [ba-composition-roadmap-transfer.pdf](ba-composition-roadmap-transfer.pdf), from [ba-composition-roadmap-transfer.html](ba-composition-roadmap-transfer.html): the B.A. in Music from Music ADT transfer entry with the music electives filled from composition, production, and music business courses, four semesters, with the music electives list, two pages.
- [ba-certificate-roadmap-4-year.pdf](ba-certificate-roadmap-4-year.pdf), from [ba-certificate-roadmap-4-year.html](ba-certificate-roadmap-4-year.html): the B.A. in Music with the Certificate in Music Education from first-year entry, eight semesters, two pages.
- [ba-certificate-roadmap-transfer.pdf](ba-certificate-roadmap-transfer.pdf), from [ba-certificate-roadmap-transfer.html](ba-certificate-roadmap-transfer.html): the B.A. in Music with the Certificate in Music Education from Music ADT transfer entry, four semesters, two pages.
- [fast-certificate-roadmap.pdf](fast-certificate-roadmap.pdf), from [fast-certificate-roadmap.html](fast-certificate-roadmap.html): FAST 4+1 with the Certificate in Music Education from first-year entry, ten semesters, three pages.
- [fast-transfer-certificate-roadmap.pdf](fast-transfer-certificate-roadmap.pdf), from [fast-transfer-certificate-roadmap.html](fast-transfer-certificate-roadmap.html): FAST 2+1 with the Certificate in Music Education from Music ADT transfer entry, six semesters, two pages.

Each roadmap sheet is the download behind the download pdf button on its online roadmap in `../roadmaps/`. The semester tables match the online roadmaps row for row.

Stylesheet and script:

- [print.css](print.css): the shared print stylesheet. Roadmap rows are tinted by type: general education, units counting toward both degrees, graduate credit by petition, and certificate.
- [qr.py](qr.py): draws the QR codes into the sheets.

## QR codes

Each sheet has 0.85-inch QR codes, captioned with the destination. A square is written as `<div class="qr" data-href="URL">`, and [qr.py](qr.py) draws the code for that URL inside it as inline SVG. A caption that appears on several sheets takes the same code everywhere.

| caption | sheets | destination |
| --- | --- | --- |
| B.A. in Music page | B.A. infosheet, FAST infosheet, music education infosheet | https://www.csueastbay.edu/music/prospective/ba.html |
| M.A. in Music page | M.A. infosheet, music education infosheet | https://www.csueastbay.edu/music/prospective/ma.html |
| Music education, Music education page | M.A. infosheet, B.A. infosheet, FAST infosheet, music education infosheet | https://www.csueastbay.edu/music/prospective/music-ed.html |
| FAST 4+1, FAST 4+1 page | M.A. infosheet, B.A. infosheet, FAST infosheet | https://www.csueastbay.edu/music/prospective/blended-b.a-m.a-4+1.html |
| Cal State Apply | M.A., B.A., and music education infosheets | https://www.calstate.edu/apply |
| Transcripts and documents | M.A., B.A., and music education infosheets | https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/transcript-and-document-submission.html |
| Graduate deadlines | M.A. infosheet, music education infosheet | https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/graduate-and-credential-students.html |
| Undergraduate deadlines | B.A. infosheet | https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/index.html |
| How to Apply, M.A. materials | M.A. infosheet, FAST infosheet | https://www.csueastbay.edu/music/prospective/how-to-apply/index.html#M.A. |
| Auditions and placements | B.A. infosheet | https://www.csueastbay.edu/music/prospective/how-to-apply/auditions.html |
| Music scholarships | M.A. infosheet, B.A. infosheet | https://www.csueastbay.edu/music/scholarships/index.html |
| Ensembles | B.A. infosheet | https://www.csueastbay.edu/music/ensembles.html |
| Roadmaps and undergraduate handbook | B.A. infosheet | https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html#roadmaps |
| FAST roadmaps | FAST infosheet | https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html#fast-roadmap |
| FAST in the undergraduate handbook | FAST infosheet | https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html#s8 |
| Certificate roadmap | music education infosheet | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html |
| Single Subject Credential | music education infosheet | https://www.csueastbay.edu/cssc/prospective-cred-student/single-subject.html |
| Roadmap and graduate handbook | M.A. infosheet | https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html#roadmap |
| This roadmap online | B.A. 4-year roadmap, fall A | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html |
| This roadmap online | B.A. 4-year roadmap, fall B | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html#fall-b |
| This roadmap online | B.A. transfer roadmap, fall A | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html |
| This roadmap online | B.A. transfer roadmap, fall B | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html#fall-b |
| This roadmap online | FAST 4+1 roadmap, fall A | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html |
| This roadmap online | FAST 4+1 roadmap, fall B | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html#fall-b |
| This roadmap online | FAST 2+1 transfer roadmap, fall A | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html |
| This roadmap online | FAST 2+1 transfer roadmap, fall B | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html#fall-b |
| This roadmap online | music education roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html |
| This roadmap online | M.A. roadmap, fall A | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ma-roadmap.html |
| This roadmap online | M.A. roadmap, fall B | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ma-roadmap.html#fall-b |
| This roadmap online | B.A. transfer roadmap, composition and production | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-composition-roadmap-2-year-transfer.html |
| This roadmap online | B.A. with certificate 4-year roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-certificate-roadmap-4-year.html |
| This roadmap online | B.A. with certificate transfer roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-certificate-roadmap-2-year-transfer.html |
| This roadmap online | FAST 4+1 with certificate roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-certificate-roadmap.html |
| This roadmap online | FAST 2+1 transfer with certificate roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-certificate-roadmap.html |

## rendering

Run `python3 qr.py` in this folder after adding or changing a QR square. Render with WeasyPrint, with Montserrat (400, 600, 700) and Roboto Serif (400, 600) available to it. University admission deadlines stay off the sheets.
