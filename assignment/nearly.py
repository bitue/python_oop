

def nearly_equal(one, two):
    i = 0
    j=0 
    co =0 

    while i <len(one) and j < len(two) :
      
            if one[i] == two[j]:
                i+=1
                j+=1
                print("milse")
            else :
                print("milenai")
                j+=1 
                co+=1
    

    print(co)
    if co >1 :
        return False
    else :
        return True



print(nearly_equal("python", "pyt"))

