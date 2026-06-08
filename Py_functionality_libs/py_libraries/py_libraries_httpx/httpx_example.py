# pip install httpx
# httpx - это современная библиотека для выполнения
# HTTP-запросов в Python. Она предоставляет простой
# и удобный интерфейс для отправки
# GET, POST, PUT, DELETE и других
# типов запросов к веб-серверам.
# httpx поддерживает асинхронные запросы,
# что позволяет эффективно обрабатывать
# множество запросов одновременно.
# Библиотека также обеспечивает поддержку
# HTTP/2 и автоматическое управление соединениями,
# что улучшает производительность при работе с
# API и веб-сервисами.
# В этом примере мы покажем, как использовать
# httpx для отправки GET и POST запросов, а также обработки ответов от сервера.


import httpx

# Отправка GET-запроса
# response = httpx.get("https://api.github.com")
response = httpx.get("https://jsonplaceholder.typicode.com/posts")

# Проверка статуса ответа
if response.status_code == 200:
    print("Успешный запрос!")
    print("Содержимое ответа:", response.text)
else:
    print("Ошибка:", response.status_code)

# Отправка POST-запроса
data = {"key1": "value1", "key2": "value2"}
# response = httpx.post("https://httpbin.org/post", data=data)
# data =   {
#     "userId": 10,
#     "id": 26060801,
#     "title": "at nam consequatur ea labore ea harum",
#     "body": "cupiditate quo est a modi nesciunt "
#   }

response = httpx.post("https://jsonplaceholder.typicode.com/posts", data=data)

# Проверка статуса ответа
if response.status_code < 300:
    print("Успешный POST-запрос!")
    print("Содержимое ответа:", response.json())
else:
    print("Ошибка:", response.status_code)
