import sys
import json
from generation import generate_definitions, update_css_text_size, generate_definition

if __name__ == '__main__':
    if sys.argv[1].split('.')[-1] == 'csv':
        generate_definitions(sys.argv[1])
    if sys.argv[1].split('.')[-1] == 'json':
        with open(sys.argv[1]) as fp:
            parsed_json = json.load(fp)
            css_config = parsed_json
            html_config = parsed_json
            generate_definition(html_config=parsed_json, css_config=parsed_json, out_file=sys.argv[1].replace('.json', '.jpg'))