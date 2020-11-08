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
11) Створила файл monitoring.py та встановила бібліотеку

        pipenv install requests
12) Запустила сервер та monitoring.py. 
Все працює коректно.

13) **i.** Модифікувала функцію health

        def health(request):
            now = datetime.now()
            response = {'date': now.strftime("%d/%m/%Y %H:%M:%S"), 'current_page': request.build_absolute_uri(), 'server_info': os.uname(), 'client_info': request.headers['User-Agent']}
            return JsonResponse(response)    
     Результат:
     	
        date	"08/11/2020 15:24:02"
        current_page	"http://127.0.0.1:8000/health/"
        server_info	
        0	"Linux"
        1	"julia-VirtualBox"
        2	"5.4.0-52-generic"
        3	"#57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020"
        4	"x86_64"
        client_info	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0"                 
      **іі.** Дописала функціонал який буде виводити 
      повідомлення про недоступність сайту у 
      випадку якщо WEB сторінка недоступна:
      
            def main(url):
                try:
                    r = requests.get(url)
                    data = json.loads(r.content)
                    logging.info("Сервер доступний. Час на сервері: %s", data['date'])
                    logging.info("Запитувана сторінка: : %s", data['current_page'])
                    logging.info("Відповідь сервера місти наступні поля:")
                    for key in data.keys():
                        logging.info("Ключ: %s, Значення: %s", key, data[key])
                except requests.exceptions.ConnectionError:
                    logging.error("Unable to conect to the server: ")
      Результат у файлі server.log:
      
                INFO 2020-11-08 19:05:44,031 root : Сервер доступний. Час на сервері: 08/11/2020 17:05:44
                INFO 2020-11-08 19:05:44,032 root : Запитувана сторінка: : http://localhost:8000/health/
                INFO 2020-11-08 19:05:44,032 root : Відповідь сервера місти наступні поля:
                INFO 2020-11-08 19:05:44,032 root : Ключ: date, Значення: 08/11/2020 17:05:44
                INFO 2020-11-08 19:05:44,032 root : Ключ: current_page, Значення: http://localhost:8000/health/
                INFO 2020-11-08 19:05:44,032 root : Ключ: server_info, Значення: ['Linux', 'julia-VirtualBox', '5.4.0-52-generic', '#57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020', 'x86_64']
                INFO 2020-11-08 19:05:44,033 root : Ключ: client_info, Значення: python-requests/2.22.0     
      **ііi.** Щоб організувати щоб 
      дана програма запускалась раз в хвилину я зробила 
      безкінечний цикл "while True:" та час сну 60 секунд "time.sleep(60)"  
      
                def main(url):
                    while True:
                        try:
                            r = requests.get(url)
                            data = json.loads(r.content)
                            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
                            logging.info("Запитувана сторінка: : %s", data['current_page'])
                            logging.info("Відповідь сервера місти наступні поля:")
                            for key in data.keys():
                                logging.info("Ключ: %s, Значення: %s", key, data[key])
                        except requests.exceptions.ConnectionError:
                            logging.error("Unable to conect to the server: ")
                
                        time.sleep(60)  
      **іv.** Зробила аліас на запус моніторингу: 
      
                [scripts]
                monitor = "python3 monitoring.py" 
                
                                
