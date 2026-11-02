# Workflow diagrams

Four interactive pages that show how the app works. Each is one self-contained HTML file.

**To see them properly, use the live site: https://hemantmane2113.github.io/naukri-job-assistant/**
(GitHub shows an `.html` file as code.) Or clone the repository and double-click a file: no server and no internet
connection are needed. Small preview pictures are in `previews/`.

| Page | What it shows |
|---|---|
| `workflow-daily-run.html` | The morning: profile refresh, finding and reading jobs, scoring, the digest email and the Telegram ping |
| `workflow-apply-flow.html` | How an application happens: your Yes tap, the right resume, the questions Naukri's form asks, the confirmation |
| `workflow-phone-reachability.html` | Keeping your phone reachable: the always-on listener, the 10-minute guard, the 10:50 Daily check, the 19:00 reminder and the 20:00 question |
| `workflow-weekly-report.html` | The Sunday 22:00 Excel report |

The system map, the hour-by-hour day and the safety rails are on `docs/architecture.html`.

## How they are made

The pages were generated with the [Archify](https://github.com/tt-a1i/archify) diagram tool from the JSON files in
`sources/`. To change one, edit its JSON and regenerate it (Node.js and Archify installed):

```bash
node path/to/archify/bin/archify.mjs finalize workflow sources/workflow-daily-run.json workflow-daily-run.html --quality showcase
```

Two pages have no source file: `workflow-weekly-report.html` (its source was not kept) and `docs/architecture.html`, which is
a hand-edited page. Edit those directly.

These pages can be out of date after a change to the app, so the code is the truth. Last updated 2026-11-02.
