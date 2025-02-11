#!/bin/bash

set -o errexit -o nounset

rev=$(git rev-parse --short HEAD)

cd output

git init -b gh-pages
git config --global user.name "BabuSubashChandar"
git config --global user.email "babuenir@gmail.com"

git remote add upstream "git@github.com:babuenir/blog.git"
git fetch upstream
git reset upstream/gh-pages

rm -rf talks
git add -A .
git commit -m "Cleaning up talks."

cd ..

git clone https://github.com/babuenir/techtalks.git talks
cd talks
git checkout talks
cd ..
rm -rf talks/.git
cp -rf talks/talks output

cd output

#echo "babuenir.github.io" > CNAME

touch .

git add -A .
git commit -m "rebuild pages at ${rev}"
git push -q upstream HEAD:gh-pages
