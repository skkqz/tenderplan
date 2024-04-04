# Документация для приложения "tenderplan"

Tenderplan - это приложение для сбора данных о закупках с сайта zakupki.gov.ru и их последующей обработки.
## Подготовка к запуску

Убедитесь, что у вас установлен [Python 3.x](https://www.python.org/downloads/) и [Redis](https://redis.io/download/).

### Клонирование репозитория
~~~
git clone https://github.com/skkqz/tenderplan.git
~~~
- Перейдите в директорию
~~~
cd tenderplan
~~~
### Создание виртуального окружения

~~~
python -m venv venv
~~~
- Активируйте виртуальное окружение
~~~
source venv/bin/activate  # для Linux/Mac
~~~
~~~
venv\Scripts\activate  # для Windows
~~~
### Установка зависимостей
~~~
pip install -r requirements.txt
~~~

### Запуск сервера Redis
~~~
redis-server --port 6380
~~~

### Запуск сервера Celery
~~~
celery -A class_tasks worker --loglevel=Info
~~~

## Запуск программы

~~~
python -m main
~~~


### Участие в проекте
#### Если у вас есть предложения или исправления, создавайте issues или отправляйте pull requests. Будем рады вашему вкладу!

### Участники проекта
* [skkqz](https://github.com/skkqz/)
