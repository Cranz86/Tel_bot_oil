import json

ar = []     #пустой список

with open('mat.txt', encoding='utf-8') as r:
    for i in r:     #по-строчно проходим циклом
        n = i.lower().split('\n')[0]        #перевод в нижний регистор
        if n != '':     #проверка пустой строки
            ar.append(n)

with open('mat.json', 'w', encoding='utf-8') as e:      #открываем для чтения в кодировке утф-8
    json.dump(ar, e)        #из модуля json используем функцию dump которая позволяет записать данные, передаём как аргумент список из слов