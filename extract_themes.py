import json
import os.path

script_path = os.path.dirname(__file__)
raw_path = os.path.join(script_path)


def main():
    # takes in argument of json file

    with open('john_green.json', 'r') as file: 
        john_green_data = json.load(file)
    
    john_subjects = []

    for i in range(len(john_green_data['entries'])):
        try:
            john_subjects.extend(john_green_data['entries'][i]['subjects'])
        except KeyError:
            continue
    print(set(john_subjects))

    json_output = json.dumps(list(set(john_subjects)), indent=4)
    print(json_output)

    #octavia_data = set(octavia_subjects).json()
    with open(os.path.join(raw_path, 'john_theme.json'), "w") as f:
        json.dump(json_output, f, indent=4)
       
    
    # for i in range(len(octavia_butler_data['entries'])):
    #     print(octavia_butler_data['entries'][i]['subjects'])

    # result = author_theme.json

    pass

if __name__ == "__main__":
    main()