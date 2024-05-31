import os
import telebot
import tempfile
import mouse
import keyboard
from PIL import ImageGrab

my_id = Айди телеграм профиля
API_TOKEN = 'Токен'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Получить скриншот", "Выключить")
    markup.add("Перезагрузить", "Открыть Ютуб")
    markup.add("Открыть Оперу", "Открыть Пайтон")
    markup.add("Открыть Дискорд", "Открыть Стим")
    markup.add("Режим программирования","/start", "Режим игромана")
    markup.add("Написать", 'Закрыть процесс', 'Нажать')
    markup.add(' ', 'Свернуть окна', ' ')
    markup.add("Клик правый", "↑", "Клик колёсиком")
    markup.add("←", "Клик левый", "→")
    markup.add("Вниз", "↓", "Верх")
    markup.add('Зажать левую', '', 'Зажать правую')
    markup.add('Отжать левую', '', 'Отжать правую')
    bot.send_message(message.chat.id, '👋', reply_markup=markup)


@bot.message_handler(regexp='вниз')
def echo_message(message):
    bot.esend_message(message.chat.id, 'Отпустил')
    mouse.whel(-1)

@bot.message_handler(regexp='Верх')
def echo_message(message):
    bot.send_message(message.chat.id, 'Поднял')
    mouse.wheel(1)



@bot.message_handler(regexp='Зажать левую')
def echo_message(message):
    bot.send_message(message.chat.id, 'Зажал левую кнопку мыши')
    mouse.press('left')


@bot.message_handler(regexp='Отжать левую')
def echo_message(message):
    bot.send_message(message.chat.id, 'Отжал левую кнопку мыши')
    mouse.release('left')



@bot.message_handler(regexp='Зажать правую')
def echo_message(message):
    bot.send_message(message.chat.id, 'Зажал правую кнопку мыши')
    mouse.press('right')


@bot.message_handler(regexp='Отжать правую')
def echo_message(message):
    bot.send_message(message.chat.id, 'Отжал правую кнопку мыши')
    mouse.release('right')


@bot.message_handler(regexp='Клик правый')
def echo_message(message):
    bot.send_message(message.chat.id, 'Кликнул правым')
    mouse.click('right')


@bot.message_handler(regexp='↑')
def echo_message(message):
    bot.send_message(message.chat.id, 'Передвинул')
    mouse.move(0, -15, absolute=False, duration=0.1)


@bot.message_handler(regexp='Клик колёсиком')
def echo_message(message):
    bot.send_message(message.chat.id, 'Кликнул колёсиком')
    mouse.click('middle')


@bot.message_handler(regexp='←')
def echo_message(message):
    bot.send_message(message.chat.id, 'Передвинул')
    mouse.move(-15, 0, absolute=False, duration=0.1)


@bot.message_handler(regexp='Клик левый')
def echo_message(message):
    bot.send_message(message.chat.id, 'Кликнул левым')
    mouse.click('left')


@bot.message_handler(regexp='→')
def echo_message(message):
    bot.send_message(message.chat.id, 'Передвинул')
    mouse.move(15, 0, absolute=False, duration=0.2)


@bot.message_handler(regexp='↓')
def echo_message(message):
    bot.send_message(message.chat.id, 'Передвинул')
    mouse.move(0, 15, absolute=False, duration=0.1)


@bot.message_handler(regexp='выключить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Выключаю...')
    os.system("shutdown -s -t 0")


@bot.message_handler(regexp='получить скриншот')
def echo_message(message):
    path = tempfile.gettempdir() + 'screenshot.png'
    screenshot = ImageGrab.grab()
    screenshot.save(path, 'PNG')
    bot.send_photo(message.chat.id, open(path, 'rb'))


@bot.message_handler(regexp='перезагрузить')
def echo_message(message):
    bot.send_message(message.chat.id, 'Перезагружаю...')
    os.system("shutdown /r -t 0")


@bot.message_handler(regexp='открыть ютуб')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю...')
    os.system("start C:/Users/danil/AppData/Local/Programs/OperaGX/launcher.exe https://www.youtube.com")


@bot.message_handler(regexp='Режим программирования')
def echo_message(message):
    bot.send_message(message.chat.id, 'Запускаю...')
    os.system("start C:/Users/danil/AppData/Local/Programs/OperaGX/launcher.exe https://vk.com/music/playlist/688744382_3")
    os.system("start C:/Users/Public/Desktop/PyCharmProfessional2023.3.2.lnk")


@bot.message_handler(regexp='Режим игромана')
def echo_message(message):
    bot.send_message(message.chat.id, 'Запускаю...')
    os.system("start C:/Users/danil/AppData/Local/Programs/OperaGX/launcher.exe https://vk.com/music/playlist/688744382_3")
    os.system("start D:/SteamSetup.exe2/steam.exe")


@bot.message_handler(regexp='Открыть Оперу')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю...')
    os.system("start C:/Users/danil/AppData/Local/Programs/OperaGX/launcher.exe")


@bot.message_handler(regexp='Открыть пайтон')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю...')
    os.system("start C:/Users/Public/Desktop/PyCharmProfessional2023.3.2.lnk")


@bot.message_handler(regexp='Открыть Дискорд')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю...')
    os.system("start C:/Users/danil/AppData/Local/Discord/Update.exe")


@bot.message_handler(regexp='Открыть Стим')
def echo_message(message):
    bot.send_message(message.chat.id, 'Открываю...')
    os.system("start D:/SteamSetup.exe2/steam.exe")



@bot.message_handler(regexp='Написать')
def echo_message(message):
	if message.from_user.id == my_id:
		bot.send_chat_action(my_id, 'typing')
		if message.text == "Написать":
			bot.send_message(my_id, "Что надо написать: ")
			bot.register_next_step_handler(message, typi)


@bot.message_handler(regexp='Нажать')
def echo_message(message):
	if message.from_user.id == my_id:
		bot.send_chat_action(my_id, 'typing')
		if message.text == "Нажать":
			bot.send_message(my_id, "Что надо нажать: ")
			bot.register_next_step_handler(message, typi1)

@bot.message_handler(regexp='Свернуть окна')
def echo_message(message):
    bot.send_message(message.chat.id, 'Свернул...')
    keyboard.send("windows + d")

@bot.message_handler(regexp='Закрыть процесс')
def echo_message(message):
	if message.from_user.id == my_id:
		bot.send_chat_action(my_id, 'typing')
		if message.text == "Закрыть процесс":
			bot.send_message(my_id, "Укажите название процесса: ")
			bot.register_next_step_handler(message, kill_process)

def kill_process (message):
	bot.send_chat_action(my_id, 'typing')
	try:
		os.system("taskkill /IM " + message.text + " -F")
		bot.send_message(my_id, f"Процесс \"{message.text}\" убит")
	except:
		bot.send_message(my_id, "Ошибка! Процесс не найден")


def typi (message):
	bot.send_chat_action(my_id, 'typing')
	try:
		keyboard.write(message.text)
		bot.send_message(my_id, f"Вы написали \"{message.text}\"")
	except:
		bot.send_message(my_id, "Ошибка!")

def typi1 (message):
	bot.send_chat_action(my_id, 'typing')
	try:
		keyboard.send(message.text)
		bot.send_message(my_id, f"Вы нажали \"{message.text}\"")
	except:
		bot.send_message(my_id, "Ошибка!")



print("Запущен")
bot.infinity_polling()
