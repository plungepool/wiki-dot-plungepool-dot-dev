#!/usr/bin/env python3
import os
import glob
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

## Create folder for site
if not os.path.exists('site'):
    os.mkdir('site')

## Generate content pages from markdown
for f in glob.iglob('src/*.md'):
    with open("src/templates/page_template.htm", 'r') as page_template:
        page = page_template.read()

    with open(f, 'r') as file:
        raw = file.read()
        content = markdown.markdown(raw, extensions=[WikiLinkExtension(base_url='/site/', end_url='.html')])

    page = page.replace('<!--CONTENT-->', content)

    file_name = os.path.basename(f)
    destination = os.path.join("site", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(page)

## Generate index page
i_file_name = "index"
i_destination = os.path.join("site", os.path.splitext(i_file_name)[0] + ".html")
i_index_content = "<h2>Site Index</h2><br>"

with open("src/templates/page_template.htm", 'r') as page_template:
        i_page = page_template.read()

for p in os.listdir('site'):
    name = p.removesuffix('.html')
    link = "<a href=\"" + p + "\">" + name + "</a><br>"
    i_index_content += link
    print(p)

## apply generated html page to template
i_page = i_page.replace('<!--CONTENT-->', i_index_content)
with open(i_destination, 'w') as file:
        file.write(i_page)