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

def task2():
    isBreak = False

    while isBreak != True:
        word = input('Введите слово: ')
        separatedWord = list(word.lower())
        hasFs = 'ф' in separatedWord

        if(word == 'stop'):
            isBreak = True
        else:
            if hasFs:
                print("Редкое слово")
            else:
                print("Не очень редкое слово")

task1()
task2()
