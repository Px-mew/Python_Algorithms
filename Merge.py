import turtle
import random
"""
    Алгоритм сортировки слиянием с визуализацией
"""

def clear_column(value, x):
    """
        Аргументы - значение элемента массива, положение на экране по оси Х.
        Удаление колонки.
    """
    turtle.penup()
    turtle.goto(x, -300)
    turtle.pendown()
    turtle.Screen().colormode(255)
    turtle.pencolor(255, 255, 255)
    turtle.fillcolor(255, 255, 255)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(value*5)
        turtle.left(90)
    turtle.end_fill()


def column(value, x):
    """
        Аргументы - значение элемента массива, положение на экране по оси Х.
        Отрисовка колонки высотой, зависящей от значения.
    """
    turtle.penup()
    turtle.goto(x, -300)
    turtle.pendown()
    turtle.Screen().colormode(255)
    turtle.pencolor(0, 0, 0)
    turtle.fillcolor(100 + value, 200 - value, value * 2)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(value*5)
        turtle.left(90)
    turtle.end_fill()


def merge(my_list, left, mid, right):
    """
        Аргументы функции:
        - массив;
        - индекс элемента начала первой части массива для слияния;
        - индекс элемента начала второй части массива для слияния;
        - индекс последнего элемента второй части массива для слияния.
        Две части массива "сливаются" в одну в порядке возрастания.
        Изменения записываются в исходный массив.
    """
    left_list = my_list[left:mid]
    right_list = my_list[mid:right]
    sort_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] < right_list[0]:
            sort_list.append(left_list.pop(0))
        else:
            sort_list.append(right_list.pop(0))
    sort_list += left_list + right_list
    for i, item in zip(range(left, right), sort_list):
        if my_list[i] != item:
            clear_column(my_list[i], (i - 20) * 20)
            column(item, (i - 20) * 20)
    my_list[left:right] = sort_list[:]


def sort_merge(my_list, left, right):
    """
        Аргументы функции: массив, индекс первого элемента для обработки,
        длина обрабатываемой части.
        Разделение массива на малые части: рекурсивное делиние пополам,
        пока не останется 1 элемент в подмассиве.
        Вызов функции "слияние" (merge)
    """
    if left + 1 >= right:
        return
    mid = (left + right) // 2
    sort_merge(my_list, left, mid)
    sort_merge(my_list, mid, right)
    merge(my_list, left, mid, right)


my_list = [i for i in range(15, 95, 2)]
random.shuffle(my_list)

turtle.Screen().setup(950, 700)
turtle.showturtle()
turtle.speed(0)

for i in range(len(my_list)):
    column(my_list[i], (i - 20) * 20)

sort_merge(my_list, 0, len(my_list))

turtle.done()
