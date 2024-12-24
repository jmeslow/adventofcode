# %%
import numpy as np
with open('day_10.txt') as file:
    input = [list(x.strip()) for x in file.readlines()]
    input = np.array(input,np.int32)

trailheads = []
for i,val1 in enumerate(input):
    for j,val2 in enumerate(val1):
        if val2 == 0:
            trailheads.append([i,j])
dirs = [[1,0],[-1,0],[0,1],[0,-1]]
def find_summit(start):
    val = input[start[0]][start[1]]
    #print(start,val)
    if val == 9:
             print('test')
             input[start[0]][start[1]] = -1
             return 1
    total = 0
    for i in dirs:
        temp = [start[0] + i[0],start[1] + i[1]]
        if temp[0] < 0  or temp[0] > input.shape[0]-1 or temp[1] < 0 or temp[1] > input.shape[1]-1:
             #print(temp)
             continue
        if input[temp[0]][temp[1]] == val+1:    
            #print(val)
            total += find_summit(temp)
    return total
output = 0
for i in trailheads:
     temp = input.copy()
     output += find_summit(i)
     input = temp.copy()
output