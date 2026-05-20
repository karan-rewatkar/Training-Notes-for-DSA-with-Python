# str = [1,1,0,1,1,1,0,1,1,1,1]
# count =0
# max_c =0
# for i in str:
#     if i == 1:
#       count += 1
#     else:
#        max_c=max(max_c,count)
#        count=0
# max_c = max(max_c, count)
# print(max_c)         





# str="abababab"
# count =0
# print(str.count("ab"))





# i =1
# while i<=5:
#     print(i)
#     i+=1



# def hello():
#     print("Hello World")
# hello()
# hello()





# def arithmatic():
#     a= int(input("Enter value of a: "))
#     b= int(input("Enter value of b: "))
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# result = arithmatic()
# print("arithmatic = ",result)










# def arithmatic(a,b):
    
#     sum = a+b
#     sub = a-b
#     div = a/b
#     mul = a*b
#     return sum, sub, div, mul
# #positional arguments
# result = arithmatic(5,5)
# print("arithmatic = ",result)




# def crdential(username, password):
#     if username == password:
#         print("login successfully")
#     else:
#         print("invalid credentials")    
# crdential(username="admin", password="admin")




# #default argument if function call not argument in the last
# def cityName(city = "pune"):
#     print(city)
# cityName("Nagpur")
# cityName("Mumbai")
# cityName()




# #variable length argument / variable number of argument
# def cityName(*name):
#     print(name)
# cityName("Nagpur", "Delhi", "Mumbai", "Pune")







# #modularity approach in function

# def add():
#     a = int(input("Enter value of A: "))
#     b = int(input("Enter value of B: "))
#     print(a+b)

# def sub():
#     a = int(input("Enter the vlaue of A: "))
#     b = int(input("Enter the values of B: "))
#     print(a-b)

# def div():
#     a = int(input("Enter the vlaue of A: "))
#     b = int(input("Enter the values of B: "))
#     print(a/b)



# def mul():    
#     a = int(input("Enter the vlaue of A: "))
#     b = int(input("Enter the values of B: "))
#     print(a*b)



# while True:
#     print("1. Additon")
#     print("2. substraction")
#     print("3. division")
#     print("4. multiplication")
#     print("5. exit")
#     choice = int(input("Enter your choice: "))
#     if choice ==1:
#         add()
#     elif choice ==2:
#         sub()
#     elif choice ==3:
#         div()
#     elif choice ==4:
#         mul()
#     elif choice ==5:
#         exit()
#     else:
#         print("Enter valid number form 1 to 5: ")        
        










# def findBiggestNumber(sampleArray): #======> 
#     biggestNumber  = sampleArray[0] #=========> o(1)
#     for index in range(1,len(sampleArray)):#=====>o(N)
#         if sampleArray[index] > biggestNumber:#=====> o(1)
#             biggestNumber = sampleArray[index] #====>o(1)
#     print(biggestNumber)  #======>o(1)
# sampleArray = [5,7,9,2,3,4]#=======>o(1)
# findBiggestNumber(sampleArray)#======>o(1)  







# def linearSearch(array, target):
#     for i in range(0,len(array)):
#         if array[i] ==target:
#             return i
#     return -1    

# array = [1,2,3,4,8,7,9]
# target = 7 #search the target value i.e 7
# linearSearch(array, target)
# result  = linearSearch(array,target)
# if result == -1:
#   print("Target value not found")
# else:
#     print("Element found at index ", result)  





# #emoving spaces from string:
# #1. rstrip()==> To remove spaces at right hand side
# #2. lstrip()==> TO remove spaces at left hand side
# #3. strip()===> To remove spaces both sides 
# city = input("Enter your city Name: ")
# scity = city.strip()
# if scity == 'Hyderabad':
#     print("Hello Hyderabadi..adab")
# elif scity =='chennai':
#     print("Hello madrasi.. vanakkam")
# elif scity=="Banglore":
#     print("Hello kannadiga... shubhodaya")
# else:
#     print("Entered city is invalid ")            










# mylist =[[100,198,333, 323],[122,232, 221,111],[223,565,245,764]]
# newlist=[]
# for i in range(3):
#   j=0
#   max = mylist[i][j]
#   for j in range(4):
#     c_max =mylist[i][j]
#     if max < c_max:
#       max =c_max
#   newlist.append(max)
# print(newlist)






# #input = prashant*is*a*good*programmer
# #output = ****prashantisagoodprogrammer
# list = "prashant*is*a*good*programmer"
# name =''
# val=''
# for i in list:
#      if i !='*':
#           name += i
#      else:
#           val+=i     
# print(name)
# print(str(val+name))



# dict = {"aaabbbbccceeeee"}
# for i in range(len(dict)):
#     max_length = max()
# print(max_length)


# dict = {"A":50,"B":30,"C":70}
# max_value = max(dict.values())
# print(max_value) 
