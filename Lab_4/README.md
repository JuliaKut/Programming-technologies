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