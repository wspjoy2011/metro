"""Write dato to json file"""
import json


def write_to_json(json_format, output='names_most_lest_common.json'):
    """Write data to json file"""
    with open(output, "w") as outfile:
        json.dump(json_format, outfile, indent=4)
    print(f'Write data to {output}')
