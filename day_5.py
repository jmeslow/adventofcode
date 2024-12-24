#%%
import numpy as np
with open("day_5.txt") as file:
    rules = []
    temp = file.readline()
    while temp.strip():
        rules.append(temp.strip().split("|"))
        temp = file.readline()
    tests = [x.strip().split(',') for x in file.readlines()]
rules = np.array(rules,np.int32)

order = {}
for i in rules:
    if i[0] not in order:
        order[i[0]] = [i[1]]
    else:
        order[i[0]].append(i[1])
    if i[1] not in order:
        order[i[1]] = []
def test_sort(input):
    array = np.array(input,np.int32)
    for j in range(len(array)-1):
        for k in array[j+1:]:
            #print(k, order[array[j]])
            if k not in order[array[j]]:
                return 0
    mid_index = int((array.size - 1) / 2)
    print(array[mid_index])
    return array[mid_index]

total = 0          
for i in tests:
    total += test_sort(i)
print(total)