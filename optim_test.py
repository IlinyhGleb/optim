"""Модуль для интеграционного тестирования"""

from optim_gen import create_func, create_func_2, take_first
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
    xa, res = take_first(res, len(ka))
    xb, res = take_first(res, len(kb))
    xc, res = take_first(res, len(kc))
    xd, res = take_first(res, len(kd))

    # a, res = take_first(res, len(ka))
    # b, res = take_first(res, len(kb))
    # c, res = take_first(res, len(kc))
    # d, res = take_first(res, len(kd))
    # print("xa*100:", "\t".join([str(x*100) for x in xa]))
    # print("xb*100:", "\t".join([str(x*100) for x in xb]))

    print()
    print_arrays(xa=xa, xb=xb, xc=xc, xd=xd)

    k_calc = 0
    k_calc += sum([xi * ki for xi, ki in zip(xa, ka)])
    k_calc += sum([xi * ki for xi, ki in zip(xb, kb)])
    k_calc += sum([xi * ki for xi, ki in zip(xc, kc)])
    k_calc += sum([xi * ki for xi, ki in zip(xd, kd)])

    print("\nk_targ={a:12.6f}".format(a=k_targ))
    print("k_calc={a:12.6f}".format(a=k_calc))


KKAL_IN_GR = 0.01

# nelder_mead(f, (xa, xb, xc, xd, a, b, c, d))
ka = [k * KKAL_IN_GR for k in [260, 300, 280]]
kb = [k * KKAL_IN_GR for k in [400, 600, 550, 450]]
kc = [k * KKAL_IN_GR for k in [50, 20, 30, 23]]
kd = [k * KKAL_IN_GR for k in [20, 10, 10]]
k_targ = 2000
a_min = 50
a_max = 200
b_min = 50
b_max = 500
c_min = 50
c_max = 500
d_min = 50
d_max = 500

#граммовки продуктов
ga = [500, 360, 400]
gb = [500, 360, 400, 200]
gc = [500, 360, 400, 200]
gd = [500, 360, 400]

# 1
#ff = create_func_2(k_targ, ka, kb, kc, kd, a_min, a_max, b_min, b_max, c_min, c_max, d_min, d_max, k=1e1, p=2)
#новые входные данные для функции
ff = create_func_2(k_targ, ka, kb, kc, kd, a_min, a_max, b_min, b_max, c_min, c_max, d_min, d_max, ga, gb, gc, gd, k=1e1, p=2)
x0 = np.zeros((len(ka) + len(kb) + len(kc) + len(kd)))  # *2
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