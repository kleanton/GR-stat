# Узнать статистику по письмам GetResponse

API:
https://api3.getresponse360.pl/v3/newsletters/NN/statistics?request[groupBy]=total

NN - это ID письма

---
Python код
---
import requests

url = "https://api3.getresponse360.pl/v3/newsletters/ae/statistics"

querystring = {"request[groupBy]":"total"}

payload = ""
headers = {
    'X-Domain': "yourDomain.com", 
    'X-Auth-Token': "api-key 0ade8775111c88f7****************",
    'cache-control': "no-cache",
    'Postman-Token': "e247c478-b35c-4cef-89a3-455437097fc6"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)

---
 
Найти ID всех писем автоматизации+Заголовки писем автоматизации
https://api3.getresponse360.pl/v3/newsletters?
query[type]=automation&fields=name,subject,status,sendMetrics,clickTracks,
campaign&sort[createdOn]=asc&page=1,2,3&perPage=200

---
Python код
---
import requests

url = "https://api3.getresponse360.pl/v3/newsletters"

querystring = {"query[type]":"automation","fields":"name,subject,status,sendMetrics,clickTracks,campaign","sort[createdOn]":"asc","page":"1,2,3","perPage":"200"}

payload = ""
headers = {
    'X-Domain': "response.dasreda.ru",
    'X-Auth-Token': "api-key 0ade87788***********",
    'cache-control': "no-cache",
    'Postman-Token': "9f00cc8e-9daa-4d73-8698-623b38906d61"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)


-------------------------

АЛГОРИТМ

БЭК
1) Получаем newsletterId, name,subject писем, 
которые совпадают с нужными нам темами (массив тем задается в коде)
2) Поочередно подставляем newsletterId в запрос на получение статистики по каждому письму.
Сохраняем полученные поля sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,
unsubscribed,bounced, complaints в тот же json где лежит newsletterId по которому итерируемся
3) Выводим json со всеми newsletterId, name,subject, sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,
unsubscribed,bounced, complaints

ФРОНТ - MVP
1) На основании json строим таблицу. Таблицу отдаём в гугл-таблицу
