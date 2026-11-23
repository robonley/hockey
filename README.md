# Hockey Schedule

One page showing Charlie, Harry and Max's TeamSnap schedules, grouped by weekend.

## Publish on GitHub Pages (free)

1. Create a new public repo on GitHub (e.g. `hockey`).
2. Upload everything in this folder, including the hidden `.github` folder.
3. Settings → Pages → Source: "Deploy from a branch", Branch: `main`, folder `/ (root)`. Save.
4. Settings → Actions → General → Workflow permissions: "Read and write permissions". Save.
5. Actions tab → "Refresh calendars" → "Run workflow" once to confirm it works.

Your site will be at `https://<your-username>.github.io/hockey/`.

The calendars refresh automatically every 4 hours.

## Add a team

1. Add a line to `calendars/feeds.txt`: a short name, a space, then the ID from the TeamSnap link
   (the part between `team_schedule/` and `.ics`).
2. Add a matching line to the `TEAMS` list near the top of the script in `index.html`.
3. Run the workflow once (Actions → Refresh calendars → Run workflow).

## Note

The site is public, so anyone with the link can see practice times and rinks.
The repo name and URL do not need to include the kids' names.
