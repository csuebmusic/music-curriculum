#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build.py

Single source for the Music admissions email set.

Content lives in the T dictionary below, one entry per template. Running this
script writes templates/*.html and regenerates index.html from them.

    python3 build.py
"""

import os, html

FOOTER = """<p style="margin:0 0 1em 0;">All the best,<br>
Department of Music</p>

<p style="margin:0 0 1em 0;font-size:14px;color:#5E6166;">
Department of Music &middot; CSUEB Music Building, MB 2569<br>
25800 Carlos Bee Boulevard, Hayward, CA 94542<br>
(510) 885-3135 &middot; <a href="mailto:music@csueastbay.edu" style="color:#6E1F2A;">music@csueastbay.edu</a>
</p>"""

LINKS = """<p style="margin:0 0 0.4em 0;"><strong>Other links you may find useful</strong></p>
<ul style="margin:0 0 1em 0;padding-left:1.4em;">
<li><a href="https://www.csueastbay.edu/music/" style="color:#6E1F2A;">Department of Music</a></li>
<li><a href="https://www.csueastbay.edu/admissions/index.html" style="color:#6E1F2A;">Admissions</a></li>
<li><a href="https://www.csueastbay.edu/visit/campustours.html" style="color:#6E1F2A;">Campus tours</a></li>
<li><a href="https://www.csueastbay.edu/housing/" style="color:#6E1F2A;">University housing</a></li>
<li><a href="https://www.csueastbay.edu/financialaid/" style="color:#6E1F2A;">Financial aid</a></li>
<li><a href="https://www.csueastbay.edu/admissions/how-to-videos.html" style="color:#6E1F2A;">Video tutorials for common questions</a></li>
</ul>"""

OPEN = ('<div style="font-family:Georgia,\'Times New Roman\',serif;font-size:16px;'
        'line-height:1.6;color:#1B1C1E;">\n'
        '<!-- MUSIC DEPARTMENT HEADER IMAGE -->\n')
CLOSE = "\n</div>"

def P(s): return '<p style="margin:0 0 1em 0;">%s</p>' % s
def A(href, text): return '<a href="%s" style="color:#6E1F2A;">%s</a>' % (href, text)
def UL(items):
    return ('<ul style="margin:0 0 1em 0;padding-left:1.4em;">\n'
            + "\n".join('<li style="margin:0 0 0.5em 0;">%s</li>' % i for i in items)
            + "\n</ul>")
def H(s): return '<p style="margin:1.4em 0 0.4em 0;"><strong>%s</strong></p>' % s

CONTACT = "Questions at any point: (510) 885-3135, " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu") + "."

T = {}

T["01-ba-application-in-progress"] = dict(
  subject="Your application to CSUEB Music has started",
  plans="Music BA, Music Additional Degree", stage="Application in Progress",
  body="\n\n".join([
    P("Dear {{FIRST_NAME}},"),
    P("Thank you for starting your application to the " + A("https://www.csueastbay.edu/music/prospective/ba.html","B.A. in Music") + " at Cal State East Bay."),
    P("Our ensembles perform across the Bay Area and internationally. Our faculty are active performers, composers, and scholars who teach and advise closely. There is more about the programs, the faculty, and performance opportunities on the " + A("https://www.csueastbay.edu/music/about-us/index.html","Department of Music") + " site."),
    P(CONTACT),
    P("Watch for further messages from us as you complete your application. We hope to see you on campus."),
    FOOTER, LINKS]))

T["02-ba-application-received"] = dict(
  subject="Your application is complete: what happens next",
  plans="Music BA, Music Additional Degree", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Department of Music at Cal State East Bay is complete."),
    P("Come visit us on campus. Meet the faculty, sit in on a rehearsal, and see what a week looks like for a music student here. Write to " + A("mailto:music@csueastbay.edu","music@csueastbay.edu") + " to arrange a visit."),
    P("<strong>Audition for a scholarship.</strong> The Department awards scholarships to incoming students each year, and your audition materials also serve as your applied area placement. Auditions have fixed deadlines in the application season, and in-person dates are announced each year. " + A("https://www.csueastbay.edu/music/prospective/how-to-apply/auditions.html","Scholarship auditions and applied area placements") + "."),
    H("Three things to take care of now"),
    UL([
      "Activate your NetID. Every applicant receives one within 48 hours of submitting the application. You will need it for MyCSUEB and for your Horizon email account.",
      "Send your transcripts. The fastest route is to have each institution send electronic transcripts to " + A("mailto:electronictranscripts@csueastbay.edu","electronictranscripts@csueastbay.edu") + ". Your admission offer is not released until this is done.",
      "Track your status in " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + ", where you will also accept or deny your admission offer."]),
    P(CONTACT), FOOTER]))

T["03a-ma-application-in-progress"] = dict(
  subject="Your M.A. in Music application at Cal State East Bay",
  plans="Music MA", stage="Application in Progress",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thank you for starting your application to the " + A("https://www.csueastbay.edu/music/prospective/ma.html","Master of Arts in Music") + " at Cal State East Bay. The degree supports advanced study in Performance (Classical or Jazz), Choral Conducting, and Composition."),
    P("The program asks for good academic standing at your most recent college or university. A bachelor&rsquo;s degree in music from an accredited institution is the usual preparation and we strongly encourage it, though it is not a strict requirement: we review applicants without one case by case."),
    H("Submit the following through CSUApply"),
    UL([
      "Curriculum vitae or r&eacute;sum&eacute;.",
      "Two letters of recommendation, from teachers or colleagues who can assess your readiness for graduate study.",
      "Statement of purpose, 2 pages, describing your objectives for a graduate degree in music and your short- and long-term goals.",
      "Evidence of your abilities in your area of emphasis. Requirements vary by area and are listed on the " + A("https://www.csueastbay.edu/music/prospective/how-to-apply/index.html","How to Apply") + " page."]),
    P(CONTACT), FOOTER]))

T["03b-certificate-application-in-progress"] = dict(
  subject="Your application to the Single Subject Matter Preparation Certificate in Music",
  plans="Cert: Music, Single Sub Matter", stage="Application in Progress",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thank you for starting your application to the " + A("https://www.csueastbay.edu/music/prospective/music-ed.html","Single Subject Matter Preparation Certificate in Music") + " at Cal State East Bay. The certificate prepares you for the California Single Subject Teaching Credential in Music, which authorizes instruction in any area of music from kindergarten through high school."),
    P("This route is for applicants who already hold a bachelor&rsquo;s degree."),
    H("Submit the following through CSUApply"),
    UL([
      "Curriculum vitae or r&eacute;sum&eacute;.",
      "Contact information for two references, who will be asked to submit recommendation letters on your behalf.",
      "Statement of purpose, 2 to 3 double-spaced pages, describing your background and training in music and your reasons for wanting to teach K&ndash;12 music.",
      "Unofficial transcripts from all previous higher education institutions."]),
    P(CONTACT), FOOTER]))

GTA = ("<strong>Graduate Teaching Associates</strong> lead classroom and laboratory instruction, prepare course "
       "materials, administer examinations, tutor, and assign grades. Eligibility: admission to a CSUEB graduate "
       "degree program related to the assignment, current enrollment, and a 3.0 GPA with progress toward the "
       "degree. GTAs are paid per course-unit assigned.")
ISA = ("<strong>Instructional Student Assistants</strong> support instruction through grading, tutoring, and "
       "related academic work. Eligibility: relevant coursework and current enrollment in at least 4 units, or "
       "recent enrollment with continued eligibility. ISAs work up to 20 hours per week, at rates set by "
       "assignment level.")
GLASOW = ("<strong>The Glenn Glasow Graduate Fellowship in Composition</strong> supports one year of graduate study "
          "for a composer, who premieres a new work at the Glenn Glasow Memorial Concert. Selection is made from "
          "the scores submitted with the program application, with no separate application.")

def received_tail(items):
    return "\n\n".join([
      H("Funding and support"),
      P("The Office of Graduate Studies coordinates fellowships, research opportunities, and other funding across the University: " + A("https://www.csueastbay.edu/graduate-studies/graduate-opportunities.html","Graduate Opportunities") + "."),
      P("The Department offers graduate funding of its own: " + A("https://www.csueastbay.edu/music/prospective/scholarships.html","Music Scholarships") + "."),
      UL(items), P(CONTACT), FOOTER])

T["04a-ma-application-received"] = dict(
  subject="Your M.A. application is complete: what happens next",
  plans="Music MA", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Master of Arts in Music at Cal State East Bay is complete."),
    P("The Department reviews graduate applications on a rolling basis. Once the Office of Graduate Admissions has reviewed your CSUApply application, we move to a decision. Track your status in " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + "."),
    received_tail([GTA, ISA, GLASOW])]))

T["04b-certificate-application-received"] = dict(
  subject="Your certificate application is complete: what happens next",
  plans="Cert: Music, Single Sub Matter", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Single Subject Matter Preparation Certificate in Music at Cal State East Bay is complete."),
    P("The Department reviews graduate applications on a rolling basis. Once the Office of Graduate Admissions has reviewed your CSUApply application, we move to a decision. Track your status in " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + "."),
    received_tail([GTA, ISA])]))

T["05-inquiry"] = dict(
  subject="Music at Cal State East Bay",
  plans="All plans containing Music", stage="Inquired",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thank you for your interest in the " + A("https://www.csueastbay.edu/music/index.html","Department of Music") + " at Cal State East Bay."),
    UL([
      A("https://www.csueastbay.edu/music/prospective/ba.html","<strong>B.A. in Music</strong>") + ". A 120-unit degree built on applied study, ensembles, and coursework spanning performance, composition, music technology, jazz, and music education. Admission to the University is admission to the major.",
      A("https://www.csueastbay.edu/music/prospective/ma.html","<strong>M.A. in Music</strong>") + ". A 32-unit degree with emphases in Performance (Classical or Jazz), Choral Conducting, and Composition.",
      A("https://www.csueastbay.edu/music/prospective/music-ed.html","<strong>Single Subject Matter Preparation Certificate in Music</strong>") + ". The route to the California Single Subject Teaching Credential in Music, taken inside the B.A., inside the M.A., or as a stand-alone graduate certificate.",
      A("https://www.csueastbay.edu/music/prospective/blended-b.a-m.a-4+1.html","<strong>FAST 4+1 B.A./M.A.</strong>") + ". Both degrees in five years, for students already enrolled in the B.A. at East Bay, who apply in the junior year.",
      A("https://www.csueastbay.edu/music/prospective/music-minor.html","<strong>Music Minor</strong>") + ". 21 units, open to any undergraduate major."]),
    P(A("https://www.csueastbay.edu/music/prospective/how-to-apply/index.html","How to apply") + " &middot; " + A("https://www.csueastbay.edu/music/prospective/scholarships.html","Music scholarships")),
    P(CONTACT), FOOTER, LINKS]))

os.makedirs("templates", exist_ok=True)
for k, v in T.items():
    src = OPEN + v["body"] + CLOSE
    v["src"] = src
    open("templates/%s.html" % k, "w").write(src + "\n")
for k,v in T.items():
    assert "—" not in v["src"], k
    assert "\u2019" not in v["src"] or "&rsquo;" in v["src"]


# ---------------------------------------------------------------- index page

ORDER = ["01-ba-application-in-progress","02-ba-application-received",
         "03a-ma-application-in-progress","03b-certificate-application-in-progress",
         "04a-ma-application-received","04b-certificate-application-received","05-inquiry"]
LABEL = {"01-ba-application-in-progress":"email 1","02-ba-application-received":"email 2",
         "03a-ma-application-in-progress":"email 3a","03b-certificate-application-in-progress":"email 3b",
         "04a-ma-application-received":"email 4a","04b-certificate-application-received":"email 4b",
         "05-inquiry":"email 5"}

nav, cards, flowrows = [], [], []
for i, k in enumerate(ORDER):
    v = T[k]
    nav.append('  <a class="nav-sub2" href="#%s">%s</a>' % (k, LABEL[k]))
    flowrows.append('        <tr><td>%s</td><td>%s</td><td class="col-code"><a href="#%s">%s</a></td></tr>'
                    % (v["plans"], v["stage"].lower(), k, LABEL[k]))
    cards.append("""  <div class="tpl" id="%s">
    <div class="tpl-head">
      <span class="tpl-id">%s</span>
      <span class="tpl-meta">%s &middot; %s</span>
      <span class="tpl-subject"><span>subject</span>%s</span>
    </div>
    <div class="tpl-bar">
      <button class="copy-btn" data-src="src-%d">copy html source</button>
      <span class="copy-note">paste into the html source view, not the rich-text editor</span>
    </div>
    <iframe class="tpl-frame" data-src="src-%d" title="%s preview"></iframe>
  </div>
  <script type="text/plain" id="src-%d">%s</script>""" % (
      k, LABEL[k], html.escape(v["plans"]), v["stage"].lower(), html.escape(v["subject"]),
      i, i, LABEL[k], i, v["src"]))

MERGE = [
 ("{{FIRST_NAME}}", "preferred name, falling back to first name", "single formula field, used by all seven templates"),
]

page = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Admissions Email Templates &middot; CSU East Bay Department of Music</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&amp;family=Courier+Prime:ital,wght@0,400;0,700;1,400;1,700&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="../handbooks/handbooks.css">
<link rel="stylesheet" href="admissions-emails.css">
</head>
<body>

<nav>
  <div class="nav-logo">Department of Music<br>Admissions Email Templates<br>CSU East Bay</div>
  <div class="nav-version">Revised August 2026</div>

  <a href="#use">using this page</a>
  <hr class="nav-divider">

  <a href="#s1"><span class="nav-num">01</span>send configuration</a>
  <a href="#s2"><span class="nav-num">02</span>flow</a>
  <a href="#s3"><span class="nav-num">03</span>merge fields</a>
  <a href="#s4"><span class="nav-num">04</span>templates</a>
%s
  <a href="#s5"><span class="nav-num">05</span>open items</a>
</nav>

<main>

  <header class="page-header">
    <div class="institution">California State University, East Bay &middot; Department of Music</div>
    <h1>Admissions Email Templates</h1>
    <div class="subtitle">Automated messages for Music applicants and inquiries</div>
    <div class="meta-strip">
      <span class="meta-item">document: <strong>admissions email templates</strong></span>
      <span class="meta-item">system: <strong>salesforce</strong></span>
      <span class="meta-item">season: <strong>2026&ndash;2027</strong></span>
      <span class="meta-item">revised: <strong>august 2026</strong></span>
      <span class="meta-item">status: <strong>for review</strong></span>
    </div>
  </header>

  <section class="front" id="use">
    <h2>using this page</h2>
    <p class="measure">Each template below carries a rendered preview and its HTML source. Use <strong>copy html source</strong>, then paste into the HTML source view of the Salesforce editor. Pasting rendered text into the rich-text editor carries formatting from the browser and produces markup that does not survive the send.</p>
    <p class="measure">The markup is plain: paragraphs, lists, links, and inline styles only. It carries no tables, no fixed widths, and no fonts of its own beyond a serif stack, so the Salesforce wrapper controls layout and the Department header sits where the wrapper puts it. Each template marks the header position with an HTML comment.</p>
    <p class="measure">This page is the source. When a template changes, it changes here and the copy is taken again.</p>
  </section>

  <section class="hb-section" id="s1">
    <h2>send configuration</h2>
    <p class="measure">Every message in this set goes to the <strong>Email</strong> and <strong>Alternate Email</strong> fields on the applicant record. The university address issued with the NetID is not a send target for this set.</p>
    <div class="policy-block">
      <span class="policy-label">applies to all seven templates</span>
      Applicants activate the Horizon account after they apply. Messages routed there are missed.
    </div>
  </section>

  <section class="hb-section" id="s2">
    <h2>flow</h2>
    <table class="hb-table">
      <thead>
        <tr><th>plan</th><th>stage</th><th class="col-code">template</th></tr>
      </thead>
      <tbody>
%s
      </tbody>
    </table>
    <p class="measure">Three Music pathways have no application plan of their own and take no stage-triggered mail. The FAST 4+1 B.A./M.A. is an internal application filed in the junior year by students already enrolled in the B.A. The Music Minor is declared through the MyCompass Change of Major, Minor, or Concentration form. The Single Subject Matter Preparation Certificate taken inside the B.A. or the M.A. runs on the parent plan; only stand-alone certificate applicants carry the <span class="gloss">Cert: Music, Single Sub Matter</span> plan.</p>
    <p class="measure">Email 5 sends once. An inquiry that later attaches an application plan moves to the plan flow and does not repeat the inquiry message.</p>
  </section>

  <section class="hb-section" id="s3">
    <h2>merge fields</h2>
    <table class="hb-table">
      <thead>
        <tr><th class="col-code">token</th><th>field</th><th>note</th></tr>
      </thead>
      <tbody>
        <tr><td class="col-code">{{FIRST_NAME}}</td><td>preferred name, falling back to first name</td><td>one formula field, used by all seven templates</td></tr>
      </tbody>
    </table>
    <p class="measure">The templates carry a single token in a syntax Salesforce does not resolve, so an unreplaced token is visible rather than silent. Replace it with the merge syntax for the object these messages send from, and confirm the fallback returns the legal first name when the preferred name is blank.</p>
  </section>

  <section class="hb-section" id="s4">
    <h2>templates</h2>
%s
  </section>

  <section class="hb-section" id="s5">
    <h2>open items</h2>
    <p class="measure">These are for the meeting.</p>
    <table class="hb-table">
      <thead>
        <tr><th class="col-code">item</th><th>question</th></tr>
      </thead>
      <tbody>
        <tr><td class="col-code">admitted stage</td><td>The set has no message for applicants who receive an offer. The landing page exists: <a href="https://www.csueastbay.edu/music/prospective/how-to-apply/i-got-in-now-what.html">I got in! Now what?</a> Accepting the offer and the $110 pre-enrollment fee currently sit in email 2, which reaches applicants before a decision.</td></tr>
        <tr><td class="col-code">stage definition</td><td>What distinguishes Application in Progress from Application Received: submission in CSUApply, or verification by Admissions.</td></tr>
        <tr><td class="col-code">plan codes</td><td>Confirm the exact plan values, in particular Music Additional Degree, and confirm that every plan containing Music resolves to one of the four rows above.</td></tr>
        <tr><td class="col-code">gta eligibility</td><td>Graduate Teaching Associate eligibility requires admission to a graduate degree program. Whether stand-alone certificate students qualify decides whether that item stays in email 4b.</td></tr>
        <tr><td class="col-code">subject lines</td><td>Subject lines are sentence case and carry no emoji. Confirm this against the University's convention for automated mail.</td></tr>
        <tr><td class="col-code">scholarship page</td><td>Two scholarship pages are live: <span class="gloss">/music/prospective/scholarships.html</span>, linked by these templates, and <span class="gloss">/music/scholarships/index.html</span>, linked by the site navigation. One should redirect to the other.</td></tr>
        <tr><td class="col-code">reminder mail</td><td>Whether a nudge goes to applicants who start an application and do not submit, and at what interval.</td></tr>
      </tbody>
    </table>
  </section>

</main>

<script>
document.querySelectorAll("iframe.tpl-frame").forEach(function (f) {
  var src = document.getElementById(f.dataset.src).textContent;
  f.srcdoc = '<!DOCTYPE html><meta charset="utf-8"><style>body{margin:0;font-family:Georgia,serif}</style>' + src;
  f.addEventListener("load", function () {
    f.style.height = (f.contentDocument.documentElement.scrollHeight + 24) + "px";
  });
});
document.querySelectorAll(".copy-btn").forEach(function (b) {
  b.addEventListener("click", function () {
    var t = document.getElementById(b.dataset.src).textContent;
    navigator.clipboard.writeText(t).then(function () {
      b.textContent = "copied";
      b.classList.add("done");
      setTimeout(function () { b.textContent = "copy html source"; b.classList.remove("done"); }, 1800);
    });
  });
});
</script>

</body>
</html>
""" % ("\n".join(nav), "\n".join(flowrows), "\n".join(cards))

open("index.html","w").write(page)
assert "\u2014" not in page

print("wrote %d templates and index.html" % len(T))
