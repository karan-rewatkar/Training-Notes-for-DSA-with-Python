#input  = aaabbbbccceeeee
#output = a3b4c3e5



# salary = int(input('Enter your salary: '))
# rating = float(input('Enter the rating : '))
# increment= 0
# if rating >=1 and rating<= 3:
#     increment = salary*10/100
# elif rating >=3.1 and rating <=4:
#     increment = salary*30/100
# elif rating >=4.1 and rating <=5:
#     increment = salary*40/100
# else:
#     print("Invalid rating")
# print("Increment = ",increment)                




# basicSalary = 20000
# HRA_salary = basicSalary
# increment1 = basicSalary*20/100
# print("GC HRA_salary = ",increment1)

# Ta_salary = basicSalary
# increment2 = basicSalary*30/100
# print("GC of Ta_salary  = ",increment2)

# Da_salary = basicSalary
# increment3 = basicSalary*45/100
# print("GC of Da_salary = :",increment3)

# Total_salary = increment1 + increment3 +increment2
# print("Total_salary is ",Total_salary)




# def binarySearch(array, target):
#     low =0
#     high = len(array)-1
#     while low <= high:
#         mid =(low+high)//2
#         if array[mid] ==target:
#             return mid
#         elif array[mid] <target: #move right side as mid value us less as compare to target
#             low = mid+1
#         else:
#             high = mid-1
#     return -1

# array = [2,4,5,9,11,13,14,15,19,20,22,23,27,30,32,39,42,44,45,49,51,53,54,55,59,60,62,63,67,70,72,79,80]
# target = 72
# result = binarySearch(array,target)
# if result == -1:
#     print("element not found")
# else:
#     print("Element found: ",result)    





# def bubbleSort(array):
#    for i in range(len(array)-1):
#     for j in range(len(array)-i-1):
#         if array[j]>array[j+1]:
#            temp = array[j]
#            array[j]= array[j+1]
#            array[j+1]=temp
#         print(array)    
#     print() 


# array = [64,34,25,12,22,11,90]
# bubbleSort(array)




# arr = [5,7,8,3,7,8,9,2,3]
# new = []
# for i in range(len(arr)):
#     key = arr[i]
#     j = i + 1
#     while j < len(arr):
#         if key == arr[j]:
#             new.append(key)
#             break   
#         j = j + 1
# print(len(new))





# class Name:
#     age = 30
#     def display(self):
#         print("Hello world")

# obj = Name()
# print(obj.age)
# obj.display()        





# class Student:
#   def __init__(self):
#      self.name = "prashant"
#      self.age = 30
#   def display(self):
#      print("Name= ", self.name)
#      print("Age=",self.age)
# stuObj= Student()      
# print(stuObj)
    



# class Message:
#     def __init__(self):
#         print("I am constructor")#constructor call automatically as default constructor
#     def shows(self):
#         print("class program")    

# obj = Message()# one object will call one constructor only
# obj.shows()
# obj2 = Message()







# #Parameterized constructor
# class StudentInfo():
#    def __init__(self, name, age, roll_no):
#       self.Name = name
#       self.Age = age
#       self.RollNo  = roll_no
#    def displayStudentInfo(self):
#        print("Name = ",self.Name)
#        print("Age = ",self.Age) 
#        print("roll_no = ",self.RollNo)   
# studentObj = StudentInfo("Prakash",34,101)
# studentObj.displayStudentInfo()






# Stack implementation
import sys
class Stack:
    def __init__(self):
        self.myStack = []

    def push(self, value):
        self.myStack.append(value)
        print("Element push")
    
    
    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print("Number is Pop =",self.myStack.pop())    
     
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            print(self.myStack[-1])
    
    def deleteStack(self):
        self.myStack=None

    def display(self):
        print(self.myStack)
object=Stack()
print("Stack has created :")
while True: 
  print("1. Push Operation :")
  print("2. Display Stack :")
  print("3. Pop Operation :")
  print("4. Peek Operation")
  print("5. Delete operation")
  print("7. Exit :")
  choice = int(input("Enter your choice : "))
  if choice == 1:
        value = int(input("Enter value to push in stack :"))
        object.push(value)        
  elif choice == 2:
        object.display()   
  elif choice == 3:
        object.pop()  
  elif choice ==4:
        object.peek()    
  elif choice ==5:
        object.deleteStack()
  else:
      sys.exit()       