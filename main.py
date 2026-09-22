import telebot

bot = telebot.TeleBot("8781016432:AAGqgEOdYbZSl397AhJWH08FdIsr6JTEmpc")

@bot.message_handler(commands=["start"])
def boshlash(message):
    bot.reply_to(message, text="salom botimizga xush kelibsiz!!! sizga yordam keerak bo'lsa /yordam no bosing")

@bot.message_handler(commands=["yordam"])
def yordam_f(message):
    bot.send_message(message.chat.id, text="sizga qanday yordam bera olaman!!! /rasm , /rasm2 , /rasm3 , /audio , /voice2 , /audio3")

@bot.message_handler(commands=["rasm"])
def rasm_f(message):
    bot.send_photo(message.chat.id, photo="https://i.pinimg.com/736x/e2/b7/92/e2b7926598099593d1e9cfbf7c962c49.jpg")

@bot.message_handler(commands=["rasm2"])
def rasm_f(message):
    bot.send_photo(message.chat.id, photo="https://i.pinimg.com/736x/3b/d6/01/3bd6010b7dfa32e92e27277e85986d69.jpg")

@bot.message_handler(commands=["rasm3"])
def rasm_f(message):
    bot.send_photo(message.chat.id, photo="https://i.pinimg.com/736x/0c/16/4d/0c164d41524343525cf4135c00173c64.jpg")



@bot.message_handler(commands=["audio"])
def audio_f(message):
    with open("3.mp3", 'rb') as music:
        bot.send_audio(message.chat.id, audio=music)

@bot.message_handler(commands=["voice2"])
def audio_f(message):
    with open("2.mp3", 'rb') as music:
        bot.send_voice(message.chat.id, voice=music)

@bot.message_handler(commands=["audio3"])
def audio_f(message):
    with open("1.mp3", 'rb') as music:
        bot.send_audio(message.chat.id, audio=music)



print("working...")
bot.infinity_polling()