# Homepage

Quarto sources for <https://syleetim.github.io>, published from
<https://github.com/syleetim/syleetim.github.io>.

Edit the `.qmd` pages and `papers.bib`, then run `quarto render` to preview the
site. Pushing `main` renders and deploys it through GitHub Actions. Generated
`_site/` and `.quarto/` directories are ignored.

`pdfs/cv/tim_lee_cv.pdf` is the public CV. Other CV files remain in the local
Syncthing folder and are excluded from this public repository.

The `redirect/` project maintains the move notice at
<https://syleetim.quarto.pub/home>. Publish that project separately with
`quarto publish quarto-pub redirect --no-prompt --no-browser`.
