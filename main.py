import requests
import json

API_KEY = '0ade8775111c88f7af31bd7d655df0c6'
X_DOMAIN = 'response.dasreda.ru'

DSletters_name= [
    'Дожим_стандарт. Письмо1_24h',
    'Дожим_стандарт. Письмо2_48h',
    'Дожим_стандарт. Письмо3_72h',
    'Дожим_стандарт. Письмо4_96h',
    'Дожим_стандарт. Письмо5_12',
    'Дожим_стандарт. Письмо6_12',
    'Дожим_стандарт. Письмо7',
    'Дожим_вип. Письмо1_24h',
    'Дожим_вип. Письмо2_48h',
    'Дожим_вип. Письмо3_54h',
    'Дожим_вип. Письмо4_72h',
    'Дожим_миникурс_стандарт. Письмо1_24h',
    'Дожим_миникурс_стандарт. Письмо2_48h',
    'Дожим_миникурс_стандарт. Письмо3_72h',
    'Дожим_миникурс_стандарт. Письмо4_96h',
    'Дожим_миникурс_стандарт. Письмо5_120h',
    'Дожим_миникурс_стандарт. Письмо6_120h',
    'Реактивация. Прогрев 1-new links',
    'Реактивация. Прогрев 1-new links-2',
    'Письмо реактивации 2 — Антон',
    'Письмо реактивации 3 — Антон',
    'Письмо реактивации 2 — Алина',
    'Письмо реактивации 3 — Алина',
    'Письмо реактивации 4 — Антон',
    'Письмо реактивации 5 — Антон',
    'Реактивация. Пуш120-1',
    'Реактивация. Пуш120-2-3',
    'Реактивация. Опрос',
    'Реактивация. Последнее письмо',
    '120-микрокурс-Урок-1, Аветов',
    '120-микрокурс-Урок-2, Алексеева',
    '120-микрокурс-Урок-3, Горбунов',
    '120-микрокурс-Урок-4, Косенко',
    '120-микрокурс-Урок-5, Зиновьева',
    '120-микрокурс-финал',
    '120-микрокурс-финал-не смотрели все видео',
    '120мини_авто',
    '120 список лайфхаков',
    '120-инструкция для оплативших',
    '120_транзакционник, TW',
    '120 Апгрейд до ВИП'
]

def get_automation_newsletters():
    url = "https://api3.getresponse360.pl/v3/newsletters"
    querystring = {"query[type]":"automation","fields":"name,subject,status,sendMetrics,clickTracks,campaign","sort[createdOn]":"asc","page":"1,2","perPage":"100"}
    payload = ""
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_newsletter_stat(newsletterId):
    url = "https://api3.getresponse360.pl/v3/newsletters/"+newsletterId+"/statistics"
    querystring = {"request[groupBy]":"total"}
    payload = "" 
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

# allnewsletters=get_automation_newsletters() получаем все письма автоматизации
# get_newsletter_stat(allnewsletters[1]['newsletterId']) читаем Id из json массива, выводим статистику по письму с этим Id
