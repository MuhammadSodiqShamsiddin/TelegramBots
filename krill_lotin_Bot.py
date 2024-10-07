from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = ""

bot = telebot.Telebot(TOKEN, parse_mode = None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob =  "Assalomu aleykum, Krill_Lotin Telegram botiga xush kelibsiz!"
    javob += "\nMatn kiritng: "
    bot.reply_to(message, javob)
    
@bot.message_handler(commands=['help'])
def send_help(message):
    javob2 =  "Istalgan matn kiritsangiz men uni agar krill alifbosida bo'lsa lotin alifbosiga, aks holda krill alifbosiga o'tkazib beraman."
    bot.reply_to(message, javob2)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
#   if msg.isascii():
#       javob = to_cyrillic(msg)
#   else:
#       javob = to_latin(msg)
    bot.reply_to(message, javob)
    
bot.polling()
     
#matn = input("Matn kiriting: ")

#if matn.ascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))
     
    
    
    
    
    
