import numpy as np

arr = np.arange(1, 11)
print("Original Array:", arr)

print("First five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Every second element:", arr[::2])
print("Reversed array:", arr[::-1])

print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

arr = arr + 5
print("After adding 5:", arr)

arr = arr * 2
print("After multiplying by 2:", arr)