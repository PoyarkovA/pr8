def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    a_input = input("Введите число a: ")
    b_input = input("Введите число b: ")

    if not (is_number(a_input) and is_number(b_input)):
        print("Пожалуйста, введите корректные числа.")
        continue  

    a = float(a_input)
    b = float(b_input)

    if a > b:
        a, b = b, a  

    print("Целые числа между a и b:")
    for num in range(int(a) + 1, int(b)):  
        print(num)
    break
