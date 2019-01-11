def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number//2
            print(number)
        elif number % 2 == 1:
            number = (number * 3) + 1
            print(number)
        # thing = if x then y else something else

def choose():
    try:
        print('please enter a number:\n')
        global chosenNumber
        chosenNumber = int(input())
    except:
        print('please enter an integer\n') 
        choose()   

chosenNumber = None
choose()
collatz(chosenNumber)
print('\nw o a h\n')