from flask import Flask, request, jsonify
from optim import create_func, nelder_mead
import numpy as np
import sqlite3

KKAL_IN_GRAMMS = 0.01

app = Flask(__name__)


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def array_multiply_by_number(ar: list, num: float):
    return [[el * num for el in row] for row in ar]


@app.route('/optim', methods=['POST'])
def get_optim_solu():
    data = request.get_json()
    food_energy_goal = data['food_energy_goal']

    connection = sqlite3.connect('./json_server/refrigerator.db')
    cursor = connection.cursor()

    ref_id = 1
    # cursor.execute(
    #     'SELECT refrigerator_id, product_id, caloricity, amount, category_id '
    #     'FROM refrigerator_has_product JOIN product '
    #     'WHERE product_id = id AND refrigerator_id = ?',
    #     (ref_id,))


    cursor.execute(
        'SELECT refrigerator_id, product_id, caloricity, category_id '
        'FROM refrigerator_has_product JOIN product '
        'WHERE product_id = id AND refrigerator_id = ?',
        (ref_id,))
    groups = cursor.fetchall()
    # for group in groups:
    #     print(group)
    # print(len(groups))
    # калорийность продуктов
    food_energy_groups = []
    for i in range(1, 9):
        b = []
        for x in groups:
            if x[3] == i:
                b = np.append(b, x[2])
        food_energy_groups.append(b)

    food_energy_groups = array_multiply_by_number(food_energy_groups, KKAL_IN_GRAMMS)

    # граммовки продуктов
    cursor.execute(
        'SELECT refrigerator_id, product_id, amount, category_id '
        'FROM refrigerator_has_product JOIN  product '
        'WHERE product_id = id AND refrigerator_id = ?',
        (ref_id,))
    groups = cursor.fetchall()

    food_quantity_groups = []
    for i in range(1, 9):
        b = []
        for x in groups:
            if x[3] == i:
                b = np.append(b, x[2])
        food_quantity_groups.append(b)

    # ограничения групп
    cursor.execute('SELECT min, max FROM limits ORDER BY category_id')
    limits = cursor.fetchall()
    connection.close()

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
