import datetime
import telebot

API_TOKEN = '8126103952:AAGSX9IZcjAoHI1VVLgmztUGrfv_QJMIBvk'

bot = telebot.TeleBot(API_TOKEN)

# Log yozuvchi funksiyani aniqlash
def log_event(event):
    with open('admin_bot_logs.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {event}\n")

# Admin botni ishga tushirish xabari
@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(
            message.chat.id,
            "Администраторский бот активен. Жду данные от пользовательского бота."
        )
        log_event(f"Admin bot started by {message.chat.id}")
    except Exception as e:
        log_event(f"Ошибка при отправке стартового сообщения: {e}")

# Foydalanuvchi botdan kelgan barcha xabarlarni qayta ishlash
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        log_event(f"Получено сообщение от {message.chat.id}: {message.text}")
        bot.send_message(
            message.chat.id,
            f"Получено сообщение: {message.text}\nДанные записаны в логи."
        )
    except Exception as e:
        log_event(f"Ошибка обработки сообщения: {e}")
        bot.send_message(
            message.chat.id,
            "Произошла ошибка при обработке сообщения. Пожалуйста, попробуйте снова."
        )

# Botni ishga tushirish
if __name__ == '__main__':
    try:
        log_event("Admin bot started.")
        bot.infinity_polling()
    except Exception as e:
        log_event(f"Ошибка при запуске бота: {e}")

