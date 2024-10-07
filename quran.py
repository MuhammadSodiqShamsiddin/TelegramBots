import requests as r
from pprint import pprint as p
from digit import popstr
suralar = ['1. Al-Fatiha', '2. Al-Baqara', '3. Oli-Imron', '4. An-Niso', '5. Al-Moida', "6. Al-An'am", "7. Al-A'rof", '8. Al-Anfal', '9. At-Tavba', '10. Yunus', '11. Hud', '12. Yusuf', "13. Ar-Ro'd", '14. Ibrohim', '15. Al-Hijr', '16. An-Nahl', '17. Al-Isro', '18. Al-Kahf', '19. Maryam', '20. Toha', '21. Al-Anbiyo', '22. Al-Haj', '23. Al-Muminun', '24. An-Nur', '25. Al-Furqon', '26. Ash-Shuaro', '27. An-Naml', '28. Al-Qasos', '29. Al-Ankabut', '30. Ar-Rum', '31. Luqmon', '32. As-Sajda', '33. Al-Ahzab', \
        '34. Saba', '35. Fotir', '36. Yasin', '37. As-Sofat', '38. Sod', '39. Az-Zumar', "40. G'ofir", '41. Fussilat', '42. Ash-Shuro', '43. Az-Zuhruf', '44. Ad-Duxon', '45. Al-Jasiya', '46. Al-Ahqof', '47. Muhammad', '48. Al-Fath', '49. Al-Hujarot', '50. Qof', '51. Az-Zariyat', '52. At-Tur', '53. An-Najm', '54. Al-Qomar', '55. Ar-Rohman', '56. Al-Voqia', '57. Al-Hadid', '58. Al-Mujadala', '59. Al-Hashr', '60. Al-Mumtahna', '61. As-Soff', '62. Al-Jumua', "63. Al-Munafiqun", '64. At-Tag\'obun', '65. At-Tolaq', '66. At-Tahrim',\
        '67. Al-Mulk', '68. Al-Qolam', '69. Al-Haqqo', '70. Al-Arij', '71. Nuh', '72. Al-Jin', '73. Al-Muzammil', '74. Al-Muddasir', '75. Al-Qiyamat', '76. Al-Insan', '77. Al-Mursalat', '78. An-Naba', '79. An-Naziat', '80. Iso', '81. At-Takvir', '82. Al-Infitor', '83. Al-Mutoffifin', '84. Al-Inshiqoq', '85. Al-Buruj', '86. At-Toriq', "87. Al-A'la", "88. Al-G'oshiya", '89. Al-fajr', '90. Al-Balad', '91. Ash-Shams', '92. Al-Layl', '93. Az-Zuha', '94. Ash-Shatranj', '95. At-Tiyn', "96. Al-A'laq", '97. Al-Qodr', '98. Al-Bayyina', '99. Az-Zal-zala',\
        "100. Al-A'diyat", "101. Al-Qori'at", '102. At-Takasur', '103. Al-Asr', '104. Al-Humaza', '105. Al-Fil', '106. Al-Quraysh', "107. Al-Ma'un", '108. Al-Kavsar', '109. Al-Kafirun', '110. An-Nasr', '111. Al-Masad', '112. Al-Ixlos', '113. Al-Falaq', '114. An-Nas']

def hidoyat1(sura_no = 1):
    """Qur'onning ma'lum surasining to'liq tafsirini qaytaruvchi funksiya"""
    try:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura_no}.json"
        res = r.get(url)
        res = res.json()
        oyat = ''
        manzil = res['chapter']
        l = len(manzil)
        ind = 0
        for i in range(l):
            i = manzil[ind]['text']
            oyat += f"{ind+1}. "
            oyat += i
            ind += 1
            oyat += '\n\n'

        return oyat

    except:
        oyat = "❌ Xato Ma'lumot kiritdingiz ⁉️"


def hidoyat2(sura_no = 1, oyat_no = 1):
    """Qur'onning ma'lum surasining tanlangan oyatining tafsirini qaytaruvchi funksiya"""
    try:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura_no}/{oyat_no}.json"
        res = r.get(url)
        res = res.json()
        oyat = res['text']
        return oyat
    except:
        oyat = "❌ Xato Ma'lumot kiritdingiz ⁉️"


def get_l(sura_no):
    """Qur'onning ma'lum surasini nechta oyatdan tashkil topganini qaytaruvchi funksiya"""
    try:
        url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura_no}.json"
        res = r.get(url)
        res = res.json()
        manzil = res['chapter']
        l = len(manzil)

        return l

    except:
        l = "❌ Xato Ma'lumot kiritdingiz ⁉️"


def hidoyat3(sura_no):
    try:
        url = f"http://api.alquran.cloud/v1/surah/{sura_no}"
        res = r.get(url)
        res = res.json()
        manzil = res['data']['ayahs']
        l = len(manzil)
        oyat = ''
        for i in range(l):
            t = manzil[i]['text']
            oyat += t

        return oyat
    except:
        oyat = "❌ Xato Ma'lumot kiritdingiz ⁉️"



def hidoyat4(sura_no, oyat_no):
    try:
        url = f"http://api.alquran.cloud/v1/surah/{sura_no}"
        res = r.get(url)
        res = res.json()
        manzil = res['data']['ayahs'][oyat_no-1]['text']
        oyat = popstr(manzil)
        return oyat
    except:
        oyat = "❌ Xato Ma'lumot kiritdingiz ⁉️"

def get_audio(sura_no):
    pass