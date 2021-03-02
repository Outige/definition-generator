from jinja2 import Template
import imgkit
from PIL import Image, ImageFilter
import pandas as pd 
import math
import os

def generate_html(html_config):
    with open('static/templates_auto/0/index.html', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            html_config=html_config
        )
        return s

def generate_css(css_config):
    with open('static/templates_auto/0/main.css', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            css_config=css_config
        )
        return s

def handle_blur(css_config):
    if css_config.get('inner_image_blur', False):
        base_image = Image.open('static/' + css_config['inner_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(css_config['inner_image_blur']))

        css_config['inner_image'] = 'tmp_inner_image_blur.' + css_config['inner_image'].split('.')[-1]
        blur_image.save('static/' + css_config['inner_image'])

    if css_config.get('outer_image_blur', False):
        base_image = Image.open('static/' + css_config['outer_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(css_config['outer_image_blur']))

        css_config['outer_image'] = 'tmp_outer_image_blur.' + css_config['outer_image'].split('.')[-1]
        blur_image.save('static/' + css_config['outer_image'])


def generate_definitions(html_config, css_config):
    html = generate_html(html_config)
    with open('static/tmp.html', 'w') as fp:
        fp.write(html)

    handle_blur(css_config)
    css = generate_css(css_config)
    with open('static/tmp.css', 'w') as fp:
        fp.write(css)

    imgkit.from_file('static/tmp.html', 'out%d.jpg'%(0))
    os.remove("static/tmp.html")
    os.remove("static/tmp.css")

if __name__ == '__main__':
    html_config = {
        'paragraph': """A statistical way of comparing two (or more) techniques,
        typically an incumbent against a new rival. A/B testing aims to determine
        not only which technique performs better but also to understand whether the
        difference is statistically significant.""",
        'image': 'img/3d-modeling.png',
        'title': 'Random Forest',
        'source': 'Source: springboard.com/blog/data-science-terms/whgjgghkkg',
        'handle': '@conorosullyDS09d890uoh',
        'css': 'tmp.css'
    }
    css_config = {
        'image': {
            'position': 'right'
        },
        'text_size': 35,
        'title_size': 80,
        'border_colour': '#0097a7',
        'title_colour': '#696b6e',
        'text_colour': '#0097a7',
        'outer_image': 'images/sitebgw3.jpg',
        'outer_image_blur': 10,
        'inner_image': 'images/sitebgw3.jpg',
        'inner_image_blur': 0,
    }

    generate_definitions(html_config, css_config)