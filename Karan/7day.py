# # Find the First Non- Repeating Character
# def nonRepeating(s):
#     for i in s:
#         if s.count(i)==1:
#             return i
#         print("NO repeating number in string ")
# name = input("Enter the String : ")
# result = nonRepeating(name)
# print("The first repeating character is ",result)
        


        





#factorial Solution
# def factorial(num):
#     if num<=1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))





# def capitalizeFirst(arr):
#     result =[]
#     if len(arr) ==0:
#         return result
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result + capitalizeFirst(arr[1:])
# print(capitalizeFirst(['car', 'taco','banana']))



# def power(base, exponent):
#    if exponent==0:
#     return 1
#    return base * power(base, exponent-1)
# print(power(2,0))
# print(power(2,2))
# print(power(2,4))


# def productofArray(arr):
#     if len(arr)==0:
#         return 1
#     return arr[0]* productofArray(arr[1:])
# print(productofArray([1,2,3]))
# print(productofArray([1,2,3,10]))


#reverse a string using recursion
# def reverse(string):
#     if len(string) <=1:
#         return string
#     return string[len(string)-1] + reverse(string[0:len(string)-1])
# print(reverse('python'))
# print(reverse('appmillers'))



# #recursive range
# def recursiveRange(num):
#     if num<=0:
#         return 0
#     return num + recursiveRange(num-1)
# print(recursiveRange(6))



# #recursive pelindrome 
# def isPalindrome(string):
#     if len(string)==0:
#         return True
#     if string[0] != string[len(string)-1]:
#         return False
#     return isPalindrome(string[1:-1])
# print(isPalindrome('ababa'))





# #someRecursive Solution
# def someRecursive(arr,cb):
#     if len(arr) ==0:
#         return False
#     if not(cb(arr[0])):
#         return someRecursive(arr[1:],cb)
#     return True
# def isOdd(num):
#     if num%2==0:
#         return False
#     else:
#         return True
# print(someRecursive([1,2,3,4],isOdd))
# print(someRecursive([4,6,8,9],isOdd))
# print(someRecursive([4,6,8],isOdd))





#Tree structure in array
# class Tree:
#     def __init__(self,data):
#         self.data =data
#         self.child=[]
#     def addChild(self,object):
#         self.child.append(object)

#     def __str__(self,level =0):
#         ret="   "*level +str(self.data)+"\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret
    
# rootNode = Tree("Drinks")
# Hot      = Tree("Hot")
# Cold     = Tree("Cold")
# Tea      = Tree("Tea")
# coffee   = Tree("Coffee")
# NonAlcoholic = Tree("Non Alchohalic")
# Alcholic     = Tree("Alcholic")
            
    

# rootNode.addChild(Hot)#Left
# rootNode.addChild(Cold)#Rgiht
# Hot.addChild(Tea)#left
# Hot.addChild(coffee)#Right
# Cold.addChild(NonAlcoholic)#left
# Cold.addChild(Alcholic)#Right

# print(rootNode)


# class newTree:
#     def __init__(self,data):
#         self.data = data
#         self.child = []
#     def addChild(self,object):
#         self.child.append(object)

#     def __str__(self,level =0):
#         ret="   "*level +str(self.data)+"\n"
#         for ch in self.child:
#             ret += ch.__str__(level+1)
#         return ret    

# rootNode = newTree("N1")
# N2      = newTree("N2")
# N3     = newTree("N3")
# N4      = newTree("N4")
# N5   = newTree("N5")
# N6 = newTree("N6")
# N7 = newTree("N7")
# N8 = newTree("N8")
            

# rootNode.addChild(N2)#Left
# rootNode.addChild(N3)#Rgiht
# N2.addChild(N4)#left
# N2.addChild(N5)#Right
# N3.addChild(N6)#left
# N4.addChild(N7)#Right
# N4.addChild(N8)#Right

# print(rootNode)





# #Array rotation
# list= input("Enter the string : ")
# for i in range(len(list)):
    