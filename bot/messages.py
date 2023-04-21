import json
import requests


def start() -> str:
    return 'Привет, ня! Я бот, отправляющий картинки прекрасных кошкодевочек, мяу!\n' \
           'Нажми по кнопке ниже, чтобы получить свою кошкодевочку, ня!'


def neko() -> str:
    return 'Вот ваша кошкодевочка, ня!'


def neko_pic():
    pic = json.loads(requests.get('http://api.nekos.fun:8080/api/neko').text)['image']
    return pic
