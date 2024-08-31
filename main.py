import requests
from telethon import TelegramClient, events, sync
import re, os
from time import sleep

tokenbot = input("[+] Enter Token : ") 
dragon = input("[+] Enter id : ")
app = TelegramClient("aho3", api_id=24137687, api_hash="f12923309afd8b3aa021edaece63836d")
app.start()
qq = 0
numche = 1
bio = ""  # نبذه البوت
namebot = "bot"
app.send_message("botfather", f'/newbot')
app.send_message("botfather", namebot)

def fucker(o):
    global qq
    if True:
        qq += 1
        url = f"https://t.me/{o}"
        req = requests.get(url)
        if 'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"' in req.text:
            app.send_message("botfather", f'{o}')
            sleep(0.50)
            message = app.get_messages("botfather", limit=1)
            if message[0].text == "Sorry, this username is invalid.":
            	print("[ " + str(qq) + " ] Banned : @" + o)
            	open("banned4.txt","a").write(o+'\n')
            elif "Done! Congratulations on your new bot" in message[0].text:
            	print("[ " + str(qq) + " ] Done : @" + o)
            	y = requests.post(f"""https://api.telegram.org/bot{tokenbot}/sendmessage?chat_id={dragon}&text=« New UserName »
« UserName » : « @{o} »
« ClickS » : « {qq} »
« Save » : « bot »""")
            	app.send_message("botfather", f'/newbot')
            	app.send_message("botfather", namebot)
        else:
        	print("[ " + str(qq) + " ] Taken : @" + o)   
while True:
    import random
    o = "".join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for i in range(3))
    o = str(o) + "bot"
    file = open("banned4.txt","r")
    users = file.read()
    if o in users:
    	qq += 1
    	print("[ " + str(qq) + " ] Banned : @" + o)
    	continue
    if o[0].isdigit():
    	continue
    fucker(o)

app.run()
