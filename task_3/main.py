from dir_helpers import show_dir_structure
import sys
import colorama

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Enter a path as an argument [main.py path/to/directory]")
        
    
        show_dir_structure(sys.argv[1])
    except ValueError as err:
        print(f"{colorama.Fore.RED}ERROR:{colorama.Fore.LIGHTYELLOW_EX} {err}")
        sys.exit(1)

if __name__ == "__main__":
    main()