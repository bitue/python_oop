
with open('file.txt', 'r') as file :
    lines = file.readlines()
    file.close()
line_arr = lines[0].split("--")
co =0 
# print(line_arr)
print(line_arr[co], f'page no {co}/ total pages {len(line_arr)-1}')
print("[enter - read more, press q to quit]")

while True :
    res = input()
    if res =='':
        co+=1 

        print(f'page no {co} / total pages {len(line_arr)-1}')
        print(line_arr[co])
        print("[enter - read more, press q to quit]")

    elif res=="q" or res =="Q":
        break
    else:
        res = int(res)
        co+=res 
        if (co <0) :
            co = 0 
            print(f'page no {0} / total pages {len(line_arr)-1}')
            print(line_arr[0])
            print("[enter - read more, press q to quit]")
        elif co >=len(line_arr):
            co = len(line_arr)-1
            print(f'page no {len(line_arr)-1} / total pages {len(line_arr)-1}')
            print(line_arr[len(line_arr)-1])
            print("[enter - read more, press q to quit]")
        else :
            print(f'page no {co} / total pages {len(line_arr)-1}')
            print(line_arr[co])
            print("[enter - read more, press q to quit]")

