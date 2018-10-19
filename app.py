from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json


import errno
import os
import sys, random
import tempfile
import requests
import re
import requests, json

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('cJslMtdzSEUY1Yn2BOQ5/ANgkHNSd5PUXJ/8xTxDg94cEwGcc63UkqEOwi/pbDV1I15ZYIlEGKq9HxdJ7OUtfzzH4QXTkmbnLQRO+4s/xfMEVaEIyZLDyGmnu7LDzbJgpagN+zk0zoGUbHi52XmfhQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('84c75e4b3368d5a69c83549fa955a461')
#===========[ NOTE SAVER ]=======================
notes = {}

def cariayat(reference)
    URLayat = "http://api.alquran.cloud/ayah"+reference
    r = requests.get(URLayat)
    data = r.json()

    status = data['status']
    if(status == "ok"):
        text = data['data']['text']
        num = data['data']['surah']['number']
        nem = data['data']['surah']['name']
        englishName = data['data']['surah']['englishName']
        engnemtran = data['data']['surah']['englishNameTranslation']
        numofay = data['data']['surah']['numberOfAyahs']
        rt = data['data']['surah']['revelationType']

        data = "Text : "+text+"\nNama_Surat : "+englishName+"\nsuratke- : "+num+"\nAyatke- : "+numofay
        return data

    elif(status == "error"):
        return (err)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receive message
    sender = event.source.user_id #get usesenderr_id
    gid = event.source.sender_id #get group_id
    profile = line_bot_api.get_profile(sender)

    data=text.split('-')
    if(data[0]=='lihat'):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=cariayat(data[1])))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
