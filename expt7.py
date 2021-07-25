from time import time
import matplotlib.pyplot as plt
import numpy as np

class Queen:
    def __init__(self, N=4, rand=True):
        self.N = N
        self.rand = rand
        self.rd = [0]*N*2
        self.ld = [0]*N*2
        self.cl = [0]*N*2
        
    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(board[i][j], end = " ")
            print()
            
    def solveNQUtil(self, board, col):
        if (col >= self.N):
            return True
        for i in range(self.N):
            if ((self.ld[i-col+self.N-1]!=1 and
                self.rd[i+col]!=1) and self.cl[i]!=1):
                board[i][col] = 1
                self.ld[i-col+self.N-1] = self.rd[i+col] = self.cl[i] = 1
                if (self.solveNQUtil(board, col+1)):
                    return True
                board[i][col] = 0
                self.ld[i-col+self.N-1] = self.rd[i+col] = self.cl[i] = 0
        return False
        
    def solveNQ(self):
        board = [[0 for column in range(self.N)]for row in range(self.N)]
        if (self.solveNQUtil(board, 0) == False):
            print("Solution does not exist")
            return False
        if not self.rand:
            self.printSolution(board)
        return True

MAX, size = 22, 3
elements, times = [0], [0]
print("N Queen's Problem took:")
while(size < MAX):
    size += 1
    q = Queen(size)
    start = time()
    # N-Queen's
    q.solveNQ()
    end = time()
    tt  = (end - start) * 1000
    elements.append(size)
    times.append(round(tt,3))
    print(f"{tt:.3f}ms for {size} Queens")
    
# times = [0,0.0,0.0,0.0,0.001,0.003,0.018,1.0,1.034,3.008,7.01,26.002,39.996,149.028,342.701,670.0,1342.05,3499.016,12683.04,32764.0]


    
# Code for plotting Graph    
x = np.linspace(0, max(elements), 100) 
y = 2 ** (x/1.45)
plt.xlabel('Number of Queens(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='N!', color = 'orange') 
plt.plot(elements, times, label ='N-Queen\'s', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()