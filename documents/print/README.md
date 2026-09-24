# print

Printed handouts for recruiting events and graduate fairs, US Letter, in the house style (`../../conventions/house-style.md`). Each sheet has an HTML source and the PDF rendered from it. Two-page sheets print front and back.

## files

Information sheets:

- [ba-infosheet.pdf](ba-infosheet.pdf), from [ba-infosheet.html](ba-infosheet.html): the B.A. in Music starting sheet for prospective first-year, transfer, and second-bachelor's students, two pages.
- [fast-infosheet.pdf](fast-infosheet.pdf), from [fast-infosheet.html](fast-infosheet.html): the FAST 4+1 B.A./M.A. starting sheet, two pages.
- [music-ed-infosheet.pdf](music-ed-infosheet.pdf), from [music-ed-infosheet.html](music-ed-infosheet.html): the Single Subject Matter Preparation Certificate in Music starting sheet, two pages.
- [ma-infosheet.pdf](ma-infosheet.pdf), from [ma-infosheet.html](ma-infosheet.html): the M.A. in Music starting sheet for prospective students, two pages.

Roadmaps, catalog 2027–2028:

- [ba-roadmap-4-year.pdf](ba-roadmap-4-year.pdf), from [ba-roadmap-4-year.html](ba-roadmap-4-year.html): the B.A. in Music from first-year entry, eight semesters, with the music electives list, two pages.
- [ba-roadmap-transfer.pdf](ba-roadmap-transfer.pdf), from [ba-roadmap-transfer.html](ba-roadmap-transfer.html): the B.A. in Music from Music ADT transfer entry, four semesters, with the music electives list, two pages.
- [fast-roadmap.pdf](fast-roadmap.pdf), from [fast-roadmap.html](fast-roadmap.html): FAST 4+1 from first-year entry, ten semesters, two pages.
- [fast-transfer-roadmap.pdf](fast-transfer-roadmap.pdf), from [fast-transfer-roadmap.html](fast-transfer-roadmap.html): FAST 2+1 from Music ADT transfer entry, six semesters, with the music electives list, two pages.
- [music-ed-roadmap.pdf](music-ed-roadmap.pdf), from [music-ed-roadmap.html](music-ed-roadmap.html): the certificate's two-year course rotation, one page.
- [ma-roadmap.pdf](ma-roadmap.pdf), from [ma-roadmap.html](ma-roadmap.html): the M.A. in Music four-semester sequence, one page.

Stylesheet:

- [print.css](print.css): the shared print stylesheet. Roadmap rows are tinted by type: general education, free elective, units counting toward both degrees, and certificate.

## QR codes

Each sheet carries empty 0.85-inch squares for QR codes, captioned with the destination. A caption that appears on several sheets takes the same code everywhere.

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
| Graduate handbook | M.A. roadmap | https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html#roadmap |
| This roadmap online | B.A. 4-year roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html |
| This roadmap online | B.A. transfer roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html |
| This roadmap online | FAST 4+1 roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html |
| This roadmap online | FAST 2+1 transfer roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html |
| This roadmap online | music education roadmap | https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html |

## rendering

Render with WeasyPrint, with Montserrat (400, 600, 700) and Roboto Serif (400, 600) available to it. Application deadlines stay off the sheets.
