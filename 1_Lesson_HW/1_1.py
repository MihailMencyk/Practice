# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input("Vvedite 3-ex znachnoe chislo: "))
if n<100 or n>999:
    print('Chislo NE 3-ex znacnoe, povtorite popytku')
else:
    a = n//100
    b = (n//10)%10
    c = n%10
    sum = a+b+c
    print(sum)