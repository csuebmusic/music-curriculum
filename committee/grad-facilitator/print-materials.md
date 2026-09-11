# graduate fair print materials

Working file for the printed program materials taken to graduate fairs. Source set: `OneDrive_2026-09-10.zip`, folder `Grad Program Infosheets`, 49 PDFs and one QR master workbook. Scanned 10 September 2026.

Text read with Ghostscript txtwrite. Catalog links read from the PDF link annotations. The QR code destinations are encoded in the code images and have not been decoded.

## currency

- Both all-university lists are dated 25-26: `CSUEB Graduate Programs List 25-26.pdf` and `CSUEB FAST Programs List 25-26.pdf`. Recruitment this season is for Fall 2027 entry.
- Every CBE sheet is stamped F25. The Marketing Analytics sheet is dated 012224.

## hyperlinks embedded in the PDFs

These are link annotations inside each file, mostly sitting on the course lines. A link shows nothing on paper, so they reach a reader only when the file is shared digitally and clicked.

- Every catalog link in the set points at catalog year 39. The current catalog is 44. Nothing in the set links to the current catalog.
- `MBA Concentration Flyers F25 Sept 25.pdf` links to catalog year 24.
- poid 18184 appears on eight sheets: MA History, MA Music, MPA, MS Health Care Administration, MS Early Childhood Education, MS Chemistry, MS Chemistry-Biochem, MS Mathematics. On MA History it is the only link. On MS Chemistry the only links are 18184 and 18184#tt762, with no chemistry-specific program id. What 18184 resolves to is unresolved: curl and web fetch both hit the catalog's bot challenge and the search index does not carry the poid.

## destinations outside the university or retired

- PASC Credential Infosheet: `www20.csueastbay.edu/ceas/departments/el/index.html`, both a retired host and a dissolved college path.
- MA IXDIA Infosheet: `multimedia.csueastbay.edu` and `calstateapply.edu`, which is not the application domain.
- MBA Concentration Flyers: contains a link to `gorgias.com`.
- The apply link takes four forms across the set: `calstate.edu/apply`, `www2.calstate.edu/apply`, `calstateapply.edu`, `csueastbay.edu/cbegrad`.

## QR codes

- The QR master lists 33 entries and holds 32 QR images. The same image is anchored to both the MS Chemistry and the MS Computer Science rows.
- The four college QR tables carry no text layer.
- The QR index covers 32 programs plus the two lists. MS Educational Leadership has no entry of its own. All teaching credentials collapse into one Teaching Credential Programs entry. No certificate has an entry.

## sheets labeled as a program that carry one concentration

- MS Statistics InfoSheet is headed Data Science Concentration. The catalog carries five Statistics concentrations.
- MS Computer Science InfoSheet is headed Artificial Intelligence and Machine Learning Concentration. The catalog carries three.
- MS Kinesiology InfoSheet is headed Human Movement and Sport Science Concentration. The catalog carries two.

## content read page by page

Sheets read as rendered pages rather than as extracted text.

MS Statistics. The body names concentrations in Actuarial Science, Applied Statistics, Data Science, and Mathematical Statistics, omitting Biostatistics, where the catalog carries five. It then sends readers to the Biostatistics chapter of the university catalog as though Biostatistics were a separate degree. The catalog carries Biostatistics as a Statistics concentration; the Graduate Studies tile carries it as a separate master's. The sheet prints the typo "concentrations in in" and the catalog phrase "stated elsewhere in this catalog".

MS Special Education. The concentration name appears two ways on one sheet, Mild/Moderate Support Needs and Mild-Moderate Support Needs. The catalog uses the first.

## unit totals, checked across all 49

Text for every sheet is extracted with Ghostscript at `-dTextFormat=0`, which emits glyph positions. Columns are separated by finding the page gutter as the x band with the lowest line coverage, then splitting each row at it. Requirements sections and their course lines read in order.

Every declared section total was checked against the courses listed beneath it. No unit errors. Sheets that list elective menus carry course units well above the declared total by design: Marine Science lists 120 against 30, Mathematics 82 against 30, Kinesiology 73 against 32, Chemistry 43 against 30, Special Education 50 against 43. Those are menus, not errors.

Three sheets were read in full to rule out a discrepancy and are correct: Hospitality (30 units, 27 required plus an elective), History (30 units, 24 core plus a 6-unit capstone), Statistics (34 units, 20 core required).


Course titles and numbers have not been checked against the catalog. The catalog blocks automated requests, so that comparison needs a person with a browser.

Two printed program names differ from the catalog: the Hospitality sheet prints a comma before "and", and the doctorate prints "Doctor of Education in Educational Leadership for Social Justice" where the catalog and the tiles carry "Educational Leadership, Ed.D." 

## contacts to verify

- MSA sheet gives `jingwen-yang@csueastbay.edu` with a hyphen. The Graduate Program Info workbook gives `jingwen.yang@csueastbay.edu` with a dot.
- MS Marine Science gives `work--gradprog@mlml.calstate.edu`.
- MS Curriculum and Instruction and MS Early Childhood Education both give `lempesis@csueastbay.edu`. The workbook gives `valerie.helgren-lempesis@csueastbay.edu`.
- MSMA gives `yi.he@csueastbay.edu`. The workbook names Lan Wu as coordinator.
- MS Educational Leadership, a master's, routes to `credentials@csueastbay.edu` at the credentials office number.

## deadlines

Application deadlines stay off the per-program sheets. They travel on a separate dated handout, reprinted each cycle.

Four CBE sheets print application windows as month and day ranges with no year: Fall October 1 to June 1, Spring August 1 to November 1, with the international windows a month earlier. Written that way they don't go stale, and they sit outside the rule without breaking it.

The sheets send readers to three different places for dates, or to none. MA IXDIA points to the program website, MA Music to the published deadlines without naming where they are published, and the rest point nowhere.

Four CBE sheets print a version stamp on the page: VERSION: F25 on the MBA, Accountancy and Business Analytics sheets, Version: 24-25 on Marketing Analytics. Those are printed dates and they do go stale.

Date ranges that appear on several sheets (2018-2028 on MSA, 2025-2034 on MS Health Care Administration, 2009-2019 on the old MS Health Care Administration, 2019-2029 on the MBA flyers) sit next to accreditation text.

## the deadlines handout

One page, dated, carried to fairs alongside the program sheets. One row per program:

- terms accepting applications
- the university filing window for the term
- the department deadline where it falls earlier than the university one
- the department contact

Sources: `Graduate_Program_Info_Coordinator_Accepting_Deadlines.xlsx` for terms and coordinators, department confirmation for Fall 2027 dates. The International Programs admission requirements document carries department deadlines but is stamped 7/15/2025 and is a cycle behind.

Open: whether the per-program sheets should carry one line pointing to where deadlines live, and whether that line is a URL or a QR code.

## files not for use, stored with the live ones

- `MPA (Public Administration)/Old_MPA Infosheet.pdf`
- `MS Health Care Administration/Old_MS Health Care Administration Infosheet.pdf`
- `Teaching Credential Programs/Do_Not_Use_Multiple Subject Teaching Credential Infosheet.pdf`
- `Teaching Credential Programs/Do_Not_Use_Single Subject Teaching Credential Infosheet.pdf`

## filing

`MS Educational Leadership Infosheet.pdf` sits in the `EdD Educational Leadership` folder.

## coverage against the roster

No sheet exists for Quantitative Economics, Biostatistics, any certificate, or any credential other than PASC. See `programs.md` for the roster.

## the set

| college | file | program as printed | catalog links | contact | phone |
| --- | --- | --- | --- | --- | --- |
| CBE | CBE_College_Program_QR_Table.pdf | (image only, no text layer) |  |  |  |
| CBE | MBA generated/MBA Concentration  Fully Online Flyer F25 Sept 25.pdf | Master of Business Administration, General Business - Fully Online | none | cbe_grad@csueastbay.edu | (510) 885-2419 |
| CBE | MBA generated/MBA Concentration Flyers F25 Sept 25.pdf | Master of Business Administration, General Business | 24:9955 | cbe_grad@csueastbay.edu | (510) 885-2419 |
| CBE | MBA generated/MBA w Concentrations F25 Sept25.pdf | Master of Business Administration with Concentrations | none | alex.makarevich@csueastbay.edu | (510) 885-2419 |
| CBE | MSA Info Sheet/MSA Info Sheet F25 V3.pdf | Master of Science in Accountancy | none | jingwen-yang@csueastbay.edu | (510) 885-3397 |
| CBE | MSBA Info sheet/MSBA F25 V2.pdf | Master of Science in Business Analytics | none | msba@csueastbay.edu | (510) 885-2419 |
| CBE | MSMA Info sheet/msma-info-sheet-final012224.pdf | Master of Science in Marketing Analytics | none | yi.he@csueastbay.edu | (510) 885-2419 |
| CLASS | CLASS_College_Program_QR_Table.pdf | (image only, no text layer) |  |  |  |
| CLASS | EdD Educational Leadership/EdD Educational Leadership Infosheet.pdf | Doctor of Education in Educational Leadership for Social Justice | 39:18072 | edd@csueastbay.edu | (510) 885-3596 |
| CLASS | EdD Educational Leadership/MS Educational Leadership Infosheet.pdf | Master of Science in Educational Leadership | 39:18073 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | M.S. in Hospitality, Recreation and Tourism/MS HST Infosheet.pdf | Master of Science in Hospitality, Recreation, and Tourism | 39:18114 | hrt-graduate@csueastbay.edu | (510) 885-3043 |
| CLASS | MA History/MA History Infosheet.pdf | Master of Arts in History | 39:18184 | history@csueastbay.edu | (510) 885-3207 |
| CLASS | MA Music/MA Music Infosheet.pdf | Master of Arts in Music | 39:18184 | music@csueastbay.edu | (510) 885-3135 |
| CLASS | MA in Interaction Design and Interactive Art/MA IXDIA Infosheet.pdf | Master of Arts in Interaction Design and Interactive Art | 39:18041 | ixdia@csueastbay.edu | (510) 885-3111 |
| CLASS | MPA (Public Administration)/MPA Infosheet.pdf | Master of Public Administration | 39:18120, 39:18121, 39:18184 | publicadmin@csueastbay.edu | (510) 885-3253 |
| CLASS | MPA (Public Administration)/Old_MPA Infosheet.pdf | Master of Public Administration | 39:18120, 39:18121, 39:18184 | publicadmin@csueastbay.edu | (510) 885-3253 |
| CLASS | MS Counseling Psychology/MS Counseling Psychology - MFT.pdf | Master of Science in Counseling Psychology, Marriage and Family Therapy Concentration | 39:18105 | nancy.deatrick@csueastbay.edu | (510) 885-2272 |
| CLASS | MS Counseling Psychology/MS Counseling Psychology - SC.pdf | Master of Science in Counseling Psychology, School Counseling Concentration | 39:18106, 39:18107 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | MS Counseling Psychology/MS Counseling Psychology - SP.pdf | Master of Science in Counseling Psychology, School Psychology Concentration | 39:18107 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | MS Curriculum & Instruction/MS Curriculum and Instruction Infosheet.pdf | Master of Science in Curriculum and Instruction | 39:18296 | lempesis@csueastbay.edu | (510) 885-3006 |
| CLASS | MS Early Childhood Education/MS Early Childhood Education Infosheet.pdf | Master of Science in Early Childhood Education | 39:18139, 39:18184 | lempesis@csueastbay.edu | (510) 885-3006 |
| CLASS | MS Educational Technology/MS Educational Technology Infosheet.pdf | Master of Science in Educational Technology | 39:18210 | li-ling.chen@csueastbay.edu | (510) 885-4507 |
| CLASS | MS Health Care Administration/MS Health Care Administration Infosheet.pdf | Master of Science in Health Care Administration | 39:18184, 39:18328 | publicadmin@csueastbay.edu | (510) 885-3253 |
| CLASS | MS Health Care Administration/Old_MS Health Care Administration Infosheet.pdf | Master of Science in Health Care Administration | 39:18184, 39:18328 | publicadmin@csueastbay.edu | (510) 885-3253 |
| CLASS | MS Reading and Literacy_/MS Reading and Literacy Infosheet.pdf | Master of Science in Reading and Literacy | 39:18253 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | MS Special Education/MS Special Education Infosheet.pdf | Master of Science in Special Education | 39:18206, 39:18334 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | Teaching Credential Programs/Do_Not_Use_Multiple Subject Teaching Credential Infosheet.pdf | Multiple Subject Teaching Credential Program | 39:18135 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | Teaching Credential Programs/Do_Not_Use_Single Subject Teaching Credential Infosheet.pdf | Single Subject Teaching Credential Program | 39:18140 | credentials@csueastbay.edu | (510) 885-2272 |
| CLASS | Teaching Credential Programs/PASC Credential Infosheet.pdf | Preliminary Administrative Services Credential Program | 39:18133 | credentials@csueastbay.edu | (510) 885-2272 |
| COH | COH_College_Program_QR_Table.pdf | (image only, no text layer) |  |  |  |
| COH | MS Kinesiology/MS Kinesiology InfoSheet.pdf | Master of Science in Kinesiology, Human Movement and Sport Science Concentration | 39:18141, 39:18354 | kin@csueastbay.edu | (510) 885-3061 |
| COH | MS Nursing/MS Nursing InfoSheet.pdf | Master of Science in Nursing | 39:18360 | nursing@csueastbay.edu | (510) 885-3481 |
| COH | MS Speech-Language Pathology (SLP)/MS SLP InfoSheet.pdf | Master of Science in Speech-Language Pathology | 39:18176 | slhs@csueastbay.edu | (510) 885-3233 |
| COH | MSW/MSW Advanced InfoSheet .pdf | Master of Social Work, Advanced Standing Concentration | 39:18357 | swadmission@csueastbay.edu | (510) 885-4916 |
| COH | MSW/MSW InfoSheet .pdf | Master of Social Work | 39:18359 | swadmission@csueastbay.edu | (510) 885-4916 |
| CSCI | CSCI_College_Program_QR_Table.pdf | (image only, no text layer) |  |  |  |
| CSCI | MS Biological Sciences/MS Biological Sciences InfoSheet.pdf | Master of Science in Biological Sciences | 39:18117 | naturalsci@csueastbay.edu | (510) 885-3471 |
| CSCI | MS Chemistry/MS Chemistry InfoSheet.pdf | Master of Science in Chemistry | 39:18184 | chem@csueastbay.edu | (510) 885-3471 |
| CSCI | MS Chemistry/MS Chemistry-Biochem InfoSheet.pdf | Master of Science in Chemistry, Biochemistry Concentration | 39:18184, 39:18185 | chem@csueastbay.edu | (510) 885-3471 |
| CSCI | MS Computer Science/MS Computer Science InfoSheet.pdf | Master of Science in Computer Science, Artificial Intelligence and Machine Learning Concentration | 39:18207, 39:18208, 39:18353 | csgradadmissions@csueastbay.edu | (510) 885-4300 |
| CSCI | MS Construction Management/MS Construction Management InfoSheet.pdf | Master of Science in Construction Management | 39:18103 | construction@csueastbay.edu | (510) 885-4300 |
| CSCI | MS Engineering Management/MS Engineering Management InfoSheet.pdf | Master of Science in Engineering Management | 39:18104 | engineeringcsueb@csueastbay.edu | (510) 885-4300 |
| CSCI | MS Environmental Geosciences/MS Environmental Geosciences InfoSheet.pdf | Master of Science in Environmental Geosciences | 39:18108 | environmental.geosciences@csueastbay.edu | (510) 885-3471 |
| CSCI | MS Marine Science/MS Marine Science InfoSheet.pdf | Master of Science in Marine Science | 39:18186 | work--gradprog@mlml.calstate.edu | (510) 885-3471 |
| CSCI | MS Mathematics/MS Mathematics InfoSheet.pdf | Master of Science in Mathematics | 39:18128, 39:18184 | math@csueastbay.edu | (510) 885-3435 |
| CSCI | MS Statistics/MS Statistics InfoSheet.pdf | Master of Science in Statistics, Data Science Concentration | 39:18109, 39:18110, 39:18111, 39:18112, 39:18257 | statistics@csueastbay.edu | (510) 885-3435 |
| CSUEB | CSUEB Fast Program List/CSUEB FAST Programs List 25-26.pdf | FAST Programs List 2025-2026 | none | gradstudies@csueastbay.edu | 510-885-3716 |
| CSUEB | CSUEB Graduate Programs List_/CSUEB Graduate Programs List 25-26.pdf | Graduate Programs List 2025-2026 | none | gradstudies@csueastbay.edu | 510-885-3716 |
| CSUEB | CSUEB_Grad_Program_QR_Master.pdf | CSUEB Graduate Program QR Index | none |  |  |
