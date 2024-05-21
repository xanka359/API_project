# Проект по автоматизации тестирования API Petstore

> <a target="_blank" href="https://petstore.swagger.io/#/">Ссылка на сайт</a>

<img src="resources/images/API_petstore.jpg" width="1000" height="600"/>

*** 

### Проект реализован на стеке

<img src="resources/pictures/python-original.svg" width="60" height="60"/> <img src="resources/pictures/pytest-original-wordmark.svg" width="65" height="60"/> <img src="resources/pictures/pycharm-original.svg" width="60" height="60"/> <img src="resources/pictures/jira-original-wordmark.svg" width="60" height="60"/> <img src="resources/pictures/jenkins-original.svg" width="60" height="60"/> <img src="resources/pictures/allure_testops.png" width="50" height="55"/> <img src="resources/pictures/allure_report.png" width="50" height="55"/> 

***  

### Особенности проекта

* В тестах проверяются request body, response body, status code
* Логирования уровня, даты и времени запуска, request body, response body, status code
* Сборка проекта в Jenkins
* Отчеты Allure Report
* Интеграция с Allure TestOps
* Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira

----

### Реализованные проеверки

1. Добавление нового питомца (post)
2. Получение данных о питомце (get)
3. Изменение данных питомца (put)
4. Удаление несуществующего питомца (delete)
5. Удаление существующего питомца (delete)

____

### [Проект](https://jenkins.autotests.cloud/job/Diplom_API_Petstore/) в Jenkins

### Локальный запуск

**Для локального запуска необходимо выполнить:**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -s -v
```

____
**Для получения отчета:**

```bash
allure serve build/allure-results
```

____

1. **Allure testops** 

   <img src="resources/images/allure_testops.jpg" width="1000" height="450"/>

___  

2. **Jira**  
   <img src="resources/images/api.jpg" width="850" height="450"/>

___  

3. **Allure reports** 

   <img src="resources/images/allure_reports.jpg" width="850" height="400"/>
