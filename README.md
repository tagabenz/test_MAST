После запуска скрипт берет в спике последнего умершего и отправляет данные на почту, затем каждые 10 секунд проверяет на появление новых умерших.

В качетсве демонизации скрипта использовалась библиотека APScheduler.

Для запуска необходимо в файле email.ini указать параметры (для gmail.com вместо пароля необходимо использовать 16-ти значный App passwords).

`python3 main.py`