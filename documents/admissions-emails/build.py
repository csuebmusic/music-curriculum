#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build.py

Single source for the Music admissions email set.

Content lives in the T dictionary below, one entry per template, grouped by
degree and ordered by application status. Running this script writes
templates/*.html and regenerates index.html.

    python3 build.py
"""

import os, re, html

def FOOTER(close="All the best,"):
    return """<p style="margin:0 0 1em 0;">%s<br>
The Department of Music and Performing Arts</p>

<p style="margin:0 0 1em 0;font-size:14px;color:#5E6166;">
Department of Music and Performing Arts &middot; CSUEB Music Building, MB 2569<br>
25800 Carlos Bee Boulevard, Hayward, CA 94542<br>
(510) 885-3135 &middot; <a href="mailto:music@csueastbay.edu" style="color:#6E1F2A;">music@csueastbay.edu</a>
</p>""" % close

def LINKS(first):
    return """<p style="margin:0 0 0.4em 0;"><strong>Other places to look</strong></p>
<ul style="margin:0 0 1em 0;padding-left:1.4em;">
<li><a href="https://www.csueastbay.edu/music/" style="color:#6E1F2A;">%s</a></li>
<li><a href="https://www.csueastbay.edu/admissions/index.html" style="color:#6E1F2A;">Admissions</a></li>
<li><a href="https://www.csueastbay.edu/visit/campustours.html" style="color:#6E1F2A;">Campus tours</a></li>
<li><a href="https://www.csueastbay.edu/housing/" style="color:#6E1F2A;">University housing</a></li>
<li><a href="https://www.csueastbay.edu/financialaid/" style="color:#6E1F2A;">Financial aid</a></li>
<li><a href="https://www.csueastbay.edu/admissions/how-to-videos.html" style="color:#6E1F2A;">Video answers to common questions</a></li>
</ul>""" % first

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
  applyma = "https://www.csueastbay.edu/music/prospective/how-to-apply/index.html#M.A.",
  aud     = "https://www.csueastbay.edu/music/prospective/how-to-apply/auditions.html",
  gotin   = "https://www.csueastbay.edu/music/prospective/how-to-apply/i-got-in-now-what.html",
  schol   = "https://www.csueastbay.edu/music/prospective/scholarships.html",
  about   = "https://www.csueastbay.edu/music/about-us/index.html",
  home    = "https://www.csueastbay.edu/music/index.html",
  current = "https://www.csueastbay.edu/music/current/index.html",
  ens     = "https://www.csueastbay.edu/music/ensembles.html",
  mrc     = "https://www.csueastbay.edu/music/facilities/resource-center.html",
  equip   = "https://www.csueastbay.edu/music/facilities/equipment-office.html",
  events  = "https://www.csueastbay.edu/music/news-events/index.html",
  my      = "https://www.csueastbay.edu/mycsueb/",
  fee     = "https://www.csueastbay.edu/admissions/after-youre-accepted/enrollment-fee.html",
  gradopp = "https://www.csueastbay.edu/graduate-studies/graduate-opportunities.html",
  gradstudies = "https://www.csueastbay.edu/graduate-studies/index.html",
  gradadmit = "https://www.csueastbay.edu/graduate-studies/admitted-grad-students.html",
  cie     = "https://www.csueastbay.edu/cie/",
  cred    = "https://www.csueastbay.edu/cssc/prospective-cred-student/single-subject.html",
  trans   = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/transcript-and-document-submission.html",
  ughb    = "https://csuebmusic.github.io/music-curriculum/documents/handbooks/undergraduate-handbook.html",
  grhb    = "https://csuebmusic.github.io/music-curriculum/documents/handbooks/graduate-handbook.html",
  certrm  = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/music-education-certificate-roadmap.html",
  fastrm  = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-ba-ma-roadmap.html",
  fastrm2 = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/fast-transfer-ba-ma-roadmap.html",
  netid   = "https://www.csueastbay.edu/netid/netid-activation-instructions.html",
  rm4     = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-4-year.html",
  rm2     = "https://csuebmusic.github.io/music-curriculum/documents/roadmaps/ba-roadmap-2-year-transfer.html",
  ssc     = "https://www.csueastbay.edu/class-ssc/index.html",
  ugadmit = "https://www.csueastbay.edu/admissions/after-youre-accepted/undergrad-after-admitted.html",
  gradmit = "https://www.csueastbay.edu/admissions/graduate-requirements/next-steps.html",
  deadlines = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/index.html",
  gdeadlines = "https://www.csueastbay.edu/admissions/documents-deadlines-and-important-information/application-and-doc-deadlines/graduate-and-credential-students.html",
)

CALL = "Call (510) 885-3135 or write " + A("mailto:music@csueastbay.edu", "music@csueastbay.edu") + "."
GRADCLOSE = ("Whatever comes up, write to In&eacute;s Thiebaut, our Graduate Coordinator, at "
             + A("mailto:ines.thiebaut@csueastbay.edu", "ines.thiebaut@csueastbay.edu")
             + " or call (510) 885-3135. She would rather hear from you early than have you work it "
             "out alone.")
CERTCLOSE = ("Questions about the coursework or the credential pathway go to John Eros, who coordinates "
             "music education, at " + A("mailto:john.eros@csueastbay.edu", "john.eros@csueastbay.edu")
             + ". Anything about admission or sequencing goes to In&eacute;s Thiebaut, our Graduate "
             "Coordinator, at " + A("mailto:ines.thiebaut@csueastbay.edu", "ines.thiebaut@csueastbay.edu")
             + " or (510) 885-3135.")
TRANSCRIPTS = A("mailto:electronictranscripts@csueastbay.edu", "electronictranscripts@csueastbay.edu")
MYCSUEB = A(U["my"], "MyCSUEB")

T = {}

def add(key, group, stage, subject, body):
    T[key] = dict(group=group, stage=stage, subject=subject, body="\n\n".join(body))


GTA = ("<strong>Graduate Teaching Associates</strong> teach. You&rsquo;d lead classroom or lab sections, build "
       "course materials, run exams, tutor, and grade. You need to be admitted to a CSUEB graduate degree program "
       "related to the assignment, enrolled, and holding a 3.0 with progress toward the degree. Pay is per "
       "course-unit assigned.")
ISA = ("<strong>Instructional Student Assistants</strong> support teaching: grading, tutoring, and related work. "
       "You need relevant coursework and enrollment in at least 4 units, or recent enrollment with continued "
       "eligibility. Up to 20 hours a week, at rates set by level.")

def funding(items):
    return "\n\n".join([
      H("Important financial information"),
      P("The Office of Graduate Studies runs fellowships, research funding, and other support across the "
        "University: " + A(U["gradopp"], "Graduate Opportunities") + ". The Department has its own: "
        + A(U["schol"], "Music Scholarships") + ". We award music scholarships to entering students "
        "every year on the strength of the materials already in your application, and there is no "
        "extra step you need to complete to be eligible."),
      P("The graduate program also offers teaching opportunities to its graduate students as need "
        "arises. Let the Graduate Coordinator know if you are interested." + (" There are two kinds:"
        if len(items) > 1 else "")),
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
    A(U["cert"], "<strong>Single Subject Matter Preparation Certificate in Music</strong>") + ". Preparation for the California Single Subject Teaching Credential in Music. Add it to the B.A., add it to the M.A., or take it on its own if you already hold a bachelor&rsquo;s.",
    A(U["fast"], "<strong>FAST 4+1 B.A./M.A.</strong>") + " gets you both degrees in five years, for students already in the B.A. here, who apply in the junior year.",
    A(U["minor"], "<strong>Music Minor</strong>") + ". 21 units, open to any major."]),
  P(A(U["apply"], "How to apply") + " &middot; " + A(U["schol"], "Music scholarships")),
  P("Come visit us: the recital hall, the studios, and whatever rehearsal happens to be running that "
    "afternoon. " + CALL),
  FOOTER(), LINKS("Music at East Bay")])

# ============================================================ b.a.

add("ba-1-application-in-progress", "ba", "Application in Progress",
  "Your Music application", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the " + A(U["ba"], "B.A. in Music") + " at Cal State East Bay."),
  P("If anything in the application is unclear, don&rsquo;t hesitate to reach out, we are here to help. " + CALL),
  P("You can also begin thinking about your scholarship audition. We award scholarships to incoming students "
    "every year, and the same materials serve as the applied area placement that every music major completes "
    "before starting lessons. Requirements differ by area, and auditions close in February: "
    + A(U["aud"], "scholarship auditions and applied area placements") + "."),
  P("There&rsquo;s more about the programs, the faculty, and performance opportunities on the "
    + A(U["about"], "Department of Music") + " site. And remember, you&rsquo;re welcome on campus any time!"),
  FOOTER(), LINKS("Music Website")])

add("ba-2-application-received", "ba", "Application Received",
  "Now, your audition", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations! Your application IS IN."),
  H("Sign up for your scholarship audition"),
  P("We award scholarships to incoming students every year, and the same materials serve as the applied "
    "area placement that every music major completes before starting lessons. Auditions close in "
    "February. You can submit your materials online or sign up for an in-person audition. All the "
    "information is on the "
    + A(U["aud"], "scholarship auditions and applied area placements") + " page. Sign up!"),
  H("Other things to do now"),
  UL([
    "<strong>Activate your NetID.</strong> The University assigns you one within 48 hours of applying and sends it to the personal email address on your application. You need it for MyCSUEB and for your Horizon email account. " + A(U["netid"], "Activation instructions") + ".",
    "<strong>Send your transcripts.</strong> Ask each school you&rsquo;ve attended (high school, community college, or any other 4-year college) to send them electronically to " + TRANSCRIPTS + ". You will not receive an admission offer until the Office of Admissions has them. " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Check " + MYCSUEB + ".</strong> It shows your status and anything still outstanding.",
    "<strong>Come and visit.</strong> Meet the faculty, sit in on a rehearsal, and see an ordinary Tuesday here. Write or call and we will arrange it."]),
  P("Questions about a visit or an audition? " + CALL),
  FOOTER()])

add("ba-3-conditionally-admitted", "ba", "Conditionally Admitted",
  "Conditionally admitted", [
  P("Hi {{FIRST_NAME}},"),
  P("You have been conditionally admitted to the B.A. in Music. The Office of Admissions makes the offer "
    "final once the outstanding items on your record are cleared."),
  H("What is outstanding"),
  UL([
    "<strong>Read your To Do List in " + MYCSUEB + ".</strong> Everything holding up the offer is named there, usually final or official transcripts, or proof of graduation.",
    "<strong>Send the missing documents.</strong> These go to the Office of Admissions rather than to us. Ask each school you&rsquo;ve attended (high school, community college, or any other 4-year college) to send transcripts electronically to " + TRANSCRIPTS + ". " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Meet the " + A(U["deadlines"], "document deadlines") + ".</strong> They are firm, and the offer does not become final until the items clear."]),
  H("If you have not auditioned yet"),
  P("Scholarship auditions close in February. If that date has not passed, submit your materials online or "
    "sign up for an in-person audition. After it, the same materials serve as your applied area "
    "placement, which you need before starting applied lessons, any time up to the second week of the "
    "semester. All the information is on the "
    + A(U["aud"], "scholarship auditions and applied area placements") + " page. Sign up!"),
  P("Questions about any of it? " + CALL),
  FOOTER("We look forward to welcoming you as our newest CSUEB Pioneer!")])

add("ba-4-fully-admitted", "ba", "Fully Admitted",
  "Your offer of admission", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the B.A. in Music at Cal State East Bay!"),
  H("First, accept your offer"),
  P("Log in to " + MYCSUEB + ", choose the Admissions tile, select Accept Admission, and pay the $110 "
    "non-refundable " + A(U["fee"], "pre-enrollment fee") + ", which is applied toward orientation. The Office "
    "of Admissions covers the rest of the university side, from housing to student life, on its "
    + A(U["ugadmit"], "after you&rsquo;re accepted") + " page."),
  H("To help you decide if CSU East Bay is the right place for you"),
  UL([
    "<strong>What the four years hold.</strong> 120 units built on applied lessons and ensembles from your first semester to your last, alongside theory, history, conducting, and technology. The coursework spans performance, composition, production, jazz, and music education. Our students play across the Bay Area and abroad, write and record their own work, and leave ready for the stage, the studio, the classroom, or graduate school. The roadmaps show the degree term by term, " + A(U["rm4"], "four years") + " or " + A(U["rm2"], "two years for transfer students") + ".",
    "<strong>The music education add-on.</strong> You can earn the " + A(U["cert"], "Single Subject Matter Preparation Certificate in Music") + " alongside the B.A., which prepares you to apply for the California Single Subject Teaching Credential in Music and complete it successfully. John Eros coordinates music education: " + A("mailto:john.eros@csueastbay.edu", "john.eros@csueastbay.edu") + ".",
    "<strong>The FAST 4+1 B.A./M.A.</strong> gets you both degrees in five years. You apply by January 15 of your junior year, with 60 to 90 units done and a 3.0 in your music courses. " + A(U["fast"], "More about the program") + ", and the roadmaps lay out the whole sequence: " + A(U["fastrm"], "4+1") + " and " + A(U["fastrm2"], "2+1 for transfer students") + ".",
    "<strong>Come and see us.</strong> Sit in on a class, hear a rehearsal, meet the faculty you would study with, and talk to the students already doing it. Write or call and we will arrange a visit around your schedule.",
    "<strong>Complete your applied area placement.</strong> You need one to begin lessons in your principal area (if you submitted a scholarship audition, that already counts!) If you have not auditioned, sign up on the " + A(U["aud"], "scholarship auditions and applied area placements") + " page, any time up to the second week of the semester."]),
  H("Read ahead"),
  P(A(U["gotin"], "I got in! Now what?") + " walks through orientation, advising, and the steps that follow "
    "once you accept."),
  P("Questions about any of it? " + CALL),
  FOOTER("Welcome to our Musical Family!")])

add("ba-5-admission-accepted", "ba", "Admission Accepted",
  "Before classes begin", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer."),
  H("How your schedule comes together"),
  P("This depends on how you enter, and most of it happens between late May and early July. If you are "
    "starting as a first-year student, the " + A(U["ssc"], "CLASS Student Success Center") + " builds your "
    "first-semester schedule with the department&rsquo;s music advisors, and you do not register yourself in "
    "the first year. If you are transferring or already hold a bachelor&rsquo;s, we schedule an advising "
    "session with you to plan your courses, and you register yourself once they are settled. We will email "
    "you over the summer to arrange it."),
  H("Before the semester starts"),
  UL([
    "<strong>Applied area placement.</strong> You need one before starting lessons on your principal instrument or voice, any time up to the second week of the semester (if you submitted a scholarship audition, that already counts!) " + A(U["aud"], "What to prepare") + ".",
    "<strong>Ensembles.</strong> Auditions and placement happen at the first meeting of each ensemble. Register for the course, then come ready to play or sing to that first class. " + A(U["ens"], "Our ensembles") + ".",
    "<strong>Music orientation.</strong> The Department holds it the day before classes start. You will walk our facilities, rent a locker, and meet your cohort and your advisors."]),
  H("Read ahead (all of these are on our " + A(U["current"], "Student Resources") + " page)"),
  UL([
    "The " + A(U["ughb"], "Undergraduate Handbook") + " sets out the degree in full: applied levels and juries, recital requirements, ensembles, health and safety, and the academic policies of the department.",
    "The roadmaps lay out the degree term by term, " + A(U["rm4"], "four years") + " or " + A(U["rm2"], "two years for transfer students") + ".",
    "The " + A(U["mrc"], "Music Resource Center") + " lends scores, parts, and study materials.",
    "The " + A(U["equip"], "Music Equipment Office") + " lends instruments and recording equipment, and assigns lockers.",
    "The concert calendar is on " + A(U["events"], "News &amp; Events") + "."]),
  H("Two other paths, when you are ready"),
  UL([
    "For the " + A(U["cert"], "Single Subject Matter Preparation Certificate in Music") + ", write to John Eros at " + A("mailto:john.eros@csueastbay.edu", "john.eros@csueastbay.edu") + " to set up an advising session. Its " + A(U["certrm"], "roadmap") + " shows how the coursework fits alongside the degree.",
    "For the " + A(U["fast"], "FAST 4+1 B.A./M.A.") + ", the application falls on January 15 of your junior year. Roadmaps: " + A(U["fastrm"], "4+1") + " and " + A(U["fastrm2"], "2+1 for transfer students") + "."]),
  P("Questions about any of it? " + CALL),
  FOOTER("Welcome!")])


# ============================================================ m.a.

add("ma-1-application-in-progress", "ma", "Application in Progress",
  "Starting your M.A.", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the " + A(U["ma"], "Master of Arts in Music") + "."),
  P("A bachelor&rsquo;s degree in music is the usual preparation and we do encourage it, though it isn&rsquo;t "
    "a hard requirement. We read applications without one case by case, and self-taught musicians have come "
    "through the program. We do ask for good academic standing at your most recent college or university."),
  H("What goes into CSUApply"),
  UL([
    "Your CV or r&eacute;sum&eacute;.",
    "Two letters of recommendation, from teachers or colleagues who can speak to your readiness for graduate work. You enter their names and email addresses in CSUApply, and each one receives an automatic message with a form to complete and a place to upload the letter. Give them warning before you enter them.",
    "A statement of purpose, 2 pages, on what you want from a graduate degree in music and where you&rsquo;re headed in the short and long term.",
    "Evidence of your abilities in your area of emphasis. What that means differs from one emphasis to the next, and it is laid out on the " + A(U["applyma"], "How to Apply") + " page."]),
  P(GRADCLOSE),
  FOOTER()])

add("ma-2-application-received", "ma", "Application Received",
  "Your M.A. application", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, your application to the Master of Arts in Music is complete."),
  P("We read the materials you sent us, your CV, your letters, and the evidence of your abilities, as they "
    "come in. The Office of Graduate Admissions verifies your transcripts and official documents "
    "separately, and we move to a decision once both are done. You can track your status in " + MYCSUEB + "."),
  funding([GTA, ISA]),
  P(GRADCLOSE),
  FOOTER()])

add("ma-3-conditionally-admitted", "ma", "Conditionally Admitted",
  "Conditionally admitted, M.A.", [
  P("Hi {{FIRST_NAME}},"),
  P("You have been conditionally admitted to the M.A. in Music. The Office of Graduate Admissions makes the "
    "offer final once the outstanding items on your record are cleared."),
  H("What is outstanding"),
  UL([
    "<strong>Read your To Do List in " + MYCSUEB + ".</strong> Everything holding up the offer is named there, most often official transcripts or proof that your bachelor&rsquo;s degree was conferred.",
    "<strong>Send the missing documents.</strong> These go to the Office of Graduate Admissions rather than to us. Ask every college and university you have attended to send transcripts electronically to " + TRANSCRIPTS + ". " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Meet the " + A(U["gdeadlines"], "document deadlines") + ".</strong> They are firm, and the offer does not become final until the items clear."]),
  P(GRADCLOSE),
  FOOTER()])

add("ma-4-fully-admitted", "ma", "Fully Admitted",
  "Your M.A. offer", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the Master of Arts in Music at Cal State East "
    "Bay!"),
  H("First, accept your offer"),
  P("Log in to " + MYCSUEB + ", choose the Admissions tile, and select Accept Admission. The Office of "
    "Admissions covers the rest of the university side, from housing to student life, on its "
    + A(U["gradmit"], "after you&rsquo;re accepted") + " page."),
  H("To help you decide if CSU East Bay is the right place for you"),
  UL([
    "<strong>What the two years hold.</strong> 32 units across four semesters, built on a seminar core in analysis, jazz, conducting, entrepreneurship, interdisciplinary collaboration, and teaching in higher education, with applied lessons and ensemble running throughout. You finish with a public capstone of your own making, a recital, a portfolio, a project you argue for. Our graduate students perform across the Bay Area, premiere new work, conduct, record, and walk out ready to teach at the college level. All this information and more, including the roadmap, is in our " + A(U["grhb"], "Graduate Handbook") + ".",
    "<strong>The music education add-on.</strong> You can earn the " + A(U["cert"], "Single Subject Matter Preparation Certificate in Music") + " alongside the M.A. Admission to the degree is the entry point, and the certificate adds the coursework that prepares you to apply for the California Single Subject Teaching Credential in Music and complete it successfully. John Eros coordinates music education: " + A("mailto:john.eros@csueastbay.edu", "john.eros@csueastbay.edu") + ". The Graduate Coordinator can advise on fitting it to the graduate sequence.",
    "<strong>Come and see us.</strong> Sit in on a seminar, hear a rehearsal, meet the faculty you would work with, and talk to the students already doing it. Write to the Graduate Coordinator and we will arrange a visit around your schedule.",
    "<strong>Paid teaching work.</strong> Graduate Teaching Associates lead their own sections and are paid per course-unit; Instructional Student Assistants support teaching by the hour. Both open before the semester, and both are worth saying early about."]),
  H("Check in with the offices that handle the rest"),
  UL([
    "The " + A(U["gradstudies"], "Office of Graduate Studies") + " oversees graduate study across the University, and its " + A(U["gradadmit"], "admitted students") + " page carries orientation, registration, and the next steps after you accept.",
    "The " + A(U["cie"], "Center for International Education") + " advises international students on immigration, arrival, and the mandatory check-in: cie@csueastbay.edu, (510) 885-2880."]),
  P(GRADCLOSE),
  FOOTER("Sincerely,")])

add("ma-5-admission-accepted", "ma", "Admission Accepted",
  "Before the M.A. begins", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer."),
  H("How your schedule comes together"),
  P("In&eacute;s Thiebaut, our Graduate Coordinator, will be in touch shortly to set up an advising meeting. "
    "She will go through "
    "your interests and what you want from the degree, match you to an ensemble that fits, and put you in "
    "touch with your applied studies instructor. Your first semester is MUS 601, Analysis of Musical "
    "Styles, and MUS 603, Entrepreneurship in the Arts, alongside lessons and ensemble, for eight units."),
  H("Before the semester starts"),
  UL([
    "<strong>Applied lessons.</strong> Arrange your weekly lesson time directly with your instructor once she has put you in touch.",
    "<strong>Ensemble.</strong> You perform in one every semester. Placement is settled at your advising meeting, and auditions happen at the first class, so come ready to play or sing. " + A(U["ens"], "Our ensembles") + ".",
    "<strong>Teaching assignments.</strong> Teaching Associate and Instructional Student Assistant assignments open before the semester. Tell the Graduate Coordinator now if either interests you."]),
  H("Read ahead (all of these are on our " + A(U["current"], "Student Resources") + " page)"),
  UL([
    "The " + A(U["grhb"], "Graduate Handbook") + " sets out sequencing, the Level 6 juries for your area, advancement to candidacy at the end of the first year, the capstone, and the comprehensive examination.",
    "The " + A(U["mrc"], "Music Resource Center") + " lends scores, parts, and study materials.",
    "The " + A(U["equip"], "Music Equipment Office") + " lends instruments and recording equipment, and assigns lockers.",
    "The concert calendar is on " + A(U["events"], "News &amp; Events") + "."]),
  P(GRADCLOSE),
  FOOTER()])


# ============================================================ certificate

add("cert-1-application-in-progress", "cert", "Application in Progress",
  "Starting your certificate", [
  P("Hi {{FIRST_NAME}},"),
  P("Thanks for starting an application to the "
    + A(U["cert"], "Single Subject Matter Preparation Certificate in Music") + ". The certificate is the "
    "subject matter half of becoming a music teacher in California. It establishes that you know the "
    "discipline you intend to teach, across theory, history, conducting, and performance, at the depth "
    "the state expects of someone standing in front of a classroom. Completing it satisfies the subject "
    "matter requirement without a separate examination."),
  P("The teaching credential itself is the other half, and it is a separate program run by the "
    + A(U["cred"], "School of Education") + ". If you came here looking for the credential program, that "
    "is where to start."),
  P("If you hold a bachelor&rsquo;s degree and want to start a career in music education without much "
    "teaching experience behind you, you are in the right place."),
  H("Important financial information"),
  P("The stand-alone certificate is not eligible for federal or state financial aid. The University&rsquo;s "
    "Program Participation Agreement does not cover certificate programs at any level, undergraduate or "
    "graduate, and aid eligibility follows admission to a bachelor&rsquo;s, master&rsquo;s, or credential "
    "program."),
  P("If you need aid, the route is to apply to a degree and take the certificate alongside it. Without a "
    "bachelor&rsquo;s degree, or with one in a field other than music, that means the "
    + A(U["ba"], "B.A. in Music") + ". With a bachelor&rsquo;s in music already, it means the "
    + A(U["ma"], "M.A. in Music") + ". Write to the Graduate Coordinator before you decide and she will go "
    "through which one fits your situation."),
  H("What goes into CSUApply"),
  UL([
    "Your CV or r&eacute;sum&eacute;.",
    "Two letters of recommendation, from people who can speak to your readiness to teach music. You enter their names and email addresses in CSUApply, and each one receives an automatic message with a form to complete and a place to upload the letter. Give them warning before you enter them.",
    "A statement of purpose, 2 to 3 double-spaced pages, on your background in music and why you want to teach K&ndash;12.",
    "Unofficial transcripts from every school you&rsquo;ve attended."]),
  P(CERTCLOSE),
  FOOTER()])

add("cert-2-application-received", "cert", "Application Received",
  "Your certificate application", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, your application to the Single Subject Matter Preparation Certificate in Music is "
    "complete."),
  P("We read the materials you sent us, your CV, your letters, and your statement of purpose, as they come "
    "in. The Office of Graduate Admissions verifies your transcripts and official documents separately, and "
    "we move to a decision once both are done. You can track your status in " + MYCSUEB + "."),
  H("Two things worth repeating"),
  UL([
    "<strong>This is the subject matter certificate, not the credential.</strong> It establishes that you know the discipline you intend to teach. The teaching credential is a separate program run by the " + A(U["cred"], "School of Education") + ".",
    "<strong>The stand-alone certificate carries no federal or state financial aid.</strong> Aid eligibility follows admission to a bachelor&rsquo;s, master&rsquo;s, or credential program. If you need aid, apply to the " + A(U["ba"], "B.A. in Music") + " or the " + A(U["ma"], "M.A. in Music") + " and take the certificate alongside it. Write to the Graduate Coordinator and she will go through which one fits."]),
  P(CERTCLOSE),
  FOOTER()])

add("cert-3-conditionally-admitted", "cert", "Conditionally Admitted",
  "Conditionally admitted, certificate", [
  P("Hi {{FIRST_NAME}},"),
  P("You have been conditionally admitted to the Single Subject Matter Preparation Certificate in Music. The "
    "Office of Graduate Admissions makes the offer final once the outstanding items on your record are "
    "cleared."),
  H("What is outstanding"),
  UL([
    "<strong>Read your To Do List in " + MYCSUEB + ".</strong> Everything holding up the offer is named there, most often official transcripts or proof that your bachelor&rsquo;s degree was conferred.",
    "<strong>Send the missing documents.</strong> These go to the Office of Graduate Admissions rather than to us. Ask every college and university you have attended to send transcripts electronically to " + TRANSCRIPTS + ". " + A(U["trans"], "How to submit documents") + ".",
    "<strong>Meet the " + A(U["gdeadlines"], "document deadlines") + ".</strong> They are firm, and the offer does not become final until the items clear."]),
  P(CERTCLOSE),
  FOOTER()])

add("cert-4-fully-admitted", "cert", "Fully Admitted",
  "Your certificate offer", [
  P("Hi {{FIRST_NAME}},"),
  P("Congratulations, and welcome. You have been admitted to the Single Subject Matter Preparation Certificate "
    "in Music at Cal State East Bay!"),
  H("First, accept your offer"),
  P("Log in to " + MYCSUEB + ", choose the Admissions tile, and select Accept Admission. The Office of "
    "Admissions covers the rest of the university side on its " + A(U["gradmit"], "after you&rsquo;re accepted")
    + " page."),
  H("To help you decide if CSU East Bay is the right place for you"),
  UL([
    "<strong>What the certificate covers.</strong> The subject matter the state requires for the Single Subject Teaching Credential in Music: theory, history, conducting, and performance, at the depth expected of someone teaching the discipline. Completing it satisfies the subject matter requirement without a separate examination. The " + A(U["certrm"], "certificate roadmap") + " lays out the 31 units on their two-year rotation.",
    "<strong>What it is not.</strong> The teaching credential itself is a separate program run by the " + A(U["cred"], "School of Education") + ".",
    "<strong>Aid, if you need it.</strong> The stand-alone certificate is not eligible for federal or state financial aid. If that matters to your plans, apply to the " + A(U["ba"], "B.A. in Music") + " or the " + A(U["ma"], "M.A. in Music") + " and take the certificate alongside the degree. Talk to us before you decide.",
    "<strong>Come and see us.</strong> Sit in on a class, hear a rehearsal, and meet the faculty you would work with. Write to John Eros or the Graduate Coordinator and we will arrange a visit around your schedule."]),
  H("Check in with the offices that handle the rest"),
  UL([
    "The " + A(U["gradstudies"], "Office of Graduate Studies") + " oversees graduate study across the University, and its " + A(U["gradadmit"], "admitted students") + " page carries orientation, registration, and the next steps after you accept.",
    "The " + A(U["cie"], "Center for International Education") + " advises international students on immigration, arrival, and the mandatory check-in: cie@csueastbay.edu, (510) 885-2880."]),
  P(CERTCLOSE),
  FOOTER()])

add("cert-5-admission-accepted", "cert", "Admission Accepted",
  "Before the certificate begins", [
  P("Hi {{FIRST_NAME}},"),
  P("We were glad to see you accept your offer."),
  H("How your schedule comes together"),
  P("Write to John Eros to set up an advising session before you register. He coordinates music education and "
    "will go through the certificate coursework with you and work out the order you take it in, which depends "
    "on what your bachelor&rsquo;s already covered. Reach him at "
    + A("mailto:john.eros@csueastbay.edu", "john.eros@csueastbay.edu") + "."),
  P("The music education courses run Tuesday and Thursday mornings, usually 8:30 a.m. to noon, on a two-year "
    "rotation. The " + A(U["certrm"], "certificate roadmap") + " lays out the 31 units across that rotation."),
  H("Applied lessons and ensembles"),
  P("You are eligible for applied lessons as long as you also join an ensemble. To start lessons you need an "
    "applied area placement, which you can submit any time up to the second week of the semester: "
    + A(U["aud"], "scholarship auditions and applied area placements") + ". Ensemble auditions and placement "
    "happen at the first meeting of each ensemble, so register for the course and come ready to play or sing "
    "to that first class. " + A(U["ens"], "Our ensembles") + "."),
  H("Read ahead (all of these are on our " + A(U["current"], "Student Resources") + " page)"),
  UL([
    "The " + A(U["grhb"], "Graduate Handbook") + " covers the certificate alongside the M.A.: applied study policies, juries, and the academic policies that apply to you.",
    "The " + A(U["mrc"], "Music Resource Center") + " lends scores, parts, and study materials.",
    "The " + A(U["equip"], "Music Equipment Office") + " lends instruments and recording equipment, and assigns lockers.",
    "The concert calendar is on " + A(U["events"], "News &amp; Events") + ". Come to concerts as often as you can manage, since you will be teaching this repertoire soon enough."]),
  P(CERTCLOSE),
  FOOTER()])



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
    flow.append('    <h3>%s%s</h3>' % ("" if g == "all" else "Plan(s): ", gname))
    flow.append('    <table class="hb-table flow">\n      <thead>\n        <tr><th>application status</th>'
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
    <p>Each template below carries a rendered preview and its HTML source. Use <strong>copy html source</strong>, then paste into the HTML source view of the Salesforce editor.</p>
    <p>The markup is plain: paragraphs, lists, links, and inline styles only. It carries no tables, no fixed widths, and no fonts of its own beyond a serif stack, so the Salesforce wrapper controls layout and the Department header sits where the wrapper puts it. Each template marks the header position with an HTML comment.</p>
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


</main>

<script>
(function () {
  "use strict";

  function source(el) {
    var node = document.getElementById(el.dataset.src);
    return node ? node.textContent : "";
  }

  var frames = [].slice.call(document.querySelectorAll("iframe.tpl-frame"));

  function fit(f) {
    var doc = f.contentDocument;
    if (!doc || !doc.documentElement) return;
    f.style.height = (doc.documentElement.scrollHeight + 24) + "px";
  }

  frames.forEach(function (f) {
    f.srcdoc = '<!DOCTYPE html><meta charset="utf-8">'
             + '<style>body{margin:0;font-family:Georgia,serif}</style>' + source(f);
    f.addEventListener("load", function () { fit(f); });
  });

  // fonts and reflow can change the rendered height after load
  var pending;
  window.addEventListener("resize", function () {
    clearTimeout(pending);
    pending = setTimeout(function () { frames.forEach(fit); }, 150);
  });
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () { frames.forEach(fit); });
  }

  function flash(b, label) {
    b.textContent = label;
    b.classList.add("done");
    setTimeout(function () {
      b.textContent = "copy html source";
      b.classList.remove("done");
    }, 1800);
  }

  // execCommand path for browsers without the clipboard API, and for file:// pages
  function legacyCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    document.body.appendChild(ta);
    ta.select();
    var ok = false;
    try { ok = document.execCommand("copy"); } catch (e) { ok = false; }
    document.body.removeChild(ta);
    return ok;
  }

  document.querySelectorAll(".copy-btn").forEach(function (b) {
    b.addEventListener("click", function () {
      var text = source(b);
      if (!text) { flash(b, "nothing to copy"); return; }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(
          function () { flash(b, "copied"); },
          function () { flash(b, legacyCopy(text) ? "copied" : "copy failed"); }
        );
      } else {
        flash(b, legacyCopy(text) ? "copied" : "copy failed");
      }
    });
  });
})();
</script>

</body>
</html>
""" % ("\n".join(nav), len(T), "\n".join(flow), "\n".join(cards))

open("index.html", "w").write(page)

# self-check: the templates have to survive a paste into Salesforce
for k in ORDER:
    src = T[k]["src"]
    assert all(ord(c) < 128 for c in src), "%s: non-ascii" % k
    assert src.count("{{FIRST_NAME}}") == 1, "%s: merge token" % k
    assert "MUSIC DEPARTMENT HEADER" in src, "%s: header comment" % k
    for tag in ("table", "script", "font", "center"):
        assert "<" + tag not in src, "%s: <%s>" % (k, tag)
    for tag in ("p", "ul", "li", "div", "a", "strong"):
        assert len(re.findall(r"<%s[ >]" % tag, src)) == len(re.findall(r"</%s>" % tag, src)), \
            "%s: unbalanced <%s>" % (k, tag)
    for m in re.finditer(r"<a ([^>]*)>", src):
        assert 'style="color:#6E1F2A;"' in m.group(1), "%s: unstyled link" % k
assert len(set(T[k]["subject"] for k in ORDER)) == len(ORDER), "duplicate subject line"

print("wrote %d templates and index.html" % len(T))
