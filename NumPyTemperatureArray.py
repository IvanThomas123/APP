import numpy as np

temperatures = np.array([28, 30, 27, 29, 31, 32, 30, 28, 33, 29])

print("First 3 days:", temperatures[:3])
print("Day 5 to Day 8:", temperatures[4:8])

print("Average:", np.mean(temperatures))
print("Maximum:", np.max(temperatures))
print("Minimum:", np.min(temperatures))
print("Total:", np.sum(temperatures))

temperatures = temperatures + 2

print("Modified array:", temperatures)