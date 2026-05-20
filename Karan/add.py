# #why python is called as dynamic types language
# age = 33
# name = "Karan"
# pi = 3.24
# result = True
# # print(type(age))  # <class 'int'>

# age = "thirty-three"
# print(type(age))  # <class 'str'>
# print(type(pi))
# print(type(name))
# print(type(result))


# age = 33
# name = "Karan"
# pi = 3.24
# result = True
# print(type(age))  # <class 'int'>

# age = "thirty-three"
# print(id(age))  # <class 'str'>
# print(id(pi))
# print(id(name))
# print(id(result))


#why all fundamentals datatypes  are immulatable
# math = 50
# chem = 50
# print(id(math))
# print(id(chem))


# #simple if

# print(2+2)
# print("2"+"2")
# a = int(input("Enter the first  number :"))
# b = int(input("Enter the second  number :"))
# print(a+b)


# # #int() used to convert in integer 3.14=int=3
# print(int(3.14))
# # print(int(10+5j))
# print(int(True)) #=1
# print(int(False)) #=0
# # #print(int("4.22"))
# print(int("4"))
# print(int("Karan"))
# #we can not convert complex value to int
# #we can not convert floating point value string to int
# #we can not convert string name int




# compleX() used to convert
# print(complex(3))
# print(complex(12,5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex("name"))
# print(complex(5,-3))
# print(complex(True,False))



# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))
# print (bool("-karan"))




#simple if
# a = int(input("Enter any single digit :"))
# if a > 0:
#  print("positive number")
# if a<0:
#   print("Negetive number")
# if a==0:
#  print("zero")   



#a = input("Enter the day : ")
#if a == "SATURDAY" or a=="SUNDAY" or a=="saturday" or a=="sunday":
#   print("Weekend")
#else:
#     print("Working day")   




# per = 65
# if per >=65:
#     print("grade A")
# elif per<=65 and per>=50:
#     print("Grade B")
# else:
#      print("Fail")   










# chr = ord(input("Enter any single character or number : "))# ord is used for convert une code to acce code

# if chr == 65 and chr <=90:
#   print("upper case")
# elif chr >97 and chr <=122:
#     print("Lower case")
# elif chr >48 and chr <=57:
#   print("digit")
# else:
#     print("Special cases")





# #identity operator(address comparison)
# math = 50
# chem = 90
# print(math is chem)





# #for (initialization; condition; inc/dec)
# for  i in range(6): #i =0
#     print(i)




# #for (initialization; condition; inc/dec)
# for  i in range(2,10): #i =0
#     print(i)





# #for (initialization; condition; inc/dec)
# for  i in range(2,10,2): #i =2
#     print(i)

# #for (initialization; condition; inc/dec)
# for  i in range(5,-5,-2): #i =0
#     print(i)    



# for  i in range(1,11,1): #i =2 
#     print(i*2)    # table of 2


# for  i in range(1,11): #i =2 
#     print(i*2,"  ",i*3,"  ",i*4,"  ",i*5,"  ",i*6,"  ",i*7,"  ",i*8,"  ",i*9,"  ",i*10)  
# print("--------------------------------------")       
# for  i in range(1,11):
#     print(i*11,"  ",i*12,"  ",i*13,"  ",i*14," ",i*15,"  ",i*16,"  ",i*17,"  ",i*18,"  ",i*19,"  ",i*20)  
#    # table of 2    


# math = int(input("Enter the marks of math : "))
# science = int(input("Enter the marks of science : "))
# english = int(input("Enter the marks of english : "))
# gender = input("Enter your gender(male/female) : ")
# total = math + science + english
# print("Total marks is : ",total)
# per = total/3
# print("percentage is :",per)

# if per >=65:
#     print("Pass")
# else:
#      print("Fail")     
# if per>=65 and gender == "male":
#     print("You are eligible for for placement")
# else:
#     print("you are not eligible for placement")




# #using break statement in for loop
# for i in range(1,5): #i=1
#     if i==3:
#         break
#     print(i)



# #continue statement in for loop
# for i in range(1,5): #i=1
#     if i==3:
#         continue
#     print(i)    


# #continue statement in for loop
# for i in range(1,5): #i=1
#     if i==3:
#         continue
#     print(i)    

#output 
# 1     5
# 2     4
# 4     2
# 5     1
        
# for i in range(1,6): #i=1
        
#     print(i,"   ",6-i)         


# val =123
# rev = 0
# while val > 0:
#     digit = val%10
#     rev = rev*10+digit
#     val = val//10
# print(rev)   





# #zip() we an take multiple range function inside zip()
for i,j in zip(range(1,6), range(5,0,-1)):
    print(i,"  ",j)




# mylist = ["karan","Ashish","Komal", "ankush", "Ashish", 77, "sandip", 60.52,"Karan"]
# print (mylist)
# print(type(mylist))#<list>
# print(mylist[0])#karan
# print(mylist[1])#Ashish
# print(mylist[2])#Komal
# print(mylist[-1])#Karan
# print(mylist[2:5])#n=5, n-l =4 komal","ankush","Ashish"
# print(mylist[:5])#n=5, n-1=4 "karan","Ashish", "komal", "ankush", "Ashish"
# print(mylist[1:])#n=8, n-1=8-1=Ashish","komal","ankush"
# print(mylist[1:8:2])






# mylist[2]="Akahay"
# print(mylist)
   


# if "ankush" in mylist:
#     print("Yes, ankush is available")
# else:
#     print("No available")






# #append and extend both work like same
# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist)





# # insert is use for any position we want to add element in list
# mylist.insert(3,"sanket")
# print(mylist)




# remove is used to remove the element from list
# mylist.remove("ankush")
# print(mylist)






# newlist =mylist.copy()
# print(newlist)



# cpomplete till here ----------------------------------------------------------------------------------




# mylist = [['prashant', 'jha'],['85.56'],[440022,"yyy"]]
# print("example of multidimensional list : ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])#prashant
# print(mylist[0][1])#jha
# print(mylist[1][0])#85.56
# print(mylist[2][0])#440022
# print(mylist[2][1])#yyy








# #using del keyword we can delete the element from list or we can delete whole list
# list2 = [50,25,50,'prashant']
# #del list2[2]
# del list2
# print(list2)



# list2=[50,25,50,'prashant']
# list2.clear()
# print(list2)








# name = "Karan" #['k','a','r','a','n']
# print(name)#k
# myname = list(name)#typescasting
# print(myname)
# #we have used list constructor to convert string into list







# mylist = [44,22,77,0,9,88]
# #mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)
# '''default sorting order for number is acsending order and for string is alphabetical order
# default sorting order for string is alphabetical order
# we should know that list should contains only homogenous data type for sorting otherwise we will get error
# '''











# #variable
# mylist=[44,22,77,0,9,88]
# newlist = mylist
# print (id(mylist))
# print (id(newlist))









# mylist = [44,12,77,0,9,88]
# for i in mylist:#i=0
#     print(i)

# mylist = [0,1,4,0,2,5]   
# print(mylist)
# print(mylist[1])
# print(mylist[2])
# print(mylist[4])
# print(mylist[5])
# print(mylist[0])
# print(mylist[3])








# list1=[0,1,4,0,2,5]
# for i in list1:#i=1:0
#     if i==0:
#         list1.remove(i)
#         list1.append(i)
# print(list1)        






# list1 = [7,3,9,2,8]
# list1.sort()
# print(list1[-2])





# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a)


'''output
beacuse we have 5 element in list and we are trying to assign 6 element to list so we will get error
as we follow assin before collin after that is list[start:stop:step]=iterable
Traceback (most recent call last):
File "d:\karan\CRT training\add.py", line 433, in <module>
    a[::2]=10,20,30,40,50,60
ValueError: attempt to assign sequence of size 6 to extended slice '''







# a=[1,2,3,4,5]
# print(a[3:0:-1])
# '''output [4, 3, 2] beacuse 3 means position of 4 and 0 means position of 1 but 1 is not included in output because we have to stop before 1 and -1 means reverse order
# so the output is [4, 3, 2]'''





# arr=[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop())

# '''output as in nested loop we have to pop last element of each list so the output is 4,7,11,15'''






# arr = [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]
# for i in range(0,6):
#     print(arr[i], end=" ")
# '''output as in first loop the range is 1 to 6 so the elements will be 2,3,4,5,6 and 
# in second loop the range is 0 to 6 so the elements will be 1,2,3,4,5,6 but in first loop we are assigning arr[i-1]=arr[i] so the output will be 2,3,4,5,6 and 
# last element will be 6 because we are not changing last element in first loop'''






# fruit_list1=  ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1
# fruit_list3 = fruit_list1[:]
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'

# sum=0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum+=1
#     if ls[1] == 'Kiwi':
#         sum+=20
# print(sum)








# list1 = [1,2,3] 
# list2  = [2,3,4]
# list3 = [3,4,5]
# for i in list1:
#     if i in list2 and i in list3:
#         print(i)


# mylist = []
# a = int(input("Enter the number of elements in list : "))
# for i in range(a):
    
#     element = int(input("Enter the element : "))
#     mylist.append(element)
    
# print(len(mylist))
# sum =0
# for i in range (len(mylist)-1):
#     if i+1 in range(len(mylist)):
#         sum += abs(mylist[i]-mylist[i+1])
# print(sum)        

    



