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


def column(value, x, color):
    """
        Аргументы - значение элемента массива, положение на экране по оси Х.
        Отрисовка колонки высотой, зависящей от значения.
    """
    turtle.penup()
    turtle.goto(x, -300)
    turtle.pendown()
    turtle.pencolor('black')
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(value*5)
        turtle.left(90)
    turtle.end_fill()

def hoar_sort(A, xlr):
    if len(A) <= 1:
        return
    sr_znach = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < sr_znach:
            L.append(x)
        elif x == sr_znach:
            M.append(x)
        if x > sr_znach:
            R.append(x)
    xl = xlr
    xr = xlr+len(L)+len(M)
    clear_column(100, (-2 - 20) * 20)
    column(M[0], (-2 - 20) * 20, 'Aquamarine3')
    for x in L + M:
        if x in L:
            color = ('khaki1')
        if x in M:
            color = ('Aquamarine3')
        clear_column(100, (xlr - 20) * 20)
        column(x, (xlr - 20) * 20, color)
        xlr += 1
    if len(R) == 1:
        clear_column(100, (xlr - 20) * 20)
        column(R[0], (xlr - 20) * 20, 'khaki1')
    hoar_sort(L, xl)
    hoar_sort(R, xr)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

my_list = [i for i in range(15, 95, 2)]
random.shuffle(my_list)
turtle.Screen().setup(950, 700)
turtle.showturtle()
turtle.speed(0)

turtle.penup()
turtle.goto(-435, -320)
turtle.pendown()
turtle.write('барьер', align='Center')

for i in range(len(my_list)):
    column(my_list[i], (i - 20) * 20, 'khaki1')

hoar_sort(my_list, 0)

turtle.done()
