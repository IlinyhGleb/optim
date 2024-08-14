
"""Модуль для тестирования скорости функции оптимизации
При тестировании нужно создать новую функцию nelder_mead_new с которой будет вестись сравнение функции nelder_mead"""

import timeit

setup_code_function = """
from optim import nelder_mead as nelder_mead
import numpy as np
import time
x0 = np.array([0,0])
num = 0
"""

simplified_setup_code_function = """
from optim import nelder_mead_new as nelder_mead
import numpy as np
x0 = np.array([0,0])
num = 0
"""

test_code_fast_function = """
def f(vect):
    #print(True)
    x = vect[0]
    y = vect[1]
    return 1.75*(x - 3)**2 + 3.25*(y - 2)**2 + 1.5*(3)**0.5*(x - 3)*(y - 2)
nelder_mead(f, x0)
"""

test_code_slow_function = """
def f(vect):
    #print(True)
    x = vect[0]
    y = vect[1]
    time.sleep(0.00001)
    return 1.75*(x - 3)**2 + 3.25*(y - 2)**2 + 1.5*(3)**0.5*(x - 3)*(y - 2)
nelder_mead(f, x0)
"""

if __name__ == "__main__":
    repeat = 5
    number = 100
    times = timeit.repeat(stmt=test_code_fast_function, setup=setup_code_function, repeat=repeat, number=number)
    print(f"nelder_mead: Среднее время выполнения быстрой функции: {sum([time/number for time in times])/repeat} секунд")

    times = timeit.repeat(stmt=test_code_slow_function, setup=setup_code_function, repeat=repeat, number=number)
    print(f"nelder_mead: Среднее время выполнения медленной функции: {sum([time/number for time in times])/repeat} секунд")

    times = timeit.repeat(stmt=test_code_fast_function, setup=simplified_setup_code_function, repeat=repeat, number=number)
    print(f"nelder_mead_new: Среднее время выполнения быстрой функции: {sum([time/number for time in times])/repeat} секунд")

    times = timeit.repeat(stmt=test_code_slow_function, setup=simplified_setup_code_function, repeat=repeat, number=number)
    print(f"nelder_mead_new: Среднее время выполнения медленной функции: {sum([time/number for time in times])/repeat} секунд")

# Среднее время выполнения быстрой функции: 0.0015651420000358483 секунд
# Среднее время выполнения медленной функции: 0.299948602000004 секунд
# Новый optim: Среднее время выполнения быстрой функции: 0.0014880239999183686 секунд
# Новый optim: Среднее время выполнения медленной функции: 0.25174532399993044 секунд
