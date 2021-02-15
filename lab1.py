import random

# задання довільно вибраних коефіцієнтів
a0 = 2
a1 = 4
a2 = 1
a3 = 3

# порожні списки для х1, х2, х3 i y
x1 = []
x2 = []
x3 = []

max_1 = 0
max_2 = 0
max_3 = 0

xn1 = []
xn2 = []
xn3 = []

# генератор списку
def generation(generatedList):
    for i in range(8):
        r = random.randint(1, 20)
        generatedList.append(r)
        i += 1
    return generatedList

# генерація х1, х2, х3
x1 = generation(x1)
x2 = generation(x2)
x3 = generation(x3)

# обчислення у
def counting_of_y(x_1, x_2, x_3):
    return a0 + a1 * x_1 + a2 * x_2 + a3 * x_3

y = [counting_of_y(x1[i], x2[i], x3[i]) for i in range(8)]

# значення х0і
x01 = (max(x1) + min(x1)) / 2
x02 = (max(x2) + min(x2)) / 2
x03 = (max(x3) + min(x3)) / 2


dx1 = x01 - min(x1)
dx2 = x02 - min(x2)
dx3 = x03 - min(x3)


xn1 = [(x1[i] - x01)/dx1 for i in range(8)]
xn2 = [(x2[i] - x02)/dx2 for i in range(8)]
xn3 = [(x3[i] - x03)/dx3 for i in range(8)]

y_et = counting_of_y(x01, x02, x03)

# 233 вар
result_optional_value = [(y[k] - y_et) ** 2 for k in range(8)]
optional_value = max(result_optional_value)

# 201 var
# optional value
# k = 100
# for i in range(len(y)):
#    if y[i] > y_average and y[i] < k:
#       k = y[i]

# output
print("Кількість дослідів -- ", len(y))
print("Коефіцієнти : a0 = %s, a1 = %s, a2 = %s, a3 = %s"%(a0, a1, a2, a3))
print("-------------------------------------------------------")
print("X1 = ", x1)
print("X2 = ", x2)
print("X3 = ", x3)
print("-------------------------------------------------------")
print("List of x0: %s %s %s"%(x01, x02, x03))
print("-------------------------------------------------------")
print("Y", y)
print("List of dx: %s %s %s"%(dx1, dx2,dx3))
print("-------------------------------------------------------")
print("List of xn:")
print("Xn1", xn1)
print("Xn2", xn2)
print("Xn3", xn3)
print("-------------------------------------------------------")
print("Еталонне значення у :", y_et)
print("max(Y-Yэт)²: ", optional_value)
