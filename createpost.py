#!/usr/bin/python3

# argv.py
import sys
import datetime

USAGE = f"Usage: python {sys.argv[0]} TITLE"

def main(agrs: list):
    if not agrs:
        raise SystemExit(USAGE)
    
    title = " ".join(agrs)
    d = datetime.datetime.today()
    filename = f"{'-'.join(agrs)}"

    content = [
        '---',
        f'title:  "{title}"',
        f'date:   {d.strftime("%Y-%m-%d %H:%M:%S")}',
        'excerpt_separator: <!--more-->',
        'categories:',
        ' - Meeting',
        '# - Presentation',
        '# - Tutorial',
        '# - Q&A',
        '# - Blog',
        'tags:',
        ' - R',
        '# - Python',
        '# - Statistics',
        '# - HPC',
        '# - Shiny',
        '# - Bash',
        'header:',
        '# image: assets/images/...',
        '---'
    ]

    with open(f"_posts/{d.strftime('%Y-%m-%d')}-{filename}.md", "x") as f:
        sep = '\n'
        f.writelines(sep.join(content))

if __name__ == "__main__":
   main(sys.argv[1:])