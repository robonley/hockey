# Hockey Schedule

One page showing Charlie, Harry and Max's schedules, grouped by weekend.

Live site: https://robonley.github.io/hockey/

## Calendars

| Kid | Team | Source |
|---|---|---|
| Charlie | U11 Albert | TeamSnap |
| Charlie | Hawks Rep (REP badge, dashed bar) | OCHL |
| Harry | U9 Rossland | TeamSnap |
| Max | U7 King | TeamSnap |

A GitHub Action (`.github/workflows/refresh.yml`) downloads every feed every 4 hours and commits any changes.
If a feed is down, the last good copy stays up.
To refresh right away: Actions tab, "Refresh calendars", "Run workflow".

## Add a calendar

1. Add a line to `calendars/feeds.txt`: a short name, a space, then the calendar link (`webcal://` links are fine).
2. Add a line to the `TEAMS` list near the top of the script in `index.html`, using the same short name in `file`.
   Use the same `name` and `color` as an existing line to group it under that kid. Add `rep: true` for the REP badge.
3. Run the workflow once.

## Team records

Records show under each kid's name at the top of the page. They're stored in `calendars/records.json`.

- **Hawks Rep:** Updates automatically from the Lakeshore Hockey League standings on each refresh.
- **Everyone else:** No public standings exist (OCHL house league, and no standings at U7/U9). To show a record, edit `calendars/records.json` on GitHub and fill in `"record"`, e.g. `"record": "3-1-0"`.
