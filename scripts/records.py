"""Update calendars/records.json with league standings for teams that publish them.

Teams without public standings keep whatever is typed into records.json by hand.
Standard library only, so the GitHub Action needs no installs.
"""
import json, re, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

RECORDS = Path(__file__).resolve().parent.parent / "calendars" / "records.json"

# key in records.json -> (standings page, text that identifies the team's row)
LEAGUE_TEAMS = {
    "hawks-rep": ("https://lakeshorehockeyleague.net/Groups/1358/Standings/", "/Teams/2736/"),
}

def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

def standing(url, marker):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 hockey-schedule"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    i = html.find(marker)
    if i < 0:
        raise ValueError("team not found in standings")
    table = html[html.rfind("<table", 0, i): html.find("</table>", i)]
    rows = [r for r in re.findall(r"<tr.*?</tr>", table, re.S) if "<td" in r and "<th" in r]
    rank = next(n for n, r in enumerate(rows, 1) if marker in r)
    cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", rows[rank - 1], re.S)]
    gp, w, l, t, pts = (int(x) for x in cells[:5])
    return {"record": f"{w}-{l}-{t}", "detail": f"{ordinal(rank)} of {len(rows)} · {pts} pts", "gp": gp}

def main():
    data = json.loads(RECORDS.read_text()) if RECORDS.exists() else {}
    for key, (url, marker) in LEAGUE_TEAMS.items():
        try:
            entry = standing(url, marker)
        except Exception as e:  # keep the last good record if the site is down
            print(f"::warning::{key}: {e}", file=sys.stderr)
            continue
        old = {k: v for k, v in data.get(key, {}).items() if k != "updated"}
        if old != {**old, **entry} or "updated" not in data.get(key, {}):
            data[key] = {**data.get(key, {}), **entry,
                         "updated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")}
    RECORDS.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

if __name__ == "__main__":
    main()
