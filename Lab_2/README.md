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