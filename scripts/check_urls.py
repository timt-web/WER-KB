#!/usr/bin/env python3
"""Check official catalog URLs before a release.

HTTP 403 is reported as blocked rather than as a dead link. Other HTTP errors,
timeouts, and connection failures are dead links. This script is not part of
continuous integration.
"""

import ssl
import sys
import urllib.error
import urllib.request

from catalog_lib import catalog_rows

TIMEOUT_SECONDS = 20
USER_AGENT = "WER-KB-url-check/0.2"


def classify(url):
    request = urllib.request.Request(url, method="GET", headers={"User-Agent": USER_AGENT})
    context = ssl.create_default_context()
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS, context=context) as response:
            return "ok", response.status, response.geturl()
    except urllib.error.HTTPError as error:
        if error.code == 403:
            return "blocked", error.code, url
        return "dead", error.code, url
    except Exception as error:
        return "dead", type(error).__name__, url


def main():
    rows = catalog_rows()
    blocked = []
    dead = []
    for row in rows:
        status, detail, final = classify(row["official_url"])
        line = f"{status.upper():7} {detail} {row['resource_id']} {row['official_url']}"
        if final and final.rstrip("/") != row["official_url"].rstrip("/"):
            line += f" -> {final}"
        print(line)
        if status == "blocked":
            blocked.append(row["resource_id"])
        elif status == "dead":
            dead.append(row["resource_id"])

    print()
    print(f"Checked {len(rows)} URLs. Blocked (403): {len(blocked)}. Dead: {len(dead)}.")
    if blocked:
        print("Blocked, not treated as dead: " + ", ".join(blocked))
    if dead:
        print("Dead: " + ", ".join(dead), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
