
import csv
import numpy as np

total = 0

with open('day_2.txt') as file:
    reader = csv.reader(file, delimiter = " ")
    for row in reader:
        # Convert to numpy array
        array = np.array(row,dtype=np.int32)
        # Subtract shifted array from previous array to create negated values
        array = (array[1:] - array[0:-1])

        for i in range(array.size):
            # Break if value is too high or low
            if np.abs(array[i]) > 3 or np.abs(array[i]) < 1:
                break
            if i != 0:
                # Break if array changes from increasing to decreasing and vice versa
                if array[i] * array[i-1] < 0:
                    break
            if i == array.size -1 :
                #Increment if valid
                total+= 1
                print("Is Valid")

print(total)

# Start part 2