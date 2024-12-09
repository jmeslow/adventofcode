import numpy as np

# Read in data and transpose
data = np.transpose(np.genfromtxt("day_1.txt", delimiter= "   "))
# Sort 'left' side
data[0] = np.sort(data[0])
# Sort 'right side
data[1] = np.sort(data[1])
# Sum and return differences
print(np.sum(np.abs(data[1] - data[0])))

# Start part 2