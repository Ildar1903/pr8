sum=0.0
while True:
    n = input("Введите число: ")
    t1=n.replace('-','')
    t1=t1.replace('.','')
    
    if t1.isdigit():
        n = float(n) 
        sum+=n
    str = input ("Нажмите stop или end для завершения программы: " )
    if (str =="stop" or str =="end"):
        print('Сумма чисел равна:',sum)
        break
