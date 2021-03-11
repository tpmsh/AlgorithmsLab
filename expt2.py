from time import time
from random import randrange
import matplotlib.pyplot as plt
from numpy import linspace
from math import log2

MAX, size = int(1e5), 1
elements, times = [], []

def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m  
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0
    j = 0
    k = l 
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = (l+(r-1))//2
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
while(size < MAX):
    size *= 2
    arr = [0] * size
    for i in range(size):
        arr[i] = randrange(0, size)
    start = time()
    # Merge Sort
    mergeSort(arr, 0, len(arr) - 1)
    end = time()
    total_time  = (end - start) * 1000
    elements.append(size)
    times.append(total_time)
    print(f"Time taken to sort array of {size:.0E}" 
          + f" numbers is {total_time:.3f} Milliseconds")

x = linspace(0, max(elements), 100) 
y = (x/1000) ** 2
plt.plot(x, y, label ='N^2', color = 'Red')
x = linspace(0, max(elements), 100)
y = [0] * 100
for i in range(1, len(x)):
    y[i] = (x[i]/500 * (log2(x[i]/500)))
plt.plot(x, y, label ='Nlog(N)', color = 'orange')
plt.xlabel('Number Count') 
plt.ylabel('Time(in Milliseconds)')
plt.plot(elements, times, label ='Mege Sort', color = 'blue') 
plt.grid() 
plt.legend() 
plt.show()