# Wirte program to get non zero numbers in list 
# name = list(map(int,input("Enter the numbers: ").split()))
# list =[]
# for i in name:
#     if i !=0:
#         list += [i]
# print(list)



#Find the first missing positive integer
# list = list(map(int,input("Enter the number of list : ".split())))
# num =[]
# for i in range(len(list)):
#     num.sort(i)
# print(i)
#     #if i >0:
        




#Tree
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild =None
        self.rightChild=None

    


        
def insertNode (rootNode,nodevalue):
    if rootNode.data==None:
        rootNode.data =nodevalue
    elif nodevalue <=rootNode.data:
        if rootNode.leftChild is None:
           rootNode.leftChild = BSTNode(nodevalue)
        else:
            insertNode(rootNode.leftChild, nodevalue)


    else:
        if rootNode.rightChild is None:
           rootNode.rightChild = BSTNode(nodevalue)
        else:
            insertNode(rootNode.rightChild, nodevalue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end =" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

#def InorderTraversal()    

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end ="  ")
    inOrderTraversal(rootNode.rightChild)



def postOrderTraversal(rootNode):
    if not rootNode:
        return
    
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end ="  ")


# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
    
#     print(rootNode.data, end =" ")
#     levelOrderTraversal(rootNode.leftChild)
#     levelOrderTraversal(rootNode.rightChild)
#     print(rootNode.data, end =" ")



def searchNode(rootNode, nodeValue):
    
    if nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is in left side",nodeValue)
        #else:
        #    searchNode(rootNode.rightChild, nodeValue) 
    elif nodeValue > rootNode.data:
        if rootNode.rightChild.data == nodeValue:
          print("The value is in right side",nodeValue)
    else:
        rootNode.data ==nodeValue
        print("Value not found")

newBST = BSTNode(None)
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)

print("\n")
print("Preorder ")

preOrderTraversal(newBST)

print("\n")
print("Inorder ")
inOrderTraversal(newBST)

print("\n")
print("Postorder ")
postOrderTraversal(newBST)

print("\n")
searchNode(newBST,100)






