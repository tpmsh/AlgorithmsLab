from time import time
from random import randrange
import matplotlib.pyplot as plt
from numpy import linspace

MAX, size = int(5e3), 1
elements, times = [], []
while(size < MAX):
    size *= 2
    arr = [0] * size
    for i in range(size):
        arr[i] = randrange(0, size)
    start = time()
    # Selection Sort
    for i in range(size - 1):
        mi = i
        for j in range(i+1, size):
            if(arr[j] < arr[mi]):
                mi = j
        arr[i], arr[mi] = arr[mi], arr[i]
    end = time()
    total_time  = (end - start) * 1000
    elements.append(size)
    times.append(total_time)
    print(f"Time taken to sort array of {size:.0E}" 
          + f" numbers is {total_time:.3f} Milliseconds")

x = linspace(0, max(elements), 100) 
y = (x/100) ** 2
plt.xlabel('Number Count(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='N^2', color = 'orange') 
plt.plot(elements, times, label ='Selection Sort', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()