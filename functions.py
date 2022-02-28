# -*- coding: utf-8 -*-
import boto3
import requests
import random
import json
import os, sys

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tg_bot')


def add_congr(person, article_text='test', congrats_text='tessst', image_url='url'):
    try:
        counter = int(db_take(person + '_counter')['extra'])
    except:
        counter = 1
    db_create(person + '_counter', extra=str(counter + 1))
    db_create(person + str(counter), article_text, congrats_text, image_url)


def send_congr(chat_id, person):
    counter = int(db_take(person + '_counter')['extra']) - 1
    congr = db_take(person + str(random.randint(1, counter)))
    article_text, congrats_text, image = congr['article_text'], congr['congrats_text'], congr['image_url']
    send_message(chat_id, article_text)  # коммент если не хочешь отправлять article
    send_message(chat_id, congrats_text)
    send_photo(chat_id, image)


def send_message(chat_id, text):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_sticker(chat_id, sticker):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendSticker"
    )
    data = {
        "chat_id": chat_id,
        "sticker": sticker
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_photo(chat_id, photo):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendPhoto"
    )
    data = {
        "chat_id": chat_id,
        "photo": photo
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_media_group(chat_id, media):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendMediaGroup"
    )
    data = {
        "chat_id": chat_id,
        "media": json.dumps(media)
    }
    r = requests.post(url, data=data)
    print(r.json())


def delete_message(chat_id, message_id):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="deleteMessage"
    )
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_markup(chat_id, text, reply_markup):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendMessage"
    )
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": json.dumps(reply_markup)
    }
    r = requests.post(url, data=data)
    print(r.json())


def edit_markup(chat_id, message_id):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="editMessageReplyMarkup"
    )
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_location(chat_id, latitude, longitude):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendLocation"
    )
    data = {
        "chat_id": chat_id,
        "latitude": latitude,
        "longitude": longitude
    }
    r = requests.post(url, data=data)
    print(r.json())


def send_poll(chat_id, question, options):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="sendPoll"
    )
    data = {
        "chat_id": chat_id,
        "question": question,
        "options": json.dumps(options)
    }
    r = requests.post(url, data=data)
    print(r.json())


def db_take(ID):
    response = table.get_item(
        Key={
            "ID": ID
        }
    )
    item = response['Item']
    return item
    return None


def db_create(ID, article_text='', congrats_text='', image_url='', extra=''):
    table.put_item(
        Item={
            "ID": ID,
            'article_text': article_text,
            'congrats_text': congrats_text,
            'image_url': image_url,
            'extra': extra,
        }
    )
    return None


def db_delete(ID):
    table.delete_item(
        Key={
            "ID": ID
        }
    )
    return None


def refresh_keyboard(old_keyboard, item_to_delete):
    ans = {
        'inline_keyboard': []
    }
    for i in old_keyboard['inline_keyboard']:
        for j in i:
            temp_list = []
            if j['callback_data'] != item_to_delete:
                temp_list.append({
                    'text': j['text'],
                    'callback_data': j['callback_data']
                })
            if temp_list != []:
                ans['inline_keyboard'].append(temp_list)
    return ans


'''    
if command == 'poll':
    quest = 'вопрос',
    opt = ['ответ1', 'ответ2', 'ответ3', 'ответ4']
    send_poll(answer_id, quest, opt)


elif command == "/photos":
            send_media_group(event["message"]["from"]["id"], [
                {"type": "photo",
                 "media": "https://static.tildacdn.com/tild3661-3264-4362-b161-313433373535/bandicam_2018-12-16_.jpg"},
                {"type": "photo",
                 "media": "https://static.tildacdn.com/tild6662-3131-4361-b431-633535306366/bandicam_2018-12-16_.jpg"},
            ]
'''

'''
def edit_markup(chat_id, message_id, text, reply_markup):
    url = "https://api.telegram.org/bot{token}/{method}".format(
        token=my_token,
        method="editMessageReplyMarkup"
    )
    data = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "reply_markup": json.dumps(reply_markup)
    }
    r = requests.post(url, data=data)
    print(r.json())
'''