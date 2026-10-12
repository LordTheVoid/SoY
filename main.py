import telebot

# Подключаем бота по его токену
bot = telebot.TeleBot(8984567109:AAEb1GuJ1LY4FNhQV9mpkNfn1yhcmu1cHhQ)

# Ответ на команды /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот, написанный на чистом коде. Как твои дела?")

# Эхо-бот: отвечает тем же текстом, что ему прислали
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "привет":
        bot.reply_to(message, "И тебе привет! 👋")
    elif message.text.lower() == "как дела?":
        bot.reply_to(message, "Отлично, я же просто код! А у тебя?")
    else:
        bot.reply_to(message, f"Ты написал: {message.text}")

# Запуск бота 24/7 (пока работает программа)
print("Бот запущен и готов к работе!")
bot.infinity_polling()