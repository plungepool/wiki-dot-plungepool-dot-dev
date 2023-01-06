#!/usr/bin/env python3
import os
import glob
import markdown

if not os.path.exists('site'):
    os.mkdir('site')

for f in glob.iglob('src/*.md'):
    with open("src/templates/page_template.htm", 'r') as page_template:
        page = page_template.read()

    with open(f, 'r') as file:
        raw = file.read()
        content = markdown.markdown(raw, extensions=['markdown.extensions.tables'])

    page = page.replace('<!--CONTENT-->', content)

    file_name = os.path.basename(f)
    destination = os.path.join("site", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(page)