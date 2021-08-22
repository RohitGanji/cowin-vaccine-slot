import requests
import time

def telegram(message):
    """
    Sends a notification to your telegram account via a telegram bot.
    Use BotFather in Telegram to create a bot and obtain the token.
    
    inputs : message
    """
    token = '<bot_token>'
    chat_id = '<chat_id>'
    requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=HTML')

district_id = "581" # For Hyderabad
date = "20-06-2021" # Enter date based on your requirement
r = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={disctrict_id}&date={date}").json()["centers"]

# Analyse the json data to understand the next part of the code

while True:
    slots = []
    for centers in r:
        for sessions in centers["sessions"]:
            if (sessions["vaccine"] == "SPUTNIK V") and (sessions["min_age_limit"] == 18) and (sessions["available_capacity_dose1"] > 0) :
                msg = f"{centers['name']}\n{sessions['available_capacity_dose1']} slots\n{sessions['date']}"
                slots.append(msg)
    if slots != []:
        for i in slots:
            telegram(msg)
        telegram('=============================')
