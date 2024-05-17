from colorama import Fore
from pathlib import Path

def show_dir_structure(dir_path: str | Path, depth = 1) -> None:
    dir_text_color = Fore.BLUE
    file_text_color = Fore.GREEN
    indent = "  "

    path = Path(dir_path)

    if path.is_file():
        raise ValueError(f"Path '{path}' is not a directory.")

    if not path.exists():
        raise ValueError(f"Provided path '{path}' is not found")

    print(f"{indent * depth}{dir_text_color}{path.name}/")

    files = sorted([item for item in path.iterdir() if item.is_file()])
    dirs = sorted([item for item in path.iterdir() if item.is_dir()])

    for d in dirs:
        show_dir_structure(d, depth + 1)

    for f in files:
        print(f"{indent * (depth + 1)}{file_text_color}{f.name}")