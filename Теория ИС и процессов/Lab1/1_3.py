import math
import random


class dot:
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m
    def radius(self, x, y):
        return math.sqrt((self.x-x)**2 + (self.y-y)**2)



def inertia(mas):
    J = 0
    print("Введите координаты оси системы:")
    x = float(input())
    y = float(input())
    for i in range(len(mas)):
        r = mas[i].radius(x, y)
        J = J + mas[i].m * r**2
    print("Момент системы материальный точек относительно оси (", x, ";", y, ") равен ", J)

def center(mas):
    xc = 0
    yc = 0
    mc = 0
    for i in range(len(mas)):
        xc = xc + mas[i].m*mas[i].x
        yc = yc + mas[i].m*mas[i].y
        mc = mc + mas[i].m
    print("Координаты центра масс системы: ( ", xc/mc, "; ", yc/mc, ")")

def circle_invertion(mas):
    print("Введите координтаты центра окружности:")
    print("x = ")
    x0 = float(input())
    print("y = ")
    y0 = float(input())
    print("Введите радиус окружности: ")
    print("R = ")
    R = float(input())
    m = []
    for i in range(len(mas)):
        t = R**2/((mas[i].x - x0)**2 + (mas[i].y - y0)**2)
        x = x0 + t * (mas[i].x - x0)
        y = y0 + t * (mas[i].y - y0)
        point= dot(x, y, mas[i].m)
        m.append(point)
    return m


def line_invertion(mas):
    m = []
    print("Введите коэффициенты канонического уравнения прямой")
    print("A = ")
    A = float(input())
    print("B = ")
    B = float(input())
    print("C = ")
    C = float(input())
    for i in range(len(mas)):
        x = (-A*C/B-A*mas[i].y+B*mas[i].x)/(B + A**2/B)
        y = (-A*x-C)/B
        x = 2 * x - mas[i].x
        x = 2 * y - mas[i].y
        point = dot(x, y, mas[i].m)
        m.append(point)
    return m


def dot_invertion(mas):
    m = []
    print("Введите точку симметрии")
    print("x = ")
    x0 = float(input())
    print("y = ")
    y0 = float(input())
    for i in range(len(mas)):
        x = 2*x0 - mas[i].x
        y = 2*y0 - mas[i].y
        point = dot(x, y, mas[i].m)
        m.append(point)
    return m

def output(mas):
	for i in range(len(mas)):
		print(i+1, " точка. Координаты (", mas[i].x, "; ", mas[i].y, ")")
	
	
	
print("Введите количество точек:")
n=int(input())
a = []
for i in range(n):
    print('Координаты ', i+1, ' точки:')
    x = random.uniform(-10, 10)
    print('x=', x)
    y = random.uniform(-10, 10)
    print('y= ', y)
    m = random.uniform(0, 10)
    print('Масса данной точки: ', m)
    point = dot(x, y, m)
    a.append(point)

inertia(a)
center(a)
dot_inv = dot_invertion(a)
line_inv = line_invertion(a)
circle_inv = circle_invertion(a)

# Вывод 

print("Результаты инверсии относительно точки:")
output(dot_inv)
print("Результаты инверсии относительно прямой:")
output(line_inv)
print("Результаты инверсии относительно окружности:")
output(circle_inv)


