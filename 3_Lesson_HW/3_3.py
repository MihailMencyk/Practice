#  В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#  В случае с английским алфавитом очки распределяются так:
#  A, E, I, O, U, L, N, S, T, R – 1 очко; 
#  D, G – 2 очка; 
#  B, C, M, P – 3 очка; 
#  F, H, V, W, Y – 4 очка; 
#  K – 5 очков; 
#  J, X – 8 очков; 
#  Q, Z – 10 очков. 
#  А русские буквы оцениваются так: 
#  А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#  Д, К, Л, М, П, У – 2 очка; 
#  Б, Г, Ё, Ь, Я – 3 очка; 
#  Й, Ы – 4 очка; 
#  Ж, З, Х, Ц, Ч – 5 очков; 
#  Ш, Э, Ю – 8 очков; 
#  Ф, Щ, Ъ – 10 очков. 
#  Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
#  Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

word = str(input('Введите слово: '))
A1 = "AEIOULNSTRАВЕИНОРСТ" # 1 очко
A2 = "DGДКЛМПУ"  #2 очка
A3 = "BCMPБГЁЬЯ"  #3 очка
A4 = "FHVWYЙЫ"  #4 очка
A5 = "KЖЗХЦЧ"  #5 очков
A8 = "JXШЭЮ"  #8 очков
A10 = "QZФЩЪ"  #10 очков
print(word)
Word = word.upper()
s1 = sum([A1.count(Word[i])*1 for i in range(len(Word))])
s2 = sum([A2.count(Word[i])*2 for i in range(len(Word))])
s3 = sum([A3.count(Word[i])*3 for i in range(len(Word))])
s4 = sum([A4.count(Word[i])*4 for i in range(len(Word))])
s5 = sum([A5.count(Word[i])*5 for i in range(len(Word))])
s8 = sum([A8.count(Word[i])*8 for i in range(len(Word))])
s10 = sum([A10.count(Word[i])*10 for i in range(len(Word))])
print(s1+s2+s3+s4+s5+s8+s10)
