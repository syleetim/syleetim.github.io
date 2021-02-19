find -maxdepth 2 -type f -name '*.pdf' -exec pdftoppm -png {} {} \;
find -maxdepth 2 -type f -name '*.pdf-1.*' -exec rename s/.pdf-1// {} \;
find -maxdepth 2 -type f -name '*.pdf' -exec rm {} \;
