def fizzbuzz():    
    x = 1
    for i in range(1,101):
        if x % 3 == 0 and x % 5 == 0:
            print(str(i) + ' fizzbuzz')
        elif x % 5 == 0:
            print(str(i) + ' buzz')
        elif x % 3 == 0:
            print(str(i) + ' fizz')
        else:
            print((str(i)) + '\n')
        x += 1

    main()


def numberGuess():    
    from random import randint
    answer = randint(1,101)
    solution = 0

    print('guess a number between 1 and 100')

    while solution == 0:
        guess = int(input())
        
        if guess == answer:
            print('correct!')
            solution = 1
        elif guess >= answer:
            print('too high >:(')
        elif guess <= answer:
            print('too low :<')

    print(':clappingemoji:\n')

    main()


def main():
    print('Pick an exercise:\n' + '1: Fizzbuzz\n' + '2: Guess a number\n')
    choice = input()

    if choice == '1':
        fizzbuzz()
    elif choice == '2':
        numberGuess()
    else:
        print('\nno\n')
        main()

main()
