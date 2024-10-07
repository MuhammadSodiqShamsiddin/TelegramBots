import requests as r
from pprint import pprint as pr
def savob(time, city = 'toshkent'):
    """Namoz vaqtlarini qaytaradigan funksiya"""
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
    peshin_times = []
    asr_times = []
    shom_times = []
    xufton_times = []
    vaqtlar = [bomdod_times, peshin_times, asr_times, shom_times, xufton_times]
    for v in manzil:
        bomdod = manzil[ind]['fajr']
        bomdod_times.append(bomdod)

        peshin = manzil[ind]['dhuhr']
        peshin_times.append(peshin)

        asr = manzil[ind]['asr']
        asr_times.append(asr)

        shom = manzil[ind]['maghrib']
        shom_times.append(shom)

        xufton = manzil[ind]['isha']
        xufton_times.append(xufton)

        ind += 1

    b = vaqtlar[0][0]
    p = vaqtlar[1][0]
    a = vaqtlar[2][0]
    sh = vaqtlar[3][0]
    x = vaqtlar[4][0]
    date = manzil[0]['date_for']

    b2 = vaqtlar[0][1]
    p2 = vaqtlar[1][1]
    a2 = vaqtlar[2][1]
    sh2 = vaqtlar[3][1]
    x2 = vaqtlar[4][1]
    date2 = manzil[1]['date_for']

    b3 = vaqtlar[0][2]
    p3 = vaqtlar[1][2]
    a3 = vaqtlar[2][2]
    sh3 = vaqtlar[3][2]
    x3 = vaqtlar[4][2]
    date3 = manzil[2]['date_for']

    b4 = vaqtlar[0][3]
    p4 = vaqtlar[1][3]
    a4 = vaqtlar[2][3]
    sh4 = vaqtlar[3][3]
    x4 = vaqtlar[4][3]
    date4 = manzil[3]['date_for']

    b5 = vaqtlar[0][4]
    p5 = vaqtlar[1][4]
    a5 = vaqtlar[2][4]
    sh5 = vaqtlar[3][4]
    x5 = vaqtlar[4][4]
    date5 = manzil[4]['date_for']

    b6 = vaqtlar[0][5]
    p6 = vaqtlar[1][5]
    a6 = vaqtlar[2][5]
    sh6 = vaqtlar[3][5]
    x6 = vaqtlar[4][5]
    date6 = manzil[5]['date_for']

    b7 = vaqtlar[0][6]
    p7 = vaqtlar[1][6]
    a7 = vaqtlar[2][6]
    sh7 = vaqtlar[3][6]
    x7 = vaqtlar[4][6]
    date7 = manzil[6]['date_for']

    info = f"\n\nBugungi Ob - Havo:\n\nHarorat: {temp}°\nBosim: {bosim}\n\nSizni Alloh taolo qo'llasin 🤲\n\n Namozxon birodarlaringizga ham ulashing 👇\n\n@islamic_uzBot - Alloh rozi bo'lsin 🤲"


    if time == "⌛️ Bugun":
        text = f"    ***{date}***\n{city.title()} Shahrida Namoz vaqtlari:\n\nBomdod: {b}\n\nPeshin: {p}\n\nAsr: {a}\n\nShom: {sh}\n\nXufton: {x}{info}!"

    elif time == "⏳ Ertaga":
        text = f"    ***{date2}***\n{city.title()} Shahrida Namoz vaqtlari:\n\nBomdod: {b2}\n\nPeshin: {p2}\n\nAsr: {a2}\n\nShom: {sh2}\n\nXufton: {x2}{info} "

    else:
        text = f"***{date}***\n{city.title()} Shahrida Namoz vaqtlari:\n\n\
                Bomdod: {b}\n\n\
                Peshin: {p}\n\n\
                Asr: {a}\n\n\
                Shom: {sh}\n\n\
                Xufton: {x}\n\n\
                ***{date2}***\n\n\
                Bomdod: {b2}\n\n\
                Peshin: {p2}\n\n\
                Asr: {a2}\n\n\
                Shom: {sh2}\n\n\
                Xufton: {x2}\n\n\
                ***{date3}***n\n\
                Bomdod: {b3}\n\n\
                Peshin: {p3}\n\n\
                Asr: {a3}\n\n\
                Shom: {sh3}\n\n\
                Xufton: {x3}\n\n\
                ***{date4}***\n\n\
                Bomdod: {b4}\n\n\
                Peshin: {p4}\n\n\
                Asr: {a4}\n\n\
                Shom: {sh4}\n\n\
                Xufton: {x4}\n\n\
                ***{date5}***\n\n\
                Peshin: {p5}\n\n\
                Asr: {a5}\n\n\
                Shom: {sh5}\n\n\
                Xufton: {x5}\n\n\
                ***{date6}***\n\n\
                Bomdod: {b6}\n\n\
                Peshin: {p6}\n\n\
                Asr: {a6}\n\n\
                Shom: {sh6}\n\n\
                Xufton: {x6}\n\n\
                ***{date7}***\n\n\
                Bomdod: {b7}\n\n\
                Peshin: {p7}\n\n\
                Asr: {a7}\n\n\
                Shom: {sh7}\n\n\
                Xufton: {x7}{info}"

    return text
