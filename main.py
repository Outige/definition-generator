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
    if css_config.get('inner_image', False) != '#' and css_config.get('inner_image_blur', False):
        base_image = Image.open(css_config['inner_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(css_config['inner_image_blur']))

        css_config['inner_image'] = 'tmp_inner_image_blur.' + css_config['inner_image'].split('.')[-1]
        blur_image.save(css_config['inner_image'])

    if css_config.get('outer_image', False) != '#' and css_config.get('outer_image_blur', False):
        base_image = Image.open(css_config['outer_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(css_config['outer_image_blur']))

        css_config['outer_image'] = 'tmp_outer_image_blur.' + css_config['outer_image'].split('.')[-1]
        blur_image.save(css_config['outer_image'])



def update_html_config(dataframe, index, html_config):
    html_config['text'] = dataframe['text'][index]
    html_config['image'] = dataframe['image'][index]
    html_config['title'] = dataframe['title'][index]
    html_config['source'] = dataframe['source'][index]
    html_config['tag'] = dataframe['tag'][index]
    html_config['css'] = 'tmp.css'

def update_css_config(dataframe, index, css_config):
    css_config['image_position'] = dataframe['image_position'][index]
    css_config['text_size'] = 35 # TODO needs to be calculated
    css_config['title_size'] = 80 # TODO needs to be calculated
    css_config['border_colour'] = dataframe['border_colour'][index]
    css_config['border_width'] = dataframe['border_width'][index]
    css_config['border_radius'] = dataframe['border_radius'][index]
    css_config['title_colour'] = dataframe['title_colour'][index]
    css_config['text_colour'] = dataframe['text_colour'][index]
    css_config['outer_image'] = dataframe['outer_image'][index]
    if pd.isnull(css_config['outer_image']):
        css_config['outer_image'] = '#'
    css_config['outer_image_blur'] = dataframe['outer_image_blur'][index]
    css_config['inner_image'] = dataframe['inner_image'][index]
    if pd.isnull(css_config['inner_image']):
        css_config['inner_image'] = '#'
    css_config['inner_image_blur'] = dataframe['inner_image_blur'][index]
    css_config['inner_gradient_direction'] = dataframe['inner_gradient_direction'][index]
    css_config['inner_gradient_start_colour'] = dataframe['inner_gradient_start_colour'][index]
    css_config['inner_gradient_end_colour'] = dataframe['inner_gradient_end_colour'][index]

def generate_definitions(csv_path):
    html_config = {}
    css_config = {}
    dataframe = pd.read_csv(csv_path)

    for i in range(len(dataframe)):
        update_html_config(dataframe, i, html_config)
        update_css_config(dataframe, i, css_config)
        html = generate_html(html_config)
        with open('tmp.html', 'w') as fp:
            fp.write(html)

        handle_blur(css_config)
        css = generate_css(css_config)
        with open('tmp.css', 'w') as fp:
            fp.write(css)

        imgkit.from_file('tmp.html', f'out{i}.jpg')

        # clean up
        os.remove('tmp.html')
        os.remove('tmp.css')
        if os.path.exists('tmp_inner_image_blur.jpg'):
            os.remove('tmp_inner_image_blur.jpg')
        if os.path.exists('tmp_outer_image_blur.jpg'):
            os.remove('tmp_outer_image_blur.jpg')

if __name__ == '__main__':
    generate_definitions("tmp.csv")