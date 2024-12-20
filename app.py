import datetime
import telebot

API_TOKEN = '8126103952:AAGSX9IZcjAoHI1VVLgmztUGrfv_QJMIBvk'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Администраторский бот активен. Жду данные от пользовательского бота."
    )

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
        bot.send_message(message.chat.id, "Произошла ошибка при обработке сообщения. Пожалуйста, попробуйте снова.")

def log_event(event):
    with open('admin_bot_logs.txt', 'a') as log_file:
        log_file.write(f"{datetime.datetime.now()} - {event}\n")

if __name__ == '__main__':
    bot.infinity_polling()
