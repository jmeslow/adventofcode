# %%
import re
import numpy as np

# Regex for 
regex = "(?<=mul\()\d+\,\d+(?=\))"

with open('day_3.txt') as file:
    input = file.read()
# Find all regex matches
input = (re.findall(regex,input))

# Take array of regex matches and split them into two dimensions for multiplying
data = np.array([x.split(',') for x in input], dtype = np.int32)

# Transpose, multiply and report result
print(sum(data.T[0] * data.T[1]))
file.close()