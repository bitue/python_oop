class Star_cinema :
    hall_list =[]
    def __init__(self) -> None:
        pass

    def entry_hall(self, hall):
        Star_cinema.hall_list.append(hall)
    




class Hall(Star_cinema) :
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list =()
        self.__rows =rows
        self.__cols =cols
        self.__hall_no =hall_no
        super().__init__()

    def entry_show(self, id : str, movie_name : str, time : str):
        self.__id = id
        self.__movie_name = movie_name
        self.__time = time

        show_tuple = (self.__id , self.__movie_name, self.__time)
        self.__show_list += (show_tuple,)
        self.__seats[self.__id]= [[0 for i in range(self.__cols)] for j in range(self.__rows)]

    def book_seats(self, customer_name, phone_number, id, list_of_seats):
        self.__customer_name = customer_name
        self.__phone_number = phone_number
        self.__input_id = id
        self.successful = []
        self.invalid =[]
        self.booked_failed =[]
        try :
            if(self.__seats[self.__input_id]):

                seats_available = self.__seats[self.__input_id]
                for i,j in list_of_seats:
                    if (0<=i<=self.__rows) and (0 <= j <= self.__cols):
                        if seats_available[i][j]==0:
                            seats_available[i][j] =1
                            self.successful.append((i,j))
                        elif seats_available[i][j]==1:
                            self.booked_failed.append((i,j))
                    else :
                        self.invalid.append((i,j))
        except:
            print("Invalid show id !")

        if len(self.booked_failed) !=0 :
            print("! Already booked that seats ")
            for i,j in self.booked_failed :
                print(i,j)
        if len(self.invalid) !=0 :
            print("Invalid row col !  ")
            for i,j in self.invalid :
                print(i,j)
        if len(self.successful) !=0 :
            print("\t##### TICKET BOOKED SUCCESSFULLY ##### \t")
            print('---------------------------------------------------------------------------------------')
            print(f'Name: {self.__customer_name} \t Phone number :{self.__phone_number} ')
            print(f'Hall id: {self.__hall_no} \t Show id :{self.__input_id} \t Movie time {self.__time} ')

            print("Successful Booked seat list are!  ")
            for i,j in self.successful :
                print("seat row, col => ",i,j)
            print('---------------------------------------------------------------------------------------')









    def view_show_lists(self):
        print('---------------------------------------------------------------------------------------')
        for i, j , k in self.__show_list:
            print(f'\tMovie_name {j} \t show_id {i} \t movie_time {k} ')
        print('---------------------------------------------------------------------------------------')
        return

    def view_available_seats(self, id):

        try :
            if(self.__seats[id]) :
                print('---------------------------------------------------------------------------------------')
                print(f'Movie Name {self.__movie_name} \t time {self.__time}')
                print("Yes for available seat and No! for unavailable seat")
                print('---------------------------------------------------------------------------------------')
                seat_plan = self.__seats[id]
                for _ in seat_plan :
                    for j in _ :
                        if j ==0:
                            print("Yes\t", end="")
                        else :
                            print("No!\t", end="")
                    print("\n")


        except :
            print("Invalid id of show !! try again !")

        print('---------------------------------------------------------------------------------------') 

        return 
                
         

        


# list_2d = [[0 for i in range(col)] for j in range(row)]

        


obj_hall =Hall(4, 4, 1)


obj_hall.entry_hall(obj_hall)

obj_hall.entry_show("ae123", "spiderman", "12-nov-2022 10:00 PM")
obj_hall.entry_show("ae150", "superman", "18-nov-2022 12:00 PM")

while True:
    print("Enter your choices")
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS TODAY")
    print("3. BOOK TICKETS")

    chk = int(input())
    if chk ==1 :
        obj_hall.view_show_lists()
        
    elif chk == 2 :
        show_id_today = input("Enter the show id ")
        obj_hall.view_available_seats(show_id_today)

    elif chk ==3 :
        name = input("Enter your name :") 
        phn = input("Enter your phone number :")
        show_id_movie = input("ENter the show id :")
        num = int(input("Enter the number of ticket :"))
        seat_book =[]
        for i in range(num):
            print("####CAUTION####")
            print('Enter the seat row col with the separation of comma eg : row , col')
            print('################')
            str_seat = input("Enter seat no of row and col number *** eg : row, col :")
            arr_seat = str_seat.split(",")
            seat_row = int(arr_seat[0])
            seat_col =int(arr_seat[1])
            seat_book.append((seat_row, seat_col))
            
        obj_hall.book_seats(name,phn, show_id_movie, seat_book)






