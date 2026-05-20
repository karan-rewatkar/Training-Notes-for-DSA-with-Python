# def reverse(self, x: int) -> int:
#         num =0
#         rev =0
#         digit =0
#         while x>0:
#             num = num %10
#             rev = rev *10+digit
#             num  = num //10
#         print(rev)
#         reverse(123)

# num = 1234
# for i in str(num):
#         print(i)
       

# if __name__ == '__main__':
#     n = 5
#     for i in range(n):
#       i = int(i)
#       print(i*i)


# name = int(input("Enter the number: "))
# name = abs(name)
# rev=0
# while name > 0:
#     digit = name%10
#     rev = rev *10+digit
#     name = name//10
# rev= -abs(rev)
# print(rev)    



# name=int(input("Enter the number"))
# max_length =0
# for i in range(len(name)):
#     max_length=max(name)
#     print(max_length)



# num=[1,2,4,5,6]
# val =0
# for i in (num):
#     if  i %2 ==0:
#         val +=i
# print(val)



# #odd numbers addition
# num=[1,3,5,7,9,11,13,15]
# val =0
# for i in (num):
#     if  i %2 !=0:
#         val +=i
# print(val)



#Compare Reverse with original
# #Return "Same" if equal, otherwise return "Different".
# list = int(input("Enter the number "))
# rev=0
# original = list
# digit =0
# for i in str(list):

#     digit=list%10
#     rev = rev*10+digit
#     list=list//10
# print(rev)
# if original ==rev:
#         print("Same number")
# else:
#         print("Different number")    



# Remove Last Digit
# # Given an integer n, remove its last digit and return the remaining number.
# n=int(input("Enter the number "))
# rev=0
# digit=0
# digit = n%10
# rev =rev*10+digit
# n= n//10
# print(n)


# First Digit of a Number
# Given an integer n, return the first (most significant) digit.
# n = input("Enter ther number ")
# for i in range(len(n)):
#  print(n[0])
#  break




# Digital Root
# # Repeatedly sum the digits of a number until only one digit remains.
# n = input("Enter the number ")
# val =0
# for i in n:
 
 
#  while i >10:
#     i =int(i)
#     val+=i
# print(val)



#1 Count of digits
# n = input("Enter the number ")
# count = 0
# for i in range(len(n)):
#     count =count+1
# print(count)


# #2 Sum of digits
# n = input("Enter the number ")
# val=0
# for i in str(n):
#   i =int(i)
#   val +=i
# print(val)


#3 Product of Digits
# n  = input("Enter the number to multiple digits ")
# val =0
# for i in str(n):
#     i=int(i)
#     val=i*(i+1)
# print (val)    



#4 Reverse Integer
# num =int(input("Enter the number to reverse "))
# rev =0
# digit =0
# for i in str(num):
#     digit = num%10
#     rev = rev*10+digit
#     num = num //10
# print(rev)

#5 Palindrome Number
# num = int(input("Enter the number "))
# rev =0
# original = num
# digit =0
# for i in str(num):
#     digit = num %10
#     rev = rev*10+digit
#     num = num//10
# if original==rev:
#         print("the number is pelindrom")
# else:
#         print("the number is not pelindrom")    


#6 Palindrome alphabhet
# n = ("ababa")
# rev =""
# original = n
# for i in str(n):
#  rev = i+rev
# print(rev)    
# if original ==rev:
#  print("String is Pelindrome")
# else:
#  print("String is not pelindrome")



#7 display pelindrome pattern on string
# n = input("Enter the string ")
# long=""
# for i in range(len(n)):
#     for j in range(i+1,len(n)+1):
#         sub=n[i:j]
#         if sub==sub[::-1]:

#             if len(sub)>len(long):
#              long = sub
# print(long)        
     



#8 Largest Digit
# n =input("Enter how much number want to input ")
# num = input("Enter the number ".split())
# large =num[0]

# for i in num:
    
#     if i>large:
#         large=i
# print("Large number is ",large)




# #9 smallet digit
# num =input("Enter the number ")
# small = num[0]
# for i in num:
#     if i<num:
#         num =i
# print(num)


#10 Digital root

# num = 5
# while num > 0:
#     print(num)
#     num -= 1


# Reverse a string
# n= input("Enter the string ")
# reverse =""
# for i in str(n):
#   reverse = i + reverse
# print(reverse)

# check palindrome or not
# n = input("Enter the string : ")
# original = n
# reverse=""
# for i in n:
#     reverse = i + reverse
# if reverse==original:
#         print("The string is palindrome")
# else:
#         print("The string is not palindrome")   
 





#check the string contains pelindrome or not
# n = input("Enter the string: ")
# original = n
# reverse =""
# for i in n:
#    reverse = i +reverse

#    if reverse>original:
#     reverse = original
# print(reverse)






# #N=8 and arr = [4,5,0,1,9,0,5,0].
# There are 3 empty packets in the given set. These 3 empty packets represented as O should be pushed towards the end of the array
# Input :
# 8  – Value of N
# [4,5,0,1,9,0,5,0] – Element of arr[O] to arr[N-1],While input each element is separated by newline
# Output:
# 4 5 1 9 5 0 0 0

# n =list(map(int, input("Enter the number of packets ").split()))
# for i in (n):
#    if i==0:
#       n.remove(i)  
#       n.append(0)  
# print(n)
   




# num = int(input("Enter the number: "))
# original = num# Store number to original to compare after itration 
# digits = len(str(num))# length on num to mutiple in power
# total =0 #after calculating store the total calculation to compare 
# while num>0:
#    digit =num%10
#    total= total + digit ** digits #0 + 3*3
#    num = num//10
# if total ==original:
#       print("The number is Armstrong number ")
# else:
#       print("The number is not Armstrong number ")





# Create a set of vowels: a, e, i, o, u (both uppercase and lowercase
# Traverse the string.
# If the character is a vowel, increment count.
# Return count.
# name = input("Enter the String: ")
# vowels ={'a','e','o','u','A','E','O','u'}
# count=0
# for i in name:
#    if i in vowels:
#       count +=1   
# print(count)      





#Count the Number of Words in a Sentence
# Logic
# Split the sentence by spaces.
# Count the resulting words.
# Ignore extra spaces.
# name = input("Enter the string : ")
# count =0
# for i in name:
#    count +=1
# print(count)        





# Remove All Spaces from a String
# Logic
# Traverse each character.
# If character is not a space, add it to result.
# Return result.
# name = input("Enter the String : ")
# result =""
# for i in name:
#    if i != " ":
#         result = name
#    else:
#        name[i] = " "     
# print(result)
# incomplete




# Remove Duplicate Characters While Preserving Order
# Logic
# Maintain a set of seen characters.
# Traverse the string.
# If character not in seen:
# Add to result.
# Mark as seen.
# Return result.
# name = input("Enter the string : ")
# result =" "
# for i in name:
#     for j in 





#3.	Find the largest digit in a number
# num = list(map(int,input("Enter the numbers ").split()))
# large =num[0]

# for i in num:
#     if large < i:
#         large = i
# print(large)


# 4.	Check whether a number is palindrome
# num = int(input("Enter the number : "))
# original = num
# rev =0
# while num>0:
#     digit = num%10
#     rev = rev *10+digit
#     num = num//10
# if rev == original:
#     print("Number is palindrome ")
# else:
#     print("Number is not palindrome")





# 5.	Reverse a string
# name = input("Enter the string : ")
# reverse =""
# for i in name:
#     reverse = i+reverse
# print(reverse)




# 6.	Find the sum of digits of a number
# num = input("Enter the numbers: ")
# total = 0
# digit =0
# for i in num:  
#     i = int(i)
#     total = i + digit
#     digit +=i
# print(total)    





# #7.	Print all even numbers in an array
# arr = list(map(int, input("Enter the numbers ").split()))
# even =[]
# count =0
# for i in arr:
#     if i % 2 ==0:
#      count=count+1
#      if count ==3:
#       print(i)


            
    
    
# 8.	Find the second largest element
# num = input("Enter the number: ")
# second =None
# large =num[0]
# for i in num:
#     if large < i:
#         large = i
# for i in num:
#     if i !=large:
#         if second is None or i >second:
#             second = i  
# print(second)    






#9.	Check whether a string is an anagram
# #output listen  - silent
# name1 = input("Enter the first string: ")
# name2 = input("Enter the seocnd string: ")
# count = 0
# if len(name1) == len(name2):
#    for i in name1:
#      for j in name2:
    
#       if i == j:
#          count+=1
         
      
#    if count == len(name1):
#          print("The string is Anagram: ")
#    else:
#          print("The strings are not Anagram: ")
# else:
#    print("The strings are not Anagram: ")




# 10.	Count frequency of each character
# name = input("Enter the String : ")
# count =0
# store =""
# for i in name:
#     if i not in store: 
#      count =name.count(i)
#      print(i,"=",count)
#      store = store +i