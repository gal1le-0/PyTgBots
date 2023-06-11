import telebot
from telebot import types
import random
counter = 1

bot = telebot.TeleBot("TOKEN")

btn_back = types.InlineKeyboardButton(text = "Назад", callback_data = "back")
keyb_back = types.InlineKeyboardMarkup(row_width = 1)
keyb_back.add(btn_back)

def addToWatchedDeathNote(message):
    keyb_addMore = types.InlineKeyboardMarkup(row_width=2)
    btn_addMore = types.InlineKeyboardButton(text = "Додати",  callback_data = "report_watched_deathNote")
    keyb_addMore.add(btn_addMore, btn_back)
    watched_ep = message.text
    watched.append("Тетрадь смерти, серія " + watched_ep)
    bot.send_message(message.chat.id, "Серію додано до переглянутих! Бажаєте додати ще одну?", reply_markup=keyb_addMore)

def addToWatchedSk8(message):
    keyb_addMore = types.InlineKeyboardMarkup(row_width=2)
    btn_addMore = types.InlineKeyboardButton(text = "Додати",  callback_data = "report_watched_sk8")
    keyb_addMore.add(btn_addMore, btn_back)
    watched_ep = message.text
    watched.append("SK8: На скейтборді в нескінченність, серія " + watched_ep)
    bot.send_message(message.chat.id, "Серію додано до переглянутих! Бажаєте додати ще одну?", reply_markup=keyb_addMore)

def addToWatchedDemSlayS01(message):
    keyb_addMore = types.InlineKeyboardMarkup(row_width=2)
    btn_addMore = types.InlineKeyboardButton(text = "Додати",  callback_data = "report_watched_DemSlayS01")
    keyb_addMore.add(btn_addMore, btn_back)
    watched_ep = message.text
    watched.append("Винищувач демонів, сезон 1, серія " + watched_ep)
    bot.send_message(message.chat.id, "Серію додано до переглянутих! Бажаєте додати ще одну?", reply_markup=keyb_addMore)

def addToWatchedDemSlayS02(message):
    keyb_addMore = types.InlineKeyboardMarkup(row_width=2)
    btn_addMore = types.InlineKeyboardButton(text = "Додати",  callback_data = "report_watched_DemSlayS02")
    keyb_addMore.add(btn_addMore, btn_back)
    watched_ep = message.text
    watched.append("Винищувач демонів, сезон 2, серія " + watched_ep)
    bot.send_message(message.chat.id, "Серію додано до переглянутих! Бажаєте додати ще одну?", reply_markup=keyb_addMore)



demon_slayer_s01 = {
    "1 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:1",
    "2 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:2",
    "3 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:3",
    "4 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:4",
    "5 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:5",
    "6 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:6",
    "7 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:7",
    "8 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:8",
    "9 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:9",
    "10 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:10",
    "11 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:11",
    "12 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:12",
    "13 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:13",
    "14 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:14",
    "15 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:15",
    "16 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:16",
    "17 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:17",
    "18 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:18",
    "19 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:19",
    "20 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:20",
    "21 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:21",
    "22 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:22",
    "23 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:23",
    "24 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:24",
    "25 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:25",
    "26 серія" : "https://rezka.ag/animation/adventures/30522-istrebitel-demonov-tv-1-2019.html#t:56-s:1-e:26",
}

death_note = {

    "1 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:1",
    "2 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:2",
    "3 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:3",
    "4 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:4",
    "5 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:5",
    "6 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:6",
    "7 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:7",
    "8 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:8",
    "9 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:9",
    "10 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:10",
    "11 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:11",
    "12 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:12",
    "13 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:13",
    "14 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:14",
    "15 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:15",
    "16 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:16",
    "17 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:17",
    "18 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:18",
    "19 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:19",
    "20 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:20",
    "21 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:21",
    "22 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:22",
    "23 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:23",
    "24 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:24",
    "25 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:25",
    "26 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:26",
    "27 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:27",
    "28 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:28",
    "29 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:29",
    "30 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:30",
    "31 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:31",
    "32 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:32",
    "33 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:33",
    "34 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:34",
    "35 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:35",
    "36 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:36",
    "37 серія":"https://rezka.ag/animation/detective/1765-tetrad-smerti-2006.html#t:56-s:1-e:37"
    

}

demon_slayer_s02 = {

    "1 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:1",
    "2 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:2",
    "3 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:3",
    "4 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:4",
    "5 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:5",
    "6 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:6",
    "7 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:7",
    "8 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:8",
    "9 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:9",
    "10 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:10",
    "11 серія":"https://rezka.ag/animation/action/44594-istrebitel-demonov-kvartal-krasnyh-fonarey-tv-2-2021.html#t:56-s:2-e:11"

}

sk8 = {

    "1 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:1",
    "2 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:2",
    "3 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:3",
    "4 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:4",
    "5 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:5",
    "6 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:6",
    "7 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:7",
    "8 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:8",
    "9 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:9",
    "10 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:10",
    "11 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:11",
    "12 серія":"https://rezka.ag/animation/adventures/37086-sk8-na-skeyte-v-beskonechnost-2021.html#t:105-s:1-e:12"

}

watched = []

def turnaround(call):
    keyb5 = types.InlineKeyboardMarkup(row_width=1)
    btn_anim = types.InlineKeyboardButton(text = "Дивитись аніме", callback_data = "anime")
    btn_watched = types.InlineKeyboardButton(text = "Переглянуті серії", callback_data = "watched")
    keyb5.add(btn_anim, btn_watched)
    bot.send_animation(
                        call.message.chat.id,
                        open( "C:\\Users\\Professional\\Desktop\\python\\project XVI\\media\\anime-shy.gif", "rb"), 
                        caption = "І знову привіт!",
                        reply_markup = keyb5
                      )

@bot.message_handler(commands=["start"])
def welcome(message):
    keyb = types.InlineKeyboardMarkup(row_width=1)
    btn_anim = types.InlineKeyboardButton(text = "Дивитись аніме", callback_data = "anime")
    btn_watched = types.InlineKeyboardButton(text = "Переглянуті серії", callback_data = "watched")
    keyb.add(btn_anim, btn_watched)
    bot.send_animation(
                        message.chat.id,
                        open( "C:\\Users\\Professional\\Desktop\\python\\project XVI\\media\\anime-shy.gif", "rb"), 
                        caption = "Привіт! Я бот для перегляду аніме, поки що в моїй бібліотеці лише декілька аніме серіалів, проте, можливо згодом в мене з'являться й інші. Якщо ти тут вперше і тобі потрібна допомога, то пиши команду '/help'. Також хочу зауважити, що для деяких серіалів необхідний VPN!",
                        reply_markup = keyb
                      )
@bot.message_handler(commands=["help"])
def help(message):
    global btn_back
    btn_back = types.InlineKeyboardButton(text = "Назад", callback_data = "back")
    keyb1 = types.InlineKeyboardMarkup(row_width=1)
    keyb1.add(btn_back)
    bot.send_message(message.chat.id, 
        "Якщо ти натиснеш на кнопку 'Дивитись аніме', я покажу тобі список аніме, наразі доступних до перегляду з моєю допомогою \nПри натисненні на кнопку 'Переглянуті серії', я покажу тобі серії, які ти вже подивився \nІ не забувай про VPN!",
        reply_markup=keyb1)



@bot.callback_query_handler(func = lambda call:True)
def callback(call):
    if call.data == "anime":
        keyb_anime = types.InlineKeyboardMarkup(row_width=1)
        btn_demon_slayer = types.InlineKeyboardButton(text = "Винищувач демонів/Demon Slayer", callback_data="DemSlay")
        btn_sk8 = types.InlineKeyboardButton(text = "SK8: На скейтборді в нескінченність", callback_data = "sk8")
        btn_death_note = types.InlineKeyboardButton(text = "Тетрадь смерти/Death note", callback_data = "deathNote")
        keyb_anime.add(btn_demon_slayer, btn_sk8, btn_death_note, btn_back)
        bot.send_message(call.message.chat.id, "Виберіть аніме для перегляду:", reply_markup=keyb_anime)
    if call.data == "DemSlay":
        keybDemSlayS = types.InlineKeyboardMarkup(row_width = 1)
        btn_DemSlayS01 = types.InlineKeyboardButton(text = "Сезон 1", callback_data = "DemSlayS01")
        btn_DemSlayFilm = types.InlineKeyboardButton(text = "Нескінченний поїзд", callback_data= "DemSlayFilm")
        btn_DemSlayS02 = types.InlineKeyboardButton(text = "Сезон 2", callback_data = "DemSlayS02")
        keybDemSlayS.add(btn_DemSlayS01, btn_DemSlayFilm, btn_DemSlayS02)
        bot.send_animation(call.message.chat.id,
                            open("C:\\Users\\Professional\\Desktop\\python\\project XVI\\media\\nezuko.gif", "rb"),
                            caption = "Виберіть сезон",
                            reply_markup=keybDemSlayS)



    if call.data == "DemSlayS01":
        for i in range(len(demon_slayer_s01)):
            global counter
            keyb = types.InlineKeyboardMarkup(row_width=1)
            btn_s = types.InlineKeyboardButton(text = "Дивитись", url = demon_slayer_s01.get(str(counter) + " серія"))
            keyb.add(btn_s)
            bot.send_message(call.message.chat.id, "Серія " + str(counter), reply_markup=keyb)
            counter += 1
        keyb_report = types.InlineKeyboardMarkup(row_width=2)
        btn_report = types.InlineKeyboardButton(text = "Повідомити", callback_data = "report_watched_DemSlayS01")
        keyb_report.add(btn_report)
        bot.send_message(call.message.chat.id, "Повідомити про серії, які я переглянув", reply_markup=keyb_report)
        bot.send_message(call.message.chat.id, "Всьо!", reply_markup=keyb_back)
    counter = 1

    if call.data == "DemSlayFilm":
        keyb = types.InlineKeyboardMarkup(row_width=2)
        btn_InfinTrain = types.InlineKeyboardButton(text = "Дивитися", url = "https://animego.org/anime/istrebitel-demonov-poezd-beskonechnyy-1771")
        keyb.add(btn_InfinTrain)
        bot.send_message(call.message.chat.id, "Дивитися фільм 'Нескінченний поїзд'", reply_markup=keyb) 
        bot.send_message(call.message.chat.id, "Повернутись назад",  reply_markup=keyb_back)

    if call.data == "DemSlayS02":
        for i in range(len(demon_slayer_s02)):
            keyb = types.InlineKeyboardMarkup(row_width=1)
            btn_s = types.InlineKeyboardButton(text = "Дивитись", url = demon_slayer_s02.get(str(counter) + " серія"))
            keyb.add(btn_s)
            bot.send_message(call.message.chat.id, "Серія " + str(counter), reply_markup=keyb)
            counter += 1
        keyb_report = types.InlineKeyboardMarkup(row_width=2)
        btn_report = types.InlineKeyboardButton(text = "Повідомити", callback_data = "report_watched_DemSlayS02")
        keyb_report.add(btn_report)
        bot.send_message(call.message.chat.id, "Повідомити про серії, які я переглянув", reply_markup=keyb_report)
        bot.send_message(call.message.chat.id, "Всьо!", reply_markup=keyb_back)
    counter = 1



    if call.data == "deathNote":
        for i in range(len(death_note)):
            keyb = types.InlineKeyboardMarkup(row_width=1)
            btn_s = types.InlineKeyboardButton(text = "Дивитись", url = death_note.get(str(counter) + " серія"))
            keyb.add(btn_s)
            bot.send_message(call.message.chat.id, "Серія " + str(counter), reply_markup=keyb)
            counter += 1
        keyb_report = types.InlineKeyboardMarkup(row_width=2)
        btn_report = types.InlineKeyboardButton(text = "Повідомити", callback_data = "report_watched_deathNote")
        keyb_report.add(btn_report)
        bot.send_message(call.message.chat.id, "Повідомити про серії, які я переглянув", reply_markup=keyb_report)
        bot.send_message(call.message.chat.id, "Всьо!", reply_markup=keyb_back)
    counter = 1

    if call.data == "report_watched_deathNote":
        save = bot.send_message(call.message.chat.id, "Введіть лише номер серії, яку ви вже подивились")
        bot.register_next_step_handler(save, addToWatchedDeathNote)

    if call.data == "sk8":
        for i in range(len(sk8)):
            keyb = types.InlineKeyboardMarkup(row_width=1)
            btn_s = types.InlineKeyboardButton(text = "Дивитись", url = sk8.get(str(counter) + " серія"))
            keyb.add(btn_s)
            bot.send_message(call.message.chat.id, "Серія " + str(counter), reply_markup=keyb)
            counter += 1
        keyb_report = types.InlineKeyboardMarkup(row_width=2)
        btn_report = types.InlineKeyboardButton(text = "Повідомити", callback_data = "report_watched_sk8")
        keyb_report.add(btn_report)
        bot.send_message(call.message.chat.id, "Повідомити про серії, які я переглянув", reply_markup=keyb_report)
        bot.send_message(call.message.chat.id, "Всьо!", reply_markup=keyb_back)
    counter = 1



    if call.data == "report_watched_sk8":
        save = bot.send_message(call.message.chat.id, "Введіть лише номер серії, яку ви вже подивились")
        bot.register_next_step_handler(save, addToWatchedSk8)

    if call.data == "report_watched_DemSlayS01":
        save = bot.send_message(call.message.chat.id, "Введіть лише номер серії, яку ви вже подивились")
        bot.register_next_step_handler(save, addToWatchedDemSlayS01)

    if call.data == "report_watched_DemSlayS02":
        save = bot.send_message(call.message.chat.id, "Введіть лише номер серії, яку ви вже подивились")
        bot.register_next_step_handler(save, addToWatchedDemSlayS02)



    if call.data == "back":
        turnaround(call = call)



    if call.data == "watched":
        if len(watched) == 0:
            bot.send_message(call.message.chat.id, "Список переглянутих серій порожній!")
        else:
            for elem in watched:
                bot.send_message(call.message.chat.id, elem)


        

bot.polling(none_stop=True)
