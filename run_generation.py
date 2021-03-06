import sys
import json
from generation import generate_definitions, update_css_text_size, generate_definition, get_image_config

if __name__ == '__main__':
    if sys.argv[1].split('.')[-1] == 'csv':
        generate_definitions(sys.argv[1])
    if sys.argv[1].split('.')[-1] == 'json':
        with open(sys.argv[1]) as fp:
            parsed_json = json.load(fp)
            generate_definition(template_config=parsed_json, out_file=sys.argv[1].replace('.json', '.png'))
    if sys.argv[1].split('.')[-1] == 'png':
            get_image_config(sys.argv[1])