"""Модуль формирования целевых функций (включая штрафные)"""

import numpy as np


def take_first(ar, n):
    """
    разделяет список на два списка размерами [n] и [len(ar)-n]
    """
    return ar[:n], ar[n:]


def create_func(food_energy_goal,
                groups,
                food_energy_groups,
                group_limits_min,
                group_limits_max,
                food_limits,
                penalty=1e3, penalty_power=2):
    """
    создаёт функцию, f(x), где x - список граммовок продуктов, f - целевая функция со штрафами
    """

    result = []
    start = 0
    for i in groups:
        end = start + i
        result.append((start, end))
        start = end

    def groupwise(arr):
        for group in result:
            yield arr[group[0]: group[1]]

    def inner_method(x):
        EPS = 1.0  # Значение, ниже которого второй по величине параметр в группе считается подходящим
        # TODO проверку на неодинаковость размерности

        food_energy_calc = 0
        food_energy_calc += sum(x * food_energy_groups)

        f_res = (food_energy_calc - food_energy_goal)**2

        # ограничения на неотрицательность
        for xi in x:
            f_res += penalty * max(-xi, 0)**penalty_power

        # Ограничения на мин. каждой группы
        for xx, mmin in zip(groupwise(x), group_limits_min):
            f_res += penalty * max(-(sum(xx) - mmin), 0)**penalty_power

        # Ограничения на макс. каждой группы
        for xx, mmax in zip(groupwise(x), group_limits_max):
            f_res += penalty * max(-(mmax - sum(xx)), 0)**penalty_power

        # ограничение на граммовки
        for op in x - food_limits:
            f_res += penalty * max(op, 0)**penalty_power

        # ограничение на один параметр в группе
        for xx in groupwise(x):
            if len(xx) <= 1:
                continue
            xx_new = sorted(xx)
            f_res += penalty * max(xx_new[-2] - EPS, 0)**penalty_power


        #ограничение на граммовки
        for xx, gg in zip([xa, xb, xc, xd], [ga, gb, gc, gd]):
            for xi, gi in zip(xx, gg):
                f_res += k * max(gi - xi, 0) ** p
        return f_res

    return inner_method
