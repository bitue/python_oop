import shutil

def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

def read_file():
    with open ('center_text.txt', 'r') as f :
        lines = f.readlines()
        for line in lines :
            print_centre(line)

read_file()
