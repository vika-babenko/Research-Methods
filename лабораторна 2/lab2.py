import random
import math
n_variant = 201
m = 6
y_max = (30 - n_variant) * 10
y_min = (20 - n_variant) * 10

x1_min = -10
x1_max = 50
x2_min = -20
x2_max = 40

xn = [[-1, -1], [-1, 1], [1, -1]]

# середнє значення у
def average_value_of_y(counting_list):
    average_l_y = []
    for i in range(len(counting_list)):
        sum_of_el = 0
        for j in counting_list[i]:
            sum_of_el += j
        average_l_y.append(sum_of_el / len(counting_list[i]))
    return average_l_y

# дисперсія
def dispersion(counting_list):
    d = []
    for i in range(len(counting_list)):
        sum_of_y =0
        for k in counting_list[i]:
            sum_of_y += (k - average_value_of_y(counting_list)[i]) ** 2
        d.append(sum_of_y / len(counting_list[i]))
    return d

# перевірка для кожної пари комбінації
def f_uv(u, v):
    if u >= v:
        return u / v
    else:
        return v / u

# визначник для квадратної матриці n = 3
def determinant(x11, x12, x13, x21, x22, x23, x31, x32, x33):
    det = x11 * x22 * x33 + x12 * x23 * x31 + x32 * x21 * x13 -x13 * x22 * x31 - x32 * x23 * x11 - x12 * x21 * x33
    return det

# генерація у
y = [[random.randint(y_min, y_max) for j in range(6)] for i in range(3)]
average_y = average_value_of_y(y)

# основне відхилення
sigma_teta = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

fuv = []
teta = []
ruv = []

fuv.append(f_uv(dispersion(y)[0], dispersion(y)[1]))
fuv.append(f_uv(dispersion(y)[2], dispersion(y)[0]))
fuv.append(f_uv(dispersion(y)[2], dispersion(y)[1]))

teta.append(((m - 2) / m) * fuv[0])
teta.append(((m - 2) / m) * fuv[1])
teta.append(((m - 2) / m) * fuv[2])

# експериментальне значення критерію Романовського
ruv.append(abs(teta[0] - 1) / sigma_teta)
ruv.append(abs(teta[1] - 1) / sigma_teta)
ruv.append(abs(teta[2] - 1) / sigma_teta)
# візьмемо значення з таблиці при m=6 p=0.90
r_kr = 2

# перевірка гіпотези про однорідність дисперсій
for i in range(len(ruv)):
    if ruv[i] > r_kr:
        print("Неоднорідна дисперсія, потрібно збільшити кількість експериментів")

# позначення для системи рівнянь з коефіцієнтами для лінійної регресії
mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
my = (average_y[0] + average_y[1] + average_y[2]) / 3
# коефіцієнти регресії
a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
a11 = (xn[0][0] * average_y[0] + xn[1][0] * average_y[1] + xn[2][0] * average_y[2]) / 3
a22 = (xn[0][1] * average_y[0] + xn[1][1] * average_y[1] + xn[2][1] * average_y[2]) / 3

# рішення системи з коефіцієнтами регресії методом Крамера
b0 = determinant(my, mx1, mx2, a11, a1, a2, a22, a2, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b1 = determinant(1, my, mx2, mx1, a11, a2, mx2, a22, a3) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
b2 = determinant(1, mx1, my, mx1, a1, a11, mx2, a2, a22) / determinant(1, mx1, mx2, mx1, a1, a2, mx2, a2, a3)
# лінійна регресія(практичне)
y_pr1 = b0 + b1 * xn[0][0] + b2 * xn[0][1]
y_pr2 = b0 + b1 * xn[1][0] + b2 * xn[1][1]
y_pr3 = b0 + b1 * xn[2][0] + b2 * xn[2][1]

# натуралізація плану
dx1 = abs(x1_max - x1_min) / 2
dx2 = abs(x2_max - x2_min) / 2
x10 = (x1_max + x1_min) / 2
x20 = (x2_max + x2_min) / 2
# обчислення натуралізованих коефіцієнтів
a_0 = b0 - (b1 * x10 / dx1) - (b2 * x20 / dx2)
a_1 = b1 / dx1
a_2 = b2 / dx2
# натуралізоване рівняння регресії
yP1 = a_0 + a_1 * x1_min + a_2 * x2_min
yP2 = a_0 + a_1 * x1_max + a_2 * x2_min
yP3 = a_0 + a_1 * x1_min + a_2 * x2_max

print('Матриця планування для m =', m)
for i in range(3):
    print(y[i])

print('Експериментальні значення критерію Романовського:')
for i in range(3):
    print(ruv[i])

print('Натуралізовані коефіцієнти: \na0 =', round(a_0, 4), 'a1 =', round(a_1, 4), 'a2 =', round(a_2, 4))
print('У практичний ', round(y_pr1, 4), round(y_pr2, 4), round(y_pr3, 4),
'\nУ середній', round(average_y[0], 4), round(average_y[1], 4), round(average_y[2], 4))
print('У практичний норм.', round(yP1, 4), round(yP2, 4), round(yP3, 4))