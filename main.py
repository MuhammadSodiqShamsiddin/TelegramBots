"""
Loyiha: Qabul 2023-2024 Telegramm Bot
Muallif: Muhammadsodiq Shamsiddinov
Sana: 27-05-2023
"""

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler, Filters, MessageHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, Update
from datetime import datetime, timedelta

STATE_INFO = 1

btn_info, btn_study, btn_exams, btn_reg = ("📈 Litsey haqida 🏙", '📚 Yo\'nalishlar 💼', '✏ Imtihonlar 🏆', '📋 Ro\'yhatdan o\'tish ✔')
main_btns = ReplyKeyboardMarkup([
        [btn_info], [btn_study], [btn_exams], [btn_reg]
    ], resize_keyboard = True)

btn_aniq_t, btn_aniq_i, btn_tabiy, btn_xorij, btn_back = ("💡 Aniq fanlar (Texnika) 🛰", "📊 Aniq fanlar (Iqtisod) ⚡", "🧬 Tabiiy fanlar 🧪", '🗺 Xorijiy filologiya 🧭', 'Orqaga ⬅')
btns2 = ReplyKeyboardMarkup([
    [btn_aniq_t], [btn_aniq_i], [btn_tabiy], [btn_xorij], [btn_back]
    ], resize_keyboard=True)
users = []
text1 = "<b>Andijon qishloq xo'jaligi va agrotexnologiyalar instituti qoshidagi akademik litsey</b>\nManzil:   170100, O'zbekiston Respublikasi, Andijon shahar, Baynalminal ko'chasi 95-uy\nTashkill etilgan yili: Akademik litsey 2006-yil O'zbekiston Respublikasi Oliy va o'rta maxsus ta'limi vazirligi, 19.10.2006-yildagi 216-sonli buyrug'i asosida tashkil etilgan va unga ADU qoshidagi 3-sonli akademik litsey nomi berilgan. Qayta tashkil etilganligi yoki yangi qurilganligi to'g'risida ma'lumot: 'O'zbekiston Respublikasi Vazirlar Maxkamasining 31-avgust 2006-yil “Oliy ta'lim muassasalari tasarrufidagi litsey va litsey internat negizida akademik litseylar tashkil etish to'g'risida'gi 188-sonli qarori asosi da\nElektron pochta manzili: and.agraral@inbox.uz\nTelefon: (74)-225-68-24\n(90)-256 35 59\nAkademik litseyimizda viloyatdagi eng yaxshi o'qituvchilar sizga dars berishadi."
text2 = "<b>Yo'nalishlar</b>\nAkademik litseyimizda asosan 4 ta yo'nalishdan biri bo'yicha tahsil olishingiz mumkin."
text3 = "Kirish imtihonlari 2 bosqichda bo'lib o'tadi va ular Davlat testmarkazi tomonidan bo'lib o'tadi."
text4 = "Akademik litseyga qabul 1 - iyundan boshlanadi.\nBuning uchun sizdan Tug'ilganlik haqida guvohnoma, 3x4 rasm ota-ona passport nusxasi va maktab shahodatnomasi kerak bo'ladi."
text5 = "<b>Aniq Fanlar (Texnika)</b>\nBu yo'nalishga 52 ta o'quvchi qabul qilinadi va ular 2 guruhga bo'linadi.\nBu yo'nalishda siz matematika-fizika fanlari bo'yicha tahsil olasiz."
text6 = "<b>Aniq Fanlar (Iqtisod)</b>\nBu yo'nalishga 26 ta o'quvchi qabul qilinadi.\nBu yo'nalishda siz Matematika-Ingliz tili fanlari bo'yicha tahsil olasiz."
text7 = "<b>Tabiiy Fanlar</b>\nBu yo'nalishga 52 ta o'quvchi qabul qilinadi va ular 2 guruhga bo'linadi.\nBu yo'nalishda siz Kimyo-Biologiya fanlari bo'yicha tahsil olasiz."
text8 = "<b>Xorijiy filologiya</b>\nBu yo'nalishga 26 ta o'quvchi qabul qilinadi.\nBu yo'nalishda siz Ingliz tili - Ona tili tili fanlari bo'yicha tahsil olasiz."
text9 = "🔎 Marhamat kerakli ma'lumotni tanlang 👇"
text11 = "🤝 Assalomu Alaykum <b>{}</b>!\nBu bot sizga bizning <b>Andijon qishloq xo'jaligi va agrotexnologiyalari instituti qoshidagi akademik litsey</b> haqida to'liq ma'lumot beradi!\nUshbu botdan foydalanish uchun /start yordam olish uchun /help deb yozing 📡"

def start(update, context):
    user = update.message.from_user
    update.message.reply_html("✋ Assalom Alaykum hurmatli <b>{} {}</b>! Andijon qishloq xo'jaligi va agrotexnologiyalari universiteti qoshidagi akademik litseyning <b>'Qabul 2023-2024'</b> Telegram botiga hush kelibsiz!\nAgar sizda oliy o'quv yurtlaridan biriga qabul qilinib kelajakda katta maqsadlarni amalga oshirmoqchi bo'lsangiz, marhamat ushbu litsey sizga yordam beradi. <b>AQXAI akademik litsey</b> haqida to'liq ma'lumotni shu yerda olishingiz mumkin 👍".format(user.first_name, user.last_name), reply_markup = main_btns)

    return STATE_INFO

def info(update, context):
    update.message.reply_html(text1, reply_markup = InlineKeyboardMarkup([
            [
            InlineKeyboardButton('🌐 Akademik Litsey rasmiy sayti 👉', url = 'http://andalofai.uz')
            ],
            [
            InlineKeyboardButton('🌐 Akademik Litsey Telegram kanali 👉', url = 'https://t.me/AQXIakademik_litsey')
            ],
            [
            InlineKeyboardButton('🌐 Akademik Litsey Instagramm 👉', url = 'https://instagram.com/aqxai_al')
            ],
            [
            InlineKeyboardButton('🌐 Akademik Litsey You Tube 👉', url = 'https://www.youtube.com/@andalofai7425/videos')
            ]
        ]
        ))



def study(update, context):
    update.message.reply_html(text2, reply_markup = btns2)

def exam(update, context):
    update.message.reply_html(text3, reply_markup = main_btns)

def register(update, context):
    update.message.reply_html(text4, reply_markup = main_btns)

def aniq1(update, context):
    update.message.reply_html(text5, reply_markup = btns2)

def aniq2(update, context):
    update.message.reply_html(text6, reply_markup = btns2)

def tabiiy(update, context):
    update.message.reply_html(text7, reply_markup = btns2)

def filolog(update, context):
    update.message.reply_html(text8, reply_markup = btns2)

def back(update, context):
    update.message.reply_html(text9, reply_markup = main_btns)


def helps(update, context):
    name = update.message.from_user.full_name
    update.message.reply_html(text11.format(name), reply_markup = main_btns)

def main():
    updater = Updater('5898552010:AAFj4jFOIMqZrbwti9wP51j2USlJ_hzl24Q', use_context = True)

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            STATE_INFO: [
                MessageHandler(Filters.regex('^('+btn_aniq_t+')$'), aniq1),
                MessageHandler(Filters.regex('^('+btn_aniq_i+')$'), aniq2),
                MessageHandler(Filters.regex('^('+btn_info+')$'), info),
                MessageHandler(Filters.regex('^('+btn_study+')$'), study),
                MessageHandler(Filters.regex('^('+btn_exams+')$'), exam),
                MessageHandler(Filters.regex('^('+btn_reg+')$'), register),
                MessageHandler(Filters.regex('^('+btn_tabiy+')$'), tabiiy),
                MessageHandler(Filters.regex('^('+btn_xorij+')$'), filolog),
                MessageHandler(Filters.regex('^('+btn_back+')$'), back)
                ]
            },
        fallbacks = [CommandHandler('start', start)])

    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(CommandHandler('help', helps))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()