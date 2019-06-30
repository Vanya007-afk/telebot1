import telebot
import request
import array

bot = telebot.TeleBot("817064272:AAG4mCvVq3fDg0_t_7xbCQ_Soxlyx1oeOfo")

ocheredi = 0
igroc = { } #списки


class igroki():
    def __init__(self,igrok1,igrok2):
        self.igrok1 = igrok1
        self.igrok2 = igrok2

@bot.message_handler(commands=["cm"])
def handle_text(message):
    if message.chat.id == 345632366:
        try:
            bot.send_message(message.chat.id,bot.get_chat_member((message.text).strip("/cm "), (message.text).strip("/cm ")).user)
        except:
            bot.send_message(message.chat.id, "введиде /cm [id]")#d


@bot.message_handler(commands=["stop"])
def handle_text(message):
    global ocheredi  #d
    if message.chat.id in igroc:
        bot.send_message(message.chat.id,"Вы успешно покинули чат")
        bot.send_message(igroc[message.chat.id].igrok1,"Ваш собеседник покинул чат")
        print("id:" + str(message.chat.id) + " - /stop покинул чат")
        del igroc[igroc[message.chat.id].igrok1]
        del igroc[message.chat.id]
    elif message.chat.id == ocheredi:
        bot.send_message(message.chat.id,"Вы успешно покинули очередь")
        print("id:" + str(message.chat.id) + " - /stop очередь")
        ocheredi = 0  #d
    else:
        bot.send_message(message.chat.id,"-")

@bot.message_handler(commands=["help"])
def handle_text(message):
    bot.send_message(message.chat.id, "Бот создан для анонимных переписок. При вводе команды /start бот соеденяет двох рандомных пользователей"
                                      "и они общаються между собою анонимно\nДоступные команды:\n/start - начинать чат\n/stop - остановить чат\n/help - подробнее о боте")

@bot.message_handler(commands=["start"])
def handle_text(message):
    id_user = open("id_user.json", "rt")
    for line in id_user:
        l = [line.strip() for line in id_user]
        if not str(message.chat.id) in l:
            id_user = open("id_user.json", "at")
            id_user.write(str(message.chat.id) + "\n")
            print(str(message.chat.id) + " -> новый пользователь")
    id_user.close()

    global ocheredi
    if ocheredi == 0 and not message.chat.id in igroc:
        ocheredi  = message.chat.id
        bot.send_message(message.chat.id, "Вы успешно встали в очередь, подождите немного пока мы найдем вам собеседника")
        print("id:" + str(message.chat.id) + " - /start очередь")

    elif message.chat.id != ocheredi and not message.chat.id in igroc:
        igroc[message.chat.id] = igroki(ocheredi,message.chat.id)
        igroc[ocheredi] = igroki(message.chat.id,ocheredi)
        bot.send_message(message.chat.id, "Вы соедены, можете общаться")
        bot.send_message(ocheredi, "Вы соедены, можете общаться")
        print("id:" + str(message.chat.id) + " and id:" + str(int(ocheredi)) + " - соедены")

        ocheredi = 0
    elif message.chat.id in igroc:
        bot.send_message(message.chat.id, "Что-бы покинуть чат введите команду /stop")
    else:
        bot.send_message(message.chat.id, "Вы успешно встали в очередь, подождите немного пока мы найдем вам собеседника")
rek = False

@bot.message_handler(commands=["rek"])
def handle_text(message):
    global rek
    if message.chat.id == 345632366 and rek == False:
        rek = True
        bot.send_message(message.chat.id, "Rek = True\nведите текст для отправки:")
        return
    elif message.chat.id == 345632366 and rek == True:
        rek = False
        bot.send_message(message.chat.id, "Rek = False")
        return


@bot.message_handler(content_types=["text"])
def handle_text(message):
    global rek
    if message.chat.id == 345632366 and rek == True:
        id_user = open("id_user.json", "rt")
        for line in id_user:
            l = [line.strip() for line in id_user]
            for ids in l:
                try:
                    bot.send_message(ids, message.text)
                except:
                    print(" ")

        id_user.close()
    elif not message.chat.id in igroc:
        bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
    elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
        bot.send_message(igroc[message.chat.id].igrok1,message.text)
        #bot.reply_to(message,message.text)

@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    if not message.chat.id in igroc:
        bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
    elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
        file = bot.get_file(message.photo[len(message.photo)-1].file_id)
        bot.send_photo(igroc[message.chat.id].igrok1, file.file_id)


@bot.message_handler(content_types=["audio"])
def handle_audio(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            file = bot.get_file(message.audio.file_id)
            bot.send_audio(igroc[message.chat.id].igrok1, file.file_id)

@bot.message_handler(content_types=["video"])
def handle_video(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            file = bot.get_file(message.video.file_id)
            bot.send_video(igroc[message.chat.id].igrok1, file.file_id)

@bot.message_handler(content_types=["voice"])
def handle_voice(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            file = bot.get_file(message.voice.file_id)
            bot.send_voice(igroc[message.chat.id].igrok1, file.file_id)

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            file = bot.get_file(message.sticker.file_id)
            bot.send_sticker(igroc[message.chat.id].igrok1, file.file_id)

@bot.message_handler(content_types=["document"])
def handle_document(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            file = bot.get_file(message.document.file_id)
            bot.send_document(igroc[message.chat.id].igrok1, file.file_id)

@bot.message_handler(content_types=["contact"])
def handle_contact(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            bot.send_contact(igroc[message.chat.id].igrok1, message.contact.phone_number,message.contact.first_name)

@bot.message_handler(content_types=["location"])
def handle_location(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            bot.send_location(igroc[message.chat.id].igrok1, message.location.latitude, message.location.longitude)

@bot.message_handler(content_types=["chat_action"])
def handle_chat_action(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            bot.send_chat_action(igroc[message.chat.id].igrok1, message.action)

@bot.message_handler(content_types=["video_note"])
def handle_video_note(message):
        if not message.chat.id in igroc:
            bot.send_message(message.chat.id,"Введите команду /start и мы вам найдем собеседника\nВведите команду /help что-бы узнать информацию о боте")
        elif igroc[message.chat.id].igrok1 == igroc[message.chat.id].igrok1:
            bot.send_video_note(igroc[message.chat.id].igrok1,message.video_note.file_id, message.video_note.duration, message.video_note.length,)
            #print(message)

bot.polling(none_stop=True, interval=0)