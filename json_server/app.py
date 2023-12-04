from flask import Flask, request, jsonify
from optim import create_func, nelder_mead
import numpy as np
import sqlite3
from itertools import groupby

KKAL_IN_GRAMMS = 0.01

app = Flask(__name__)


def flatten(list_of_lists):
    '''превращает двухмерный массив (список списков) в одномерный массив (список)'''
    return [item for sublist in list_of_lists for item in sublist]


def array_multiply_by_number(ar: list, num: float):
    '''умножает все элементы массива (списка списков) на скалярное число'''
    return [[el * num for el in row] for row in ar]


def table_groupby(table, valnum=1, keynum=0):
    '''группирует данные в столбце №valnum в кортежи по столбцу (ключу) №keynum'''
    return [tuple(val[valnum] for val in group) for key, group in groupby(table, key=lambda x: x[keynum])]


@app.route('/optim', methods=['POST'])
def get_optim_solu():
    data = request.get_json()
    food_energy_goal = data['food_energy_goal']
    ref_id = 1

    connection = sqlite3.connect('./json_server/refrigerator.db')
    cursor = connection.cursor()

    # обращение к базе данных
    # калорийность + граммовки
    cursor.execute(
        'SELECT category_id, caloricity, amount '
        'FROM refrigerator_has_product JOIN product USING(product_id) '
        'WHERE refrigerator_id = ?'
        'ORDER BY category_id ',
        (ref_id,))
    groups = cursor.fetchall()

    # ограничения групп
    cursor.execute('SELECT min, max FROM limits ORDER BY category_id')
    limits = cursor.fetchall()
    connection.close()

    # постановка задачи оптимизации
    # калорийность продуктов
    food_energy_groups = table_groupby(groups, 1, 0)
    food_energy_groups = array_multiply_by_number(food_energy_groups, KKAL_IN_GRAMMS)

    # граммовки продуктов
    food_quantity_groups = table_groupby(groups, 2, 0)

    # ограничения групп
    group_limits_min = np.array([sublist[0] for sublist in limits])
    group_limits_max = np.array([sublist[1] for sublist in limits])

    food_energy_groups_array = np.array(flatten(food_energy_groups))
    food_limits_array = np.array(flatten(food_quantity_groups))

    groups_array = np.array([len(group) for group in food_energy_groups])

    ff = create_func(food_energy_goal,
                     groups_array,
                     food_energy_groups_array,
                     group_limits_min,
                     group_limits_max,
                     food_limits_array,
                     penalty=1e1, penalty_power=2)
    x0 = np.zeros(len(food_energy_groups_array))

    (res, iter), time = nelder_mead(ff, x0, gamma=2, maxiter=20000, dx=10)
    print(iter)
    return jsonify({'result': res.tolist()})


if __name__ == '__main__':
    app.run(debug=True)
