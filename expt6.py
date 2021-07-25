from time import time
from random import randrange
import matplotlib.pyplot as plt
import numpy as np
from sys import maxsize as MAX_INT

class Graph():
    def __init__(self, vertices, rand=True):
        self.rand = rand
        self.V = vertices
        self.graph = [[MAX_INT for column in range(vertices)] 
                    for row in range(vertices)]
        if rand:
            sz = self.V
            for i in range(int(sz**1.5)):
                row = randrange(0, sz)
                col = randrange(0, sz)
                self.graph[row][col] = randrange(0, sz * i+1)


    def floydWarshall(self):
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.graph))
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        if not self.rand:
            self.printSolution(dist)


    def printSolution(self, dist):
        print("All Pairs Shortest Path Matrix")
        for i in range(self.V):
            for j in range(self.V):
                if(dist[i][j] == MAX_INT):
                    print("%7s" % ("INF"), end='')
                else:
                    print("%7d\t" % (dist[i][j]), end='')
                if j == self.V-1:
                    print("")

MAX, size = int(90), 15
elements, times = [0], [0]
print("Floyd Warshall Algorithm took:")
while(size < MAX):
    size += 3
    g = Graph(size)
    start = time()
    # Floyd Warshall
    g.floydWarshall()
    end = time()
    tt  = (end - start) * 1000
    elements.append(size)
    times.append(tt)
    print(f"{tt:.3f}ms for Graph with {size} vertices ")
    
# Code for plotting Graph    
x = np.linspace(0, max(elements), 100) 
y = (x/11) ** 3
plt.xlabel('Number of Vertices(V)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='V^3', color = 'orange') 
plt.plot(elements, times, label ='Floyd Warshall', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()