from time import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np
from sys import maxsize as MAX_INT

class Graph():
    def __init__(self, vertices, rand=True):
        self.rand = rand
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)]
        if rand:
            sz = self.V
            for i in range(int(sz**2)):
                row = randrange(0, sz)
                col = randrange(0, sz)
                self.graph[row][col] = randrange(0, sz * i+1)
    
    def minDistance(self, dist, sptSet):
        min = MAX_INT
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
  
        return min_index
    
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
    
    def dijkstra(self, src):
  
        dist = [MAX_INT] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
  
        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                sptSet[v] == False and \
                dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
        if not self.rand:
            self.printSolution(dist)
                   

MAX, size = int(625), 25
elements, times = [0], [0]
print("Dijkstra's Algorithm took:")
while(size <= MAX):
    size += 25 
    g = Graph(size)
    start = time()
    # Dijkstra
    g.dijkstra(0)
    end = time()
    tt  = (end - start) * 1000
    elements.append(size)
    times.append(tt)
    print(f"{tt:.3f}ms for Graph with {size} vertices ")

x = np.linspace(0, max(elements), 100) 
y = (x/30) ** 2
plt.xlabel('Number Count(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='V^2', color = 'orange') 
plt.plot(elements, times, label ='Dijkstra\'s', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()
