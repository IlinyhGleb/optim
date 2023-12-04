"""Модуль для интеграционного тестирования"""

from optim import create_func, take_first
from optim import nelder_mead
import numpy as np


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def print_results(res, iter, time):
    print("\nФ(x)={a:10.2e}, iterations={b:d}, time={c:5.1f}".format(a=ff(res), b=iter, c=time))

    food_energy_calc = 0
    food_energy_calc += sum(res * food_energy_groups_array)

    result = []
    start = 0
    for i in groups_array:
        end = start + i
        result.append((start, end))
        start = end

    def groupwise(arr):
        for group in result:
            yield arr[group[0]: group[1]]

    reverse_alphabet = sorted(list('abcdefghijklmnopqrstuvwxyz'), reverse=True)

    for xx in groupwise(res):
        letter = reverse_alphabet.pop()
        print(letter + ":", end='')
        for xxx in xx:
            print("{a:10.2f}".format(a=xxx), end='')
        print()

    print("k_goal={a:12.6f}".format(a=food_energy_goal))
    print("k_calc={a:12.6f}".format(a=food_energy_calc))


food_energy_goal = 2000

KKAL_IN_GR = 0.01
food_energy_groups = [
    [k * KKAL_IN_GR for k in [68]],
    [k * KKAL_IN_GR for k in [343, 360]],
    [k * KKAL_IN_GR for k in [170]],
    [k * KKAL_IN_GR for k in [52, 89, 48]],
    [k * KKAL_IN_GR for k in [654, 553]],
    [k * KKAL_IN_GR for k in [259, 366]],
    [k * KKAL_IN_GR for k in [40, 159]],
    [k * KKAL_IN_GR for k in [15, 18]]]

# граммовки продуктов
food_quantity_groups = [
    [200],
    [300, 200],
    [500],
    [200, 200, 150],
    [40, 50],
    [300, 150],
    [1000, 500],
    [200, 200]]

group_limits_min = np.array([50, 50, 50, 50, 10, 10, 50, 50])
group_limits_max = np.array([200, 200, 300, 200, 30, 30, 200, 150])

food_energy_groups_array = np.array(flatten(food_energy_groups))
food_limits_array = np.array(flatten(food_quantity_groups))

groups_array = np.array([len(group) for group in food_energy_groups])

# 1
ff = create_func(food_energy_goal,
                 groups_array,
                 food_energy_groups_array,
                 group_limits_min,
                 group_limits_max,
                 food_limits_array,
                 penalty=1e1, penalty_power=2)
x0 = np.zeros(len(food_energy_groups_array))

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=1, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=1)
print_results(res, iter, time)

x0 = np.random.random_sample(len(food_energy_groups_array)) * 100

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=1, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=1)
print_results(res, iter, time)


# X = np.array(np.linspace(0, 4, 50))
# Y = np.array(np.linspace(0, 4, 50))
# X, Y = np.meshgrid(X, Y)
# Z = ff([X, Y])
#
# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# ax.plot_surface(X, Y, Z)#, vmin=Z.min() * 2)#, cmap=cm.Blues)
# ax.scatter(xk.c()[0], xk.c()[1], func(xk.c()), marker='o', color='Red', s=50)
# plt.show()