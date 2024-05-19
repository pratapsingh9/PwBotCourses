import telebot
from telebot import types
from dotenv import load_dotenv
import logging
import os
from msgs import gfgMessage, starterMessage, listMessage, helpMessage, aboutMessage, feedbackMessage, resourcesMessage, courseDetails, Cpp_Courses, WebDev

# Initialize bot with token
token  = os.getenv('telegramToken')
if not token:
    raise ValueError("Token Toth dede bsdk")
bot = telebot.TeleBot(token)

try:
    load_dotenv()
    print("env Variable Loaded")
    print(token)
except:
    print('Not able to laoad env varibale')
finally:
    print("Proccess Env Is done")

# Logging configuration
logging.basicConfig(level=logging.INFO)

print("Bot is running")

# Exception handling decorator
def handle_exceptions(func):
    def wrapper(message):
        try:
            func(message)
        except Exception as e:
            bot.reply_to(message, "Oops! Something went wrong. Please try again later.")
            logging.error(f"Error: {e}")
    return wrapper

# Command to stop the bot
@bot.message_handler(commands=['end'])
@handle_exceptions
def endMessage(msg):
    bot.stop_polling()
    bot.reply_to(msg, "Bot is shutting down. Goodbye!")

# Welcome message with username
@bot.message_handler(commands=['start'])
@handle_exceptions
def send_welcome(message):
    username = message.from_user.first_name if message.from_user.first_name else "there"
    welcome_message = f"Hello, {username}! 🎉\n\n{starterMessage}"
    bot.reply_to(message, welcome_message)

# Sending GFG message
@bot.message_handler(commands=['gfg', 'gfgPython', 'python'])
@handle_exceptions
def send_gfg_message(msg):
    bot.reply_to(msg, gfgMessage)

# Sending list message
@bot.message_handler(commands=['list'])
@handle_exceptions
def send_list(msg):
    bot.reply_to(msg, listMessage)

# Sending help message
@bot.message_handler(commands=['help'])
@handle_exceptions
def send_help(msg):
    bot.reply_to(msg, helpMessage)

# Sending C++ course message
@bot.message_handler(commands=['cpp', 'c++', 'cpp ka batch', 'dot batch'])
@handle_exceptions
def send_cpp_message(msg):
    bot.reply_to(msg, Cpp_Courses)

# Sending about message
@bot.message_handler(commands=['about'])
@handle_exceptions
def send_about(msg):
    bot.reply_to(msg, aboutMessage)

# Sending course details
@bot.message_handler(commands=['course'])
@handle_exceptions
def send_course_details(msg):
    try:
        course_name = msg.text.split('/course ', 1)[1].strip().lower()
        if course_name in courseDetails:
            bot.reply_to(msg, courseDetails[course_name])
        else:
            bot.reply_to(msg, "Sorry, I couldn't find that course. Please check the name and try again.")
    except IndexError:
        bot.reply_to(msg, "Please provide a course name after the /course command.")

# Handle feedback
@bot.message_handler(commands=['feedback'])
@handle_exceptions
def send_feedback(msg):
    bot.reply_to(msg, feedbackMessage)

# Handle resources
@bot.message_handler(commands=['resources'])
@handle_exceptions
def send_resources(msg):
    bot.reply_to(msg, resourcesMessage)

# Inline buttons example (if needed)
@bot.message_handler(commands=['buttons'])
@handle_exceptions
def send_buttons(msg):
    markup = types.InlineKeyboardMarkup()
    button_gfg = types.InlineKeyboardButton("GFG DSA Course", url="https://t.me/+utCkhOCbI3NkNDk1")
    button_cpp = types.InlineKeyboardButton("Supreme Batch", url="https://t.me/+QR74R2BTGrsyZTY1")
    markup.add(button_gfg, button_cpp)
    bot.send_message(msg.chat.id, "Choose a course:", reply_markup=markup)

# Start polling
try:
    bot.polling()
except Exception as e:
    logging.error(f"Bot polling error: {e}")
