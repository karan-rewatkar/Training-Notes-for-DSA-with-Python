# import math
# num = 8
# arr= [79,77,54,81,48,34,25,16]
# count =0
# for i in arr:
#     root =int(i**0.5)
#     if root*root==i:
#         count+=1
# print(count)        
      
    



# def func(value,values):#[1,2,3] =v[0]=44
#     var =1               
#     values[0]=44
# t =3
# v = [1,2,3]
# func(t,v)
# print(t,v[0])    



# def f(i,values =[]):#[1][1,2][1,2,3]
#     values.append(i)
#     print(values)
# f(1)#Calling function
# f(2)
# f(3)

# Queue DS:-
# 1. Queue
# 2. Dequeue
# 3. display queue
# 4. isEmpty()
# 5. isFull()
# 6. Delete
# # 7. peek()


# #Queue using list
# import sys
# class Queue:
#     def __init__(self,size):
#         self.myQueue=[] #creating stack
#         self.queueSize = size#stack size define

#     def isFull(self):
#        if len(self.myQueue) == size:
#           return True
#        else:
#            return False
    
#     def enQueue(self,value):
#        if self.isFull():
#           print("Queue is full")
#        else:
#           self.myQueue.append(value)#myQueue is queue which is created and entering the numbers in it
    
#     def displayQueue(self):
#        print(self.myQueue)

#     def isEmpty(self):
#        if self.myQueue==[]:
#          return True
#        else:
#           return False
    
#     def deleteQueue(self):
#        if  self.isEmpty():
#           print("Queue is Empty : ")
#        else:
#           self.myQueue.pop(0)
#     def peek(self):
#        if self.isEmpty():
#           print("Queue is Empty")
#        else:
#           print(self.myQueue[0])
    
#     def delete(self):
#        self.myQueue= None

          
       

            
          
# size = int(input("Enter the size of Queue : "))
# obj = Queue(size)
# print("Stack has created")
# while True: 
#   print("1. Inqueue Operation :")
#   print("2. Display queue :")
#   print("3. delete Operation :")
#   print("4. Peek Operation")
#   print("5. Delete Queue")
#   print("6. Exit :")
#   choice = int(input("Enter your choice : "))
#   if choice==1:
#      value= int(input("Enter element to add in queue : "))
#      obj.enQueue(value)
#   elif choice ==2:
#      obj.displayQueue()
#   elif choice ==3:
#      obj.deleteQueue()
#   elif choice ==4:
#      obj.peek()
#   elif choice ==5:
#      obj.delete()
#   elif choice ==6:
#      exit()
#   else:
#      print("Enter valid number")   






# fruit={}
# def addone(index):
#    if index in fruit:
#       fruit[index]+=1
#    else:
#       fruit[index] =1
# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit))         





# n = int(input("Enter the number of students : "))
# Student={}
# for i in range(n):
#   student_name = input("Enter the name of student: ")
#   student_marks=int(input("Enter the marks of students: "))
# while True:
#    student_name =input("Enter student Name to get Marks: ")
#    student_marks = Student.get(student_name,-1)
#    if student_marks==-1:
#       print("Student Not Found")
#    else:
#       print("The marks of", student_name,"are",student_marks)
#       option=input("Do you want to find another student marks[yes|No]")
#       if option=="No":
#          break 
# print("Thanks for using our application")         






# str = "Learning Python is very easy"
# n =len(str)
# i =0
# print("FOward direction")
# while i<n:
#    print(str[i],end=' ')
#    i+=1
# print("Backward direction")  
# i= -1
# while i>=-n:
#    print(str[i],end=' ')
#    i=i-1 



# s =input()
# for ch in range(1,len(s)):
#    if s[ch]==' ':
#      print(s[ch-1])      


# v =['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels: ")
# found=[]
# for i in w:
#    if i in v:
#       if i not in found:
#          found.append(i)
# print('Found vowels= ',found)
# print('unique vowels', len(found), 'from the given word = ',w)         





# x,y,z=map(int,input().split())
# mylist =[]
# for i in range(x):
#    a = int(input())
#    mylist.append(a)
# for j in mylist:
#    if j>= y and j<=z:
#       print(j,end=' ')




# import datetime
# date = datetime.datetime.now()
# print("it's now:{:%d/%m/%y %H:%M:%S}".format(date))

# x =['A','B','C']
# y =['A','B','C']
# z=[1,2,3,4]
# print(x==y)
# print(x==z)
# print(x!=z)



#s =[1,4,9,16,25,36,49,64,81,100]
# val =[2**i for i in range(1,6)]
# print(val)

# s =[i*i for i in range(1,11)]
# print(s)


# squares = {x:x*x for x in range(1,6)}
# print(squares)


# doubles = {x:2*x for x in range(1,6)}
# print(doubles)



# a,b =[int(x) for x in input("Enter 2 numbers: ").split()]
# print("Product is : ",a*b)



# a,b,c = [float(x) for x in input("Enter 3 folat numbers : ").split(',')]
# print("The sum is :",a+b+c)



# mycart= [10,20,800,60,70]
# for item in mycart:
#    if item>400:
#       print("This is not in my budget = ",item)
#       continue
#    print(item)
# else:
#    print("you have purchased everything")



# while True:
#    Username = input("Enter the username ")
#    username='admin'
#    Password = input("Enter the password ")
#    password='admin'
#    if Username==username and Password ==password:
#       print("login succesfully!")
#       break
#    else:
#       print("Renter admin or password ")     




#Tower of honai
import time
class Tower:
    def __init__(self):
      print("WELCOME TO TOWER OF HONAI GAME")
      print()
      print("Given Problem   A=[3,2,1]    B=[]  c[]   ")
      print()
      print("Expected output  A=[]        B=[]  c[3,2,1]  ")
      self.A=[]
      self.B=[]
      self.C=[]
   
    def tower(self,item):
         self.A.append(item)
         time.sleep(3)
         print("A=",self.A)
         print("Items in Tower A\n")
    
    def pass1(self):
         self.temp = self.A.pop(2)#A=[3,2,]
         self.C.append(self.temp)#c=[1])=>temp=1
         time.sleep(3)
         print("A=",self.A      ,"   ",   "B=",self.B     ,"     ","C=",self.C)
         print("<============Pass one completed =============>\n")
    
    def pass2(self):
         self.temp =self.A.pop(1)#A=[3]
         self.B.append(self.temp) #B=[2] =>temp=2
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","C=",self.C)
         print("<============Pass two compeleted ============>\n")
    
    def pass3(self):
         self.temp =self.C.pop(0)#C=[1]
         self.B.append(self.temp) #B=[2,1] =>temp=2,1
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","C=",self.C)
         print("<============Pass three compeleted ============>\n")

    def pass4(self):
         self.temp =self.A.pop(0)#A=[3]
         self.C.append(self.temp) #C=[3] =>temp=3
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","C=",self.C)
         print("<============Pass Four compeleted ============>\n")
    def pass5(self):
         self.temp =self.B.pop(1)#A=[3]
         self.A.append(self.temp) #B=[1] =>temp=1
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","c=",self.C)
         print("<============Pass Five compeleted ============>\n")
    def pass6(self):
         self.temp =self.B.pop(0)#A=[3]
         self.C.append(self.temp) #C=[3,2] =>temp=3,2
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","c=",self.C)
         print("<============Pass Six compeleted ============>\n")
    def pass7(self):
         self.temp =self.A.pop(0)#A=[3]
         self.C.append(self.temp) #C=[3,2,1] =>temp=3,2,1
         time.sleep(3)
         print("A=",self.A      ,"     ",  "B=",self.B    ,"    ","c=",self.C)
         print("<==========Pass Seven compeleted ============>\n")

obj=Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

print("problem solved")
          
     
            