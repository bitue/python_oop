
# def inner_function():
#     msg = "welcome"

#     def outer_function():
#         print(msg)
#     return outer_function


# # res = inner_function()
# # print(res)

# def sum():
#     return ("hi")

# print(sum()) 


def dp ( l1 , l2 ) : 
    def p ( ll1 , ll2 , n ) : 
        return ll1[n] * ll2[n] 
    r = 0 
    for i in range ( len ( l1 ) ) : 
      r += p ( l1 , l2 , i ) 
    return r 


print (dp ( [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ))



