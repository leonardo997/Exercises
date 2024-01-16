# Scrivi uno script bash o python che conta il numero di file script in una directory raggruppandoli in base allo shebang interpreter. 

# Esempio di output: 
# $ contaScript /usr/bin
# 81 #!/usr/bin/perl
# 52 #!/usr/bin/perl5.18
# 47 #!/bin/sh
# 44 #!/usr/bin/perl5.28
# 22 #!/usr/sbin/dtrace -s
# ...

# I'll use python to create thte script because I'm more familiar with it.
# I assume that the shebang interpreters have to be fetched from the files, instead of just looking at the filenames

import os
import sys

interpreters = []
zombie_scripts = []

def count_scripts(directory:str) -> str:
    if not isinstance(directory, str):
        sys.exit()

    dir_content = (os.listdir(directory))

    for item in dir_content:
        full_path = os.path.join(directory, item)

        if os.path.isdir(full_path):
            print("here")
            print(item)
            count_scripts(full_path)
        elif os.path.isfile(full_path):
            shebang = get_shebang(str(full_path))
            if shebang:
                found = False
                for dictionary in interpreters:
                    if dictionary["shebang"] == shebang:
                        dictionary["count"] += 1
                        found = True
                        break
                if not found:
                    interpreters.append({"count": 1, "shebang": shebang})
                if len(interpreters) == 0:
                    print("here")
                    interpreters.append({"count": 1, "shebang" : shebang})
            else:
                zombie_scripts.append(str(item))
    return interpreters, zombie_scripts
    

def get_shebang(file_path:str) -> str:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            try:
                first_line = file.readline().strip()
            except UnicodeDecodeError:
                print(f"Error decoding file: {file_path}")
                return None
        shebang = ""
        # I assume shebang line is positioned at the beginning of the script
        if first_line.startswith("#!"):
            shebang = first_line
        else:
            shebang = None
        return shebang

def main() -> None:
    if len(sys.argv) > 1:
        search_dir = sys.argv[1]
    else:
        search_dir = os.getcwd()

    script_numb = count_scripts(search_dir)
    for dictionary in script_numb[0]:
        print(f"{dictionary["count"]} {dictionary["shebang"]}")

if __name__ == "__main__":
    main()
