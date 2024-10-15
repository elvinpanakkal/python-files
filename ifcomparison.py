

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
def equal_to(sum1,sum2):
    if sum1 == sum2:
        return sum1
    else:
        return sum2
def less_than(no1,no2):
    if no1 <= no2:
        return no2
    else:
        return no1

print(less_than(45,89)) 

print(equal_to(67,34))

print(max_num(3,4,5))




