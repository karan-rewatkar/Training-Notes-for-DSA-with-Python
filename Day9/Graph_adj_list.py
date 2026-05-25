#====================================== GRAPH ======================================

#Q1
#          graph                          Adjacency matrix                 Adjacency List

#        A ___ B __                        A   B   C   D   E               # A : [B,D,C]
#       | \        \                   A   0   1   1   1   0               # B : [A,E]
#       |  \        E                  B   1   0   0   0   1               # C : [A,D]
#       |   \      /                   C   1   0   0   1   0               # D : [A,C,E]
#       C __ D ___/                    D   1   0   1   0   1               # E : [B,D]
#                                      E   0   1   0   1   0

#---------------------------------------------------------------------------------------------------
#Implementation of above graph

# class Graph:
#     def __init__(self):
#         self.adjacency_list ={}

#     def add_vertex(self, vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex] = []
#             return True
#         return False
    
#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex,":",self.adjacency_list[vertex])

#     def add_edge(self, vertex1, vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)

#     def remove_vertex(self,vertex):
#         if vertex not in self.adjacency_list.keys():
#             print("the vertex not exist")
#         else:
#             self.adjacency_list.pop(vertex)
#             for v in self.adjacency_list.keys():
#                 if vertex in self.adjacency_list[v]:
#                     self.adjacency_list[v].remove(vertex)


# my_graph = Graph()
# my_graph.add_vertex('A')
# my_graph.add_vertex('B')
# my_graph.add_vertex('C')
# my_graph.add_vertex('D')
# my_graph.add_vertex('E')

# my_graph.add_edge('A','B')
# my_graph.add_edge('A','C')
# my_graph.add_edge('A','D')
# my_graph.add_edge('B','A')
# my_graph.add_edge('B','E')
# my_graph.add_edge('C','A')
# my_graph.add_edge('C','D')
# my_graph.add_edge('D','A')
# my_graph.add_edge('D','C')
# my_graph.add_edge('D','E')
# my_graph.add_edge('E','B')
# my_graph.add_edge('E','D')
# my_graph.print_graph()
# print()
# my_graph.remove_vertex('A')
# my_graph.print_graph()


# # output:
# # A : ['B', 'C', 'D']
# # B : ['A', 'E']
# # C : ['A', 'D']
# # D : ['A', 'C', 'E']
# # E : ['B', 'D']

# # B : ['E']
# # C : ['D']
# # D : ['C', 'E']
# # E : ['B', 'D']
