# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите кол-во монет лежащих на столе: '))
sum = 0
for i in range(n):
    side = int(input('Введите 1 - если ОРЕЛ, 0 - если решка: '))
    if side == 0:
        sum+=1
if (n-sum) > sum:
    print (sum)
else:
    print (n-sum)