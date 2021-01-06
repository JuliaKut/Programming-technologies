
###  Лабораторна 5
***

1) Прочитала про docker-compose.
2) Прочитала про бібліотеку Flask. 
3) Переглянуто
4) Переглянуто
5) Створила папку my_app в якій буде знаходитись проект. 
Створила папку tests де будуть тести на перевірку працездатності 
проекту. Скопіювала файли у свій репозиторій. Ознайомилася із вмістом 
кожного з файлів
6)  Виконала команди:  

        pip3 install redis
        pipenv --python 3.8
        pipenv install -r requirements.txt
        pipenv run python app.py
     Результат:
     
         * Serving Flask app "app" (lazy loading)
         * Environment: production
           WARNING: This is a development server. Do not use it in a production deployment.
           Use a production WSGI server instead.
         * Debug mode: on
         * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger PIN: 219-277-297  
    Також ініціалузувала середовище для 
    тестів у іншій вкладці шелу та запустила їх командою  
    
         pipenv run pytest test_app.py --url http://localhost:5000
    Тести не запустилися.  
7) Видалила файли які постворювались після тестового запуску. 
 Створила два Dockerfile та Makefile який допоможе автоматизувати процес розгортання;  
8) Опис директив мейкфайлу
   * app - білдить контейнер з додатком
   * tests - білдить контейнер з тестами
   * run - запускає контейнер та створює нетворк
   * test-app - запускає контейнер з тестами
   * prune - очищає невикористані контейнери, волюми, з'єднання та імеджі   
9) Збілдила та запустила сайт і тести.

         sudo make run
         sudo make tests
         sudo make test-app
   Результат:      
         
         ===================================================================================================== test session starts =====================================================================================================
         platform linux -- Python 3.8.7, pytest-6.2.1, py-1.10.0, pluggy-0.13.1
         rootdir: /tests
         collected 4 items                                                                                                                                                                                                             
         
         test_app.py ....                                                                                                                                                                                                        [100%]
         
         ====================================================================================================== 4 passed in 1.10s ======================================================================================================
   ![alt text](https://raw.githubusercontent.com/JuliaKut/Programming-technologies/main/Lab_5/screenshots/1.png)
   ![alt text](https://raw.githubusercontent.com/JuliaKut/Programming-technologies/main/Lab_5/screenshots/2.png)
   ![alt text](https://raw.githubusercontent.com/JuliaKut/Programming-technologies/main/Lab_5/screenshots/3.png)
10) Почистила середовище :

        sudo make docker-prune
11) Створила директиву для того, щоб пушити імеджі:

        push:
        	@$(foreach state,$(STATES), docker push $(REPO):$(state);)
12) Створила директиву для автоматизації процесу видалення імеджів: 

        delete:
        	@sudo docker image rm --force $(shell docker images -q)
    Перевірила docker images:
    
            (Lab_5-QfkFtov1) julia@julia-VirtualBox:~/IdeaProjects/Programming-technologies/Lab_5$ sudo docker images
            REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
	
13) Створила docker-compose.yml у кориневій папці проекту. у даному варіанті є дві мережі - публічна та секретна.
Публічна мережа використовується  для загального доступу , а секретна для бекенду та баз даних , до яких 
доступ мають мати не усі користувачі.       	        	
14) Запустила докер компос:  

        sudo docker-compose -p lab5 up  
15) Перевірила чи сайт працює. Для цього зайшла на адресу 127.0.0.1:80  
16) Перевірила чи докер компос створив необхідін імеджі.

        (Lab_5-QfkFtov1) julia@julia-VirtualBox:~/IdeaProjects/Programming-technologies/Lab_5$ sudo docker images
        [sudo] пароль до julia: 
        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        juliakut/lab5       compose-tests       1452152ffde8        3 minutes ago       147MB
        juliakut/lab5       compose-app         3aa3cd3063fb        10 minutes ago      143MB
        python              3.8-alpine          64df5e2068e3        2 weeks ago         44.5MB
        redis               alpine              c678242f9116        2 weeks ago         31.6MB
17) Зупинила проект та почистила усе:

        (Lab_5-QfkFtov1) julia@julia-VirtualBox:~/IdeaProjects/Programming-technologies/Lab_5$ sudo docker-compose down
        Removing network lab5_secret
        Removing network lab5_public
18) Запушила імеджі до репозиторію:

        sudo docker-compose push
19) На мою думку компос кращий , це новіша технологія , також він простіший у використанні і пришвидшує
виконання усіх етапів.       

     	         	        