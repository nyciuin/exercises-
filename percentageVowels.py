# input = string
# tell user what % of the string is vowels

print('Please enter string:')
phrase = str(input())

phraseLength = len(phrase)
lettersList = []
vowels = 0
consonants = 0
vowelList = ['a', 'e', 'i', 'o', 'u']

for i in range(len(phrase)):
    lettersList.append(phrase[i])
    print(lettersList)

for e in lettersList:
    print(e)
    if e in vowelList:
        vowels +=1
    else:
        consonants +=1
    print('v = ' + str(vowels))
    print('c = ' + str(consonants))

vowelPercent = ( vowels / (vowels + consonants) ) * 100
print(str(vowelPercent) + '% vowels')