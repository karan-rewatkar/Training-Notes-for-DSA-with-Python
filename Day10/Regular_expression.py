#=========================== Regular Expression in Python ==============================

# Q1
# Find Number of Occurrences of "function" Using Regular Expressions

# import re
# count=0
# pattern = re.compile("function")
# matcher = pattern.finditer("A function in python is defined by a def statment. Python the general syntax looks like this : def function-name(paramenter list) statements, i.e. the function body. The parameter python list consist of none or more parameter")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print('the number of occurrences:',count)

#---------------------------------------------------------------------------------------------------

# Q2
# Find Number of Occurrences of "Hi" Using finditer()

# import re
# count=0
# matcher = re.finditer("Hi","HiHiHiHIi")

# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print('the number of occurrences:',count)

#---------------------------------------------------------------------------------------------------

# Q3
# Find Position of Entered Character in a String Using Regular Expressions

# import re
# obj= input('Enter any character: ') #Enter any character: d
# objmatch= re.finditer(obj,"india")

# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group()) # op 2 ... 3 ... d

#---------------------------------------------------------------------------------------------------

# Q4
#Check Matching at Beginning of String Using re.match()

# import re
# a = input("enter string to perform match opration: ")
# mtch = re.match(a,"Python is very important language")
# print(mtch)
# if mtch!=None:
#     print('match found at begining level')
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching at begining level")

# #output:
# # enter string to perform match opration: Python
# # <re.Match object; span=(0, 6), match='Python'>
# # match found at begining level
# # 0 ... 6

#---------------------------------------------------------------------------------------------------

# Q5
# Check Full String Match Using re.fullmatch()

# import re
# a = input("enter string to perform match opration: ")
# mtch = re.fullmatch(a,"Pythonisvery")
# print(mtch)
# if mtch!=None:
#     print('match found')
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("Full match not found")

# #output:
# # enter string to perform match opration: Pythonisvery
# # <re.Match object; span=(0, 12), match='Pythonisvery'>
# # match found
# # 0 ... 12

#---------------------------------------------------------------------------------------------------

# Q6
# Validate Gmail ID Using Regular Expressions

# import re
# s = input("Enter Mail-ID: ")
# m = re.fullmatch("\w[a-zA-Z0-9]*@gmail[.]com",s)
# if m!=None:
#     print('Valid Email_ID')
# else:
#     print('Invalid Email_ID')

# #output:
# # Enter Mail-ID: sam@gmail.com
# # Valid Email_ID

#---------------------------------------------------------------------------------------------------

# Q7
# Validate Mobile Number Using Regular Expressions

# import re
# mo = input("Enter Mobile number: ")
# m = re.fullmatch("[0-9]\d{9}",mo)
# if m!=None:
#     print('Valid Mobile number')
# else:
#     print('Invalid Mobile number')

# #output:
# Enter Mobile number: 9889897845
# Valid Mobile number

#---------------------------------------------------------------------------------------------------

# Q8
# Search Matching Anywhere in String Using re.search()

# import re
# a = input("enter string to perform match opration: ")
# mtch = re.search(a,"Python sss dynamic lannn")
# print(mtch)
# if mtch!=None:
#     print(mtch.start(),"...",mtch.end(),"...",mtch.group())
# else:
#     print("there is no matching anywhere")

# #output:
# enter string to perform match opration: sss 
# <re.Match object; span=(7, 10), match='sss'>
# 7 ... 10 ... sss

#---------------------------------------------------------------------------------------------------

# Q9
# Find All Matches Using re.findall()

# import re
# mtch = re.findall('[A-Z]',"abch32hAhBr24r2dssSQ")
# print(mtch)                                         #op- ['A', 'B', 'S', 'Q']

#---------------------------------------------------------------------------------------------------

# Q10
# Replace Lowercase Letters Using re.sub()

# import re
# obj = re.sub('[a-z]','*',"3123 ASDAH rtyui")
# print(obj)                                          #op- 3123 ASDAH *****

#---------------------------------------------------------------------------------------------------

# Q11
# Replace Digits Using re.subn()

# import re
# obj = re.subn('[0-7]','@','av2sda7yahj8')
# print(obj)
# print('the string is: ',obj[0])
# print('the number of replacement is: ',obj[1])

# #output:
# # ('av@sda@yahj8', 2)
# # the string is:  av@sda@yahj8
# # the number of replacement is:  2

#---------------------------------------------------------------------------------------------------

# Q12
# Extract All Mobile Numbers From input.txt and Store in output.txt

# import re
# f1 = open('input.txt','r')
# f2 = open('output.txt','w')
# for line in f1:
#     numbers = re.findall('[0-9]{10}', line)
#     for n in numbers:
#         f2.write(n + '\n')

# print("Mobile numbers extracted successfully")
# f1.close()
# f2.close()

#---------------------------------------------------------------------------------------------------

# Q13
#Program to print the number of lines, words and characters present in the given file.

# import os, sys
# fname = input("Enter File Name: ")
# if os.path.isfile(fname):
#     print("File exists:", fname)
#     f=open(fname, "r")
# else:
#     print("File does not exist:", fname)
#     sys.exit(0)
# lcount=wcount=ccount=0
# for line in f:
#     lcount= lcount+1
#     ccount= ccount+len(line)
#     words=line.split()
#     wcount= wcount+len(words)

# print("The number of Lines:", lcount)
# print("The number of Words:", wcount)
# print("The number of Characters:", ccount)

# # Output:
# # Enter File Name: input.txt
# # File exists: input.txt
# # The number of Lines: 2
# # The number of Words: 6
# # The number of Characters: 40
#---------------------------------------------------------------------------------------------------