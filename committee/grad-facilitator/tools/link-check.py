"""Open every URL in tile-urls.tsv and record where it lands.

Input:  committee/grad-facilitator/tools/tile-urls.tsv
Output: committee/grad-facilitator/documents/tile-link-check.tsv
"""

import csv
import html
import re
import sys
import time
from collections import Counter
from datetime import date
from urllib.parse import urlsplit

import requests

ROOT = "committee/grad-facilitator"
SRC = f"{ROOT}/tools/tile-urls.tsv"
OUT = f"{ROOT}/documents/tile-link-check.tsv"

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"
)
TITLE = re.compile(r"<title[^>]*>(.*?)</title>", re.I | re.S)
H1 = re.compile(r"<h1[^>]*>(.*?)</h1>", re.I | re.S)


def text_of(match):
    if not match:
        return ""
    raw = re.sub(r"<[^>]+>", " ", match.group(1))
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def main():
    with open(SRC, newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))

    counts = Counter(r["url"] for r in rows)
    results = []

    for row in rows:
        url = row["url"]
        record = {
            "group": row["group"],
            "tile": row["tile"],
            "url": url,
            "status": "",
            "landed on": "",
            "page title": "",
            "page heading": "",
            "notes": "",
        }
        notes = []
        if counts[url] > 1:
            notes.append(f"url shared by {counts[url]} tiles")

        try:
            resp = requests.get(url, headers={"User-Agent": UA}, timeout=30, allow_redirects=True)
            record["status"] = str(resp.status_code)
            record["landed on"] = resp.url
            body = resp.text
            record["page title"] = text_of(TITLE.search(body))
            record["page heading"] = text_of(H1.search(body))
            if resp.history:
                codes = ",".join(str(h.status_code) for h in resp.history)
                notes.append(f"redirected ({codes})")
            if urlsplit(resp.url).netloc != urlsplit(url).netloc:
                notes.append("left the requested host")
            if urlsplit(url).netloc not in ("www.csueastbay.edu", "catalog.csueastbay.edu"):
                notes.append("off the university domain")
            if resp.status_code >= 400:
                notes.append("dead")
        except Exception as exc:  # noqa: BLE001
            record["status"] = "error"
            notes.append(type(exc).__name__)

        record["notes"] = "; ".join(notes)
        results.append(record)
        time.sleep(1)

    fields = ["group", "tile", "url", "status", "landed on", "page title", "page heading", "notes"]
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        fh.write(f"# Graduate Studies tile destinations, opened {date.today().isoformat()}\n")
        writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(results)

    bad = [r for r in results if r["status"] != "200"]
    print(f"{len(results)} checked, {len(bad)} not 200")
    for r in bad:
        print(f"  {r['tile']}: {r['status']} {r['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
