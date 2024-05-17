from pathlib import Path

def get_cats_info(path: str):
    cats = []

    try:
        with open(path, "r") as file:
            for cat_info_line in file.readlines():
                id, name, age = cat_info_line.strip().split(",")
                cats.append({"id": id, "name": name, "age": int(age)})

        return cats
    except FileNotFoundError as error:
        print("Error: file not found, enter valid path")
        
cats_path = f"{Path(__file__).absolute().parent}/cats.txt"
print(get_cats_info(cats_path))