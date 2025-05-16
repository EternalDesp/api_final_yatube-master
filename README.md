# api_final
api final

Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке, развернуть виртуальное окружение

python -m venv venv

Активировать виртуальное окружение:

venv/Scripts/acitavte - Windows
source venv/bin/activate - Linux/macOS

Установить зависимости:

pip install -r requirements.txt

Перейти в папку, содержащую файл manage.py:

cd yatube_api

Выполнить миграции:

python manage.py makemigrations

python manage.py migrate

Запустить сервер:

python manage.py runserver



