class A :
    def run(self):
        print("I am form A")

class B(A) :
    def run(self):
        print("I am form B")

class C(A) :
    def run(self):
        print("I am form C")

class D(B, C) :
    def run(self):
        print("I am form D")