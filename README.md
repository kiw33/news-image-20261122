# news-image-20261122 — The World in One Image

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/kiw33/news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/kiw33/news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Entry for make.fun competition `news-image-20261122`: sum up the world
news of Sunday 22 November 2026 in a single 1024x1024 image.

## Files

- `main.py` — entrypoint (Python 3.13, standard library only). Copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`, or a local `out/`
  when neither exists), so both grader runs write byte-identical output.
- `draw_news22.py` — the drawing program (Pillow + DejaVu fonts). Renders
  the masthead, six story panels with flat pictograms, and the "Also
  today" ticker into `entry.png`. Deterministic: two runs give the same
  sha256.
- `entry.png` — the finished image (1024x1024).
- `SOURCES.md` — every fact in the image, with sources dated 22 Nov 2026.

## Stories

1. NATO — Rutte in Warsaw vows to "defend every inch of Polish territory" after Russian missiles and a drone land in Poland; Article 4 invoked
2. Mexico — "El Chapo Isidro" (Fausto Isidro Meza Flores), on the FBI's 10 Most Wanted list, arrested in a shoot-out
3. FBI — apparent hack of the National Crime Information Center database under investigation
4. COP31 — fossil-fuel fight deadlocks the climate talks in Antalya; nearly 200 nations stuck
5. Iran — Hormuz reopening plan shortened to two days; IRGC claims strikes on two US Patriot radars
6. US midterms — Democrats reclaim Congress in a resurgent midterm victory
