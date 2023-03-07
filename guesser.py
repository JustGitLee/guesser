start = 0
end = 0
count = 0
mid = 0

def starting():
    global start
    global end
    global count
    count = 0
    print('Введи диапазон чисел')
    print('Начало - ', end='')
    start = input()
    while checking_digit(start) == False:
        print('Начало - ', end='')
        start = input()
    start = int(start)
    print('Конец - ', end='')
    end = input()
    while checking_digit(end) == False:
        print('Начало - ', end='')
        end = input()
    end = int(end)
    main()

def checking_digit(num):
    if not num.isdigit():
        print('\nНекорректный ввод')
        print("Введи целое число!")
        return False
    else:
        return True

def again():
    print("\nХочешь сыграть ещё? (да/нет)")
    answer_again = input()
    if answer_again.lower() == 'да':
        starting()
    elif answer_again.lower() == 'нет':
        print('\nНе хочешь, как хочешь! Пока!')
        exit()
    else:
        print('\nНекорректный ввод')
        print("Введи 'да' или 'нет'")
        again()

def func_more_less(answer_more_less):
    global mid
    global start
    global end
    if answer_more_less.lower() == 'больше':
        start = mid + 1
    elif answer_more_less.lower() == 'меньше':
        end = mid - 1
    else:
        print('\nНекорректный ввод')
        print("Введи 'больше' или 'меньше'")
    main()

def checking_answer(answer_yes_no):
    global mid
    global count
    if answer_yes_no.lower() == 'да':
        print(f"\nОтлично. Я угадал с {count} попыток")
        again()
    elif answer_yes_no.lower() == 'нет':
        print('\nОтветь, твоё число больше или меньше?')
        func_more_less(input())
    else:
        print('\nНекорректный ввод')
        print("Введи 'да' или 'нет')")
        main()

def main():
    global mid
    global start
    global end
    global count
    while start < end:
        mid = (start + end) // 2
        print(f'\nТвоё число {mid}? (да/нет)')
        count += 1
        checking_answer(input())
    print(f"\nТвоё число должно быть {end}")
    again()

print('Могу угадать любое твоё число')
starting()

