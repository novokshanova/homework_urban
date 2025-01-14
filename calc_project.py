def calculator():

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            operator = input("Введите арифметический знак (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числа.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Деление на ноль невозможно!")
            return
        else:
            result = num1 / num2
    else:
        print("Некорректный арифметический знак.")
        return

    print("Результат:", result)

if __name__ == "__main__":
    calculator()