while True:
    num1 = input("Введите первое число: ")
    num2 = input("Введите второе число: ")
    t1=num1.replace('-','')
    t2=num2.replace('-','')
    
    if t1.isdigit() and t2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        print("Сумма чисел: ", num1+num2)
    else:
        print("Одно или оба введенных числа не являются целыми числами!")
    str = input ("Нажмите q для завершения программы: " )
    if (str =="q"):
        break
