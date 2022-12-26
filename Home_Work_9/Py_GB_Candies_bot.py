# Добавить игру, реализованную ранее, с конфетами к боту.
# ' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

import telebot
from random import randint
from random import choice

bot = telebot.TeleBot("5847853376:AAHEF1hShc07jI4NfgwCvfGULVq1poUZato")
candies = dict()
enable_game = dict()
turn = dict()


def handle_game_proc(message):
    global enable_game
    try:
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False
    except KeyError:
        enable_game[message.chat.id] = False
        if enable_game[message.chat.id] and 1 <= int(message.text) <= 28:
            return True
        else:
            return False


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global turn, candies, enable_game
    bot.reply_to(message, "Welcome to the Candy Game Bot!)))\nGame rules:\nThere are 117 candies on the table. The player or bot makes a move after each other. The first move is determined randomly. In one move, you can pick up no more than 28 candies. All of the opponent's candies go to the one who made the last move.\nGood Luck!")
    candies[message.chat.id] = 117
    turn[message.chat.id] = choice(['Bot', 'Human'])
    bot.send_message(message.chat.id, f'{turn[message.chat.id]} player goes first.')
    enable_game[message.chat.id] = True
    if turn[message.chat.id] == 'Bot':
        take = randint(1, candies[message.chat.id] % 29)
        candies[message.chat.id] -= take
        bot.send_message(message.chat.id, f'Bot took {take}.')
        bot.send_message(message.chat.id,
                         f'{candies[message.chat.id]} left')
        turn[message.chat.id] = 'Human'


@bot.message_handler(func=handle_game_proc)
def game_process(message):
    global candies, turn, enable_game
    if turn[message.chat.id] == 'Human':
        if candies[message.chat.id] > 28:
            candies[message.chat.id] -= int(message.text)
            bot.send_message(message.chat.id,
                             f'{candies[message.chat.id]} left')
            if candies[message.chat.id] > 28:
                take = randint(1, candies[message.chat.id] % 28)
                candies[message.chat.id] -= take
                bot.send_message(message.chat.id,
                                 f'Bot took {take}.')
                bot.send_message(message.chat.id,
                                 f'{candies[message.chat.id]} left')
                if candies[message.chat.id] <= 28:
                    bot.send_message(message.chat.id, 'Human Win!')
                    enable_game[message.chat.id] = False
            else:
                bot.send_message(message.chat.id, 'Bot Win!')
                enable_game[message.chat.id] = False
        else:
            bot.send_message(message.chat.id, 'Bot Win!')
            enable_game[message.chat.id] = False


bot.infinity_polling()
