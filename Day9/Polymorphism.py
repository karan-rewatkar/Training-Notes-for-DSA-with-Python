#============================= POLYMORPHISM ==============================


# 1) COMPILE TIME

# - Python doesn't supports Method and Constructor overlaoding.
# - Only supports Oprator overlaoding

# 2) RUN TIME

# - Run time polymorphism is achieved using Method Overriding.
# - Same method name is used in Parent and Child class.
# - Method call is decided at run time.

#---------------------------------------------------------------------------------------------------

#Q1
# class RBI:
#     def home_loan(self):
#         print('Home Loan ROI = 8%')

#     def education_loan(self):
#         print('Education Loan ROI = 9%')

# class SBI(RBI):
#     def education_loan(self):
#         print('Education Loan ROI = 10%')
#         super().education_loan()

# obj = SBI()
# obj.education_loan()        #Education Loan ROI = 10%   Education Loan ROI = 9%

#---------------------------------------------------------------------------------------------------

#Q2
# class RBI:
#     def __init__(self):
#         print('parent class constructor')

# class SBI(RBI):
#     def __init__(self):
#         print('child class constructor')

# obj = SBI() #child class constructor

#---------------------------------------------------------------------------------------------------
