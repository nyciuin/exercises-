catNames = []

while True:
    print('Enter name of cat ' + str(len(catNames) + 1) + ', or enter nothing to stop:')

    name = input()
    if name =='':
        break
    
    catNames = catNames + [name]

print('The names of your cats are:')
for i in catNames:
    print(' ' + i)

for i in range(len(catNames)):
    print('The cat in index ' + str(i) + ' is called ' + catNames[i])