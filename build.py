#!/usr/bin/env python3
import os
import glob
import markdown

if not os.path.exists('site'):
    os.mkdir('site')

for f in glob.iglob('src/*.md'):
    with open(f, 'r') as file:
        raw = file.read()
        html = markdown.markdown(raw, extensions=['markdown.extensions.tables'])

    file_name = os.path.basename(f)
    destination = os.path.join("site", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(r'''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>devices</title>
    <link rel="stylesheet" href="../links/style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
''')
        file.write(html)
        file.write(r'''
</body>
</html>''')