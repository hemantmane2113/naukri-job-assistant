# Sample output

What you actually receive. These samples were produced by running the application's own renderers (`render_digest`,
`format_job_card`, `build_alive_text`) on **invented jobs and companies**, so they show the real format without anyone's
real data. Your own messages will show your jobs, your resumes and your scores.

## The daily digest email

Sent after the 10:00 run. Part 1 lists the company-website jobs to apply to yourself, Part 2 what the app applied to after your
Yes on Telegram, and Part 3 where recent company-website jobs stand. Nothing is applied by the email itself.

```text
[naukri-agent] 1 to apply yourself, 0 applied for you — 09 Sep 2026

Daily Naukri job digest — 09 Sep 2026

PART 1 — APPLY YOURSELF ON THE COMPANY'S WEBSITE (1)
These match your criteria but only offer "Apply on company site". Open each link, press that button on Naukri, and apply on
the company's own website. Afterwards record it with: naukri-agent mark-applied <job>.

1. Data Scientist — Acme Analytics
   Location: Pune
   Experience: 3-6 yrs
   Job type: not confirmed
   Salary: 12-18 LPA
   Match score: 88.0 / 100 (ACCEPT)
   Recommended resume: data_scientist [SELECTED]
   Application status: New
   Freshness: Newly discovered (first seen 02 Nov 2026)
   Why it matches:
     - skills match: Python, SQL
   Important gaps:
     - salary below expectation
   How to apply: ON THE COMPANY'S WEBSITE - apply manually, then run mark-applied
   Direct apply link: https://careers.example.com/jobs/12345
   Naukri: https://www.naukri.com/job-listings-ds-040926000001

PART 2 — APPLIED FOR YOU VIA TELEGRAM (0), since the last digest
Nothing was applied via Telegram since the last digest.

PART 3 — COMPANY-WEBSITE JOBS: WHERE THEY STAND (0)
No company-website jobs from the last 7 days (other than today's Part 1).

---
Part 1 applications are manual. Part 2 were made by the app only after you tapped Yes on Telegram. Part 3 shows what you
told the app about company-website jobs.
Application status is from your local database only.
```

When Naukri Apply jobs are ready, a closing line tells the reader how many are waiting for Telegram and how to start.

## The Telegram job card

Sent when you start `/apply`. It has two buttons, **Yes** and **No**. Nothing is applied until you tap Yes on that card.
The card's buttons belong to that one card only; after a tap they turn into a single grey button ("Applying... please wait"
or "No - skipped").

```text
Apply to this job?

Machine Learning Engineer
Globex Software
Match score: 83.5
Experience required: 4-7 yrs  (you have 5 yrs)
Resume: ai_ml_engineer
Job type: Full Time, Permanent

Matched - required (3): Python, PyTorch, SQL
Matched - preferred (1): Docker
MISSING - required (1): Kubernetes
Missing - preferred (1): Airflow

https://www.naukri.com/job-listings-machine-learning-engineer-globex-software-bengaluru-040926000002

Tap Yes or No once - the card will change to "Applying... please wait" when I have it.
```

If Naukri's form then asks a question the app cannot answer from your profile, it sends only that question ("Question 1"),
as buttons for a choice or as text you type back. A typed answer gets a short Yes/No before it is sent.

## The daily check

One message a day (10:50) from the phone guard. If it does not arrive, the PC or its internet is down.

```text
Daily check (Tue 27 Oct, 10:50): the PC is on and the app is alive.
Phone control is running, so /apply works.
Job search: finished at 11:09 - 50 jobs read, 34 new. Digest emailed: nothing new to apply for yourself.
Telegram apply: 2 job(s) ready; you can approve up to 4 more today. Send /apply.
I will remind you at 19:00 if jobs are still waiting.
```

## Other output

- **Weekly report:** an Excel file, `Summary` and `Jobs` sheets, emailed on Sundays. See [OPERATIONS.md](OPERATIONS.md).
- **Diagrams:** the interactive pages in `workflow-diagrams/` show the same flows as pictures.
