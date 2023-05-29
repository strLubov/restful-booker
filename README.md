# Проект автотестирования для платформы RestfulBooker

[RestfulBooker] (https://automationintesting.online/) - тестовая платформа, реализующая функционал для онлайн бронирования гостиницы

## Проверяется функционал

API:

* Создание бронирования (метод POST)
* Редактирование бронирования (метод PUT)
* Частичное обновление бронирования (метод PATCH)
* Удаление бронирования (метод DELETE)
* Получение бронирования по различным фильтрам (метод GET)

UI:

* Создание комнаты
* Редактирование комнаты
* Редактирование контактной информации

## Особенности тестов

В UI тестах реализована авторизации через API с помощью фистуры open_browser_with_cookie.

Тест test_create_room параметризован для проверки создания всех видов комнат.

## Запуск тестов

Локально 

```bash
pytest
```

С помощью [JOB](https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/) в Jenkins

![Нажать "Собрать с параметрами"](https://drive.google.com/drive/folders/1rjBsIQlHP4TXxwfGMGPFY6kxeO3RvjfR)

![Указать значение версии браузера при необходимости](https://drive.google.com/drive/folders/1rjBsIQlHP4TXxwfGMGPFY6kxeO3RvjfR)

![Посмотреть выполнение прогона](https://drive.google.com/drive/folders/1rjBsIQlHP4TXxwfGMGPFY6kxeO3RvjfR)

![Посмотреть подробный отчет](https://drive.google.com/drive/folders/1rjBsIQlHP4TXxwfGMGPFY6kxeO3RvjfR)

[Ссылка]((https://jenkins.autotests.cloud/job/StrelnikovaL_restful-booker/allure/) на allure отчет. Allure отчет содержит два suites: API и UI. Для UI тестов приложены логи, скриншот и видео о прохождении теста




