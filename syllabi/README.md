# semester syllabi

California State University, East Bay, Department of Music.

Posted syllabi for individual sections in a given term, one file per section. Each file has a permanent web address that can go straight into a Canvas course. The master templates stay in [`curriculum/`](../curriculum/) and are copied here at the start of a term.

## terms

- [fall 2026](https://csuebmusic.github.io/music-curriculum/syllabi/fall-2026/)

## naming

Term folders are `fall-2026`, `spring-2027`, `summer-2027`. Files are the course code and the section number: `MUS108-01.html`, `MUS118-02.html`.

The Canvas link for a posted syllabus follows the same pattern:

```
https://csuebmusic.github.io/music-curriculum/syllabi/fall-2026/MUS108-01.html
```

The address stays fixed once the file exists, and edits appear at it within about a minute.

## posting a syllabus

1. Open the term folder for your course.
2. Copy the master template from `curriculum/` into it, or copy an existing file from a previous term.
3. Rename it to the course code and section number.
4. Fill in the editable block at the top of the file.
5. Add a row for it in the term's `index.html`.
6. Paste the link into your Canvas course.

## editing a file in the browser

A GitHub account with collaborator access on this repository is all that is required. Ask Inés for an invitation.

1. Open the file on github.com and click the pencil icon at the top right.
2. Edit the text in the box.
3. Click **Commit changes**, write one line describing the edit, keep **Commit directly to the main branch** selected, and confirm.
4. Wait about a minute, then reload the live page to see the result.

Pressing the period key anywhere in the repository opens a full editor in the browser tab, with search and replace across the file. Commits happen in the source control panel on the left.

## what to edit

Every file marks one block near the top, between comment rules, holding the term, section, class number, meeting days and times, room, final exam slot, and instructor contact details. Replace the text between the tags and leave the tags themselves in place.

Below that block sits the approved course text: catalog description, learning outcomes, workload, materials, requirements, grading, policies, and the university statements. The week-by-week schedule can be adjusted for pacing. Changes to outcomes, unit values, or grading weights go through the curriculum process rather than here.

Every version of a file is kept, and any earlier version can be restored from the file's history on github.com.
