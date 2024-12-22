sum= 0
isRepeat = True

while isRepeat == True:
    num = eval(input("Enter a number ---> "))
    sum += num
    if num == 0:
        isRepeat = False
        print(f"The sum of all the number is {sum}")