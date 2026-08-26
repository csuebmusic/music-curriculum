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

LINKS = """<p style="margin:0 0 0.4em 0;"><strong>Other places to look</strong></p>
<ul style="margin:0 0 1em 0;padding-left:1.4em;">
<li><a href="https://www.csueastbay.edu/music/" style="color:#6E1F2A;">Department of Music</a></li>
<li><a href="https://www.csueastbay.edu/admissions/index.html" style="color:#6E1F2A;">Admissions</a></li>
<li><a href="https://www.csueastbay.edu/visit/campustours.html" style="color:#6E1F2A;">Campus tours</a></li>
<li><a href="https://www.csueastbay.edu/housing/" style="color:#6E1F2A;">University housing</a></li>
<li><a href="https://www.csueastbay.edu/financialaid/" style="color:#6E1F2A;">Financial aid</a></li>
<li><a href="https://www.csueastbay.edu/admissions/how-to-videos.html" style="color:#6E1F2A;">Video answers to common questions</a></li>
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

ASK = ("Call (510) 885-3135 or write " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu")
       + ". A person reads that inbox.")

T = {}

T["01-ba-application-in-progress"] = dict(
  subject="You've started your application to CSUEB Music",
  plans="Music BA, Music Additional Degree", stage="Application in Progress",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("You&rsquo;ve started an application to the " + A("https://www.csueastbay.edu/music/prospective/ba.html","B.A. in Music") + " at Cal State East Bay, and we&rsquo;re glad you did."),
    P("A little about us. Our ensembles play around the Bay Area and abroad. Our faculty are working performers, composers, and scholars, and classes are small enough that they will know your name and your playing. Students here write, produce, perform, conduct, and teach, often in the same week. There is more on the " + A("https://www.csueastbay.edu/music/about-us/index.html","Department of Music") + " site."),
    P("If anything about the application is unclear, ask us. " + ASK),
    P("We&rsquo;ll be in touch as you go. Come see us on campus when you can."),
    FOOTER, LINKS]))

T["02-ba-application-received"] = dict(
  subject="Your application is in. Here's what comes next",
  plans="Music BA, Music Additional Degree", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Department of Music is in. Nice work."),
    P("Now come visit. You can meet the faculty, sit in on a rehearsal, and see what an ordinary week looks like around here. Write to " + A("mailto:music@csueastbay.edu","music@csueastbay.edu") + " and we&rsquo;ll set it up."),
    P("And audition for a scholarship. We award them to incoming students every year, and the same materials count as your applied area placement, so one audition does both jobs. Deadlines are fixed in the application season, and in-person dates go up each year: " + A("https://www.csueastbay.edu/music/prospective/how-to-apply/auditions.html","scholarship auditions and applied area placements") + "."),
    H("Three things to take care of"),
    UL([
      "Activate your NetID. It reaches you within 48 hours of applying, and you&rsquo;ll need it for MyCSUEB and for your Horizon email.",
      "Send your transcripts. The fastest route is to have each school send them electronically to " + A("mailto:electronictranscripts@csueastbay.edu","electronictranscripts@csueastbay.edu") + ". Your admission offer won&rsquo;t come until they arrive.",
      "Watch " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + ". That&rsquo;s where you track your status and, later, accept your offer."]),
    P("Questions about a visit or an audition? " + ASK),
    FOOTER]))

T["03a-ma-application-in-progress"] = dict(
  subject="Your M.A. in Music application at Cal State East Bay",
  plans="Music MA", stage="Application in Progress",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thanks for starting an application to the " + A("https://www.csueastbay.edu/music/prospective/ma.html","Master of Arts in Music") + ". You&rsquo;ll pick one area to work in: Performance (Classical or Jazz), Choral Conducting, or Composition."),
    P("A bachelor&rsquo;s degree in music is the usual preparation and we do encourage it, though it isn&rsquo;t a hard requirement: we read applications without one case by case, and self-taught musicians have come through the program. We do ask for good academic standing at your most recent college or university."),
    H("What goes into CSUApply"),
    UL([
      "Your CV or r&eacute;sum&eacute;.",
      "Two letters of recommendation, from teachers or colleagues who can speak to your readiness for graduate work.",
      "A statement of purpose, 2 pages, on what you want from a graduate degree in music and where you&rsquo;re headed in the short and long term.",
      "Evidence of your abilities in your area. What that means varies by area, and it&rsquo;s laid out on the " + A("https://www.csueastbay.edu/music/prospective/how-to-apply/index.html","How to Apply") + " page."]),
    P("Stuck on any of it? " + ASK),
    FOOTER]))

T["03b-certificate-application-in-progress"] = dict(
  subject="Your certificate application at Cal State East Bay",
  plans="Cert: Music, Single Sub Matter", stage="Application in Progress",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thanks for starting an application to the " + A("https://www.csueastbay.edu/music/prospective/music-ed.html","Single Subject Matter Preparation Certificate in Music") + ". It&rsquo;s the path to the California Single Subject Teaching Credential in Music, which lets you teach any area of music from kindergarten through high school."),
    P("This route is for people who already hold a bachelor&rsquo;s degree."),
    H("What goes into CSUApply"),
    UL([
      "Your CV or r&eacute;sum&eacute;.",
      "Contact details for two references. They&rsquo;ll be asked for letters later, so give them a heads up.",
      "A statement of purpose, 2 to 3 double-spaced pages, on your background in music and why you want to teach K&ndash;12.",
      "Unofficial transcripts from every school you&rsquo;ve attended."]),
    P("Questions while you put it together? " + ASK),
    FOOTER]))

GTA = ("<strong>Graduate Teaching Associates</strong> teach. You&rsquo;d lead classroom or lab sections, build "
       "course materials, run exams, tutor, and grade. You need to be admitted to a CSUEB graduate degree program "
       "related to the assignment, enrolled, and holding a 3.0 with progress toward the degree. Pay is per "
       "course-unit assigned.")
ISA = ("<strong>Instructional Student Assistants</strong> support teaching: grading, tutoring, and related work. "
       "You need relevant coursework and enrollment in at least 4 units, or recent enrollment with continued "
       "eligibility. Up to 20 hours a week, at rates set by level.")
GLASOW = ("<strong>The Glenn Glasow Graduate Fellowship in Composition</strong> covers a year of study for one "
          "composer, who premieres a new piece at the Glenn Glasow Memorial Concert. There&rsquo;s no separate "
          "application. We choose from the scores already in your program application.")

def received_tail(items):
    return "\n\n".join([
      H("Paying for it"),
      P("The Office of Graduate Studies runs fellowships, research funding, and other support across the University: " + A("https://www.csueastbay.edu/graduate-studies/graduate-opportunities.html","Graduate Opportunities") + "."),
      P("The Department has its own: " + A("https://www.csueastbay.edu/music/prospective/scholarships.html","Music Scholarships") + "."),
      UL(items),
      P("Anything you want to ask before you hear from us? " + ASK),
      FOOTER])

T["04a-ma-application-received"] = dict(
  subject="Your M.A. application is complete. What happens now",
  plans="Music MA", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Master of Arts in Music is complete. Thank you."),
    P("We read graduate applications as they come in. Once the Office of Graduate Admissions has been through your CSUApply file, we move to a decision. Your status shows up in " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + "."),
    received_tail([GTA, ISA, GLASOW])]))

T["04b-certificate-application-received"] = dict(
  subject="Your certificate application is complete. What happens now",
  plans="Cert: Music, Single Sub Matter", stage="Application Received",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Your application to the Single Subject Matter Preparation Certificate in Music is complete. Thank you."),
    P("We read graduate applications as they come in. Once the Office of Graduate Admissions has been through your CSUApply file, we move to a decision. Your status shows up in " + A("https://www.csueastbay.edu/mycsueb/","MyCSUEB") + "."),
    received_tail([ISA])]))

T["05-inquiry"] = dict(
  subject="Music at Cal State East Bay",
  plans="All plans containing Music", stage="Inquired",
  body="\n\n".join([
    P("Hi {{FIRST_NAME}},"),
    P("Thanks for getting in touch with the " + A("https://www.csueastbay.edu/music/index.html","Department of Music") + ". Here&rsquo;s what we run."),
    UL([
      A("https://www.csueastbay.edu/music/prospective/ba.html","<strong>B.A. in Music</strong>") + ". 120 units of applied lessons, ensembles, and coursework across performance, composition, music technology, jazz, and music education. If the University admits you, you&rsquo;re in the major.",
      A("https://www.csueastbay.edu/music/prospective/ma.html","<strong>M.A. in Music</strong>") + ". 32 units, in Performance (Classical or Jazz), Choral Conducting, or Composition.",
      A("https://www.csueastbay.edu/music/prospective/music-ed.html","<strong>Single Subject Matter Preparation Certificate in Music</strong>") + ". The path to the California teaching credential in music. Take it inside the B.A., inside the M.A., or on its own if you already hold a bachelor&rsquo;s.",
      A("https://www.csueastbay.edu/music/prospective/blended-b.a-m.a-4+1.html","<strong>FAST 4+1 B.A./M.A.</strong>") + ". Both degrees in five years, for students already in the B.A. here, who apply in the junior year.",
      A("https://www.csueastbay.edu/music/prospective/music-minor.html","<strong>Music Minor</strong>") + ". 21 units, open to any major."]),
    P(A("https://www.csueastbay.edu/music/prospective/how-to-apply/index.html","How to apply") + " &middot; " + A("https://www.csueastbay.edu/music/prospective/scholarships.html","Music scholarships")),
    P("Come see the place. Write to " + A("mailto:music@csueastbay.edu","music@csueastbay.edu") + " and we&rsquo;ll show you around."),
    FOOTER, LINKS]))

os.makedirs("templates", exist_ok=True)
for k, v in T.items():
    v["src"] = OPEN + v["body"] + CLOSE
    open("templates/%s.html" % k, "w").write(v["src"] + "\n")

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
    <table class="hb-table">
      <thead>
        <tr><th class="col-code">item</th><th>question</th></tr>
      </thead>
      <tbody>
        <tr><td class="col-code">admitted stage</td><td>The set has no message for applicants who receive an offer. The landing page exists: <a href="https://www.csueastbay.edu/music/prospective/how-to-apply/i-got-in-now-what.html">I got in! Now what?</a> Accepting the offer and the $110 pre-enrollment fee currently sit in email 2, which reaches applicants before a decision.</td></tr>
        <tr><td class="col-code">stage definition</td><td>What distinguishes Application in Progress from Application Received: submission in CSUApply, or verification by Admissions.</td></tr>
        <tr><td class="col-code">plan codes</td><td>Confirm the exact plan values, in particular Music Additional Degree, and confirm that every plan containing Music resolves to one of the four rows above.</td></tr>
        <tr><td class="col-code">subject lines</td><td>Subject lines are sentence case and carry no emoji. Confirm this against the University's convention for automated mail.</td></tr>
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
print("wrote %d templates and index.html" % len(T))
