read -p "Message for git commit > " message
bundle exec jekyll build
git add .
git commit -m "$message"
git push origin main
cd _site
git add .
git commit -m "$message$"
git push origin gh-pages
cd ..
