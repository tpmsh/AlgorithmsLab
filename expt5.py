from time import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np
from math import log2
from sys import maxsize as MAX_INT

class Graph():
    def __init__(self, vertices, rand=True):
        self.rand = rand
        self.costs = []
        self.mincost = 0
        self.V = vertices
        self.parent = [i for i in range(self.V)]
        self.graph = [[MAX_INT for column in range(vertices)] 
                    for row in range(vertices)]
        if rand:
            sz = self.V
            for i in range(int(sz**2)):
                row = randrange(0, sz)
                col = randrange(0, sz)
                self.graph[row][col] = randrange(0, sz * i+1)
        
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i
  
    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        self.parent[a] = b
  
    def kruskalMST(self):
        for i in range(self.V):
            self.parent[i] = i
        edge_count = 0
        while edge_count < self.V - 1:
            min_c = MAX_INT
            a = -1
            b = -1
            for i in range(self.V):
                for j in range(self.V):
                    if self.find(i) != self.find(j) and \
                    self.graph[i][j] < min_c:
                        min_c = self.graph[i][j]
                        a = i
                        b = j
            self.union(a, b)
            self.costs.append([edge_count, a, b, min_c])
            edge_count += 1
            self.mincost += min_c
      
        if not self.rand:
            self.printSolution()
        
    def printSolution(self):
        for i in range(len(self.costs)):
            edge_count, min_c = self.costs[i][0], self.costs[i][3]
            a, b = self.costs[i][1], self.costs[i][2]
            print(f'Edge {edge_count}:({a}, {b}) cost:{min_c}')
        print(f"Minimum cost = {self.mincost}")
         

MAX, size = int(90), 15
elements, times = [0], [0]
print("Kruskal's Algorithm took:")
while(size < MAX):
    size += 3
    g = Graph(size)
    start = time()
    # Kruskal's
    g.kruskalMST()
    end = time()
    tt  = (end - start) * 1000
    elements.append(size)
    times.append(tt)
    print(f"{tt:.3f}ms for Graph with {size} vertices ")
    
# Code for plotting Graph    
x = np.linspace(0, max(elements), 100) 
y = [0] * 100
for i in range(1, len(x)):
    y[i] = (x[i]/0.25 * (log2(x[i]/0.25)))
plt.xlabel('Number Count(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='Elog(V)', color = 'orange') 
plt.plot(elements, times, label ='Kruskal\'s', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()