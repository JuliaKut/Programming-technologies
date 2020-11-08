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
5) Cтворила темплейт додатку та коміт із новоствореними
 файлами темплейту додатка:

        pipenv run python manage.py startapp main
6) Створила потрібні папки та файли.
7) Вказала Django frameworks його назву додатку (main) 
та де шукати веб сторінки. 
8) Cтворила сторінки двох типів - перша буде зчитуватись 
з .html темплейта. друга сторінка буде просто повертати
 відповідь у форматі JSON; 
9)  
    Результат 1 сторінка:
 
        You are at main page. Hello world
        
        test test2 test3 
    Результат 2 сторінка:
    
        {"date": "test1", "current_page": "test2", "server_info": "test3", "client_info": "test4"}  
10) Все працює , коміт виконано.        
        

