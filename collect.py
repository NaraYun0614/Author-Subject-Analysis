import requests
import os.path
import json

script_path = os.path.dirname(__file__)
raw_path = os.path.join(script_path)

def main():
    author_name = r"octavia%20butler"

    # get author key
    query_url = "https://openlibrary.org/search/authors.json?q=" + author_name
    r = requests.get(query_url)
    # print(r.text)

    author_data = r.json()
    author_key = author_data["docs"][0]["key"]
    # print("Author key: ", author_key)

    books_url = "https://openlibrary.org/authors/" + author_key + "/works.json"
    r = requests.get(books_url)

    books_data = r.json()
    # print(r.text)

    # write out raw data
    fname = f"author_{author_key}_works.json"
    with open(os.path.join(raw_path, fname), "w") as f:
        json.dump(books_data, f, indent=4)

    # every book has a subjects dict, counting topics and subjects, compare counts? 

if __name__ == "__main__":
    main()