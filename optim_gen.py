"""Модуль формирования целевых функций (включая штрафные)"""


def take_first(ar, n):
    return ar[:n], ar[n:]


def create_func(k_targ, ka, kb, kc, kd, a_min, a_max, b_min, b_max, c_min, c_max, d_min, d_max, k=1000, p=2):
    def inner_method(x):
        take_first = lambda ar, n: (ar[:n], ar[n:])

        # TODO проверку на неодинаковость размерности
        xa, x = take_first(x, len(ka))
        xb, x = take_first(x, len(kb))
        xc, x = take_first(x, len(kc))
        xd, x = take_first(x, len(kd))
        a, x = take_first(x, len(ka))
        b, x = take_first(x, len(kb))
        c, x = take_first(x, len(kc))
        d, x = take_first(x, len(kd))

        k_calc = sum([xi * gi * ki for xi, gi, ki in zip(xa, a, ka)])
        k_calc += sum([xi * gi * ki for xi, gi, ki in zip(xb, b, kb)])
        k_calc += sum([xi * gi * ki for xi, gi, ki in zip(xc, c, kc)])
        k_calc += sum([xi * gi * ki for xi, gi, ki in zip(xd, d, kd)])

        f_res = (k_calc - k_targ) ** 2

        for x in [xa, xb, xc, xd, a, b, c, d]:
            f_res += k * sum([max(-y, 0) ** p for y in x])
        for x in [a, b, c, d]:
            f_res += k * sum([max(-y, 0) ** p for y in x])
        for x in [a, b, c, d]:
            f_res += k * sum([max(y-100, 0) ** p for y in x])

        f_res += k * max(-(sum([xi*gi for xi, gi in zip(xa, a)])-a_min), 0) ** p
        f_res += k * max(-(sum([xi*gi for xi, gi in zip(xb, b)])-b_min), 0) ** p
        f_res += k * max(-(sum([xi*gi for xi, gi in zip(xc, c)])-c_min), 0) ** p
        f_res += k * max(-(sum([xi*gi for xi, gi in zip(xd, d)])-d_min), 0) ** p

        f_res += k * max(-(a_max-(sum([xi*gi for xi, gi in zip(xa, a)]))), 0) ** p
        f_res += k * max(-(b_max-(sum([xi*gi for xi, gi in zip(xb, b)]))), 0) ** p
        f_res += k * max(-(c_max-(sum([xi*gi for xi, gi in zip(xc, c)]))), 0) ** p
        f_res += k * max(-(d_max-(sum([xi*gi for xi, gi in zip(xd, d)]))), 0) ** p

        return f_res

    return inner_method


def create_func_2(k_targ, ka, kb, kc, kd, a_min, a_max, b_min, b_max, c_min, c_max, d_min, d_max, ga, gb, gc, gd, EPS=1.0, k=1e3, p=2):
    def inner_method(x):
        #EPS = 1.0 убрали епс в входные параметры # Значение, ниже которого второй по величине параметр в группе считается подходящим
        # TODO проверку на неодинаковость размерности
        xa, x = take_first(x, len(ka))
        xb, x = take_first(x, len(kb))
        xc, x = take_first(x, len(kc))
        xd, x = take_first(x, len(kd))

        k_calc = 0
        k_calc += sum([xi * ki for xi, ki in zip(xa, ka)])
        k_calc += sum([xi * ki for xi, ki in zip(xb, kb)])
        k_calc += sum([xi * ki for xi, ki in zip(xc, kc)])
        k_calc += sum([xi * ki for xi, ki in zip(xd, kd)])

        f_res = (k_calc - k_targ) ** 2

        # ограничения на неотрицательность
        for xx in [xa, xb, xc, xd]:
            f_res += k * sum([max(-xi, 0) ** p for xi in xx])

        # Ограничения на мин. каждой группы
        for xx, mmin in zip([xa, xb, xc, xd], [a_min, b_min, c_min, d_min]):
            f_res += k * max(-(sum([xi for xi in xx]) - mmin), 0) ** p
        # Ограничения на макс. каждой группы
        for xx, mmax in zip([xa, xb, xc, xd], [a_max, b_max, c_max, d_max]):
            f_res += k * max(-(mmax - sum([xi for xi in xx])), 0) ** p

        # ограничение на один параметр в группе
        for xx in [xa, xb, xc, xd]:
            xx_new = sorted(xx)
            f_res += k * max(xx_new[-2]-EPS, 0) ** p


        #ограничение на граммовки
        for xx, gg in zip([xa, xb, xc, xd], [ga, gb, gc, gd]):
            for xi, gi in zip(xx, gg):
                f_res += k * max(gi - xi, 0) ** p
        return f_res

    return inner_method
