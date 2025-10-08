import json
import os.path

script_path = os.path.dirname(__file__)
raw_path = os.path.join(script_path)


def main():
    with open('john_theme.json', 'r') as file: 
        john_data = json.load(file)
    with open('octavia_theme.json', 'r') as file: 
        octavia_data = json.load(file)
    
    

    pass

if __name__ == "__main__":
    main()