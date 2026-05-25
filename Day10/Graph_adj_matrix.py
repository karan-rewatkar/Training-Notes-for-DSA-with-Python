#=========================================== GRAPH =================================================

#Consider this graph                     =            ADJACENCY MATRIX
#                                        =               A   B   C   D
#    A----B                              =           A   0   1   1   0
#    |    |                              =           B   1   0   0   1
#    C----D                              =           C   1   0   0   1
#                                        =           D   0   1   1   0

# Connections=>
# A --> B  (0,1) (1,0)
# A --> C  (0,2) (2,0)
# B --> D  (1,3) (3,1)
# C --> D  (2,3) (3,1)

#===================================================================================================

# class Graph:
#     def __init__(self,vertices):
#         self.v = vertices # total no. of vertices

#         # create adjacency matrix with all 0s
#         self.matrix = [[0 for _ in range(vertices)] 
#                        for _ in range(vertices)]
        

#     def display(self):
#         for row in self.matrix:
#             print(row)

#     def add_edge(self,u,v):
#         self.matrix[u][v] =1
#         self.matrix[v][u] =1
    
#     def remove_edge(self,u,v):
#         self.matrix[u][v] =0
#         self.matrix[u][v] =0

# g = Graph(4)
# g.add_edge(0,1)
# g.add_edge(0,2)
# g.add_edge(1,3)
# g.add_edge(2,3)

# g.display()

# g.remove_edge(0,1)
# print()
# g.display()

# #output
# # [0, 1, 1, 0]
# # [1, 0, 0, 1]
# # [1, 0, 0, 1]
# # [0, 1, 1, 0]

# # [0, 0, 1, 0]
# # [1, 0, 0, 1]
# # [1, 0, 0, 1]
# # [0, 1, 1, 0]
#---------------------------------------------------------------------------------------------------