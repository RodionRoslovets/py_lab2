def task1():
    words = []

    while True:
        word = input('Введите слово: ')
        if(word == 'stop'):
            break
        else:
            words.append(word)
    
    print(" ".join(words))

def task2():
    while True:
        word = input('Введите слово: ')
        separatedWord = list(word.lower())
        hasFs = 'ф' in separatedWord

        if(word == 'stop'):
            break
        else:
            if hasFs:
                print("Редкое слово")
            else:
                print("Не очень редкое слово")

task1()
task2()
