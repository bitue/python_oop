import shutil
with open('center_text.txt', "r") as file :
   lines =  file.readlines()


def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))

for line in lines:
    line = line.strip("\n")
    print_centre(line)
