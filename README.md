# Morning Letter: data job

A free, scheduled job that collects public market data each weekday morning
and saves it to `data/`. The morning letter uses only the numbers in these files.

- `scripts/fetch_snapshot.py` pulls the data and computes unusual-move scores.
- `.github/workflows/snapshot.yml` runs it at 6:45 AM New York time on weekdays.
- `data/latest.md` is the readable table; `data/latest.json` is the machine-readable version.
- `data/snapshots/` keeps one file per day.

Failed sources are listed in the output. Nothing is estimated or filled in.
Rows marked "experimental" use sources that haven't been confirmed to work.

This repository is public. Keep private notes and anything you trade out of it.
