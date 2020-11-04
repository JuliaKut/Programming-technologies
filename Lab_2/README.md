###  Лабораторна 2
***
1) Створюю папку Lab_2 та README.md.  
2) За допомогою пакетного менеджера PIP інсталювала pipenv та створила ізольоване середовище для Python.
   
        pip install pipenv  
        pipenv --python 3.7  
        pipenv shell  
3) Встановила бібліотеки requests та ntplib  у своєму середовищі.  
                                                                                     
       pipenv install requests
       pipenv install ntplib
       
4) Закинула файл app.py у свою папку. 

5) Переконаласьсь що програма працює правильно.
   
       python app.py
    Результат:
       
       ========================================
       Результат без параметрів: 
       No URL passed to function
       ========================================
       Результат з правильною URL: 
       Time is:  10:57:23 AM
       Date is:  11-03-2020
6) Встановила бібліотеку pytest.

       pipenv install pytest
       
7) Запустила тести:

       pytest tests/tests.py
   Результат:

       ========================================================================= test session starts =========================================================================
       platform linux -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
       rootdir: /home/julia/IdeaProjects/Programming-technologies/Lab_2
       collected 4 items                                                                                                                                                     

       tests/tests.py ....                                                                                                                                             [100%]

       ========================================================================== 4 passed in 2.47s ==========================================================================
8) Написала свою функцію:
        
          def home_work(h=''):
                        if not h:
                            print("\n----------------------------------------------\n")
                            time = datetime.now().time()
                            hours = time.hour
                            print("Точний час: ",time,"\n")
                            if 6 <= hours <= 20 :
                                hello="Доброго дня!"
                                print(hello)
                            else:
                                hello="Доброї ночі!"
                                print(hello)
                            return hello
                        else:
                            print("\n----------------------------------------------\n")
                            if  6 <= h <= 20 :
                                hello="Доброго дня!"
                                print(hello)
                            else:
                                hello="Доброї ночі!"
                                print(hello)
                            return hello
        
          
   Результат (виклик без параметрів):

        ----------------------------------------------

        Точний час:  17:07:37.223223 

        Доброго дня!

9) Написала тест , який перевіряє чи функція доречно виводить
"Доброго дня!" або "Доброї ночі!"

         def test_home_work(self):
                 # Ваш захист
                 self.assertTrue(home_work(15) == "Доброго дня!")
                 self.assertTrue(home_work(23) == "Доброї ночі!")
   Результат:

          ========================================================================= test session starts =========================================================================
          platform linux -- Python 3.8.5, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
          rootdir: /home/julia/IdeaProjects/Programming-technologies/Lab_2
          collected 4 items                                                                                                                                                     

          tests/tests.py ....                                                                                                                                             [100%]

          ========================================================================== 4 passed in 3.02s ==========================================================================          
 10) Результат виконання тестів був перенаправлений у файл results.txt:

           pytest tests/tests.py >> results.txt            
 11) Зроблений коміт.      