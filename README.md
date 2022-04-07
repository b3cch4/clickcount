# Click Count
Программа для укорачивания ссылок с помощью сервиса [bitly](https://bitly.com).
>Если в программу ввести битли ссылку, она посчитает количество переходов.

### Пример работы утилиты
Передача сылки в программу осуществляется через аргумент командной строки:
```commandline
$ python clickcount.py [full_name_of_link] 
```
<a href="https://ibb.co/jZv0FSL"><img src="https://i.ibb.co/G3vYjqV/example-clickcount.jpg" alt="example-clickcount" border="0"></a>
------------------
##### Зависимости
* python3 >= 3.6
* python-dotenv >= 0.20.0
* requests >= 2.27.1
------------------
##### Установка
- Клонировать репозиторий локально на компьютер.
- Получить токен на bitly.com
- Поместить токен в корневой файл .env
```
$ git clone https://github.com/b3cch4/clickcount.git
$ cd clickcount
$ python -m venv env
$ .\env\Scripts\Activate.ps1
$ pip install -r requirements.txt
```
------------------
##### Переменные окружения
Для работы программы требуется личный токен, полученный с сайта [bitly](https://bitly.com)

В корневой директории проекта нужно создать файл `.env` с таким содержанием:
```
BITLY_TOKEN=your_own_token
```






