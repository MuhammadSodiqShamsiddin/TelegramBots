def popdigit(word):
    """Matndan faqat raqamlarni ajratib oluvchi funksiya"""
    raqamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    digits = ''
    for i in word:
        if i in raqamlar:
            digits+=i

    digits = int(digits)
            
    return digits

def popstr(word):
    """Matndan faqat harflarni ajratib oluvchi funksiya"""
    raqamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    strings = ''
    for i in word:
        if i not in raqamlar:
            strings += i
                       
    return strings

def get_index(item, liste):
    l = len(liste)
    for e in list(range(l)):
        if type(item) == str:
            if liste[e] == item:
                return e + 1
            
        if type(item) == int:
            if liste[e] == item:
                return e + 1