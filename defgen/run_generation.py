import sys
import json
from generation import generate_definitions_from_csv, generate_definition_from_json, get_image_config

if __name__ == '__main__':
    if sys.argv[1].split('.')[-1] == 'csv':
        if len(sys.argv) == 2:
            generate_definitions_from_csv(sys.argv[1])
        elif len(sys.argv) > 2:
            generate_definitions_from_csv(sys.argv[1], list_of_indexes=sys.argv[2:])

    if sys.argv[1].split('.')[-1] == 'json':
        with open(sys.argv[1]) as fp:
            parsed_json = json.load(fp)
            generate_definition_from_json(template_config=parsed_json, out_file=sys.argv[1].replace('.json', '.png'))

    if sys.argv[1].split('.')[-1] == 'png':
            hidden_message = get_image_config(sys.argv[1])
            with open(sys.argv[1].replace('.png', '.json'), 'w') as fp:
                json.dump(hidden_message, fp, indent=4)