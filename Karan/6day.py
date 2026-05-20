
# #Reverse each word in a string
# n = input("Enter the String ")
# reverse=""
# for i in str(n):
#     reverse = i +reverse
# print(reverse)    




# mystack = "()"
# stack=""
# for i in mystack:
#     if i == "(" or "{" or "[":
#         print("invalid")
#     elif i=="()"or i=="{}"or i=="[]":
#         print ("valid")

#     else:
#         print("Give me input")



#insertion sort
# arr =[5,3,8,6,2]
# for i in range(1,len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j>=0 and arr[j]>key:
#         arr[j+1] = arr[j]
#         j-= 1

#     arr[j+1] = key
# print(arr)





# #selection sort
# array=[20,12,10,15,2]
# for i in range(len(array)):
#     print('for i =',i)
#     min = i
#     j=i+1
#     while j<len(array):
#         if array[j]<array[min]:
#             min =j
#         j=j+1
#     array[i],array[min] = array[min],array[i]
#     print(array)        





# #sort dictionary by key or value
# def sort_item(data):
#   sort = sorted(data.items())
#   return dict(sort)
# dict={
#     "c":3,
#     "B":2,
#     "A":1
#         }
# result =sort_item(dict)
# print(result)




# Types of variable(instance var)
# class New:
#     def __init__(self):
#         self.a  =10# this is istance variable
# obj1 =New()
# obj2 = New()
# obj3=New()
# #obj1.a =20
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)




# class New:
#     a =10

#     def __init__(self):
#         self.name="Prashant"
# obj1= New()
# obj2=New()
# obj3=New() 
# #New.a =50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)





#
# class College:
#     collegename ="Modern College"
#     def __init__(self):
#         self.studentname ="Prashant"
# principal = College()
# teacher = College()
# accountant = College()
# print("principal=",principal.collegename,"........",principal.studentname)
# print("teacher =",teacher.collegename,"......",teacher.studentname)
# print("accountant = ",accountant.collegename,"......",accountant.studentname)
# College.collegename="HBD"
# principal.studentname="Prashant jha"
# print("Principal =",principal.collegename,"|",principal.studentname)
# print("teacher =",teacher.collegename,"|",teacher.studentname)
# print("acconutant =",accountant.collegename,"|",accountant.studentname)





# class Node:
#     def __init__(self, data):
#         self.data = data  #instance variable
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None

# linkedlist = Linkedlist()

# linkedlist.head = Node(5)
# second          = Node(10)
# third           = Node(15)
# fourth          = Node(20)
# #connecting a nodes
# linkedlist.head.next = second
# second.next = third
# third.next = fourth


# #display linked
# while linkedlist.head !=None:
#     print(linkedlist.head.data,"|","->", end= " ")
#     linkedlist.head = linkedlist.head.next




# class Node:
#     def __init__(self,data):
#         self.data = data#instance variable(5)
#         self.next =None
# class LinkList:
#     def __init__(self):
#         self.head = None
#         self.tail =None

#     def addNode(self,value):
#         self.node =Node(value)
#         if self.head is None:
#             self.head = self.node
#             self.tail = self.node
#         else:
#             self.tail.next = self.node
#             self.tail      = self.node

#     def addNodeBeginning(self,value):
#       self.node =Node(value)
#       if self.head is None:
#         self.head = self.node
#         self.tail = self.node
#       else:
#          self.node.next = self.head
#          self.head = self.node

#     def addNodeBetween(self,position,value):
#       self.node =Node(value)
#       if self.head is None:
#         self.head = self.node
#         self.tail = self.node
#       else:
#          for _ in range(position -1):
#             if self.head is None:
#                print("Position outy of bound ")
#                return
#             self.head = self.head.next
#          if self.head is None:
#             print("Position out of bound ")
#             return
         
#          self.node.next = self.head.next
#          self.head.next = self.node
#          if self.node.next is None:
#             self.tail =self.node
    
#     def displayNode(self):
#        if not self.head:
#         print("LinkList is empty: ")
#         return
#        temp = self.head 

#        while temp:
#          print(temp.data," |"," ->\n", end= " ")
#          temp = temp.next
#        print("None")

# if __name__ =="__main__":
#     object  =LinkList()
#     while True:
#         print("1. Add Node Linkedlist: ")
#         print("2. Add Node in begining: ")
#         print("3. Add Node in Between: ")
#         print("4. Add Node in End: ")
#         print("5. Display Linked List: ")
#         print("6. Exit")
#         ch = int(input("Enter your choice: "))
#         if ch ==1:
#           value = int(input("Enter value for node: "))
#           object.addNode(value)
#           print("Node added successfully us single Linkedlist: ")
        
#         elif ch==2:
#            value=int(input("Enter value for node: "))
#            object.addNodeBeginning(value)
           
#         elif ch==3:
#            position =int(input("Enter Position"))
#            value = int(input("Enter the number to add between : "))
#            object.addNodeBetween(position,value)


#         elif ch ==5:
#             object.displayNode()
