#!/bin/bash

set -o errexit -o nounset

if [ "$TRAVIS_BRANCH" != "master" ]
then
  echo "This commit was made against the $TRAVIS_BRANCH and not the master! No deploy!"
  exit 0
fi

rev=$(git rev-parse --short HEAD)

cd output

git init
git config --global user.name "BabuSubashChandar"
git config --global user.email "babuenir@gmail.com"

git remote add upstream "https://$GH_TOKEN@github.com/babuenir/blog.git"
git fetch upstream
git reset upstream/gh-pages

# git submodule add https://github.com/babuenir/techtalks.git talks
# git commit -m "Submodule talks."
# git submodule init
# cd talks
# git checkout talks
# git pull
# cd ..

git clone https://github.com/babuenir/techtalks.git talks
cd talks
git checkout talks
git pull
cd ..

#echo "babuenir.github.io" > CNAME

touch .

git add -A .
git commit -m "rebuild pages at ${rev}"
git push -q upstream HEAD:gh-pages
