#============================================ HASHING ==============================================

# hashing is the technique that is used to convert data into a fixed value called as hash function.

# Time Compexity: O(1)

# hash function converts input into fixed index.

#collision problem:
# key     calculation     Index
# 15        15%10           5
# 25        25%10           5
# 35        35%10           5

# ASCII values:
# C = 67
# A = 65
# T = 84

# sum => 67+65+84 = 216
# if table size  = 10
# 216%10 = 6
# the index is 6

# why collision happens?
#    infinite inputs
#    limited table size


#===================================================================================================

# class HashTable:
#     def __init__(self):
#         self.size =self.size
#         self.table = [[] for _ in range(size)]

#     def hash_function(self, key):
#         return key % self.size
    
#     def insert(self,key):
#         index = self.hash_function(key)
#         self.table[index].append(key)
    
#     def display(self):
#         print(self.table)
