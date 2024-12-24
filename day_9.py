with open('day_9.txt') as file:
    input = file.readline()
disk_map = []
for i in range(len(input)):
    if i % 2:
        for k in range(int(input[i])):
            disk_map.append('.')
    else:
        for k in range(int(input[i])):
            disk_map.append(str(max(0,i//2)))

final_map = []
print(disk_map)
while len(disk_map) != 0:
    temp = disk_map.pop(0)
    if temp == '.':
        if len(disk_map) == 0:
            continue
        while disk_map[-1] == '.':
            disk_map.pop(-1)
        final_map.append(disk_map.pop(-1))
    else:
        final_map.append(temp)
total = 0
for i,v in enumerate(final_map):
    total += i * int(v)

print(total)