
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
      
#       result  = ""
#       for i in s:
#         if i not in result:
#          result += i
#       print(len(result))
#       import string

# name = "prashantjha"#this is string 012345678910
# print(name[0])#p
# print(name[1])#r
# print(name[-1])#a
# #print(name[15])#error
# print(name[0:5])# end-1, 5-1=4 prash
# print(name[1:])#rashantjha
# print(name[:5])# 5-1=4 prash
# print(name[:])# prashantjha
# print(name[1:8:2])# 8-1=7 rsat
# print(name[::-1])#reverse pf string





# s= "python are High level programming language"
# print(s.lower())#python are high level programming language
# print(s.upper())#PYTHON ARE HIGH LEVEL PROGRAMMING LANGUAGE
# print(s.swapcase())#PYTHON ARE hIGH LEVEL PROGRAMMING LANGUAGE
# print(s.title())#Python Are High Level Programming Language
# print(s.capitalize())#Python are high level programming language

# name = "prashant"
# sal = 5000
# age = 28
# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name,y=sal,z=age))
# A=1
# print(f"{A} is a good boy")




# name  = "Karan Rewatkar"
# for i in name:#i=0:K, i=1:a, i=2:r, i=3:a, i=4:n, i=5: , i=6:R, i=7:e, i=8:w, i=9:a, i=10:t, i=11:k, i=12:a, i=13:r
#     print(i)



# name  = "Karan Rewatkar is a good"
# newname = ""
# for i in name:#i=0:K, i=1:a, i=2:r, i=3:a, i=4:n, i=5: , i=6:R, i=7:e, i=8:w, i=9:a, i=10:t, i=11:k, i=12:a, i=13:r
#     if i not in newname:
#      newname = newname + i    
# print(newname)




# name  = "Karan Rewatkar is a good"
# newname = ""
# N = len(name)
# for i in range(N-1,-1,-1):          
#     newname += name[i]
# print(newname)






# name = "12321"
# print(name)
# print(name[::-1])
# if name == name[::-1]:
#     print("palindrome")
# else:    
#    print("not palindrome")  






# #angram string
# name1 = "listen"  #where the lettters of one string are same as the 
# name2 = "silent"   #letters of another string but in different order
# if sorted(name1) == sorted(name2):
#     print("angram")
# else:
#     print("not angram")





# vowel = ['a','e','i','o','u']
# name = "hello"
# cons=0
# vow=0
# for i in name:
#     if i in vowel:
#         vow+= 1
#     else:
#         cons+=1
# print("consonants=",cons) 
# print("vowels=",vow)       





# name= "Karan Rewatkar"
# count = 0
# for i in name:
#     count = (name.count(i))
# print(count)



# #BODMAS
# a=50
# b=30
# c=20
# d=10

# print((a+b)*(c/d))
# print((a-b)*(c/d))
# print(a+(b*c)/d)






# a = input("Enter the string : ")
# for i in a:
#     if i == 65 and i <=90 :
#      continue
#      i >97 and i <=122 
#     elif i>= 48 and i <= 57:
#        continue
#     else:
#         count +=1
#     print(count)    
       





# name = "this is a test"
# print(name.title())



# print("hello world".isalnum())
# print(''.islower())
# print('karan87887'.isalnum())
# print('karan'.isalpha())
# print('My Name Is Karan'.istitle())
# print('karan'.startswith('ka'))
# print(' '.isspace())
# print('Karan Rewatkar'.rstrip())
# print('Karan Rewatkar '.isspace())
# print('8788870545'.isdigit())
# print('karan'.endswith('ran'))








# print("Karan Rewatkar".find("r"))
# print("Karan Rewatkar".index("q"))





# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end="  ")
#     print()    





# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end="  ")
#     print()



# #right angle triangle
# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print("*",end="  ")
#     print()




# #left angle triangle
# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end="  ")
#     print()









# import time
# n= int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     print(" "*(n-i),end="  ")
#     for j in range(1,i+1):
#         time.sleep(3)
#         print("*",end="  ")
#     print()








# n= [1,2,3,4]
# for i in range(1,5):
#     print(n[i]*i+1,end="  ")
# print()





# mytuple=("Prashant", "Ashish", "Rahul", "sandip","komal","ankush", "rajesh",23,3,15,77,"sandip")

# print(mytuple)
# print(type(mytuple))
# # mytuple[2]="sunil"#immutable errors
# # print(mytuple)




# init_tuple=()# if the value is not present in tuple then deafault value is zero
# print(init_tuple.__len__())



# init_tuple_a ='a','b'
# init_tuple_b = ('a','b') #('a', 'b')
# print(init_tuple_a==init_tuple_b)



# init_tuple_a ='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a+init_tuple_b)





# l=[1,2,3]
# init_tuple = ('Python',) * (l.__len__() -l[::-1][0])
# print(init_tuple)



# init_tuple = ('Python',) * 3
# print(type(init_tuple))






# init_typle=(1,)*3
# init_tuple[0]=2
# print(init_tuple)




# init_tuple =((1,2),)*7
# print(len(init_tuple[3:8]))





# mydict = {
#     101: "prashant",
#     102: "Ashish",
#     "103": "mohini",
#     "104": "trvani",
#     101: "ashish",
#     104: "ashish"
#     }
# print(mydict)
# print(type(mydict))
# a = mydict[102]
# print(a)

# mydict[102]="peter"
# print(mydict)




# for i in mydict:
#     print(i)

# for i in mydict.values():
#       print(i)



# for x,y in mydict.items():
#     print(x,y)



# #adding a new key : value pair
# mydict["mobile_no"] = 4646463738
# print(mydict)    




# #pop 
# mydict.pop(101)
# print(mydict)




# a ={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])




# #in tuple here is two keys are passing in one tuple so not allow error forms 
# a={'a':1,'b':2,'c':3}
# print(a['a','b'])





# arr={} #{1:2,'1':2}
# arr[1] =1
# arr['1'] = 2
# arr[1] +=1
# print(arr)
# sum = 0
# for k in arr:#k='1'
#     sum += arr[k]
# print(sum)





# my_dict ={}
# my_dict[1] = 1
# my_dict['1'] =2
# my_dict[1.0]=4
# print(my_dict)

# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)    








# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum += my_dict[k]
# print(sum)
# print(my_dict)    







# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len(crates[box]))





# dict = {'c':97, 'a': 96,'b':98}
# for _ in sorted(dict):
#   print(dict[_])






# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r) ==id(rec))




# rec = {"Name" : "Python", "Age":"20"}
# r = rec.copy()
# print(id(r) ==id(rec))
# print(id(r))
# print(id(rec))




# rec ={"Name": "python", "Age":"20", "Addr": "NJ","Country":"USA"}
# id1 = id(rec)
# print(id1)
# del rec
# rec ={"Name": "python", "Age":"20", "Addr": "NJ","Country":"USA"}
# id2 = id(rec)
# print(id2)
# print(id1 == id2)





# dict = {"A":50,"B":30,"C":70}
# max_value = max(dict.values())
# print(max_value) 




# dict = {"X":20,"Y":10,"Z":30}
# min_key = min(dict, key=dict.get)

# print(min_key) 




# dict={}
# a = [1,2,2,3,4,3,5]
# for i in a:
#     if i in dict:
#         dict[i] +=1
#     else:
#         dict[i] = 1
# print(dict)            





# num = 123 #321
# a = num % 10 # a=3
# num = num // 10 #num =12
# b = num% 10 #b =2
# c = num// 10 #c=1
# rev = a*100 + b*10 +c*1 #
# print(rev)


#123456 output 654321
#num = 123456






# Amount = int(input("Please Enter Amount for window : "))
# print("100 notes = ", Amount//100)
# print("50 notes = ", (Amount % 100//50))
# print("20 notes = ", ((Amount % 100)%50)//20)
# print("10 notes = ", (((Amount % 100)%50)%20)//10)
# print("5 notes = ", ((((Amount % 100)%50)%20)%10)//5)
# print("2 notes = ", (((((Amount % 100)%50)%20)%10)%5)//2)
# print("1 notes = ", ((((((Amount % 100)%50)%20)%10)%5)%2)//1)






# num=int(input("Enter the number: "))
# a= num % 10
# num = num // 10
# b = num % 10
# c = num // 10
# x = a*100+b*10+c*1
# print(x) 



# num = 123 #321
# a = num % 10 # a=3
# num = num // 10 #num =12
# b = num% 10 #b =2
# c = num// 10 #c=1
# rev = a*100 + b*10 +c*1 #
# print(rev)





