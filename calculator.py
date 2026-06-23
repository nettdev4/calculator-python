import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
while True:
    clear_screen()
    
    print("====КАЛЬКУЛЯТОР====")
    print("Операции: '+', '-', '*', '/'")
    print("Для выхода введите 'Q'")

    operation = input("Выберите операцию: ")

    if operation.lower() =='q':
        print("Пока")
        break
    
    if operation not in ('+', '-', '*', '/'):
        input("Неверная операция. Нажиите Enter......")
        continue
    
    clear_screen()
    
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        input("Ошибка. Вводите Числа. Нажмите Enter......")
        continue
    
    clear_screen()
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            input("Ошибка. На ноль делить нельзя! Нажмите Enter......")
            continue
        result = num1 / num2
    
    print(f"{num1} {operation} {num2} = {result}")
    input("Нажмите Enter для продолжения......")
