# from bank import Account

# me = Account("ash", 12, 122, 1200)
# print(me.account_id)



# seats = [[0]*5]*5 
seats = [[0,0, 0], [0, 0, 0], [0, 0, 0], [0,0, 0]]
book ={"abc":seats}


# def book_seats(id, list_of_seats):
#     for i in list_of_seats :
#         seats[i[0]]


tu = [(2, 2), (1, 2), (1, 1)]



for _ in seats:
    for j in _:
        print(j, end=" ")
    print("\n")

for i,j in tu :
    seats[i][j] = 500


for _ in seats:
    for j in _:
        print(j, end=" ")
    print("\n")

    
        
    

   
    

# for i in seats:
#     for j in i :
#         print(j, end=" ")
#     print("\n")



