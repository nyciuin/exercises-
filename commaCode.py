
# # take a list value
# return a string of all items in the list separated by commas 
# 'and' separates the last two items 
# needs to work with any list

spam = ['apples', 'bananas', 'tofu', 'cat']
spam1 = ['bananas', 'tofu', 'cat']
spam2 = ['apples', 'cat']


def commaCode(inputlist):
    for i in inputlist[:-1]:
        print(str(i) + ', ', end='')
    print('and ' + inputlist[-1] + '.')

commaCode(spam)
commaCode(spam1)
commaCode(spam2)