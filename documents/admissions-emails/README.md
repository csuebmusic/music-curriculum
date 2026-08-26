# admissions emails

The automated messages Salesforce sends to Music applicants and inquiries, with the flow that triggers them.

`index.html` is the source and the thing to share. It carries the send configuration, the plan and stage flow, the merge fields, a rendered preview of each template, and a copy control that puts the HTML source on the clipboard. Published at
[csuebmusic.github.io/music-curriculum/documents/admissions-emails/](https://csuebmusic.github.io/music-curriculum/documents/admissions-emails/).

`templates/` holds the same seven templates as standalone files, one per message.

The template markup is paragraphs, lists, links, and inline styles. It carries no tables, no fixed widths, and no font declarations beyond a serif stack, so the Salesforce wrapper controls layout and the Department header sits where the wrapper puts it. Each template marks the header position with an HTML comment. All text is ASCII with named entities for anything outside it.

Paste into the HTML source view of the Salesforce editor. Pasting rendered text into the rich-text editor carries formatting from the browser.

`build.py` is the single source for the content. Edit the entry for a template there and run `python3 build.py` to rewrite `templates/` and `index.html`. Styling comes from `../handbooks/handbooks.css` with `admissions-emails.css` for the page furniture.
