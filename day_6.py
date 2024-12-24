# %%
with open("day_6.txt") as file:
    input = [list(x.strip()) for x in file.readlines()]
input

dir = ['<','V','>','^']
coords = [[0,-1],[1,0],[0,1],[-1,0]]

locs = {}

for i in range(len(input)):
    
    for j in range(len(input[i])):
        if input[i][j] in dir:
            cur_loc = (i,j)
            cur_dir = input[i][j]
        locs[(i,j)] = input[i][j]
total = 0
while True:
    new_loc = (cur_loc[0] + coords[dir.index(cur_dir)][0], cur_loc[1] + coords[dir.index(cur_dir)][1])
    if new_loc not in locs:
        locs[cur_loc] = 'X'
        total +=1
        break
    if locs[new_loc] == '#':
        cur_dir = dir[dir.index(cur_dir)-1]
        print(cur_dir)
        continue
    elif locs[new_loc] == '.':
        total +=1
    locs[cur_loc] = 'X'
    cur_loc = new_loc

for x in locs:
    input[x[0]][x[1]] = locs[x]
print(total)