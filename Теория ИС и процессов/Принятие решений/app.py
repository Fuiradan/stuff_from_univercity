import numpy as np

def maximax(mas):
    maximum = mas[0][0]
    maxI = 0
    for i in range(len(mas)):
        for j in range(len(mas[i])):
            if (mas[i][j] > maximum):
                maximum = mas[i][j]
                maxI = i
    return maxI


def Vald(mas):
    maxmin = mas[0][0]
    minI = 0
    for i in range(len(mas)):
        tmp = min(mas[i])
        maxmin = max(tmp, maxmin)
        if (maxmin == tmp):
            minI = i
    return minI

def Savidge(mas):
    minmax = max(mas[0])
    minI = 0
    for i in range(len(mas)):
        tmp = max(mas[i])
        minmax = min(tmp, minmax)
        if (minmax == tmp):
            minI = i
    return minI


def Hurwicz(mas):
    minI = 0
    p = 0.4
    msum = -1
    for i in range(len(mas)):
        summa = min(mas[i])*p + (p-1)*max(mas[i])     
        msum = max(summa, msum)
        if (msum == summa):
            minI = i
    return minI

def create_risks(mas):
    mas = mas.transpose()
    m = []
    for i in range(len(mas)):
        t = max(mas[i])
        tmp = []
        for j in range(len(mas[i])):
            tmp.append( t -mas[i][j])
        m.append(tmp)
    m = np.array(m)    
    m = m.transpose()
    return m


profit = np.array([[300, 300, 300, 300], [100, 450, 450, 450], [-100, 390, 600, 600], [-300, 190, 400, 610]])
risks = create_risks(profit)
print('Матрица доходов:\n',profit)
print('Матрица рисков:\n', risks)
print('Критерий "максимакс": альтернатива ', maximax(profit)+1)
print('Критерий Вальда: альтернатива ', Vald(profit)+1)
print('Критерий Сэвиджа: альтернатива ', Savidge(risks)+1)
print('Критерий Гурвица: альтернатива ', Hurwicz(profit)+1)
