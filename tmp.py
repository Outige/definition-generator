from jinja2 import Template
import imgkit
import pandas as pd 
import math

def generate_html(html_config):
    with open('static/templates/auto/template0/index.html', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            html_config=html_config
        )
        return s

def generate_css():
    with open('static/templates/auto/template0/main.css', 'r') as fp:
        return fp.read()

def generate_definitions(html_config):
    html = generate_html(html_config)
    with open('static/tmp.html', 'w') as fp:
        fp.write(html)

    css = generate_css()
    with open('static/tmp.css', 'w') as fp:
        fp.write(css)

    imgkit.from_file('static/tmp.html', 'out%d.jpg'%(0))

if __name__ == '__main__':
    html_config = {
        'paragraph': """A statistical way of comparing two (or more) techniques,
        typically an incumbent against a new rival. A/B testing aims to determine
        not only which technique performs better but also to understand whether the
        difference is statistically significant.""",
        'image': 'img/3d-modeling.png',
        'title': 'Random Forest',
        'source': 'Source: springboard.com/blog/data-science-terms/whgjgghkkg',
        'handle': '@conorosullyDS09d890uoh'
    }

    generate_definitions(html_config)
    import os
    os.remove("static/tmp.html")
    os.remove("static/tmp.css")