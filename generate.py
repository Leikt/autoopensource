import datetime
from pathlib import Path

import jinja2


def main():
    now = datetime.datetime.now()

    env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
    template = env.get_template('__init__.j2.py')

    init_content = template.render(now=now.strftime('%Y/%m/%d-%H:%M:%S'))
    Path('autoopensource/__init__.py').write_text(init_content, encoding='utf-8', newline='\n')


if __name__ == '__main__':
    main()
