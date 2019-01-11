

### 3 variables ###

first = 0
second = 1
third = 0

for i in range(101):
    third = first + second  
    first = second
    second = third       

    print(str(i +1) + ': ' + str(third))


###2 variables ###

n1, n2 = 0, 1

for i in range(101):
    n1, n2 = n2, (n1 + n2)
    print(str(i +1) + ': ' + str(n2))