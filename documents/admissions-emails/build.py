#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build.py

Single source for the Music admissions email set.

Content lives in the T dictionary below, one entry per template, grouped by
degree and ordered by application status. Running this script writes
templates/*.html and regenerates index.html.

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

U = dict(
  ba      = "https://www.csueastbay.edu/music/prospective/ba.html",
  ma      = "https://www.csueastbay.edu/music/prospective/ma.html",
  cert    = "https://www.csueastbay.edu/music/prospective/music-ed.html",
  fast    = "https://www.csueastbay.edu/music/prospective/blended-b.a-m.a-4+1.html",
  minor   = "https://www.csueastbay.edu/music/prospective/music-minor.html",
  apply   = "https://www.csueastbay.edu/music/prospective/how-to-apply/index.html",
  aud     = "https://www.csueastbay.edu/music/prospective/how-to-apply/auditions.html",
  gotin   = "https://www.csueastbay.edu/music/prospective/how-to-apply/i-got-in-now-what.html",
  schol   = "https://www.csueastbay.edu/music/prospective/scholarships.html",
  about   = "https://www.csueastbay.edu/music/about-us/index.html",
  home    = "https://www.csueastbay.edu/music/index.html",
  current = "https://www.csueastbay.edu/music/current/index.html",
  ens     = "https://www.csueastbay.edu/music/ensembles.html",
  mrc     = "https://www.csueastbay.edu/music/facilities/resource-center.html",
  equip   = "https://www.csueastbay.edu/music/facilities/equipment-office.html",
  fac     = "https://www.csueastbay.edu/music/faculty.html",
  events  = "https://www.csueastbay.edu/music/news-events/index.html",
  my      = "https://www.csueastbay.edu/mycsueb/",
  fee     = "https://www.csueastbay.edu/admissions/after-youre-accepted/enrollment-fee.html",
  gradopp = "https://www.csueastbay.edu/graduate-studies/graduate-opportunities.html",
  trans   = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/transcript-and-document-submission.html",
  ughb    = "https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html",
  grhb    = "https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html",
  certrm  = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html",
  deadlines = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/index.html",
  gdeadlines = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/graduate-and-credential-students.html",
)

CALL = "Call (510) 885-3135 or write " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu") + "."
ASK = CALL
COORD = ("Write to the Graduate Coordinator at " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu")
         + " or call (510) 885-3135.")
TRANSCRIPTS = A("mailto:electronictranscripts@csueastbay.edu", "electronictranscripts@csueastbay.edu")
MYCSUEB = A(U["my"], "MyCSUEB")

T = {}

def add(key, group, stage, subject, body):
    T[key] = dict(group=group, stage=stage, subject=subject, body="\n\n".join(body))

CONDITIONS = P("Open " + MYCSUEB + " and read your To Do List. Whatever is holding up the offer is named "
               "there, usually final transcripts or proof that a degree was conferred. Ask each school to "
               "send transcripts electronically to " + TRANSCRIPTS + ". The deadlines on those items are firm.")

GTA = ("<strong>Graduate Teaching Associates</strong> teach. You&rsquo;d lead classroom or lab sections, build "
       "course materials, run exams, tutor, and grade. You need to be admitted to a CSUEB graduate degree program "
       "related to the assignment, enrolled, and holding a 3.0 with progress toward the degree. Pay is per "
       "course-unit assigned.")
ISA = ("<strong>Instructional Student Assistants</strong> support teaching: grading, tutoring, and related work. "
       "You need relevant coursework and enrollment in at least 4 units, or recent enrollment with continued "
       "eligibility. Up to 20 hours a week, at rates set by level.")
GLASOW = ("<strong>The Glenn Glasow Graduate Fellowship in Composition</strong> covers a year of study for one "
          "composer, who premieres a new piece at the Glenn Glasow Memorial Concert. There is no separate "
          "application. We choose from the scores already in your program application.")

def funding(items):
    return "\n\n".join([
      H("Paying for it"),
      P("The Office of Graduate Studies runs fellowships, research funding, and other support across the "
        "University: " + A(U["gradopp"], "Graduate Opportunities") + ". The Department has its own: "
        + A(U["schol"], "Music Scholarships") + "."),
      UL(items)])

# ============================================================ all plans

add("00-inquiry", "all", "Inquired",
  "Music at East Bay", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for your interest in the " + A(U["home"], "Department of Music") + " at Cal State East Bay. We&rsquo;re a small department "
    "inside a large and unusually mixed university, and we take our students seriously as the musicians "
    "they already are. They perform and record, compose and arrange, score for film and games, produce "
    "and design sound in the studios, conduct choirs and ensembles, teach music in California schools, "
    "and go on to graduate study."),
  UL([
    A(U["ba"], "<strong>B.A. in Music</strong>") + ". 120 units of applied lessons, ensembles, and coursework across performance, composition, music technology, jazz, and music education.",
    A(U["ma"], "<strong>M.A. in Music</strong>") + ". 32 units, in Performance (Classical or Jazz), Choral Conducting, or Composition.",
    A(U["cert"], "<strong>Single Subject Matter Preparation Certificate in Music</strong>") + ". The path to the California teaching credential in music. Take it inside the B.A., inside the M.A., or on its own if you already hold a bachelor&rsquo;s.",
    A(U["fast"], "<strong>FAST 4+1 B.A./M.A.</strong>") + ". Both degrees in five years, for students already in the B.A. here, who apply in the junior year.",
    A(U["minor"], "<strong>Music Minor</strong>") + ". 21 units, open to any major."]),
  P(A(U["apply"], "How to apply") + " &middot; " + A(U["schol"], "Music scholarships")),
  P("Come visit us: the recital hall, the studios, and whatever rehearsal happens to be running that "
    "afternoon. " + ASK),
  FOOTER, LINKS])

# ============================================================ b.a.

add("ba-1-application-in-progress", "ba", "Application in Progress",
  "Your Music application", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the " + A(U["ba"], "B.A. in Music") + " at Cal State East Bay."),
  P("If anything in the application is unclear, don&rsquo;t hesitate to reach out, we are here to help. " + CALL),
  P("You can also begin thinking about your scholarship audition. We award scholarships to incoming students "
    "every year, and the same materials serve as the applied area placement that every music major completes "
    "before starting lessons. Requirements differ by area, and the deadlines fall during the application "
    "season: "
    + A(U["aud"], "scholarship auditions and applied area placements") + "."),
  P("There&rsquo;s more about the programs, the faculty, and performance opportunities on the "
    + A(U["about"], "Department of Music") + " site. And remember, you&rsquo;re welcome on campus any time!"),
  FOOTER, LINKS])

add("ba-2-application-received", "ba", "Application Received",
  "Now, your audition", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations! Your application IS IN."),
  H("Sign up for your scholarship audition"),
  P("We award scholarships to incoming students every year, and the same materials serve as the applied "
    "area placement that every music major "
    "completes before starting lessons. All the information is on the "
    + A(U["aud"], "scholarship auditions and applied area placements") + " page. Sign up!"),
  H("Other things to do now"),
  UL([
    "<strong>Activate your NetID.</strong> The University assigns you one within 48 hours of applying, and you need it for MyCSUEB and for your Horizon email account.",
    "<strong>Send your transcripts.</strong> Ask each school you&rsquo;ve attended (high school, community college, or any other 4-year college) to send them electronically to " + TRANSCRIPTS + ". Your admission offer will not be released until we receive them. " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Check " + MYCSUEB + ".</strong> Your status and anything still outstanding show up there.",
    "<strong>Come and visit.</strong> Meet the faculty, sit in on a rehearsal, and see an ordinary Tuesday here. Write to " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu") + " and we&rsquo;ll set it up."]),
  P("Questions about a visit or an audition? " + CALL),
  FOOTER])

add("ba-3-conditionally-admitted", "ba", "Conditionally Admitted",
  "Conditionally admitted", [
  P("Hi {{FIRST_NAME}},"),
  P("You have been conditionally admitted to the B.A. in Music. The offer becomes final once the outstanding "
    "items on your record are cleared."),
  H("What is outstanding"),
  UL([
    "<strong>Read your To Do List in " + MYCSUEB + ".</strong> Everything holding up the offer is named there, usually final transcripts or proof that a degree was conferred.",
    "<strong>Send the missing documents.</strong> Ask each school you&rsquo;ve attended (high school, community college, or any other 4-year college) to send transcripts electronically to " + TRANSCRIPTS + ". " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Meet the " + A(U["deadlines"], "document deadlines") + ".</strong> They are firm, and the offer does not become final until the items clear."]),
  H("If you have not auditioned yet"),
  P("Scholarship auditions are still open, and we award scholarships to incoming students every year. All the "
    "information is on the " + A(U["aud"], "scholarship auditions and applied area placements") + " page. "
    "Sign up!"),
  P("Questions about any of it? " + CALL),
  FOOTER])

add("ba-4-fully-admitted", "ba", "Fully Admitted",
  "Your offer of admission", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the B.A. in Music at Cal State East Bay."),
  P("To claim your spot, log in to " + MYCSUEB + ", open the Admissions tile, choose Accept Admission, and "
    "pay the $110 " + A(U["fee"], "pre-enrollment fee") + ", which goes toward orientation. Your status "
    "updates once the payment clears."),
  P("Then read " + A(U["gotin"], "I got in! Now what?") + ", which walks through orientation, advising, and "
    "the department steps ahead."),
  P("Scholarships ask nothing further of you. We consider incoming students from the audition and application "
    "materials already on file."),
  P("Questions before you accept? " + CALL),
  FOOTER])

add("ba-5-admission-accepted", "ba", "Admission Accepted",
  "Before classes begin", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer, and there are four things worth lining up before the "
    "semester starts."),
  UL([
    "<strong>Applied area placement.</strong> Every music major does one before starting lessons on a principal instrument or voice, any time up to the end of the first week. A scholarship audition already counts. " + A(U["aud"], "What to prepare") + ".",
    "<strong>Ensembles.</strong> Auditions and placement happen at the first meeting of each ensemble. Register for the course, then turn up to that first class. " + A(U["ens"], "Our ensembles") + ".",
    "<strong>Advising.</strong> You&rsquo;ll be assigned a faculty advisor in the Department for the major itself. General education runs through Bay Advisor, where your GE advisor and the rest of your success team are listed. See both before you register.",
    "<strong>Keyboard.</strong> Three semesters of group keyboard, normally MUS 118, MUS 119, and MUS 218. Get them into your plan early."]),
  P("Questions about any of it? " + ASK),
  FOOTER])

add("ba-6-active", "ba", "Active",
  "Welcome to Music", [
  P("Hi {{FIRST_NAME}},"),
  P("You are enrolled now, and welcome to the Department."),
  P("Read the " + A(U["ughb"], "Undergraduate Handbook") + " when you have an hour. Applied levels and juries, "
    "recital requirements, the keyboard sequence, ensembles, health and safety, and the policies you&rsquo;ll "
    "want in hand are all in it. " + A(U["current"], "Student Resources") + " is the shorter route, with "
    "advising, roadmaps, and forms alongside."),
  P("One thing to build into the semester from the start is concert attendance: while you are enrolled in "
    "applied lessons you need ten a semester, any Department event counts as one credit, and performing in "
    "one counts as a half. You record your own attendance with OneTap on your phone, and the visitor app is "
    "worth installing before your first event."),
  P("The building is yours to use. The " + A(U["mrc"], "Music Resource Center") + " and the "
    + A(U["equip"], "Music Equipment Office") + " hold the scores, instruments, and gear, and concerts and "
    "deadlines go up on " + A(U["events"], "News &amp; Events") + "."),
  P("Your applied teacher and your advisor are the first people to ask. After that, " + CALL.lower()[0] + CALL[1:]),
  FOOTER])

# ============================================================ m.a.

add("ma-1-application-in-progress", "ma", "Application in Progress",
  "Starting your M.A.", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the " + A(U["ma"], "Master of Arts in Music") + ". You&rsquo;ll "
    "work in one area: Performance (Classical or Jazz), Choral Conducting, or Composition."),
  P("A bachelor&rsquo;s degree in music is the usual preparation and we do encourage it, though it isn&rsquo;t "
    "a hard requirement. We read applications without one case by case, and self-taught musicians have come "
    "through the program. We do ask for good academic standing at your most recent college or university."),
  H("What goes into CSUApply"),
  UL([
    "Your CV or r&eacute;sum&eacute;.",
    "Two letters of recommendation, from teachers or colleagues who can speak to your readiness for graduate work.",
    "A statement of purpose, 2 pages, on what you want from a graduate degree in music and where you&rsquo;re headed in the short and long term.",
    "Evidence of your abilities in your area. What that means varies by area, and it&rsquo;s laid out on the " + A(U["apply"], "How to Apply") + " page."]),
  P("Questions about any of it? " + ASK),
  FOOTER])

add("ma-2-application-received", "ma", "Application Received",
  "Your M.A. application", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, your application to the Master of Arts in Music is complete."),
  P("We read graduate applications as they come in, and once the Office of Graduate Admissions has been "
    "through your CSUApply file we move to a decision. Your status shows up in " + MYCSUEB + "."),
  funding([GTA, ISA, GLASOW]),
  P("Anything you want to ask before you hear from us, " + CALL.lower()[0] + CALL[1:]),
  FOOTER])

add("ma-3-conditionally-admitted", "ma", "Conditionally Admitted",
  "Conditionally admitted, M.A.", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations. You&rsquo;re admitted to the M.A. in Music, with a couple of documents still outstanding."),
  CONDITIONS,
  P("Nothing about the conditions changes the work ahead: the seminar core, four semesters of applied lessons "
    "and ensemble in your area, a public capstone, and an oral comprehensive examination."),
  P("Anything unclear, " + COORD.lower()[0] + COORD[1:]),
  FOOTER])

add("ma-4-fully-admitted", "ma", "Fully Admitted",
  "Your M.A. offer", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the Master of Arts in Music at Cal State East "
    "Bay."),
  P("To accept your offer, log in to " + MYCSUEB + " and open the Admissions tile. The pre-enrollment fee is "
    "listed there and paid at the same time."),
  P("What lies ahead is 32 units over four semesters. A shared seminar core in analysis and post-tonal "
    "practice, the history and theory of jazz, interdisciplinary collaboration, advanced conducting, "
    "entrepreneurship in the arts, the social and ecological dimensions of music, and teaching music in higher "
    "education. Alongside it, four semesters of applied lessons and ensemble in your area, a public capstone, "
    "and an oral comprehensive examination in the final semester."),
  P("Questions before you accept? " + COORD),
  FOOTER])

add("ma-5-admission-accepted", "ma", "Admission Accepted",
  "Before the M.A. begins", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer. Here is how the first semester takes shape."),
  UL([
    "<strong>Applied lessons.</strong> The Graduate Coordinator registers you from the emphasis you declared at admission. You then arrange the weekly lesson time directly with your instructor.",
    "<strong>Ensemble.</strong> You perform in one every semester. Auditions and placement happen at the first meeting, so register for the course and turn up to that first class. " + A(U["ens"], "Our ensembles") + ".",
    "<strong>Seminars.</strong> Your first semester is MUS 601, Analysis of Musical Styles, and MUS 603, Entrepreneurship in the Arts, alongside lessons and ensemble. Eight units.",
    "<strong>Funding.</strong> Teaching Associate and Instructional Student Assistant assignments open before the semester. If either interests you, say so now rather than later."]),
  P("The Graduate Coordinator is your first stop for sequencing, the capstone, or the exam. " + COORD),
  FOOTER])

add("ma-6-active", "ma", "Active",
  "Welcome to the M.A.", [
  P("Hi {{FIRST_NAME}},"),
  P("You are enrolled now, and welcome."),
  P("Read the " + A(U["grhb"], "Graduate Handbook") + " when you have an hour. Sequencing, the Level 6 juries "
    "for your area, advancement to candidacy, the capstone, and the comprehensive examination are all in it, "
    "and " + A(U["current"], "Student Resources") + " carries the same material in shorter form."),
  P("The degree runs two years and they go quickly. Advancement to candidacy falls at the end of the first "
    "year, and the capstone starts in your second semester and runs through the third and fourth, which "
    "leaves room to settle on repertoire, program, or portfolio before you have to. The comprehensive "
    "examination is oral, taken in the final semester, and scored in three categories: your area of "
    "emphasis, analysis and musical styles, and the profession and its contexts."),
  P("The building is yours to use. The " + A(U["mrc"], "Music Resource Center") + " and the "
    + A(U["equip"], "Music Equipment Office") + " hold the scores, instruments, and gear, and concerts go up "
    "on " + A(U["events"], "News &amp; Events") + "."),
  P("Anything to do with sequencing, candidacy, the capstone, or the exam comes to the Graduate Coordinator. "
    + COORD),
  FOOTER])

# ============================================================ certificate

add("cert-1-application-in-progress", "cert", "Application in Progress",
  "Starting your certificate", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the "
    + A(U["cert"], "Single Subject Matter Preparation Certificate in Music") + ". It&rsquo;s the path to the "
    "California Single Subject Teaching Credential in Music, which lets you teach any area of music from "
    "kindergarten through high school."),
  P("This route is for people who already hold a bachelor&rsquo;s degree."),
  H("What goes into CSUApply"),
  UL([
    "Your CV or r&eacute;sum&eacute;.",
    "Contact details for two references. They&rsquo;ll be asked for letters later. Give them a heads up.",
    "A statement of purpose, 2 to 3 double-spaced pages, on your background in music and why you want to teach K&ndash;12.",
    "Unofficial transcripts from every school you&rsquo;ve attended."]),
  P("Questions while you put it together? " + ASK),
  FOOTER])

add("cert-2-application-received", "cert", "Application Received",
  "Your certificate application", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, your application to the Single Subject Matter Preparation Certificate in Music is "
    "complete."),
  P("We read graduate applications as they come in, and once the Office of Graduate Admissions has been "
    "through your CSUApply file we move to a decision. Your status shows up in " + MYCSUEB + "."),
  funding([ISA]),
  P("Anything you want to ask before you hear from us, " + CALL.lower()[0] + CALL[1:]),
  FOOTER])

add("cert-3-conditionally-admitted", "cert", "Conditionally Admitted",
  "Conditionally admitted, certificate", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations. You&rsquo;re admitted to the Single Subject Matter Preparation Certificate in Music, "
    "with a couple of documents still outstanding."),
  CONDITIONS,
  P("Anything unclear about the conditions, " + CALL.lower()[0] + CALL[1:]),
  FOOTER])

add("cert-4-fully-admitted", "cert", "Fully Admitted",
  "Your certificate offer", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the Single Subject Matter Preparation "
    "Certificate in Music at Cal State East Bay."),
  P("To accept your offer, log in to " + MYCSUEB + " and open the Admissions tile. The pre-enrollment fee is "
    "listed there and paid at the same time."),
  P("The certificate covers the subject matter the state requires for the Single Subject Teaching Credential "
    "in Music. Finish it and you move into the credential program without a separate subject-matter "
    "examination."),
  P("Questions before you accept? " + CALL),
  FOOTER])

add("cert-5-admission-accepted", "cert", "Admission Accepted",
  "Before the certificate begins", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer."),
  P("Come and talk to us before you register. The coursework spans theory, history, conducting, and applied "
    "study, and the order you take it in depends on what your bachelor&rsquo;s already covered. The "
    + A(U["certrm"], "certificate roadmap") + " lays out the 31 units on their two-year rotation."),
  P("If applied lessons or an ensemble are part of your plan, ensemble auditions and placement happen at the "
    "first meeting: register for the course and turn up to that first class. " + A(U["ens"], "Our ensembles")
    + "."),
  P("Write or call to set up that conversation. " + ASK),
  FOOTER])

add("cert-6-active", "cert", "Active",
  "Welcome to the certificate", [
  P("Hi {{FIRST_NAME}},"),
  P("You are enrolled now, and welcome."),
  P("The " + A(U["grhb"], "Graduate Handbook") + " covers the certificate alongside the M.A.: applied study "
    "policies, juries, and the academic policies that apply to you. Advising, the certificate roadmap, and "
    "forms are on " + A(U["current"], "Student Resources") + "."),
  P("The building is yours to use. The " + A(U["mrc"], "Music Resource Center") + " and the "
    + A(U["equip"], "Music Equipment Office") + " hold the scores, instruments, and gear, the teaching "
    "studios are open to you, and concerts go up on " + A(U["events"], "News &amp; Events") + "."),
  P("Come to concerts as often as you can manage, since you will be teaching this repertoire soon enough and "
    "hearing it live is the fastest way into it."),
  P("Anything to do with sequencing or the credential pathway comes to us. " + CALL),
  FOOTER])


# ---------------------------------------------------------------- assembly

GROUPS = [
  ("all",  "all music plans",  None),
  ("ba",   "b.a. in music and additional degree", "Music BA, Music Additional Degree"),
  ("ma",   "m.a. in music",    "Music MA"),
  ("cert", "single subject matter preparation certificate", "Cert: Music, Single Sub Matter"),
]
CODE = {"all": "inq", "ba": "ba", "ma": "ma", "cert": "cert"}

ORDER, LABEL = [], {}
for g, _, _ in GROUPS:
    keys = [k for k in T if T[k]["group"] == g]
    keys.sort()
    for k in keys:
        ORDER.append(k)
        n = k.split("-")[1]
        LABEL[k] = CODE[g] if g == "all" else "%s %s" % (CODE[g], n)

os.makedirs("templates", exist_ok=True)
for k in ORDER:
    T[k]["src"] = OPEN + T[k]["body"] + CLOSE
    open("templates/%s.html" % k, "w").write(T[k]["src"] + "\n")

nav, cards, flow = [], [], []
i = 0
for g, gname, gplans in GROUPS:
    keys = [k for k in ORDER if T[k]["group"] == g]
    nav.append('  <a class="nav-sub" href="#g-%s">%s</a>' % (g, gname))
    flow.append('    <h3 id="f-%s">%s</h3>' % (g, gname))
    flow.append('    <table class="hb-table">\n      <thead>\n        <tr><th>application status</th>'
                '<th class="col-code">template</th></tr>\n      </thead>\n      <tbody>')
    cards.append('  <h3 id="g-%s">%s</h3>' % (g, gname))
    for k in keys:
        v = T[k]
        nav.append('  <a class="nav-sub2" href="#%s">%s</a>' % (k, LABEL[k]))
        flow.append('        <tr><td>%s</td><td class="col-code"><a href="#%s">%s</a></td></tr>'
                    % (v["stage"].lower(), k, LABEL[k]))
        cards.append("""  <div class="tpl" id="%s">
    <div class="tpl-head">
      <span class="tpl-id">%s</span>
      <span class="tpl-meta">%s</span>
      <span class="tpl-subject"><span>subject</span>%s</span>
    </div>
    <div class="tpl-bar">
      <button class="copy-btn" data-src="src-%d">copy html source</button>
      <span class="copy-note">paste into the html source view, not the rich-text editor</span>
    </div>
    <iframe class="tpl-frame" data-src="src-%d" title="%s preview"></iframe>
  </div>
  <script type="text/plain" id="src-%d">%s</script>""" % (
          k, LABEL[k], v["stage"].lower(), html.escape(v["subject"]), i, i, LABEL[k], i, v["src"]))
        i += 1
    flow.append('      </tbody>\n    </table>')

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
    <div class="subtitle">Automated messages for Music applicants, admits, and new students</div>
    <div class="meta-strip">
      <span class="meta-item">document: <strong>admissions email templates</strong></span>
      <span class="meta-item">system: <strong>salesforce</strong></span>
      <span class="meta-item">season: <strong>2026&ndash;2027</strong></span>
      <span class="meta-item">templates: <strong>%d</strong></span>
      <span class="meta-item">status: <strong>for review</strong></span>
    </div>
  </header>

  <section class="front" id="use">
    <h2>using this page</h2>
    <p>Each template below carries a rendered preview and its HTML source. Use <strong>copy html source</strong>, then paste into the HTML source view of the Salesforce editor. Pasting rendered text into the rich-text editor carries formatting from the browser and produces markup that does not survive the send.</p>
    <p>The markup is plain: paragraphs, lists, links, and inline styles only. It carries no tables, no fixed widths, and no fonts of its own beyond a serif stack, so the Salesforce wrapper controls layout and the Department header sits where the wrapper puts it. Each template marks the header position with an HTML comment.</p>
    <p>This page is the source. When a template changes, it changes here and the copy is taken again.</p>
  </section>

  <section class="hb-section" id="s1">
    <h2>send configuration</h2>
    <p>Every message in this set goes to the <strong>Email</strong> and <strong>Alternate Email</strong> fields on the applicant record. The university address issued with the NetID is not a send target for this set.</p>
    <div class="policy-block">
      <span class="policy-label">applies to every template</span>
      Applicants activate the Horizon account after they apply. Messages routed there are missed.
    </div>
  </section>

  <section class="hb-section" id="s2">
    <h2>flow</h2>
    <table class="hb-table">
      <thead>
        <tr><th>degree</th><th class="col-code">plan value</th></tr>
      </thead>
      <tbody>
        <tr><td>b.a. in music and additional degree</td><td class="col-code">Music BA, Music Additional Degree</td></tr>
        <tr><td>m.a. in music</td><td class="col-code">Music MA</td></tr>
        <tr><td>single subject matter preparation certificate</td><td class="col-code">Cert: Music, Single Sub Matter</td></tr>
      </tbody>
    </table>
%s
  </section>

  <section class="hb-section" id="s3">
    <h2>merge fields</h2>
    <table class="hb-table">
      <thead>
        <tr><th class="col-code">token</th><th>field</th><th>note</th></tr>
      </thead>
      <tbody>
        <tr><td class="col-code">{{FIRST_NAME}}</td><td>preferred name, falling back to first name</td><td>one formula field, used by every template</td></tr>
      </tbody>
    </table>
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
        <tr><td class="col-code">stage definitions</td><td>What distinguishes Application in Progress from Application Received: submission in CSUApply, or verification by Admissions. And what moves a record from Admission Accepted to Active: registration, or census.</td></tr>
        <tr><td class="col-code">plan codes</td><td>Confirm the exact plan values, in particular Music Additional Degree, and confirm that every plan containing Music resolves to one of the three degree groups above.</td></tr>
        <tr><td class="col-code">conditional wording</td><td>The conditional-admit templates send applicants to the MyCSUEB To Do List rather than naming conditions. If Salesforce can carry the outstanding items into the message, the templates should say so instead.</td></tr>
        <tr><td class="col-code">graduate fee</td><td>The undergraduate templates name the $110 pre-enrollment fee. Confirm the graduate figure, or leave those templates pointing at the amount shown in MyCSUEB.</td></tr>
        <tr><td class="col-code">active stage</td><td>Whether an enrolled student should receive automated mail from the admissions sequence at all, or whether the Active message belongs in a departmental list instead.</td></tr>
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
""" % ("\n".join(nav), len(T), "\n".join(flow), "\n".join(cards))

open("index.html", "w").write(page)
print("wrote %d templates and index.html" % len(T))
