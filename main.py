def task1():
    isBreak = False
    words = []

    while isBreak != True:
        word = input('Введите слово: ')
        if(word == 'stop'):
            isBreak = True
        else:
            words.append(word)
    
    print(" ".join(words))

task1()
