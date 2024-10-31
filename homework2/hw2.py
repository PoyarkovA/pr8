while True:
    user_input_a = input("Введите первое число (или 'q' для выхода): ")
    if user_input_a.lower() == 'q':
        print("Выход из программы.")
        break
    
    user_input_b = input("Введите второе число (или 'q' для выхода): ")
    if user_input_b.lower() == 'q':
        print("Выход из программы.")
        break

    try:
        a = float(user_input_a)
        b = float(user_input_b)
        print("Сумма:", a + b)
    except ValueError:
        print("Пожалуйста, введите корректные числа (целые или вещественные).")
        continue  
