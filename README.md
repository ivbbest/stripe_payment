# Реализовать Django + Stripe API бэкенд
## Задача

* Создать Django Модель Item с полями (name, description, price) 
* Реализовать API с двумя методами:
* GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
* GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)
* Залить решение на Github, описать запуск в README.md

## Использование Docker

### Установка Docker.
Установите Docker, используя инструкции с официального сайта:
- для [Windows и MacOS](https://www.docker.com/products/docker-desktop)
- для [Linux](https://docs.docker.com/engine/install/ubuntu/).

### Запуск проекта.
Склонируйте репозиторий `git clone https://github.com/ivbbest/stripe_payment.git` в текущую папку.

### Настройка проекта

#### Задать SECRET_KEY выбрать один из вариантов:

* указать его в настройках Django проекта (settings.py) payment и там SECRET_KEY = 'your-key';
* или создать файл config.py рядом c settings.py в папке payment и там указать SECRET_KEY = 'your-key';
* через создать `.env` файл в корне репозитория и через environment variables указать SECRET_KEY = 'SECRET_KEY'.


#### Задать STRIPE_SECRET_KEY выбрать один из вариантов:

* Cоздать файл config.py рядом c settings.py в папке payment и там указать STRIPE_SECRET_KEY = 'your-key';
* Кастомно вписать в файле payment->api->views.py следующим образом:

```python
stripe.api_key = 'STRIPE_SECRET_KEY'
```

STRIPE_SECRET_KEY можно найти в личном кабинете [stripe.com](https://dashboard.stripe.com/apikeys).

### Сборка образа 

`docker build -t stripe-test`

### Запуск контейнера

`docker run stripe-test`


## Доступны следующие страницы

Указано для localhost, но вместо localhost можно указать актуальный сервер.

| Страница                                     | Описание                                                     |
|----------------------------------------------|--------------------------------------------------------------|
| `http://127.0.0.1:8000/admin/`               | Админская часть. Посмотреть все созданное в админке          |
| `http://127.0.0.1:8000/buy/<int:pk>`         | Просмотр SessionID конкретного товара                        |
| `http://127.0.0.1:8000/buy`                  | Создать товар. POST запрос. Как вариант использовать POSTMAN |
| `http://127.0.0.1:8000/item/{id}`            | Cтраница товара с возможностью его купить.                   |


## Добавление нового товара

Отправить POST запрос по адресу `http://127.0.0.1:8000/buy` через Postman, в теле запроса указать, например, такой json:

```json
{
    "name": "Other Product",
    "description": "Other description Product",
    "price": 666
}
```

## Использовано:
- Python 3.9.5
- Django 4.0.4
- Django Rest Framework 3.13.1
- Stripe 3.0.0