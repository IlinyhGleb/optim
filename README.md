# OPTIM

- optim.py - Модуль содержит методы оптимизации

- optim_gen.py - Модуль формирования целевых функций (включая штрафные)

- optim_test.py - Модуль для интеграционного тестирования (запускаем для тестов его)

- json_server - сервер на Flask, принимающий json over http запрос и обрабатывающий его

обратиться к серверу можно с помощью curl:
curl -X POST -H "Content-Type: application/json" -d '{"food_energy_goal": 2000}' http://localhost:5000/optim  