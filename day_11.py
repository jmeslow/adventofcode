# %%
with open('day_11.txt') as file:
    input = [x for x in file.readline().strip().split()]

def blink(iter):
    i = 0
    while(i < iter):
        point = 0
        while point < len(input):
            if(int(input[point]) == 0):
                input[point] = 1
                point+=1
            elif(len(str(input[point]))%2 == 0):
                temp = input[point]
                left = str(temp)[:len(str(temp))//2]
                right = str(temp)[len(str(temp))//2:]
                if int(left) != 0:
                    left = left.lstrip('0')
                if int(right) != 0:
                    right = right.lstrip('0')
                input[point] = left
                input.insert(point+1,right)
                point +=2
            else:
                input[point] = str(int(input[point]) * 2024)
                point+=1
        i += 1


blink(25)
print(len(input))