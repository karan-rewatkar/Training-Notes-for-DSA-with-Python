#============================== linklist with stack ===========================

# push method
# pop method
#---------------------------------------------------------------------------------------------------
# class Node:
#     def __init__(self,value= None):
#         self.value = value
#         self.next = None

# class Linkedlist:
#     def __init__(self):
#         self.head = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Stack:
#     def __init__(self):
#         self.Linkedlist = Linkedlist()

#     def __str__(self):
#         values = [str(x.value) for x in self.Linkedlist]
#         return '\n'.join(values)

#     def push(self,value):
#         node = Node(value)
#         node.next = self.Linkedlist.head
#         self.Linkedlist.head = node

#     def isEmpty(self):
#         if self.Linkedlist.head == None:
#             return True
#         else:
#             return False
    
#     def pop(self):
#         if self.isEmpty():
#             return "there is no element in the stack"
#         else:
#             nodeValue = self.Linkedlist.head.value
#             self.Linkedlist.head = self.Linkedlist.head.next
#             return nodeValue
        
#     def delete(self):
#         self.Linkedlist.head = None


# stack = Stack()
# while True:
#     print("\n----- STACK MENU -----")
#     print("1. Push")
#     print("2. Pop")
#     print("3. Display")
#     print("4. Check Empty")
#     print("5. Delete Stack")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         value = int(input("Enter value to push: "))
#         stack.push(value)
#         print("Element pushed successfully")

#     elif choice == 2:
#         print("Popped Element:", stack.pop())

#     elif choice == 3:
#         if stack.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack Elements:")
#             print(stack)

#     elif choice == 4:
#         if stack.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Stack is not empty")

#     elif choice == 5:
#         stack.delete()
#         print("Stack deleted successfully")

#     elif choice == 6:
#         print("Program exited")
#         break

#     else:
#         print("Invalid choice")
    