import requests
from .models import TeleSettings


def send_telegram(tg_name, tg_phone):
    settings = TeleSettings.objects.get(pk=1)
    token = settings.tg_token
    chat_id = settings.tg_chat
    text = settings.tg_message
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    if text.find('{') and text.find('}') and text.rfind('{'):
        par_1 = text[:text.find('{')]
        par_2 = text[text.find('}') + 1:text.rfind('{')]

        text_slice = par_1 + tg_name + par_2 + tg_phone

    else:
        text_slice = text

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text_slice
    })
