import json

def main():
    # takes in argument of json file

    with open('octavia_butler.json', 'r') as file: 
        octavia_butler_data = json.load(file)
    
    octavia_subjects = []
    
    for i in range(len(octavia_butler_data['entries'])):
        print(octavia_butler_data['entries'][i]['subjects'])

    # result = author_theme.json

    pass

if __name__ == "__main__":
    main()