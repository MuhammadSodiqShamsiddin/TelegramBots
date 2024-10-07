import requests as r

def sabr(time, city = 'toshkent'):
    """Ramazon vaqtlarini qaytaradigan funksiya"""
    try:
        url = f"https://muslimsalat.com/{city}/weekly.json"
        res = r.get(url)
        res = res.json()
    except:
        text = "❌ Noto'g'ri Shahar kiritdingiz!"

    havo = res["today_weather"]
    bosim = havo['pressure']
    temp = havo['temperature']

    manzil = res['items']
    ind = 0
    bomdod_times = []

    shom_times = []

    vaqtlar = [bomdod_times, shom_times]
    for v in manzil:
        bomdod = manzil[ind]['fajr']
        bomdod_times.append(bomdod)

        shom = manzil[ind]['maghrib']
        shom_times.append(shom)

        ind += 1

    b = vaqtlar[0][0]
    sh = vaqtlar[1][0]
    date = manzil[0]['date_for']

    b2 = vaqtlar[0][1]
    sh2 = vaqtlar[1][1]
    date2 = manzil[1]['date_for']

    b3 = vaqtlar[0][2]
    sh3 = vaqtlar[1][2]
    date3 = manzil[2]['date_for']

    b4 = vaqtlar[0][3]
    sh4 = vaqtlar[1][3]
    date4 = manzil[3]['date_for']

    b5 = vaqtlar[0][4]
    sh5 = vaqtlar[1][4]
    date5 = manzil[4]['date_for']

    b6 = vaqtlar[0][5]
    sh6 = vaqtlar[1][5]
    date6 = manzil[5]['date_for']

    b7 = vaqtlar[0][6]
    sh7 = vaqtlar[1][6]
    date7 = manzil[6]['date_for']

    info = f"\n\n<b>Bugungi Ob - Havo:</b>\n\nHarorat: <b>{temp}°</b>\nBosim: <b>{bosim}</b>\n\nSizni Alloh taolo qo'llasin 🤲\n\n Muslim birodarlaringizga ham ulashing 👇\n\n@islamic_uzBot - Alloh rozi bo'lsin 🤲"


    if time == "⌛️ BUGUN":
        text = f"    ***{date}***\n<b>{city.title()}</b> Shahrida Bugungi Ramazon vaqtlari:\n\nSaharlik: <b>{b}</b>\nIftorlik: <b>{sh}</b>{info}!"

    elif time == "⏳ ERTAGA":
        text = f"    ***{date2}***\n<b>{city.title()}</b> Shahrida Ertangi Ramazon vaqtlari:\n\nSaharlik: <b>{b2}</b>\nIftorlik: <b>{sh2}</b>{info}!"

    elif time == "📆 HAFTALIK":
        text = f"<b>{city.title()}</b> Shahrida Haftalik Ramazon vaqtlari vaqtlari:\n\n***{date}***\n\n\n\
                Saharlik: {b}\n\n\
                Iftorlik: {sh}\n\n\
                ***{date2}***\n\n\
                Saharlik: {b2}\n\n\
                Iftorlik: {sh2}\n\n\
                ***{date3}***n\n\
                Saharlik: {b3}\n\n\
                Iftorlik: {sh3}\n\n\
                ***{date4}***\n\n\
                Saharlik: {b4}\n\n\
                Iftorlik: {sh4}\n\n\
                ***{date5}***\n\n\
                Saharlik: {b5}\n\n\
                Iftorlik: {sh5}\n\n\
                ***{date6}***\n\n\
                Saharlik: {b6}\n\n\
                Iftorlik: {sh6}\n\n\
                ***{date7}***\n\n\
                Saharlik: {b7}\n\n\
                Iftorlik: {sh7}{info}"

    return text