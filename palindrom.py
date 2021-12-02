#import locale
#locale.setlocale(locale.LC_ALL,'Polish')

def only_letter(str):
    """
       funkcja zwraca string pozbawiony 
       innych znaków niż litery
    """
    str_only_alfa=''
    for char in str:
       if char.isalpha():
        str_only_alfa += char
    return str_only_alfa

def palindrom(str):
    """
       funkcja sprawdza, czy string jest palindromem
       return - True/False
    """
    word=only_letter(str)
    word=word.lower()
    cc=len(word)
    flaga=True
    for i in range(int(cc/2)):
        if word[i]!=word[cc-1-i]:
           flaga=False
    return flaga

print(palindrom('Kobyła ma MAŁY bok.'))