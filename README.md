# OPTIM

- optim.py - Модуль содержит методы оптимизации

- optim_gen.py - Модуль формирования целевых функций (включая штрафные)

- optim_test.py - Модуль для интеграционного тестирования (запускаем для тестов его)

## Использование:
```python
from optim import nelder_mead

function = lambda x: x[0]**2+(x[1]-2)**2+x[2]**2
x0 = [1.0, 1.0, 1.0]

(xmin, iters), time = nelder_mead(function, x0)
print(f"Получен экстремум {xmin} за {iters} итераций и {time} секунд")
```

