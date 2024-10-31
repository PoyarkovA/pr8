def clean_input(user_input):
    user_input = user_input.replace(',', '.')  
    cleaned = ''.join(filter(lambda x: x.isdigit() or x in ['-', '.'], user_input))
    return cleaned if cleaned else '0' 

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

total = 0
while True:
    user_input = input("Введите число (или 'stop' / 'end' для завершения): ")
    if user_input.lower() in ["stop", "end"]:
        break
    
    cleaned_input = clean_input(user_input) 
    if not is_number(cleaned_input):
        print("Пожалуйста, введите корректное число.")
        continue  

    total += float(cleaned_input)  
print("Сумма введённых чисел:", total)
