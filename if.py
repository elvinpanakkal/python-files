
is_male = True
 #is_male = False
is_tall = True

if is_male:
    print("YOu are a male")
else:
    print("You are a female")


if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither are a male nor tall")


if is_tall and is_male:
    print("You are tall and male ")
else:
    print("You are neither tall nor male")


if is_tall and is_male:
    print("You are tall and male ")
elif is_male and not (is_tall):
    print("You are a short male ")
elif not(is_male) and is_tall:
    print("You are a tall male")
else:
    print("You are neither tall nor male")














