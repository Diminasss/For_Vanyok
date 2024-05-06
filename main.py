from telebot import TeleBot
from time import sleep
from config import Telegram_API

bot: TeleBot = TeleBot(Telegram_API)


if __name__ == "__main__":
    while True:
        try:
            bot.polling(none_stop=True)

        except KeyboardInterrupt as e:
            print("Ручной выход")
            exit(0)

        except Exception as e:
            print(f"Ошибка {e}")
            sleep(5)
