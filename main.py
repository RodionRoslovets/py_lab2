from random import randint

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

def task3():
    correctAnswersCounter = 0
    errorsCounter = 0

    while errorsCounter < 3:
        a = randint(0, 100)
        b = randint(0, 100)
        answer = input(f"{a} + {b} = ")

        if answer.isdigit():
            if a + b == int(answer):
                correctAnswersCounter += 1
                print('Верно!')
            else:
                errorsCounter += 1
                print('Не верно')
        else:
            print('Не числовое значение')

    print(f'Игра окончена. Количество верных ответов: {correctAnswersCounter}')


task1()
task2()
task3()
