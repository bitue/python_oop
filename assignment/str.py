str = input()

def palindrome_or_not(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str) -i-1] :
            return False 
    return True 

if palindrome_or_not(str) :
    print("Palindrome ")
else :
    print("Not palindrome")




