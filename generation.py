from jinja2 import Template
import imgkit
from PIL import Image, ImageFilter
import pandas as pd
from numpy import int64
import math
import os
import json
from stegano import lsb

def generate_html(template_config):
    with open('static/templates_auto/0/index.html', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            template_config=template_config
        )
        return s

def generate_css(template_config):
    with open('static/templates_auto/0/main.css', 'r') as fp:
        template_str = Template(fp.read())
        s = template_str.render(
            template_config=template_config
        )
        return s

def handle_blur(template_config):
    if template_config.get('inner_image', False) != '#' and template_config.get('inner_image_blur', False):
        base_image = Image.open(template_config['inner_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(template_config['inner_image_blur']))

        template_config['tmp_inner_image'] = template_config['inner_image']
        template_config['inner_image'] = 'tmp_inner_image_blur.png'# + template_config['inner_image'].split('.')[-1]
        blur_image.save(template_config['inner_image'])

    if template_config.get('outer_image', False) != '#' and template_config.get('outer_image_blur', False):
        base_image = Image.open(template_config['outer_image'])
        blur_image = base_image.filter(ImageFilter.GaussianBlur(template_config['outer_image_blur']))

        template_config['outer_image'] = 'tmp_outer_image_blur.png'# + template_config['outer_image'].split('.')[-1]
        blur_image.save(template_config['outer_image'])

def update_css_text_size(template_config, len_text, len_title):
    template_config['text_size'] = 55#int(10000*(len(dataframe['text'][index])/350)/len(dataframe['text'][index])) # TODO needs to be calculated
    template_config['text_size'] -= int((len_text -100) / 20)*1.7 #TODO if less than 100
    template_config['text_size'] = max(template_config['text_size'], 15)
    if len_text < 100:
        template_config['text_size'] = 55
    template_config['title_size'] = 80
    template_config['title_size'] -= int((len_title -12) / 2)*3
    template_config['title_size'] = max(template_config['title_size'], 15)
    if len_title < 13:
        template_config['title_size'] = 80

def update_template_config(dataframe, index, template_config):
    # css config
    template_config['image_position'] = dataframe['image_position'][index]
    template_config['border_colour'] = dataframe['border_colour'][index]
    template_config['border_width'] = dataframe['border_width'][index]
    template_config['border_radius'] = dataframe['border_radius'][index]
    template_config['title_colour'] = dataframe['title_colour'][index]
    template_config['text_colour'] = dataframe['text_colour'][index]
    template_config['outer_image'] = dataframe['outer_image'][index]
    if pd.isnull(template_config['outer_image']):
        template_config['outer_image'] = '#'
    template_config['outer_image_blur'] = dataframe['outer_image_blur'][index]
    template_config['inner_image'] = dataframe['inner_image'][index]
    if pd.isnull(template_config['inner_image']):
        template_config['inner_image'] = '#'
    template_config['inner_image_blur'] = dataframe['inner_image_blur'][index]
    template_config['inner_gradient_direction'] = dataframe['inner_gradient_direction'][index]
    template_config['inner_gradient_start_colour'] = dataframe['inner_gradient_start_colour'][index]
    template_config['inner_gradient_end_colour'] = dataframe['inner_gradient_end_colour'][index]
    template_config['shadow_size'] = dataframe['shadow_size'][index]
    template_config['shadow_rgba'] = dataframe['shadow_rgba'][index]
    template_config['tag_colour'] = dataframe['tag_colour'][index]
    template_config['source_colour'] = dataframe['source_colour'][index]

    # html config
    template_config['text'] = dataframe['text'][index]
    template_config['image'] = dataframe['image'][index]
    template_config['title'] = dataframe['title'][index]
    template_config['source'] = dataframe['source'][index]
    template_config['tag'] = dataframe['tag'][index]

def generate_definition_from_json(template_config, out_file):
        # automatically resieze the text and title, based on length
        update_css_text_size(template_config, len(template_config['text']), len(template_config['title']))

        # generate html from config and save as tmp file to root dir
        html = generate_html(template_config)
        with open('tmp.html', 'w') as fp:
            fp.write(html)

        # create tmp blury images in root dir (if indicate by settings)
        handle_blur(template_config)

        # generate css from config and save as tmp file to root dir
        css = generate_css(template_config)
        with open('tmp.css', 'w') as fp:
            fp.write(css)

        # create the definition image and save to out_file
        imgkit.from_file('tmp.html', out_file)

        # replacing the blury image path with the original image path
        if template_config.get('tmp_inner_image', None):
            template_config['inner_image'] = template_config['tmp_inner_image']
            template_config.pop('tmp_inner_image', None)
        if template_config.get('tmp_outer_image', None):
            template_config['outer_image'] = template_config['tmp_outer_image']
            template_config.pop('tmp_outer_image', None)

        # save the template_config inside of metadata on the generated definition
        secret = lsb.hide(out_file, str(template_config))
        secret.save(out_file)

        # remove all the tmp files created
        os.remove('tmp.html')
        os.remove('tmp.css')
        if os.path.exists('tmp_inner_image_blur.png'):
            os.remove('tmp_inner_image_blur.png')
        if os.path.exists('tmp_outer_image_blur.png'):
            os.remove('tmp_outer_image_blur.png')

def get_image_config(image_path):
    hidden_message = json.loads(lsb.reveal(image_path).replace('\'', '\"').replace(': None,', ': null,').replace(': nan,', ': null,'))
    return hidden_message

def generate_definitions_from_csv(csv_path, list_of_indexes=None):
    # create the pointer to the template config structure
    template_config = {}

    # read the csv into a dataframe and generate an image from each row
    dataframe = pd.read_csv(csv_path)

    if list_of_indexes:
        # generate all the definitions selected
        for i in list_of_indexes:
            # populate template_config with the image settings of csv row i
            update_template_config(dataframe, int(i), template_config)

            # generate definition i
            generate_definition_from_json(template_config, f'output/out{i}.png')
    else:
        # generate all the definitions in the csv
        for i in range(len(dataframe)):
            # populate template_config with the image settings of csv row i
            update_template_config(dataframe, i, template_config)

            # generate definition i
            generate_definition_from_json(template_config, f'output/out{i}.png')