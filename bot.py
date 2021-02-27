import telebot

from comics_parser import parse_comics


bot = telebot.TeleBot("your_token")

insults = ["fuck you", "go fuck", "fool", "looser"]

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row("/start")


@bot.message_handler(commands=["start"])
def start_msg(message):
    bot.send_message(message.chat.id, "Yo! Send me the comic number you want to watch", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_msg(message):
    import json

    if message.text.isdigit():
        try:
            comic = parse_comics(message.text)

            bot.send_photo(message.from_user.id, photo=comic["img"])
        except json.JSONDecodeError:
            bot.send_message(message.chat.id, "Oops, no such comics.")
    elif message.text.lower() in insults:
        bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAMbYDfWEJ_QQUeJNeWYD6xRzWmLSsMAAsQCAAM4oArdJsvMWM1-TR4E")
    else:
        bot.send_message(message.chat.id, "I don't understand you.")


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    bot.send_message(message.chat.id, "Nice sticker!")


print("Bot running...\n______________")

bot.polling()
