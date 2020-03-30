from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('hXgcnkaAxXj4+xTcmEOZCVrU8Pwk5kS9qiB6gJX7msIlOYJkwTO4bFzh2lgFgbdnROSB3apQGarvQS6REB+JDANY1CUuL82RFEORBleo1Ogi3OJzsQZSK8fhTZIr//BQ8CVSdxrT25otDcm/hqsVBgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('338644819138a86bd22b88b740255b03')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
######################################################################
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
@app.route("/ConfirmTemplate/")
def handle_message(event):
    if (event.message.text == '123'):   #獲取測試訊息
        replymessage = ('234')          #設定回復訊息(replymessage)
    elif(event.message.text == 'Wifi'): 
        replymessage = (' ASUS-RT51U: \n Password: d0645758\n\n dlink-F392:\n Password: 51232960\n\n ASUS_Zenfone3:\n Password: D0645758\n') 
    elif(event.message.text == '生存場地'):
        replymessage = ('各場地資料彙整\n場地地圖 https://goo.gl/dV8xwq\n各場地資料彙整如下\n\n山湖戰術中心\n官網:  https://www.facebook.com/hillfoxtacticsCenter/\n導航直接搜尋 山狐戰術中心\n收費場 半天200/人 全天300/人溪湖戰役\n官網:  https://www.facebook.com/XIHUAirsoftWar/\nGoogle 導航溪湖戰役即可\n收費場 入場費平日200/人 假日300/人 \n有販賣飲料/出租裝備\n\n烏日橋下\n地址:  https://goo.gl/maps/6eFPrSx4AU42\n橋下鐵絲網後就是活動場地 為免費場地\n可走筏子溪東街或新鎮和路再轉至橋下\n請禮讓偶爾出現的工程車在那邊施工\n\n春田惡魔島\n官網:  https://goo.gl/E4gPqY\n導航” 春田惡魔島” 或東山樂園再往上一點\n收費場 250/人\n有販賣簡單的飲料\n\n大甲野戰場\n地址：台中市大甲區同安里中山路二段1195巷32號\n導航：台中市大甲區長壽東西七路（靠近省道\n收費場 150/人\n\n清水66眷村\nGoogle導航至”港區藝術中心”\n在鎮政路、鱉峰路380巷與藝術街所圍起來的廢棄房區\n入口須從農田靠近鱉峰路380巷的缺口進去\n***為軍方土地，進去遊玩請保持低調****\n\n台灣民俗村\n官網: https://www.facebook.com/TFV.gun/\n導航請搜尋”日華大飯店”\n入場費 150/人\n\nJEA共同決戰區生存遊戲訓練基地\n網址 https://www.facebook.com/jea.shootingclub/\n地址 苗栗縣後龍鎮龍坑里十班坑172號\n收費場 半天200/人 有提供裝備出借\n\n南投千秋戰場\n網址:  https://www.facebook.com/groups/299470600702193/?fref=nf\n地址;  南投市千秋里菓稟路3號\n收費場 100/人/半天\n\n')
    elif(event.message.text == '生存地圖'):
        replymessage = ('台中生存遊戲Google Map: https://goo.gl/dV8xwq')
    elif(event.message.text == '槍店'):
        replymessage = ('KUI 酷愛生存遊戲專賣 - 台中總店\n地址： 406台中市北屯區軍功路一段243-1號\n營業時間:13:00~21:30\n電話： 04-24376402\n露天:https://www.ruten.com.tw/user/index00.php?s=paymy168\n\nKUI 酷愛生存遊戲專賣 - 台中西屯店\n地址： 407台中市西屯區福雅路335號\n營業時間:13:00~21:30\n電話：04-24653131\n\nIDCF艾利斯生存遊戲工作坊台中店\n地址： 407台中市西屯區西屯路二段上石北二巷15號 地下一樓\n營業時間:13:30~22:30\n電話： 04-24522047\n露天:https://www.ruten.com.tw/user/index00.php?s=sky19840716\n\n翔準生存遊戲專賣\n地址:508彰化縣和美鎮彰新路二段479號\n營業時間:12:00~22:00\n電話:04-7353481\n官網:https://www.aog.com.tw/\n露天賣場1:https://www.ruten.com.tw/user/index00.php?s=zzzlin8899\n露天賣場2:https://www.ruten.com.tw/user/index00.php?s=and888999\n\nBCS武器空間生存遊戲專賣 台中美村店\n地址:403台中市西區美村路一段109號\n營業時間:13:00~22:00\n電話:04-23269483\n露天:https://www.ruten.com.tw/user/index00.php?s=bcsbcs\n\nBCS武器空間生存遊戲專賣-台中NOVA英才店\n地址:403台中市西區英才路508號2號2樓241櫃位\n營業時間:11:00~21:30\n電話:04-23293192\n\n金和勝玩具-西屯店\n地址:407台中市西屯區西屯路三段79-8號\n營業時間14:00~22:00\n電話:04-24511795\n露天:https://www.ruten.com.tw/user/index00.php?s=a400258\n\n金和勝玩具-彰化店\n地址:500彰化縣彰化市中央路9號\n電話:04-7621300\n\n')
    elif(event.message.text == '推廣'):
        replymessage = TemplateSendMessage(
            alt_text = ('我是一個確認模板')  # 當你發送到你的Line bot 群組的時候，通知的名稱
            template = ConfirmTemplate(
                text = ('你確定要買晚餐嗎?')  # 你要問的問題，或是文字敘述
                # action 最多只能兩個喔！
                actions = [
                    PostbackAction(
                        label = ('確認')  # 顯示名稱
                        display_text = ('那還不快去買！？')  # 點擊後，回傳的文字
                        data = ('action=buy&itemid=1')  # 取得資料！？
                    )
                    MessageAction(
                        label = ('不買')  # 顯示名稱
                        text = ('那就不買吧！')  # 點擊後，回傳的文字
                    )
                ]
            )
        )
        
    
    message = TextSendMessage(text=replymessage)              #將回復訊息(replymessage)輸入LINE BOT(message)
    line_bot_api.reply_message(event.reply_token,message)     #LINE BOT回復訊息
#######################################################################
if __name__ == "__main__":
    app.run()
    
