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