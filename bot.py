import telebot
from msgs import gfgMessage, starterMessage, listMessage, helpMessage, aboutMessage, courseDetails, Cpp_Courses, WebDev
token = "6273816057:AAEZTnvB7X9wUdGnHyLogb5HrcEkD2F2y9E"
bot = telebot.TeleBot(token)
print("Bot is  running")
@bot.message_handler(commands=['end'])
def endMessage(msg):
    bot.close()

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, starterMessage)

@bot.message_handler(commands=['gfg','gfgPytrhon',"python"])
def sendMessgae(msg):
    bot.reply_to(msg,gfgMessage)

@bot.message_handler(commands=['list'])
def send_list(msg):
    bot.reply_to(msg, listMessage)

@bot.message_handler(commands=['help'])
def send_help(msg):
    bot.reply_to(msg, helpMessage)

@bot.message_handler(commands=['cpp','c++','cpp ka batch' , 'dot batch'])
def sendMessage(msg):
    bot.reply_to(msg,Cpp_Courses)

@bot.message_handler(commands=['about'])
def send_about(msg):
    bot.reply_to(msg, aboutMessage)

@bot.message_handler(commands=['course'])
def send_course_details(msg):
    course_name = msg.text.split('/course ',1)[1].strip().lower()
    if course_name in courseDetails:
        bot.reply_to(msg, courseDetails[course_name])
    else:
        bot.reply_to(msg, "Sorry, I couldn't find that course. Please check the name and try again.")

# Start polling
bot.polling()
