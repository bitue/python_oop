
def remove_by_idx(str, idx):
    
    str = list(str)
    del str [idx]
    str = "".join(str)
    return str 


def nearly_equal(one, two):
    for i in one :
        if i in two:
            
            two = remove_by_idx(two, two.index(i))
            
        else :
            return False
    return True
       

print(nearly_equal('perla', 'pearl'))
# if res :
#     print("Yes")
# else :
#     print("NO")



