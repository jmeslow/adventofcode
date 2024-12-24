import numpy as np

# Read in data and transpose
data = np.transpose(np.genfromtxt("day_1.txt", delimiter= "   "))
# Sort 'left' side
data[0] = np.sort(data[0])
# Sort 'right side
data[1] = np.sort(data[1])
# Sum and return differences
print("Sum of differences: " + str(np.sum(np.abs(data[1] - data[0]))))

# Start part 2

occurences = {}

for i in data[1]:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i] = 1

similarity_score = 0
for i in data[0]:
    if i in occurences:
        similarity_score += i * occurences[i]
print(f'The similarity score for this input is: {similarity_score}')