#metod split



print("Hello! Choose an action: add(+), sub(-), mul(*), div (/)")
print ("Input example: add mul")
print(input("Select an action:"))

actions = input().split()


'''
Entering numbers and exit condition
'''

while True:
    numbers= input("Enter numbers separated by a space or end to exit:").split()

    if numbers[0] == "end":
        break
    
    numbers = [int(num) for num in numbers]

'''
Performing actions
'''
for action in actions:
    if action =="add":
        res = sum(numbers)
    elif action == "sub":
        res = numbers[0]-sum(numbers[1:])
    elif action == "mul":
        res = 1
        for num in numbers:
            res *= num
    elif action == "div":
        res = numbers[0]
        for num in numbers[1:]:
            res /= num
    else:
        print("Enter correctly")
        break

'''
Output the results of actions
'''

print (f"{actions}={res}")

print("The program is completed, goodbye!")

