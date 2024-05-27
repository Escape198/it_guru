# Currency Converter API

Это REST-API для конвертации валют, написанное на Flask.

## Требования

- Python 3.7+
- pip

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/ваш-репозиторий/currency-converter-api.git
    cd it_guru
    ```

2. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

## Запуск с Gunicorn

1. Запустите приложение с Gunicorn:
    ```bash
    gunicorn -w 4 -b 127.0.0.1:8000 app:app
    ```

2. API будет доступно по адресу `http://127.0.0.1:8000`.

## Использование

Для получения курса обмена и конвертации валют используйте следующий запрос:

```bash
GET http://127.0.0.1:8000/api/rates?from=EUR&to=RUB&value=1

GET http://127.0.0.1:8000/api/currencies
