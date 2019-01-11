# list of unordered numbers (>3)
# sort without .sort-ing

print('please enter some numbers:')
numberList = []

while True:
    selection = input()
    try:
        if selection != 'stop':
            numberList.append(selection)
        elif selection == 'stop' or selection == 'Stop':
            break
        print('\nadd another number (type "stop" to finish):')
    except:
        print('please enter an integer.')

print('your chosen numbers are:')
for i in numberList:
    print(' ' + str(i))

def Ascending(inList):
# sort into new list, lowest first
# copy first value into final list
# delete first value from sorted list
# repeat until sorted list is empty
    finalList = []

    while inList:
        comp = inList[0]
        for i in inList:
            if i <= comp:
                comp = i
        
        print('minimum=' + str(comp))
        inList.remove(comp)
        finalList.append(comp)
        print('new inList: ' + str(inList))
    
    print(finalList)

            
Ascending(numberList)


### How to find a minimum in a list ###

# def Minimum(inList):
#     comp = inList[0]

#     for i in inList:
#         if i <= comp:
#             comp = i
    
#     print('The minimum value in the list is ' + str(comp))
