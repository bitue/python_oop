with open('file..txt', 'r') as file:
    lines = file.readlines()


file.close()

lines = lines[0].split("--")

print(lines[0])
print("[enter - read more, press q to quit]")
counter = 1
while True:
    inputfu = input()
    wentInside = False

    fakeInputfu = inputfu
    inputfu = inputfu.strip("-")

    if (inputfu.isnumeric()):
        intInput = int(fakeInputfu)
        wentInside = True 
        counter = counter + intInput 
        print(lines[counter]) 

    if (inputfu != "q" and wentInside == False):
        print(lines[counter]) 
        counter += 1 
    elif (inputfu == "q" or inputfu == "Q"):
        break 
    print("[enter - read more, press q to quit]")


