a = input("Введите первое число: ")
b = input("Введите второе число: ")
t1=a.replace('-','')
t2=b.replace('-','')
t1=t1.replace('.','')
t2=t2.replace('.','')    
if t1.isdigit() and t2.isdigit():
    a = float(a)
    b = float(b)
    a = int(a)
    b = int(b)
    for i in range(a,b):
        print(i)
else:
    print("Одно или оба введенных числа не являются числами!")
