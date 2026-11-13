# Current state

- Homepage: <https://syleetim.github.io/>; repository `syleetim/syleetim.github.io`, `main`. Pushes render/deploy through GitHub Actions.
- Latest content: 13 November UBC slides, publication `c668724`; deployment succeeded and live HTML matched the local render at the final check. Existing URL: <https://syleetim.github.io/project_assets/ubcswf/slides/ubc_slides_running.html>.
- Conclusion includes “Open economy, political economy…?”; Tim confirmed this was the requested update. Screen/print checks passed after disabling MathJax fast-preview; no PDF refreshed.
- Working folder: `~/Sync/homepage/quarto_site`. Overlapping unrelated changes remain in its original checkout; publication used clean isolated worktree `/tmp/homepage-ubcswf-20261113`. Slide assets were also copied to the original requested folder.

## Completed and superseded

- `c668724` supersedes slide publications `19dae16`, `3c34b73` and `fc21cab`.
- Previous Lee–Shin update remains live as `pdfs/mpsc.pdf`: 106 pages, title-page date 17 October 2026; SHA256 `7efa6774e63a1a26ec3f8ebbf028c94893dc57f1effcbfe18e380caadcfac508`. Title/abstract and CV updates retained; earlier NBER/slides links remain labelled.
- <https://syleetim.quarto.pub/home> remains the three-second move redirect. Local CV files preserved; only the public CV PDF is tracked.

## Tim decides

None.

## Ready for execution / acceptance and stop

No pending publication; await new author edits. For requested UBC updates, use `ubc_slides_running.qmd` in `~/QMUL Dropbox/Tim Lee/ubc/ubc_slides`; its README owns author choices and scientific limitations. Render successfully with Quarto cache access before copying HTML, referenced figures/styles and complete runtime into `project_assets/ubcswf/slides`; preserve the existing URL. Synchronize a clean isolated checkout when original local changes overlap remote history; preserve those changes. No new numerical work authorized.

## Source checkpoint

Checked 13 November 2026: deployed content `c668724`; HTML SHA256 `79f85ab9b59a7e452a3627e2b659d3fb42cca1f2704393861681ba04c708cde3`. Research source SHA256 `fe749a09599d2df308801053499f1bd4c90dd562a689b1e0c9adb8693a5dda69` (dirty research checkout; not a committed source release). Handoff-only commits after this checkpoint do not change slide content.
