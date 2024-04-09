import random

import telebot
from telebot import types


TOKEN = '7088374644:AAGYU38OazuZ6shmMMRCJ1LM7HULFOPhytA'
bot = telebot.TeleBot(TOKEN)
x = 0
question_nam = 0

vop_ok = {'vop1': ["Вопрос 1: В каком году вышел фильм 'Америкаский психопат?'", '2000'], 'vop2': ["Вопрос 2: Кто такой Патрик Бейтман ?", 'Сигма'], 'vop3': ["Вопрос 3: Кто исполняет главную роль в фильме 'Америкаский психопат'?",'Кристиан Бейл'], 'vop4': ["Вопрос 4: Кто такой Nix?", 'Стример-Сигма']}
answe = ['2000','2002','1998']
answe1 = ['Сигма','Псих','Обычный человек','Кристиан Бейл','Бред Питт','Леонардо ДиКаприо','Стример-Сигма','Скуф','Обычный человек']
list_vop = ['vop1','vop2','vop3', 'vop4']

@bot.message_handler(commands=['start'])
def start(message):
   kb = types.InlineKeyboardMarkup(row_width=1)
   btn1 = types.InlineKeyboardButton(text='Начать тест',callback_data='test')
   btn2 = types.InlineKeyboardButton(text='Нет', callback_data='no')
   kb.add(btn1, btn2 )
   bot.send_message(message.chat.id,'Вы готовы начать тест?',reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_vopros1(callback):
   global x, question_nam, answe
   if callback.data == 'test':
      vop = list_vop[question_nam]
      a = [
         types.InlineKeyboardButton(text=i, callback_data='2000')

         for i in [random.choice(answe), random.choice(answe)] if i == 
      ]

      kb = types.InlineKeyboardMarkup(row_width=1)

      kb.add(a)
      bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text='Вопрос №1: В каком году вышел фильм "Америкаский психопат"?', reply_markup=kb )

   elif callback.data =='no':
      bot.send_message(callback.message.chat.id, 'Пока!!!')

   elif callback.data == '2000':
      x += 1
      kb = types.InlineKeyboardMarkup(row_width=1)
      btn = types.InlineKeyboardButton(text='Да', callback_data='Yes')
      btn1 = types.InlineKeyboardButton(text='Нет', callback_data='No')
      kb.add(btn, btn1)
      bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text='Правильно.Продолжаем?', reply_markup=kb)


   elif callback.data == 'vopr2':
      kb = types.InlineKeyboardMarkup(row_width=1)
      btn = types.InlineKeyboardButton(text='Сигма ', callback_data='Сигма')
      btn1 = types.InlineKeyboardButton(text='Псих', callback_data='Псих')
      btn2 = types.InlineKeyboardButton(text='Человек', callback_data='Обычный человек')
      kb.add(btn,btn1,btn2)
      bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text='Вопрос №2: Кто такой Патрик Бейтман ?', reply_markup=kb)


   elif callback.data == 'Сигма':
      x += 1
      kb = types.InlineKeyboardMarkup(row_width=1)
      btn = types.InlineKeyboardButton(text='Да', callback_data='Yes')
      btn1 = types.InlineKeyboardButton(text='Нет', callback_data='No')
      kb.add(btn, btn1)
      bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text='Правильно.Продолжаем?', reply_markup=kb)


   elif callback.data in 'ДаНет':
      if callback.data == 'Да':
      kb = types.InlineKeyboardMarkup(row_width=1)
      btn = types.InlineKeyboardButton(text='Да', callback_data='Yes')
      btn1 = types.InlineKeyboardButton(text='Нет', callback_data='No')
      kb.add(btn, btn1)
      bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id,text='Не правильно.Продолжаем?', reply_markup=kb)







bot.polling()