import requests
import json
import datetime
from gd import postongdoc

import pandas as pd

API_KEY = '**********31bd7d655df0c6'
X_DOMAIN = '***********************'


def get_automation_newsletters():
    url = "https://api3.getresponse360.pl/v3/newsletters"
    querystring = {"query[type]":"automation","fields":"name,subject,status,sendMetrics,clickTracks,campaign","sort[createdOn]":"asc","page":"1,2,3,4","perPage":"100"}
    payload = ""
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()

def get_newsletters_stat(newsletterId):
    url = "https://api3.getresponse360.pl/v3/newsletters/"+newsletterId+"/statistics"
    querystring = {"request[groupBy]":"total"}
    payload = "" 
    headers = { 'X-Domain': X_DOMAIN, 'X-Auth-Token': "api-key "+API_KEY, 'cache-control': "no-cache" }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.json()


# newsletter['newsletterId'] # перебираем все письма автоматизации по их id
#print(allnewsletters)
#print(get_newsletter_stat(allnewsletters[1]['newsletterId'])) # читаем Id из json массива, выводим статистику по письму с этим Id



allnewsletters=get_automation_newsletters() # получаем все письма автоматизации
letterid,name,subject,st = [],[],[],[]
sent, totalOpened, uniqueOpened = [],[],[]
totalClicked, uniqueClicked = [],[]
unsubscribed,bounced, complaints =[],[],[]
for letter in allnewsletters:
        # if letter['name'] in DSletters_name:
        #     letterid.append(letter['newsletterId'])
        #     name.append(letter['name'])
        #     subject.append(letter['subject'])
        #     get_newsletters_stat(letter['newsletterId'])
        #     for key in get_newsletters_stat(letter['newsletterId']):
        #             sent.append(key['sent'])
        #             uniqueOpened.append(key['uniqueOpened']) 

        #             totalClicked.append(key['totalClicked'])
        #             uniqueClicked.append(key['uniqueClicked'])
        #             unsubscribed.append(key['unsubscribed'])
        #             complaints.append(key['complaints'])
        letterid.append(letter['newsletterId'])
        name.append(letter['name'])
        subject.append(letter['subject'])
        get_newsletters_stat(letter['newsletterId'])
        for key in get_newsletters_stat(letter['newsletterId']):
                sent.append(key['sent'])
                uniqueOpened.append(key['uniqueOpened']) 
                totalClicked.append(key['totalClicked'])
                uniqueClicked.append(key['uniqueClicked'])
                unsubscribed.append(key['unsubscribed'])
                bounced.append(key['bounced'])
                complaints.append(key['complaints'])


df= pd.DataFrame([letterid,name,subject,sent, totalOpened, uniqueOpened, totalClicked, uniqueClicked,unsubscribed,bounced, complaints]).T
postongdoc(df,'kleanton@gmail.com','Статистика по письмам_Антон','stat_on'+str(datetime.datetime.now()))
print('import Done!')
