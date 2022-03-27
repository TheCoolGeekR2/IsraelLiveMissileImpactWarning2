from telethon import TelegramClient
from telethon import events
import DataExctract
import logging
import re


api_id = 0 #Telegram API ID
api_hash = "" #Telegram API HASH
logging.basicConfig(level=logging.DEBUG)
user_input_channel = 'CumtaAlertsEnglishChannel' #Missile Alert channel
ChatFilter = 'red'
SessionName = "Reddy"
phone = 0 #Phone number of the telegram User


client = TelegramClient(SessionName, api_id, api_hash)
@client.on(events.NewMessage(chats=user_input_channel))
async def newMessegeListener(event):
    newMessage = event.message.message
    afterFilter= re.findall(r"(?=("+'|'.join(ChatFilter)+r"))", newMessage, re.IGNORECASE)
    if len(afterFilter) != 0:
        DataExctract.conv_txt(newMessage)
with client:
    client.run_until_disconnected()



