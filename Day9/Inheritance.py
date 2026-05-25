#============================= INHERITANCE =============================
##  sigle level Inheritance  ##
# class College:
#     def college_name(self):
#         print('University: RBU Nagpur')
    
# class Student(College):
#     def student_info(self):
#         print('Name: sahil dahake')
#         print('Branch: MCA')

# obj= Student()
# obj.college_name()
# obj.student_info()
# #op
# # University: RBU Nagpur
# # Name: sahil dahake
# # Branch: MCA

#-------------------------------------------------------------------------------

##  Multi-level Inheritance  ##
# class College:
#     def college_name(self):
#         print('University: RBU Nagpur')
    
# class Student(College):
#     def student_info(self):
#         print('Name: sahil dahake')
#         print('Branch: MCA')

# class Exam(Student):
#     def subject(self):
#         print('Subject1: ML')
#         print('Subject2: OOPS')
#         print('Subject3: DSA')

# obj= Exam()
# obj.college_name()
# obj.student_info()
# obj.subject()
# #op
# # University: RBU Nagpur
# # Name: sahil dahake
# # Branch: MCA
# # Subject1: ML
# # Subject2: OOPS
# # Subject3: DSA

#-------------------------------------------------------------------------------

# Multiple Inheritance
# class Submarks:
#     math=int(input('Enter paper marks of maths: '))
#     DE=int(input('Enter paper marks of DE: '))
#     c=int(input('Enter paper marks of c: '))
#     english=int(input('Enter paper marks of english: '))

# class Practmarks:
#     cpract = int(input('Enter practical marks for c language: '))

# class Result(Submarks,Practmarks):
#     def total(self):
#         if self.math>=40 and self.DE>=40 and self.c>=40 and self.english>=40 and self.cpract>=20:
#             print('PASS')
#         else:
#             print('FAIL')

# obj= Result()
# obj.total()