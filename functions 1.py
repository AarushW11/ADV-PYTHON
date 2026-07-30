#Required argument
def add(a,b):
    print("sum:", a+b)

add(78,96)



#default argument

def student(rollno,name,age=18):
    print("details of the student", rollno,name,age)

student(10,"axy",19)

#keyword argument
def employee(id  , name):
 
   
 employee(name="xyz", id =45)

 #variable length 
def total(*numbers):
    print("total:", sum(numbers))

total(10, 20 , 30)

def display(numbers):
   print("numbers entered", numbers)
   print("total", sum(numbers))

numbers=[]

n= int(input("enter the number of elements:"))

for i in range(n):
   num=int(input(f"enter element {i + 1}:"))
   numbers.append(num)

display(numbers)
