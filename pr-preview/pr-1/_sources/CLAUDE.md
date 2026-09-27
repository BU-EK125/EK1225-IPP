# Cross-repo context for EK1225-IPP

This file exists to carry over knowledge from work done across the wider
EK125 repo ecosystem that isn't written down in this repo's own README.md
(which is authoritative for this repo's own build mechanics -- read that
first, don't duplicate it here).

## What this repo is, and its name

A public, permanent home for EK125's per-class Individual Practice Problem
(IPP) handouts, published as marimo slide decks -- built by cloning
EK125-C1-DePasquale-Slides' pattern almost verbatim (same jupyter-book
shell, same `build_slides.sh`/`colab_button.html`/`strip_marimo_import.py`
pipeline). One deck per class, sourced from that class's original PDF
handout (kept for reference in `docs/`).

**The repo/org name is literally `EK1225-IPP`** (with a typo -- "1225" not
"125" -- inherited from a local folder name), not `EK125-IPP`. This is now
permanent and live at that URL; don't "fix" the name without the
instructor's explicit go-ahead, and be careful when typing it out.

## The content-policy distinction this repo established

IPP decks show **questions only, no answer reveal** -- unlike GPP decks
(in EK125-C1-DePasquale-Slides), which may use a reveal-on-click fragment
for their quick-checks. This was a deliberate choice (confirmed even after
verifying the correct answers by running the code and having a reveal
option available): IPPs are individual assessments, kept as blank practice
worksheets. Preserve this distinction in any future IPP-related work.

This is also the model for how sensitive-but-instructor-wants-it-public
content gets handled ecosystem-wide: rather than adding it to the main
EK125 site (which is policy-locked to no-IPPs/no-solutions except two
narrow Fall-2026 exceptions -- see EK125's own CLAUDE.md), it gets its own
dedicated single-purpose public repo, following this repo's and
EK125-C1-DePasquale-Slides' precedent.

## Gotcha when cloning this repo's pattern elsewhere

`colab_button.html` has the **source repo's org/name hardcoded** (e.g. a
link to `github.com/BU-EK125/EK125-C1-DePasquale-Slides/blob/main/
notebooks/...`) and must be manually find-and-replaced if this pattern is
copied to yet another new repo. `build_slides.sh` and
`strip_marimo_import.py` were checked and have no hardcoded repo
references.

## Toolchain notes

- pip-installed console scripts (`marimo`, `jb`) can end up off `PATH`
  (installed under `/Library/Frameworks/Python.framework/.../bin`) -- not
  a code bug, just check your shell's PATH if a command "isn't found."
- `marimo check` reliably emits `markdown-indentation` warnings on fenced
  code-block cells in this deck pattern -- expected/accepted noise (the
  reference repo's existing decks produce the same warning), not a real
  issue to chase.
- GitHub Pages deploy config here uses the legacy build type, serving from
  the `gh-pages` branch at `path: /`.

## Relation to EK125-notebooks' own `/ipp/` folder

EK125-notebooks (private) has its own gitignored `/ipp/` folder with real
IPP content (e.g. `Class 5 IPP SOLUTION.docx`) -- a **different
provenance** from this repo's PDF-sourced decks. Don't assume the two
overlap 1:1; if extending this repo to a new class, check whether a PDF
handout exists first rather than assuming EK125-notebooks' `/ipp/` has the
matching source.

## The wider ecosystem

See `EK125`'s own `CLAUDE.md` for the full repo map, the Act 1/2/3 course
structure, and the PII-stripping rule for anything sourced from
EK125-notebooks or EK125-Instructors (the private raw-material repo,
transferred from a personal repo formerly called "EK125WIP").
