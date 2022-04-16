#Создать 3 кортежа(третий это 1 + 2 ) и посчитать нули
# import random
# tuple_1 = tuple([random.randint(0,5) for i in range(10)])
# tuple_2 = tuple([random.randint(-5,0) for i in range(10)])
# tuple_3=tuple_1 + tuple_2
# print(f'{tuple_3}\n количесвто нулей: {tuple_3.count(0)}')

#Запись кортежа в одну строку через запятую без скобок
# a = ('sdf', 'gh', 'gfjhfg', 'ggg')
# c = ' ,'.join(a)
# print(c)

#Сравнить суммы кортежей
# A = (13,5,43,39,67,32,12,98,6,10,34,20,55,68,14,60,14)
# B = (53,21,4,23,76,3,43,12,54,342,21)
# if sum(A) > sum(B):
#     print('Сумма больше в кортеже А')
# elif sum(A) < sum(B):
#     print('Сумма больше в кортеже B')
# else:
#     print('суммы равны')

#Создать кортеж из 10-ти чисел и посчитать сумму
# a = [i for i in range(10)]
# tuple_1 = tuple(a)
# print(f'сумма кортежа = {sum(a)}')

# num_1 = int(input())
# num_2 = int(input())
# list_1 = []
# for i in range(num_1, num_2+1):
#     list_1.append(i)
# tuple_1 = tuple(list_1)
# print(tuple_1)

#Самое большое слово
# words = input()
# max_words = ""
# list_1 = words.split()
# for i in list_1:
#     if len(i)>len(max_words):
#         max_words = i
# print(max_words)

#Преобразовать текст в список с удалением знаков препинания
#from string import punctuation
##print(punctuation)   - список знаков препинания
# words = input()
# for i in words:
#     if i in punctuation:
#         words = words.replace(i, '')
# print(words)


#Словари
#Если распаковывать словарь - распакуются только ключи
