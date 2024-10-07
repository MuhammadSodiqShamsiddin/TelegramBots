from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, ReplyKeyboardRemove
from telegram.ext import Updater, CallbackContext, MessageHandler, Filters
from digit import popdigit, popstr, get_index
from namoz import savob
from quran import hidoyat1, hidoyat2, hidoyat3, hidoyat4, suralar
from ramadan import sabr

def message_handler(update: Update, context: CallbackContext):
    global i1
    global name
    main_buttons = ReplyKeyboardMarkup(
        keyboard = [
            [
            KeyboardButton("🕋 Qur'on Tafsiri"),
            ],
            [
            KeyboardButton("⏰ Vaqtlar")
            ]
        ],
        resize_keyboard = True
        )

    tanlov2 = ReplyKeyboardMarkup(
        keyboard = [
            [
            KeyboardButton("☪️ Namoz Vaqtlari"),
            KeyboardButton("🌙 Ramazon vaqtlari")
            ],
            [
            KeyboardButton("Back ➡️")
            ]
        ],
        resize_keyboard = True
        )

    suralar_btn = ReplyKeyboardMarkup(
        keyboard = [
            ['1. Al-Fatiha', '2. Al-Baqara', '3. Oli-Imron'], ['4. An-Niso', '5. Al-Moida', "6. Al-An'am"], ["7. Al-A'rof", '8. Al-Anfal', '9. At-Tavba'], ['10. Yunus', '11. Hud', '12. Yusuf'], ["13. Ar-Ro'd", '14. Ibrohim', '15. Al-Hijr'], ['16. An-Nahl', '17. Al-Isro', '18. Al-Kahf'], ['19. Maryam', '20. Toha', '21. Al-Anbiyo'], ['22. Al-Haj', '23. Al-Muminun', '24. An-Nur'], ['25. Al-Furqon', '26. Ash-Shuaro', '27. An-Naml'], ['28. Al-Qasos', '29. Al-Ankabut', '30. Ar-Rum'], ['31. Luqmon', '32. As-Sajda', '33. Al-Ahzab'], \
            ['34. Saba', '35. Fotir', '36. Yasin'], ['37. As-Sofat', '38. Sod', '39. Az-Zumar'], ["40. G'ofir", '41. Fussilat', '42. Ash-Shuro'], ['43. Az-Zuhruf', '44. Ad-Duxon', '45. Al-Jasiya'], ['46. Al-Ahqof', '47. Muhammad', '48. Al-Fath'], ['49. Al-Hujarot', '50. Qof', '51. Az-Zariyat'], ['52. At-Tur', '53. An-Najm', '54. Al-Qomar'], ['55. Ar-Rohman', '56. Al-Voqia', '57. Al-Hadid'], ['58. Al-Mujadala', '59. Al-Hashr', '60. Al-Mumtahna'], ['61. As-Soff', '62. Al-Jumua', "63. Al-Munafiqun"], ['64. At-Tag\'obun', '65. At-Tolaq', '66. At-Tahrim'],\
            ['67. Al-Mulk', '68. Al-Qolam', '69. Al-Haqqo'], ['70. Al-Arij', '71. Nuh', '72. Al-Jin'], ['73. Al-Muzammil', '74. Al-Muddasir', '75. Al-Qiyamat'], ['76. Al-Insan', '77. Al-Mursalat', '78. An-Naba'], ['79. An-Naziat', '80. Iso', '81. At-Takvir'], ['82. Al-Infitor', '83. Al-Mutoffifin', '84. Al-Inshiqoq'], ['85. Al-Buruj', '86. At-Toriq', "87. Al-A'la"], ["88. Al-G'oshiya", '89. Al-fajr', '90. Al-Balad'], ['91. Ash-Shams', '92. Al-Layl', '93. Az-Zuha'], ['94. Ash-Shatranj', '95. At-Tiyn', "96. Al-A'laq"], ['97. Al-Qodr', '98. Al-Bayyina', '99. Az-Zal-zala'],\
            ["100. Al-A'diyat", "101. Al-Qori'at", '102. At-Takasur'], ['103. Al-Asr', '104. Al-Humaza', '105. Al-Fil'], ['106. Al-Quraysh', "107. Al-Ma'un", '108. Al-Kavsar'], ['109. Al-Kafirun', '110. An-Nasr', '111. Al-Masad'], ['112. Al-Ixlos', '113. Al-Falaq', '114. An-Nas'], ['Orqaga ⏪']
        ],
        resize_keyboard = True)

    tanlov = ReplyKeyboardMarkup(
        keyboard = [
        [
        KeyboardButton("📖 To'liq Tafsir")
        ],
        [
        KeyboardButton("📚 Oyat Tanlash")
        ],
        [
        KeyboardButton('Orqaga ➡️')
        ],
    ],
    resize_keyboard = True
    )

    tugmalar = ReplyKeyboardMarkup(
        keyboard = [
            [
            KeyboardButton("Andijon"),
            KeyboardButton("Toshkent")
            ],
            [
            KeyboardButton("Farg'ona"),
            KeyboardButton("Namangan")
            ],
            [
            KeyboardButton("Samarqand"),
            KeyboardButton("Buxoro")
            ],
            [
            KeyboardButton("Navoiy"),
            KeyboardButton("Guliston")
            ],
            [
            KeyboardButton("Xiva"),
            KeyboardButton("Kokand")
            ],
            [
            KeyboardButton("Nukus"),
            KeyboardButton('Orqaga ⏩')
            ],

        ],
        resize_keyboard = True
        )

    sanalar = ReplyKeyboardMarkup(
        keyboard = [
            [
            KeyboardButton("⌛️ Bugun"),
            KeyboardButton("⏳ Ertaga")
            ],
            [
            KeyboardButton("📆 Haftalik")
            ],
            [
            KeyboardButton("Orqaga ⬅")
            ],

        ],
        resize_keyboard = True
        )

    sanalar_r = ReplyKeyboardMarkup(
        keyboard = [
            [
            KeyboardButton("⌛️ BUGUN"),
            KeyboardButton("⏳ ERTAGA")
            ],
            [
            KeyboardButton("📆 HAFTALIK")
            ],
            [
            KeyboardButton("ORQAGA ⬅")
            ],

        ],
        resize_keyboard = True
        )

    ml = "\n\nSizni Alloh taolo qo'llasin 🤲\n\n Muslim birodarlaringizga ham ulashing 👇\n\n@islamic_uzBot - Alloh rozi bo'lsin 🤲"
    user = update.message.from_user
    t = update.message.text
    ism = user.full_name

    coms = ["☪️ Namoz Vaqtlari", "ORQAGA ⬅", "📆 HAFTALIK", "⏳ ERTAGA", "⌛️ BUGUN", "🌙 Ramazon vaqtlari", '/start', '/my_bots', '/help', '/home', "⌛️ Bugun", "⏳ Ertaga", "📆 Haftalik", 'Orqaga ⬅', 'Orqaga ⏩', 'Orqaga ⏪', 'Orqaga ➡️', "🕋 Qur'on Tafsiri", "⏰ Vaqtlar", "📖 To'liq Tafsir"]

    if t == "/start":
        update.message.reply_html(f"✋ Assalomu Aleykum <b>{ism.title()}!</b> Namoz Vaqti Telegram botiga hush kelibsiz! Siz bu bot oyordamida p'z shahringizning nomini yuborish orqali Namoz va Ramazon vaqtlarini bilib olishingiz mva Qur'oni - Karmning arabcha  teksti va tafsirlari va audiolari bilan tanishib chiqishingiz mumkin! 👇",reply_markup = main_buttons)

    elif t == '/my_bots':
        pass

    elif t == '/help':
        update.message.reply_html(f"🤝 Hurmatli <b>{ism.title()}</b>Bu bot sizga Namoz vaqtlari haqidagi ma'lumotlarni sizga taqdim etadi.Ma'lumotlarni olish uchun O'z shahringiznning nomini yuborishingiz kifoya!\nBu botdan foydalanish uchun - /start\nYordam olish uchun - /help\nBotlarimizni ko'rish uchun - /my_bots\n/home - Bosh Menyuga qaytish\n Komandalariga murojaat qiling!\nAlloh amallaringizni muvaffaqiyatli qilsin 🤲 !")

    elif t == "🕋 Qur'on Tafsiri" or t == 'Orqaga ➡️':
        update.message.reply_text("Suralardan birini tanlang 👇\n\nOgohlantiraman ‼\n\nMen Katta o'lchamli suralarni to'liq holdagi tafsirini taqdim eta olmayman. Ularning ma'lum bir oyatini tanlashingiz mumkin 👇", reply_markup = suralar_btn)

    elif t == 'Orqaga ⬅' or t == "ORQAGA ⬅":
        update.message.reply_text("Marhamat qilib o'z shahringizning nomini yuboring 👇", reply_markup = tanlov2)

    elif t == 'Orqaga ⏩' or t == '/home' or t == 'Orqaga ⏪' or t == 'ORQAGA ⏪':
        update.message.reply_text(f"Marhamat {ism}! Sizga kerak bo'lgan ma'lumotni tanlang 👇", reply_markup = main_buttons)

    elif t == "⏰ Vaqtlar" or t == "Back ➡️":
        update.message.reply_text("Marhamat qilib o'z shahringizning nomini yuboring va Ibodat vaqtlarini bilib oling 👇", reply_markup = tugmalar)

    elif t == "📚 Oyat Tanlash":
        update.message.reply_html(f"<b>{name}</b> surasining oyat raqamini yuboring 👇")

    elif t in suralar or t == 'Orqaga ➡️':
        try:
            name = popstr(t)
            i1 = popdigit(t)
            update.message.reply_html(f"<b>{name}</b> Surasining to'liq tafsirini taqdim etaymi yoki oyat tanlaysizmi?", reply_markup = tanlov)
            update.message.reply_audio(f"https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/{i1}.mp3")
        except:
            update.message.reply_text(f"https://cdn.islamic.network/quran/audio-surah/128/ar.alafasy/{i1}.mp3")

    elif t ==  "📖 To'liq Tafsir":
        try:
            tafsir = f"{name} Surasi.\n\n"
            tafsir += hidoyat3(i1)
            tafsir += '\n\n'
            tafsir += hidoyat1(i1)
            tafsir += ml
            update.message.reply_text(tafsir)
        except:
            tafsir = f"{name} Surasi.\n\n"
            tafsir += hidoyat3(i1)
            tafsir += '\n\n'
            tafsir += hidoyat1(i1)
            tafsir += ml
            filename = f"{name}.pdf"
            with open(filename, 'w+') as file:
                file.write(tafsir)
            update.message.reply_document(document = file, caption = f"{name} Surasi tafsiri")

    elif t.isdigit():
        tafsir = f"{name} Surasi {t} - Oyat\n\n"
        t = int(t)
        tafsir += hidoyat4(i1, t)
        tafsir += '\n\n'
        tafsir += hidoyat2(i1, t)
        tafsir += ml
        update.message.reply_text(tafsir)

    elif t not in coms and t not in suralar:
        global city
        f = popstr(t)
        if f != '':
            city = t[:]
            update.message.reply_text("Quyidagilardan birini tanlang 👇", reply_markup = tanlov2)


    elif t == "⌛️ Bugun" or t == "⏳ Ertaga" or t == "📆 Haftalik":
        update.message.reply_text(savob(t, city))

    elif t == "⌛️ BUGUN" or t == "⏳ ERTAGA" or t == "📆 HAFTALIK":
        update.message.reply_html(sabr(t, city))

    elif t == "🌙 Ramazon vaqtlari":
        update.message.reply_text("🧭 Ramazon vaqtlarini bilish uchun quyidagi sanalardan birini tanlang 👇", reply_markup = sanalar_r)

    elif t == "☪️ Namoz Vaqtlari":
        update.message.reply_text("Sizga kerakli sanani tanlang 👇", reply_markup = sanalar)

def main():
    updater = Updater(
        token = "5610376374:AAF_zGxjWg3BHHuh7hIcyXCuNKModJcYqTk",
        use_context = True
        )
    updater.dispatcher.add_handler(MessageHandler(filters = Filters.all, callback = message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()