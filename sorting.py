import time
import random
import numpy as np
from matplotlib import pyplot as plt

def bubble(a:list) -> list: # sorts using Bubble method

    n = len(a)
    for k in range(n):
        for i in range(n-1):
            if a[i]>a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        else:
            continue
    return a
        
def selection(a:list) -> list: # sorts using (Min) Selection method in Recursive way DO IT ITERATIVE
    n = len(a)
    if n==1:
        return a
    elif n<=100: # Recursive approach for less than 100 entries
        indmin = a.index(min(a))
        a_min = a[indmin]
        a.remove(a_min)
        a = [a_min] + selection(a)
        return a    
    else: #iterative approach for more then 100 entries (recursion depth avoided)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if a[j] < a[min_index]:
                    min_index = j
            a[i], a[min_index] = a[min_index], a[i]
        return a
                
def quicksort(a:list) -> list: # sorts using Quicksort method 
    n=len(a)
    if n<=1:
        return a
    
    pivot = a[-1]
    indpiv = a.index(pivot)
    c = [x for x in a if x<pivot]
    d = [x for x in a if x>pivot]
    return quicksort(c) + [a[indpiv]] + quicksort(d)

def merge(a):
    divided = [[value] for value in a]
    print(divided)
    return divided

xdata = [10**i for i in range(1,6)]
array = [[int((random.random())*1000) for x in range(int(i))] for i in xdata]  #unsorted array


t_bubble, t_selection, t_quick, built_in = [],[],[],[]

#Bubble
for i in range(len(xdata)):
    start_bubble = time.time()
    bubble(array[i][:])
    end_bubble= time.time()
    t_bubble.append((end_bubble - start_bubble)*1e3)

#Selection
for i in range(len(xdata)):
    start_selection = time.time()
    selection(array[i][:])
    end_selection = time.time()
    t_selection.append((end_selection - start_selection)*1e3)

#Quicksort
for i in  range(len(xdata)):
    start_quick = time.time()
    quicksort(array[i][:]) 
    end_quick = time.time()
    t_quick.append((end_quick - start_quick)*1e3)


# #Mergesort
# start_merge = time.time()
# merge(arr)
# end_merge = time.time()

# build-in SORTED function
for i in range(len(xdata)):
    s = time.time()
    sorted(array[i][:])
    e = time.time()
    built_in.append((e-s)*1e3)

    
# print(f"Computational Bubble time = {(end_bubble-start_bubble)*1e3:.3f}ms")
# print(f"Computational Selection time = {(end_selection-start_selection)*1e3:.3f}ms")
# print(f"Computational Quicksort time = {(end_quick-start_quick)*1e3:.3f}ms")
# print(f"Computational Mergesort time = {(end_merge-start_merge)*1e3:.3f}ms")
print(f"Total Computational time = {(e-start_bubble):.3f}s")

# --- PLOTTING --- #

plt.scatter(np.log10(xdata),np.log10(t_bubble), label = "Bubble")
plt.scatter(np.log10(xdata),np.log10(t_selection), label = "Selection")
plt.scatter(np.log10(xdata),np.log10(t_quick), label = "Quick")
plt.scatter(np.log10(xdata),np.log10(built_in), label = "Built-in Sorted")
plt.legend()
plt.xlabel("$log_{10}N$ -  N =Array lenght")
plt.ylabel("$Log_{10}(T)$ - T = Computational time[ms]")
plt.title("My Sorting Algorithms Comparison")
plt.show()



