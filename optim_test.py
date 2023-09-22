"""Модуль для интеграционного тестирования"""

from optim_gen import create_func, take_first
from optim import nelder_mead
import numpy as np


def print_arrays(**kwargs):
    for arg_name in kwargs:
        xx = kwargs[arg_name]
        print(arg_name, end=':')
        for x in xx:
            print("{a:10.2f}".format(a=x), end='')
        print()


def print_results(res, iter, time):
    print("\nФ(x)={a:10.2e}, iterations={b:d}, time={c:5.1f}".format(a=ff(res), b=iter, c=time))

    food_energy_calc = 0
    food_energy_calc += sum(res * food_energy_groups)

    xa, res = take_first(res, len(ka))
    xb, res = take_first(res, len(kb))
    xc, res = take_first(res, len(kc))
    xd, res = take_first(res, len(kd))
    xe, res = take_first(res, len(ke))
    xf, res = take_first(res, len(kf))
    xg, res = take_first(res, len(kg))

    print_arrays(xa=xa, xb=xb, xc=xc, xd=xd, xe=xe, xf=xf, xg=xg)

    print("k_targ={a:12.6f}".format(a=food_energy_targ))
    print("k_calc={a:12.6f}".format(a=food_energy_calc))


KKAL_IN_GR = 0.01

ka = [k * KKAL_IN_GR for k in [68]]
kb = [k * KKAL_IN_GR for k in [343, 360]]
kc = [k * KKAL_IN_GR for k in [170]]
kd = [k * KKAL_IN_GR for k in [52, 89, 48]]
ke = [k * KKAL_IN_GR for k in [654, 553]]
kf = [k * KKAL_IN_GR for k in [259, 366]]
kg = [k * KKAL_IN_GR for k in [40, 159]]
kh = [k * KKAL_IN_GR for k in [15, 18]]
food_energy_targ = 2000

# граммовки продуктов
ga = [200]
gb = [300, 200]
gc = [500]
gd = [200, 200, 150]
ge = [40, 50]
gf = [300, 150]
gg = [1000, 500]
gh = [200, 200]

group_limits_min = np.array([50, 50, 50, 50, 10, 10, 50, 50])
group_limits_max = np.array([200, 200, 300, 200, 30, 30, 200, 150])

food_energy_groups = np.array(ka + kb + kc + kd + ke + kf + kg)
food_limits = np.array(ga + gb + gc + gd + ge + gf + gg)

groups = np.array([len(group) for group in [ka, kb, kc, kd, ke, kf, kg]])

#граммовки продуктов
ga = [500, 360, 400]
gb = [500, 360, 400, 200]
gc = [500, 360, 400, 200]
gd = [500, 360, 400]

# 1
ff = create_func(food_energy_targ,
                 groups,
                 food_energy_groups,
                 group_limits_min,
                 group_limits_max,
                 food_limits,
                 penalty=1e1, penalty_power=2)
x0 = np.zeros((len(ka) + len(kb) + len(kc) + len(kd) + len(ke) + len(kf) + len(kg)))

# x0 = np.random.random_sample(len(ka) + len(kb) + len(kc) + len(kd)) * 100
(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100, stop=400.)
print_results(res, iter, time)

# 2
(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10, stop=400.)
print_results(res, iter, time)

# 3
(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=1, stop=400.)
print_results(res, iter, time)

(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=100)
print_results(res, iter, time)

# 2
(res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10)
print_results(res, iter, time)

# 3
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