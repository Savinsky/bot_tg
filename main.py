import telebot, datetime

bot = telebot.TeleBot('6698192087:AAHfDFSYXlc0m3chrldzd779Qpl4N2Etmrk') # Токен
chat_id = "" # User
date_remind = datetime.date.today() + datetime.timedelta(days=1) # Переменная дата встречи. Например, завтра.
zoom_link = "https://zoom.us/meeting/123456789"  # Замените на реальную ссылку на Zoom.

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}. '
                                      f'Хочу напомнить, что у нас пройдет встреча {date_remind.strftime("%d.%m.%y")}. '
                                      f'Подтверди ответным сообщением ДА или НЕТ, пожалуйста.')

# Функция получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def process_response(response):
    response = response.text.lower()  # Преобразуем ответ в нижний регистр для удобства обработки
    if response == "да":
        answer = f'Ссылка на встречу в Zoom: {zoom_link}'
    elif response == "нет":
        answer = "Введите дату, когда вы сможете провести встречу в формате dd.mm.yy(например, '05.05.24'): "
        # Здесь можно добавить код для выделения даты из ответа
        try:
            day, month, year = map(int, response.text.split('.'))
            answer = f'Встреча подтверждена на {day:02}.{month:02}.{year:02}.'
        except ValueError:
            answer = "Неправильный формат даты. Пожалуйста, введите дату в формате dd.mm.yy(например, '05.05.24')."
    else:
        answer = "Пожалуйста, ответьте 'Да' или 'Нет'."

    #bot.send_message(response.chat.id, answer)

# Запускаем бота
bot.polling(none_stop=True, interval=0)
