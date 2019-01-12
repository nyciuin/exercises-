# user input
# if number, sum inputs
# if anything else, stop and show result

number2 = 0

print('please enter a number')
number1 = int(input())

while True:
    print('please enter another number ("stop to exit")')
    number2 = input()
    if number2.isdigit():
        number1 = number1 + int(number2)        
    else:
        break
    
print(str(number1))
