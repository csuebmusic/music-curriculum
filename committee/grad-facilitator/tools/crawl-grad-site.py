"""Crawl the Office of Graduate Studies section and inventory what each page holds.

Outputs, both under committee/grad-facilitator/documents/:
  grad-site-inventory.tsv  one row per page
  grad-site-overlap.tsv    one row per page and program name found on it
"""

import csv
import html
import re
import sys
import time
from collections import Counter, deque
from datetime import date
from urllib.parse import urldefrag, urljoin, urlsplit

import requests

ROOT = "committee/grad-facilitator"
SEED = "https://www.csueastbay.edu/graduate-studies/"
PREFIX = "/graduate-studies/"
HOST = "www.csueastbay.edu"
MAX_PAGES = 150

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)

TAG = re.compile(r"<[^>]+>")
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
HEAD = re.compile(r"<h([1-3])[^>]*>(.*?)</h\1>", re.I | re.S)
ANCHOR = re.compile(r'<a\s[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', re.I | re.S)
SCRIPTY = re.compile(r"<(script|style|noscript)[^>]*>.*?</\1>", re.I | re.S)
MAIN = re.compile(r"<main[^>]*>(.*?)</main>", re.I | re.S)
EMAIL = re.compile(r"[\w.+-]+@[\w.-]*csueastbay\.edu", re.I)
DATEISH = re.compile(
    r"\b(?:january|february|march|april|may|june|july|august|september|october|november|december)\s+\d{1,2}",
    re.I,
)


def flat(raw):
    return re.sub(r"\s+", " ", html.unescape(TAG.sub(" ", raw))).strip()


def programs():
    with open(f"{ROOT}/tools/tile-urls.tsv", newline="", encoding="utf-8") as fh:
        return sorted({r["tile"] for r in csv.DictReader(fh, delimiter="\t")})


def main():
    names = programs()
    seen, pages, overlap = set(), [], []
    queue = deque([SEED])
    session = requests.Session()
    session.headers["User-Agent"] = UA

    while queue and len(pages) < MAX_PAGES:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        try:
            resp = session.get(url, timeout=30, allow_redirects=True)
        except Exception as exc:  # noqa: BLE001
            pages.append({"url": url, "status": type(exc).__name__})
            continue

        body = resp.text if "html" in resp.headers.get("content-type", "") else ""
        stripped = SCRIPTY.sub(" ", body)
        main_block = MAIN.search(stripped)
        content = main_block.group(1) if main_block else stripped
        text = flat(content)

        links = []
        for href, label in ANCHOR.findall(content):
            target = urldefrag(urljoin(url, href.strip()))[0]
            links.append((target, flat(label)))

        internal = [t for t, _ in links if urlsplit(t).netloc == HOST and urlsplit(t).path.startswith(PREFIX)]
        offsection = [t for t, _ in links if urlsplit(t).netloc == HOST and not urlsplit(t).path.startswith(PREFIX)]
        offsite = [t for t, _ in links if urlsplit(t).netloc not in ("", HOST)]

        heads = [flat(h) for _, h in HEAD.findall(content)]
        emails = sorted(set(m.lower() for m in EMAIL.findall(text)))

        pages.append(
            {
                "url": resp.url,
                "status": str(resp.status_code),
                "title": flat(TITLE.search(body).group(1)) if TITLE.search(body) else "",
                "headings": " / ".join(heads[:18]),
                "words": str(len(text.split())),
                "links in section": str(len(internal)),
                "links elsewhere on campus": str(len(offsection)),
                "links off site": str(len(offsite)),
                "emails": ", ".join(emails),
                "dates named": ", ".join(sorted(set(d.lower() for d in DATEISH.findall(text)))[:12]),
                "programs named": "",
            }
        )

        hits = []
        for name in names:
            probe = name.split(" (")[0]
            if len(probe) > 5 and re.search(re.escape(probe), text, re.I):
                hits.append(name)
                overlap.append({"url": resp.url, "program": name})
        pages[-1]["programs named"] = str(len(hits))

        for target in internal:
            if target not in seen and target.rstrip("/") != url.rstrip("/"):
                queue.append(target)
        time.sleep(1)

    fields = list(pages[0].keys())
    with open(f"{ROOT}/documents/grad-site-inventory.tsv", "w", newline="", encoding="utf-8") as fh:
        fh.write(f"# Office of Graduate Studies section crawled {date.today().isoformat()}\n")
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(pages)

    with open(f"{ROOT}/documents/grad-site-overlap.tsv", "w", newline="", encoding="utf-8") as fh:
        fh.write(f"# Program names found on more than one Graduate Studies page, {date.today().isoformat()}\n")
        w = csv.DictWriter(fh, fieldnames=["program", "pages", "urls"], delimiter="\t")
        w.writeheader()
        per = Counter(o["program"] for o in overlap)
        for name, count in sorted(per.items(), key=lambda kv: (-kv[1], kv[0])):
            urls = [o["url"] for o in overlap if o["program"] == name]
            w.writerow({"program": name, "pages": count, "urls": " ".join(urls)})

    print(f"{len(pages)} pages")
    for p in pages:
        print(f"  {p['status']:5} {p.get('words','?'):>6}w {p.get('programs named','?'):>3}p  {p['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
