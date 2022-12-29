# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)

import telebot  # Импорт библиотек
import requests
# Использована библиотека beautifulsoup4 4.11.1 (Beautiful Soup is a library that makes it easy to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree. https://pypi.org/project/beautifulsoup4/)
from bs4 import BeautifulSoup

bot = telebot.TeleBot('token') # Токен для работы бота в Телеграм


@bot.message_handler(commands=['start']) # Приветственное сообщение
def hello_commands(message):
    global chat_id
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome. Here you can find out the current exchange rate of the American dollar (USD) to the Russian ruble (RUB). Please click on this link or enter from the keyboard -> '/currency_USD'")


@bot.message_handler(commands=['currency_USD']) # Парсинг необходимых данных на сайте www.banki.ru при помощи библиотеки Beautiful Soup
def hello_commands(message):
    global chat_id
    chat_id = message.chat.id
    url = 'https://www.banki.ru/products/currency/cash/moskva/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mass = soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')
    date_time_update = soup.find_all(class_='text-align-center font-size-small text-no-transform font-normal')
    print(mass)
    print(date_time_update)
    string = str(soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-left-default')[0])
    print(string)
    currencyUSD = string[string.find('>')+1:string.find('</div>'):].replace(',', '.')
    print(currencyUSD)
    string2 = str(soup.find_all(class_='text-align-center font-size-small text-no-transform font-normal'))
    date_time = string2[string2.find('>')+1:string2.find('</div>'):]
    print(date_time)
    bot.send_message(chat_id, f'1 US dollar is now worth {currencyUSD} Russian rubles. {date_time}') # Вывод сообщения с полученным курсом доллара к рублю


print('server start') # сообщение о статусе бота в консоль
bot.infinity_polling()
