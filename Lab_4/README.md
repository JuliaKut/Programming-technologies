###  Лабораторна 4
***

1) Ознайомилася з документацією докер.
2) Виконала команди, перенаправила вивід 
цих команд у файл my_work.log та закомітила
його до репозиторію.

        docker -v>>my_work.log
        docker -h>>my_work.log
        docker run docker/whalesay cowsay Docker is fun>>my_work.log
3) Ознайомилася з документацією.
4) Використала команду щоб завантажити 
базовий імедж з репозиторію , 
створила Dockerfile та закомітила його  : 
        
         sudo docker pull python:3.8-slim
         sudo docker images
         sudo docker inspect python:3.8-slim
5) Створила реаозиторій на Docker Hub 
6) Виконала білд (build) Docker імеджа та завантажила 
його до репозиторію.  
[Репозиторій](https://hub.docker.com/r/juliakut/progrtech)   
[Імедж](https://hub.docker.com/layers/juliakut/progrtech/django/images/sha256-dcf0b362a359a80f261936a450413e2f1ffc2b24f85686576322998520202bcb?context=explore)
        
          sudo docker build -t juliakut/progrtech:django .
          sudo docker images
          sudo docker push juliakut/progrtech:django
7) Запустила сайт (все працює)
    
          sudo docker run -it --rm -p 8000:8000 juliakut/progrtech:django 
8) Cтворила Dockerfile.monit. Виконала білд (build) Docker імеджа 
 з моніторингом та завантажила його до репозиторію.    
[Імедж](https://hub.docker.com/layers/juliakut/progrtech/monitoring/images/sha256-d84a56e8c4f76588f6206c0012fa8ac758ed4686a0b937f1beeda6b589f62ec9?context=explore)

          sudo docker build -t juliakut/progrtech:monitoring --file Dockerfile.monit .
          sudo docker images
          sudo docker push juliakut/progrtech:monitoring
    Запустила обидва імеджі.
    
          sudo docker run -it --rm -p 8000:8000 juliakut/progrtech:django
          sudo docker run --net=host --rm -it serjuliakut/progrtech:monitoring
9) Для того щоб отримати логи я використала  docker exec

          sudo docker ps
    Знайшла необхідний ID (d1ad98df8ba4)
    
          sudo docker exec -it d1ad98df8ba4 /bin/bash   
          cat server.log
    Частина з виведедених даних
    
          root@julia-VirtualBox:/app# cat server.log
          INFO 2020-11-08 19:05:44,031 root : Сервер доступний. Час на сервері: 08/11/2020 17:05:44
          INFO 2020-11-08 19:05:44,032 root : Запитувана сторінка: : http://localhost:8000/health/
          INFO 2020-11-08 19:05:44,032 root : Відповідь сервера місти наступні поля:
          INFO 2020-11-08 19:05:44,032 root : Ключ: date, Значення: 08/11/2020 17:05:44
          INFO 2020-11-08 19:05:44,032 root : Ключ: current_page, Значення: http://localhost:8000/health/
          INFO 2020-11-08 19:05:44,032 root : Ключ: server_info, Значення: ['Linux', 'julia-VirtualBox', '5.4.0-52-generic', '#57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020', 'x86_64']
          INFO 2020-11-08 19:05:44,033 root : Ключ: client_info, Значення: python-requests/2.22.0
          INFO 2020-11-08 19:21:03,824 root : Сервер доступний. Час на сервері: 08/11/2020 17:21:03
          INFO 2020-11-08 19:21:03,827 root : Запитувана сторінка: : http://localhost:8000/health/
          INFO 2020-11-08 19:21:03,827 root : Відповідь сервера місти наступні поля:
          INFO 2020-11-08 19:21:03,827 root : Ключ: date, Значення: 08/11/2020 17:21:03
          INFO 2020-11-08 19:21:03,827 root : Ключ: current_page, Значення: http://localhost:8000/health/
          INFO 2020-11-08 19:21:03,828 root : Ключ: server_info, Значення: ['Linux', 'julia-VirtualBox', '5.4.0-52-generic', '#57-Ubuntu SMP Thu Oct 15 10:57:00 UTC 2020', 'x86_64']
               