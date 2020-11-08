###  Лабораторна 2
***

1) Була створена папка з назвою лабораторної роботи у власному репозиторію ,ініціалізоване середовище pipenv та встановлені необхідні пакети.

        pipenv --python 3.8
        pipenv install django

2) За допомогою Django Framework створила заготовку проекту та винесла всі створені файли на один рівень вище :

        pipenv run django-admin startproject site_lab3
    
        mv site_lab3/site_lab3/* site_lab3/
        mv site_lab3/manage.py ./

3) Переконалась що все встановилось правильно:

        pipenv run python manage.py runserver      
    Результат:

        November 08, 2020 - 10:48:03
        Django version 3.1.3, using settings 'site_lab3.settings'
        Starting development server at http://127.0.0.1:8000/
        Quit the server with CONTROL-C.

4) Створений коміт з базовим темплейтом сайту.
