from time import time
from random import randint
import matplotlib.pyplot as plt
from numpy import linspace
from math import log2

MAX, size = int(1e8), int(1e2)
elements, times = [], []
while(size < MAX):
    size *= 10
    arr = linspace(0, size, num=size, dtype=int)
    to_search = randint(0, size * 4)
    start = time()
    # Binary Search
    found = False
    low, mid, high = 0, 0, len(arr)-1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < to_search:
            low = mid + 1
        elif arr[mid] > to_search:
            high = mid - 1
        else:
            found = True
            break
    end = time()
    result = "Found!" if found else "Not Found!"
    total_time  = (end - start) * 1000
    elements.append(size)
    times.append(total_time)
    print(f"{result} Time taken to search {to_search} in array of {size:.0E} numbers is {total_time:.3f} Milliseconds")

x = linspace(0, max(elements), 100) 
y = [0] * 100
for i in range(1, len(x)):
    y[i] = (log2(x[i]/1000))
plt.xlabel('Number Count(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='log2(N)', color = 'orange') 
plt.plot(elements, times, label ='Binary Search', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()