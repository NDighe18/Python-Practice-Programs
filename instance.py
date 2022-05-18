class student():

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def show(self):
        print("---------------------")
        print("Marks in Python = ",self.a)
        print("Marks in Python Lab = ",self.b)
        print("---------------------")      

s1=student(12,10)
s2=student(13,11)
s3=student(14,9)
s1.show()
s2.show()
s3.show()
