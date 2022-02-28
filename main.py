import boto3
import os, sys
import requests
import random
import json
from functions import *


def point(event, context):
    print(event)
    admin_id =
    try:
        first_name = event['message']['from']['first_name']
    except:
        pass
    chat_id = event['message']['chat']['id']
    msg = event['message']['text']

    if msg.lower() == '/start':
        send_message(chat_id, 'Привет,' + first_name)
        send_message(chat_id, '''Выберите праздник
        8 Марта - /8March
        23 Февраля - /23Febru
        ''')

    if msg.lower() == "/8march":
        send_message(chat_id, 'Привет,' + first_name)
        send_message(chat_id, '''Кому вы хотите отправить поздравление с 8 Марта?
        Маме - /mom
        Бабушке - /gran
        Сестре - /sis
        Девушке - /girl
        Дочери - /daug
        Крестной -/gdmo
        Тёте - /uncl
        Подруге - /frnd
        ''')

    if msg.lower() == "/23febru":
        send_message(chat_id, 'Привет,' + first_name)
        send_message(chat_id, '''Кому вы хотите отправить поздравление с 23 Февраля?
        Папе - /dad
        Дедушке - /grand
        Брату - /bro
        Парню - /boy
        Сыну - /son
        Крестному - /gdfa
        Дяде - /uncld
        Другу - /frndb
        ''')

    persons = [
        '/mom', '/gran', '/sis', '/girl', '/daug', '/gdmo', '/uncl', '/frnd',
        '/dad', '/grand', '/bro', '/boy', '/son', '/gdfa', '/uncld', '/frndb',
    ]

    if msg.lower()[:4:] == '/add':  # and chat_id == admin_id
        for i in persons:
            if ('/' + msg.lower().split('_')[1].split()[0]) == i:
                print(i)
                try:
                    msg = msg.lstrip('/add_' + i[1:])
                    article_text, congrats_text, image_url = msg.split('$')[0], msg.split('$')[1], msg.split('$')[2]
                    add_congr(i, article_text, congrats_text, image_url)
                    send_message(chat_id, 'Поздравление успешно добавлено!')
                except:
                    send_message(chat_id, 'Неверный ввод')

    if msg.lower() in persons:
        try:
            send_congr(chat_id, msg.lower())
        except:
            send_message(chat_id, 'Сегодня без подарков!')

