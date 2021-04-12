read -p "Message for git commit > " message
bundle exec jekyll build
git add .
git commit -m "$message"
git config --global user.email "sylee.tim@gmail.com"
git config --global user.name "Tim Lee"
git push origin main
cd _site
git add .
git commit -m "$message$"
git push origin gh-pages
cd ..
