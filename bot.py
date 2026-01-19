import os, json, random, telebot, firebase_admin
from firebase_admin import credentials, firestore

# Firebase Setup
firebase_info = json.loads(os.environ['FIREBASE_JSON'])
cred = credentials.Certificate(firebase_info)
firebase_admin.initialize_app(cred)
db = firestore.client()

# Bot Setup
bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    item = telebot.types.KeyboardButton("📲 Share Number & Get PIN", request_contact=True)
    markup.add(item)
    bot.send_message(message.chat.id, "welcome aspirant ! Rankify Control Room mein Apka swagat hai.\n\nNiche button dabakar number share karein, PIN turant mil jayega.", reply_markup=markup)

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact:
        phone = str(message.contact.phone_number).replace("+", "")
        pin = str(random.randint(1111, 9999))
        db.collection('login_pins').document(phone).set({'pin': pin})
        bot.send_message(message.chat.id, f"✅ Verification Successful!\n\nYour Access PIN: {pin}\n\nIse App mein enter karein.")

bot.infinity_polling()

