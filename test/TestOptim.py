"""Модуль содержит тесты модуля оптимизации"""

import pytest
import numpy as np
from optim import nelder_mead


class Test_Optim:
    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    @pytest.mark.positive
    @pytest.mark.nelder_mead
    @pytest.mark.parametrize("input_data,expected_result",
                             [((lambda x: x[0]**2+(x[1]-2)**2+x[2]**2, np.array([1.0, 1.0, 1.0])),
                               np.array([0.0, 2.0, 0.0])),
                              ((lambda x: (1-x[0])**2 + 100*(x[1]-x[0]**2)**2, np.array([1.0, 1.0, 1.0])),
                               np.array([1.0, 1.0, 1.0])),
                              ((lambda x: x[0]+x[1]+1e5*sum([max(-y, 0)**2 for y in x]), np.array([1.0, 1.0])),
                               np.array([0.0, 0.0])),
                              ])
    def test_nelder_mead(self, input_data, expected_result):
        EPS = 1e-5
        ff = input_data[0]
        x0 = input_data[1]

        (xmin, iters), time = nelder_mead(ff, x0)
        actual_result = xmin

        assert np.all(abs(actual_result - expected_result) <= EPS)

    @pytest.mark.positive
    @pytest.mark.nelder_mead
    @pytest.mark.parametrize("input_data,expected_result",
                             [((lambda x: x[0]**2+(x[1]-2)**2+x[2]**2, [1.0, 1.0, 1.0]),
                               [0.0, 2.0, 0.0]),
                              ])
    def test_nelder_mead_without_numpy(self, input_data, expected_result):
        EPS = 1e-5
        ff = input_data[0]
        x0 = input_data[1]

        (xmin, iters), time = nelder_mead(ff, x0)
        actual_result = xmin

        assert np.all(abs(actual_result - expected_result) <= EPS)