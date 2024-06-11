# n = None
# print(n)

# n = 'jdsh'
# n1 = "sdjhj"
# print(n)

# n = 5
# print(type(n))

# n = 'djhdj\' kdjsk'
# print(n)

# n = 'sd"ksdl"isdhf'
# print(n)

# a = 5
# b = 5.89
# c = 'Hello'
# print("{} - {} - {}".format(a,b,c))

# print("Введите первую строку")
# a = input()
# print(a)
# Второй способ ввода

# print("Введите первую строку")
# a = input()
# b = input('Введите второе число')

# c = 1
# print(type(c))
# c = str(c)
# print(type(c))

# print("Введите первую строку")
# a = int(input())
# b = int(input('Введите второе число '))

# print(a + b )


# a = 5.89564
# b = 7.98564
# print(round(a*b, 2))

# a = 1 > 4 
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2 
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Введите имя ')
# if username == 'Дастан':
#     print('Ура, это же Дастан!')
# elif username == 'Арман':
#     print('Я так ждал вас, Арман')
# elif username == 'Турарбек':
#     print('Турарбек - топ')
# else:
#     print('АссалямуА\'лейкум, ', username)

# Цикл While
# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
#     print(summa)

# i = 0 
# while i < 5:
#     if i == 3:
#         break
#     i += 1
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(i)

# i = 0 
# while i < 5:
#         i += 1
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(i)

# n = int(input("Введите число "))
# flag = True
# i = 2 
# while flag == True:
#     if n % i == 0:
#         flag = False
#         print(i)
#     elif i > n // 2:
#         print(n)
#         flag = False
#         i += 1

# r = range(5)
# r = range (2,5)
# r = range (0,-5)
# r = range (1,10, 2)
# r = range (100,0,-20)

# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СьЕШЬ еще этих МяГких французских булок'
# print(len(text))
# print ('еще' in text)
# print(text.lower())
# print(text.upper())
# print(text.replace('еще',"ЕЩЕ"))

text = 'СьЕШЬ еще этих МяГких французских булок'
# print(text[0]) # с
# print(text[1]) # ь
# print(text[len(text) - 1]) # к
# print(text[-5]) # б
# print(text[:]) # СьЕШЬ еще этих МяГких французских булок
# print(text[:2]) #сь
# print(text[len(text) - 2:]) # ок
# print(text[2:9]) # ешь еще
# print(text[6:-18]) # еще этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# print(text[2:9] + text[-5] + text [:2]) # ешь ещебсь