#============================== linklist with stack ===========================

# enqueue() method
# dequeue() method
#---------------------------------------------------------------------------------------------------
# class Node:
#     def __init__(self,value=None):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)
    
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

#     def __str__(self):
#         values = []
#         temp = self.head
#         while temp:
#             values.append(str(temp.value))
#             temp = temp.next
#         return ' -> '.join(values)

# class Queue:
#     def __init__(self):
#         self.Linkedlist = Linkedlist()

#     def __str__(self):
#         values = [str(x.value) for x in self.Linkedlist]
#         return '\n'.join(values)
    
#     def isEmpty(self):
#         if self.Linkedlist.head == None:
#             return True
#         else:
#             return False
#     def enQueue(self,value):
#         newnode = Node(value)
#         if self.Linkedlist.head is None:
#             self.Linkedlist.head = newnode
#             self.Linkedlist.tail = newnode
#         else:
#             self.Linkedlist.tail.next = newnode
#             self.Linkedlist.tail      = newnode

#     def deQueue(self):
#         if self.isEmpty():
#             return "there is no node in the Queue"
#         else:
#             tempnode = self.Linkedlist.head
#             if self.Linkedlist.head == self.Linkedlist.tail:
#                 self.Linkedlist.head = None
#                 self.Linkedlist.tail = None
#             else:
#                 self.Linkedlist.head = self.Linkedlist.head.next
#             return tempnode

#     def peek(self):
#         if self.isEmpty():
#             return "there is no node in the Queue"
#         else:
#             return self.Linkedlist.head
        
#     def display(self):
#         print(self.Linkedlist)

#     def deletequeue(self):
#         self.Linkedlist.head = None
#         self.Linkedlist.tail = None

# obj = Queue()
# while True:
#     print()
#     print("==================")
#     print("1. EnQueue")
#     print("2. DeQueue")
#     print("3. DISPLAY QUEUE")
#     print("4. PEEK OPRATION")#only returns top element doesn't delete
#     print("5. DELETE QUEUE")
#     print("6. EXIT")
#     print("==================")

#     choice = int(input("Enter your Choice: "))
#     if choice == 1:
#         value = int(input("Enter value to ADD in Queue: "))
#         obj.enQueue(value)
#     elif choice == 2:
#         obj.deQueue()
#     elif choice == 3:
#         obj.display()
#     elif choice == 4:
#         obj.peek()
#     elif choice == 5:
#         obj.deletequeue()
#     else:
#         break