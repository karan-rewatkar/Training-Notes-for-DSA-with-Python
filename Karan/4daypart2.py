

# # Stack implementation
# import sys
# class Stack:
#     def __init__(self,size):
#         self.myStack = []#creating stack
#         self.stacksize = size#stack size defined

        
#     def isFull(self):
#         if len(self.myStack)== self.stacksize:
#             return True
#         else: 
#             return False
            
#     def push(self, value):
#         if self.isFull():
#            print("Stack is full")
#         else:   
#             self.myStack.append(value)
#             print("Element push")
    
    
#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
#     def pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print("Number is Pop =",self.myStack.pop())   
#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print(self.myStack[-1])
    
#     def deleteStack(self):
#         self.myStack=None

#     def display(self):
#         print(self.myStack)
# size = int(input("Enter the size of stack :"))        
# object=Stack(size)
# print("Stack has created :")
# while True: 
#   print("1. Push Operation :")
#   print("2. Display Stack :")
#   print("3. Pop Operation :")
#   print("4. Peek Operation")
#   print("5. Delete operation")
#   print("7. Exit :")
#   choice = int(input("Enter your choice : "))
#   if choice == 1:
#         value = int(input("Enter value to push in stack :"))
#         object.push(value)        
#   elif choice == 2:
#         object.display()   
#   elif choice == 3:
#         object.pop()  
#   elif choice ==4:
#         object.peek()    
#   elif choice ==5:
#         object.deleteStack()

#   else:
#       sys.exit()       







arr = [5,7,2,3,7,8,2,3,3,3]
newdict={}
for i in range(len(arr)):
   count =0
   key = arr[i]
   j =1
   while j<len(arr):
      if key == arr[j]:  
       count +=1
      j= j+1
   if count >1:
      newdict[key] = count
max = newdict
print(max)