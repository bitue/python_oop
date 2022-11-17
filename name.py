# import math
#
# def exp(a, n):
#     return math.pow(a, n)
#
#
# a, n= input().split(" ")
#
#
# res = exp(int(a), int(n))
# print(res)

# res = input();
# res = res.split("-")
# co =0 ;
#
# for i in res :
#     ch = float(i);
#     co+=ch
#
# print(co)
#


# res = input()
# out : str =""
# res_arr :list[str] = res.split(" ")
# for i in range(len(res_arr)):
#     out+=res_arr[i][::-1]
#     if(i != len(res_arr) -1):
#         out+=" "
#
#
# print(out)


#
# import uuid
# class Student:
#
#     def __init__(self, name, mark):
#         self.name =name
#         self.mark = mark
#     def get_uid(self):
#         self.unique_id = uuid.uuid4()
#         return self.unique_id
#
#
# with open ("student_info.txt", "a") as f:
#
#     while True :
#         name = input("enter the name if -1 then exit  ")
#         if(name == "exit"):
#             break
#         mark =int(input("enter the mark if -1 then exit "))
#         if(mark ==-1):
#             break
#         student = Student(name, mark)
#
#         student_info = f' id : {student.get_uid()} name : {student.name} mark : {student.mark} \n '
#         f.write(student_info)
#
#
#

# def get_target_pairs(numbers, target):
#     for i in range(0, len(numbers) - 1, 1):
#         if (numbers[i] + numbers[i + 1] == target):
#             print(i + 1, i + 2)
#
#
# numbers = [10, 20, 10, 40, 50, 60, 70]
# target = 50
#
# get_target_pairs(numbers, target)
# import math
# class Calculator :
#     def __init__(self, X, n):
#         self.X = X
#         self.n =n
#
#     def sum(self):
#         return self.X+self.n
#     def pow(self):
#         return math.pow(self.X, self.n)
#
# me = Calculator(2, 3)
# print(me.pow())
# print(me.sum())

#
# import math
#
# class Distance :
#     def __init__(self, X1, Y1, X2, Y2):
#         self.X1 =X1
#         self.Y1 =Y1
#         self.X2 = X2
#         self.Y2 =Y2
#
#     def get_distance(self):
#         dx = math.pow((self.X2-self.X1), 2)
#         dy = math.pow((self.Y2-self.Y1), 2)
#         return math.sqrt(dx+dy)
#
#
# m = Distance(3,1, 4, 1)
# print(m.get_distance())


# from itertools import combinations
#
# def sub_lists(l):
#   comb = []
#   for i in range(len(l)+1):
#     comb += [list(j) for j in combinations(l, i)]
#   return comb
#
#
# print(sub_lists([2, 4, 6]))


s = input()
di = dict(zip(s[::2], s[1::2]))

sortedDict = dict(sorted(di.items(), key=lambda x: x[0].lower()))


for key, value in sortedDict.items():
    for i in range(int(value)):
      print(key, end="")

