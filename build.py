#!/usr/bin/env python3
import os
import glob
import markdown
from markdown.extensions.wikilinks import WikiLinkExtension

## Create folder for site
if not os.path.exists('site'):
    os.mkdir('site')

## Empty contents of HTML folder
files = glob.glob('site/*')
for f in files:
    os.remove(f)

## Generate content pages from markdown
for f in glob.iglob('src/*.md'):
    with open("src/templates/page_template.htm", 'r') as page_template:
        page = page_template.read()

    with open(f, 'r') as file:
        raw = file.read()
        content = markdown.markdown(raw, extensions=[WikiLinkExtension(base_url='https://wiki.plungepool.dev/site/', end_url='.html')])

    file_name = os.path.basename(f)
    destination = os.path.join("site", os.path.splitext(file_name)[0] + ".html")

    page = page.replace('<!--TITLE-->', file_name.removesuffix('.md')  + " - plungepool wiki.")
    page = page.replace('<!--CONTENT-->', content)
    with open(destination, 'w') as file:
        file.write(page)

## Generate hub pages from markdown
for f in glob.iglob('src/hubs/*.md'):
    with open("src/templates/page_template.htm", 'r') as page_template:
        page = page_template.read()

    with open(f, 'r') as file:
        raw = file.read()
        content = markdown.markdown(raw, extensions=[WikiLinkExtension(base_url='https://wiki.plungepool.dev/site/', end_url='.html')])

    file_name = os.path.basename(f)
    destination = os.path.join("site", os.path.splitext(file_name)[0] + ".html")

    page = page.replace('<!--TITLE-->', file_name.removesuffix('.md')  + " hub - plungepool wiki.")
    page = page.replace('<!--CONTENT-->', content)
    with open(destination, 'w') as file:
        file.write(page)

## Generate home page
with open("src/templates/home_template.htm", 'r') as home_template:
    h_page = home_template.read()

with open("src/root/home.md", 'r') as h_file:
    h_raw = h_file.read()
    h_content = markdown.markdown(h_raw, extensions=[WikiLinkExtension(base_url='https://wiki.plungepool.dev/site/', end_url='.html')])

h_file_name = os.path.basename("src/root/home.md")
h_destination = os.path.join("", os.path.splitext(h_file_name)[0] + ".html")

h_page = h_page.replace('<!--TITLE-->', "home - plungepool wiki.")
h_page = h_page.replace('<!--CONTENT-->', h_content)
with open(h_destination, 'w') as h_file:
    h_file.write(h_page)

## Generate index page
i_file_name = "index"
i_destination = os.path.join("site", os.path.splitext(i_file_name)[0] + ".html")
i_index_content = "<h1>site index.</h1><br>"

with open("src/templates/page_template.htm", 'r') as page_template:
    i_page = page_template.read()

for p in os.listdir('site'):
    name = p.removesuffix('.html')
    link = "<a href=\"" + p + "\">" + name + "</a><br>"
    i_index_content += link
    print(p)

i_page = i_page.replace('<!--TITLE-->', "index - plungepool wiki.")
i_page = i_page.replace('<!--CONTENT-->', i_index_content)
with open(i_destination, 'w') as file:
    file.write(i_page)