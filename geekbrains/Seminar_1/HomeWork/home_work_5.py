# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A(3, 6)
# B(2, 1) -> 5, 09
# - A(7, -5)
# B(1, -1) -> 7, 21

print('Точка А:')
x_a = float(input('X = '))
y_a = float(input('Y = '))

print('Точка B:')
x_b = float(input('X = '))
y_b = float(input('Y = '))

# Стандартное округление работает криво, поэтому делаем через строку:
distance = str(((x_a - x_b) ** 2 + (y_a - y_b) ** 2) ** 0.5) \
    .split('.', maxsplit=1)

print(f'Расстояние между точками: {distance[0]},{distance[1][0:2]}')