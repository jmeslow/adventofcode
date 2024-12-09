import numpy as np

with open('day_4.txt') as file:
    input = file.readlines()
data = np.array([list(x[:-1]) for x in input])

# Probably a better way of doing this, but each column cooresponds to location on the 'board'
# i.e index 0 is one row 'back' and one col 'back'
# This is used to indicate direction in recursive function i.e index 0 is top-left-diagonal
row_val = [-1,-1,-1,0,0,1,1,1]
col_val = [-1,0,1,-1,1,-1,0,1]

def find_xmas(array,y,x,dir):
    xmas  = "XMAS"
    #If current letter is S, end recursion
    if array[y][x] == xmas[-1]:
        return 1
    
    try:
        # Check to make sure index is inbounds
        if y+row_val[dir] < 0 or x+col_val[dir] < 0:
            # Array is wrapping around
            return 0
        temp = array[y+row_val[dir]][x+col_val[dir]]
    except:
        # Invalid index
        return 0
    
    # If next letter along the direction is the next letter in XMAS then recurse
    if temp == xmas[xmas.find(array[y][x])+1]:
        return find_xmas(array,y+row_val[dir],x+col_val[dir],dir)
    else:
        # Otherwise end recursion
        return 0

# Function for part 2
def find_mas(array,y,x,dir):

for row in range(data.shape[0]):
    for col in range(data.shape[1]):
        if data[row][col] == "X":
            for i in range(len(row_val)): 
                total += find_xmas(data,row,col,i)

print(total)