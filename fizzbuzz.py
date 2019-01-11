
x = 1
for i in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print(str(i) + ' fizzbuzz')
    elif x % 5 == 0:
        print(str(i) + ' buzz')
    elif x % 3 == 0:
        print(str(i) + ' fizz')
    else:
        print(str(i))
    x += 1
    
