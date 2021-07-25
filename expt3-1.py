from time import time
from random import randrange, randint
import matplotlib.pyplot as plt
from numpy import linspace

MAX, size = int(1e6), int(1e3)
elements, times = [], []
while(size < MAX):
    size *= 2
    arr = [0] * size
    for i in range(size):
        arr[i] = randrange(0, size)
    to_search = randint(0, size * 2)
    start = time()
    # Linear Search
    found = False
    for ele in arr:
        if ele == to_search:
            found = True
            break
    result = "Found!" if found else "Not Found!"
    end = time()
    total_time  = (end - start) * 1000
    elements.append(size)
    times.append(total_time)
    print(f"{result} Time taken to search {to_search} in array of" 
          + f" {size:.0E} numbers is {total_time:.3f} Milliseconds")

x = linspace(0, max(elements), 100) 
y = x/10000
plt.xlabel('Number Count(N)') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(x, y, label ='N', color = 'orange') 
plt.plot(elements, times, label ='Linear Search', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()