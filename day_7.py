with open('day_7.txt') as file:
    input = file.readlines()
file.close()

# There has to be a better way of doing this but it does accomplish the task of removing trailing
# whitespace and newlines and formatting it how I want
input = ([[int(x[0]),[int(x) for x in x[1].strip().split()]] for x in [x.split(":") for x in input]])

def check_sum_product(value,equation):

    # If down to the last two, check to see if either of them can complete the equation
    if len(equation) == 2:
        if (equation[0] * equation[1] == value) or (equation[0] + equation[1] == value):
            return True
        else:
            return False
    # If it is not the last two values then call the function recursively with both possible outcomes
    return check_sum_product(value,[equation[0]*equation[1]]+equation[2:]) or check_sum_product(value,[equation[0]+equation[1]]+equation[2:])


# Loop through created list
output = 0
for i in input:
    if(check_sum_product(i[0],i[1])):
        output += i[0]
print(output)
