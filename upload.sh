#!/bin/sh

# update Home.md in hoisanwa-src
python update.py

# update hoisanwa-src
git add .
git commit -m "update"
git push -f origin main

# update hoisanwa.github.io
obsidianhtml convert -i config.yaml

REPO_DIR=../hoisanwa.github.io
cd ${REPO_DIR}
git rm -rf .
cp -r ./html/* .
rm -rf ./html
cp ../logo/favicon.ico .
git add .
git commit -m "update"
git push -f origin main