import random
import math

maxX = []
max_prisp = 0
gener_number = 1
prisposob = []
stock = []
summa = 0
disp = 0
GENS = 10
POPULATION = 10


def result(mas):
    global max_prisp, maxX
    maximum = max(prisposob)
    maxpos = prisposob.index(maximum)
    if (max_prisp < maximum):
        max_prisp = maximum
        maxX = mas[maxpos]
    print('[№', gener_number, '] ', mas[maxpos], '[', maximum,']')


def new_gener(mas):
    p1 = False
    p2 = False
    tmp = [[0] for i in range(POPULATION)]
    for i in range(0, POPULATION-1, 2):
        while (p1 == False):
            k = random.uniform(0, 1)
            pos1 = random.randint(0, POPULATION-1)
            if (k < 0.85):
                if (prisposob[pos1] > 0.86*max(prisposob)):
                    p1 = True
                    par1 = mas[pos1]
            else:
                p1 = True
                par1 = mas[pos1]
        while (p2 == False):
            k = random.uniform(0, 1)
            pos2 = random.randint(0, POPULATION-1)
            if (pos1 != pos2):
                if (k < 0.85):
                    if (prisposob[pos2] > 0.86*max(prisposob)):
                        p2 = True
                        par2 = mas[pos2]
                else:
                    p2 = True
                    par2 = mas[pos2]
        crossover(par1, par2)
        tmp[i] = par1
        tmp[i+1] = par2        





        



def func(mas):
    tmp = []
    for i in range(POPULATION):
        W = 0
        for j in range(GENS):
            W = W + mas[i][j]*stock[j]
        if (W>capacity):
            alpha = 1 - math.sqrt(abs(W - capacity)/disp)
        else:
            alpha = 1 - math.sqrt(abs(W - capacity)/capacity)
        tmp.append(alpha)
    return tmp    

def crossover(one, two):
    s = random.randint(0, GENS-2)
    tmp1 = one
    tmp2 = two
    for i in range(s, GENS):
        tmp1[i] = two[i]
        tmp2[i] = one[i]
    one = tmp1
    two = tmp2
    k = random.uniform(0, 1)
    if (k > 0.88):
        mutation(one)
    k = random.uniform(0, 1)
    if (k > 0.88):
        mutation(two)



def mutation(mas):
    k = 0.95
    for j in range(GENS):
        tmp = random.uniform(0, 1)
        if (tmp>=k):
            if (mas[j] == 1):
                mas[j] = 0
            else:
                mas[j] = 1
    return mas



def start_population(mas):
    for i in range(POPULATION):
        for j in range(GENS):
            mas[i][j] = random.randint(0,1)



print('Грузоподъемность:')
capacity = int(input())
for i in range(GENS):
    print('Введите вес ', i+1, '-ой коробки. Осталось ввести ', GENS-i+1, ' значений')
    tmp = int(input())
    summa = summa + tmp 
    stock.append(tmp)
disp = max(capacity, capacity-summa)
m = [[0] * GENS for i in range(POPULATION)]
start_population(m)
prisposob = func(m)
result(m)
while ((max(prisposob) != 1) and (gener_number <= 5000)):
    gener_number = gener_number +1
    new_gener(m)
    prisposob = func(m)
    result(m)

print('Максимально приближенное решение: ', maxX, '[ ', max_prisp,']')





