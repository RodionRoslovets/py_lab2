from random import randint
from collections import UserDict
import re

# get key by value
def getKey(value:list, dictionary:dict):
    for key, val in dictionary.items():
        if val == value:
            return key
        
# get value index, difference from index in parameters
def getDifferentIndex(index:int, list:list):
    ind = randint(0, len(list ) - 1)

    if ind != index:
        return ind
    else:
        return getDifferentIndex(index, list)

# create dictionary from file
f = open('./synonyms.txt', 'r')

dict = UserDict()

for line in f:
    spl = line.split(' - ')

    #clear dict from separate lines
    if len(spl) == 1:
        continue

    dict[spl[0].lower()] = spl[1].replace('\n', '').split("; ")

f.close()

word = input("Введите слово: ").lower()

answer = ''

if word in dict.keys():
    answer = dict[word][randint(0, len(dict[word]) - 1)]
else:
    for val in dict.values():
        if word in val:
            if len(val) > 1:
                ind = val.index(word)
                returnInd = getDifferentIndex(ind, dict[getKey(val, dict)])
                answer = dict[getKey(val, dict)][returnInd]
            else:
                answer = getKey(val, dict)

if answer:
    print(answer)

    writeNew = input('Добавить новый синоним к введенному слову? (д/н): ').lower()

    if writeNew == 'д':
        newSynonym = input('Введите новый синоним: ').lower()
        f = open('./synonyms.txt', 'r')
        lines = f.readlines()

        for line in lines:
            if re.match(word, line, re.IGNORECASE) or re.match(answer, line, re.IGNORECASE):
                splittedLine = line.split('\n')
                splittedLine[0] += '; ' + newSynonym
                newLine = ''.join(splittedLine) + '\n'
                lines[lines.index(line)] = newLine
            else:
                continue

        f.close()
        f = open('./synonyms.txt', 'w')
        f.write(''.join(lines))
        f.close()

        print('Синоним добавлен')
else: 
    print("Слово не найдено")

