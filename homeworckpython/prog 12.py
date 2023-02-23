f(x) = -12x4sin(cos(x)) - 18x3 + 5x*2 + 10x - 30

import numpy as np
import matplotlib.pyplot as plt
limit = 10
step = 0.01
color = 'b'
line_s = '-'
direct_up = True
x = np.arange(-limit, limit, step)
def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color
def switch_line():
    global line_s
    if line_s == '-':
        line_s = '--'
    else:
        line_s = '-'
    return line_s
a, b, c, d, e = -12, -18, 5, 10, 30
def func(x):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x - e
    
x_change = [(-limit, 'limit')]
for i in range(len(x) - 1):
    if (func(x[i]) > 0 and func(x[i + 1]) < 0) or (func(x[i]) < 0 and func(x[i + 1]) > 0):
        x_a = np.arange(x[i], x[i+1], 0.0000001)
        for j in range(len(x_a) - 1):
            if (func(x_a[j]) > 0 and func(x_a[j + 1]) < 0) or (func(x_a[j]) < 0 and func(x_a[j + 1]) > 0):
                x_change.append((x_a[j] if abs(0 - x_a[j]) < abs(0 - x_a[j+1]) else x_a[j+1], 'zero'))
    if direct_up:
        if func(x[i]) > func(x[i + 1]):
            x_a = np.arange(x[i], x[i + 1], 0.0000001)
            for j in range(len(x_a) - 1):
                if func(x_a[j]) > func(x_a[j + 1]):
                    x_change.append((x_a[j], 'direct'))
                    direct_up = False
                    break
    else:
        if func(x[i]) < func(x[i + 1]):
            x_a = np.arange(x[i], x[i + 1], 0.0000001)
            for j in range(len(x_a) - 1):
                if func(x_a[j]) < func(x_a[j + 1]):
                    x_change.append((x_a[j], 'direct'))
                    direct_up = True
                    break

x_change.append((limit, 'limit'))

print(x_change)
[(-10, 'limit'), (-9.978953800006359, 'direct'), (-7.650622199973752, 'zero'), (-6.830000000000068, 'direct'), (-5.026865899991317, 'zero'), (-4.1677834999939085, 'direct'), (-1.3389665999995812, 'zero'), (-0.39000000000020485, 'direct'), (0.45457359999990876, 'direct'), (1.7006073000001052, 'direct'), (2.2730567999947358, 'zero'), (3.8199999999997054, 'direct'), (4.383523600009575, 'zero'), (7.001031700002531, 'direct'), (8.035164099968233, 'zero'), (9.879999999999576, 'direct'), (10, 'limit')]
for i in range(len(x_change) - 1):
    cur_x = np.arange(x_change[i][0], x_change[i + 1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct','limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]

roots = []
for x in x_change:
    if x[1] == 'zero':
        roots.append(str(round(x[0], 2)))
        plt.plot(x[0], func(x[0]), 'gx')

plt.plot(min_x, min_y, 'yo', label=f'Экстремум функции на промежутке [{-limit};{limit}]: ({round(min_x, 2)}, {round(min_y, 2)})')

plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {", ".join(roots)}')
plt.legend()
plt.show()
