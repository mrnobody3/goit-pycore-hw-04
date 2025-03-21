import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(directory, indent=""): 
    try:
        path = Path(directory)
        if not path.exists() or not path.is_dir():
            print(Fore.RED + "Path not found" + Style.RESET_ALL)
            return
        
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(Fore.BLUE + f"{indent}📂 {item.name}" + Style.RESET_ALL)
                print_directory_structure(item, indent + "  ")
            else:
                print(Fore.GREEN + f"{indent}📜 {item.name}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    init(autoreset=True)
    
    if len(sys.argv) != 2:
        print(Fore.RED + "Use: python 3_task.py /Users/serhii-demydenko/Documents/VSC projects/goit-pycore-hw-04" + Style.RESET_ALL)
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)
from pathlib import Path

directory = Path('.')
absolute_path = directory.resolve()
