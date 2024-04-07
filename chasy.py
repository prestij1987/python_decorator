'''Домащнее задание:

Создать функцию.
Она возвращает "песочные часы" заданного размера.
Потом их можно напечатать.
Например, для 10:

**********
 *      *
  *    *
   *  *
    **
   *  *
  *    *
 *      *
**********

Кому сложно, напечатайте прямоугольник

Создать декоратор.
Он перед часами пишет:
"Смотрите, как я могу!"
А после часов:
"Правда, красиво?"'''

kolvo = 5

def main(kolvo): # Создаем основную функцию
    storona_1 = kolvo * ' * '
    storona_2 = kolvo * ' * '
    for i in storona_1(range(kolvo, 10)):
        chast1 = (" " * (storona_1 - i) + "*" * (2 * i - 1))
        print(chast1)    
    
    for it in storona_2(range()):

        print(chast1)
        for i in range(2, it+ 1):  # Нижняя часть песочных часов
            chast2 = (" " * (it - i) + "*" * (2 * i - 1)) 
            print(chast2)
        full = chast1, chast2
        return full

main(kolvo)


def decorator_function(func):
    def func_add():
        print("Первая функция")
        print("Cмотри как я могу {}".format(func))
       
        func1 = func()
        print("Правда красиво")
        return func1
 
    return func_add
@decorator_function
def first_decorator():
    print("Часы готовы")

first_decorator()