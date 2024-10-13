import string
from collections import defaultdict

def wyczysc_dokument(dokument):
    # kod analogiczny do wskazówki z prezentacji
    znaki_interpunkcyjne = string.punctuation 
    slowa = ''.join([znak if znak not in znaki_interpunkcyjne else ' ' for znak in dokument])
    return slowa.lower().split() 

# input
liczba_dokumentow = int(input())

dokumenty = []
for dok in range(liczba_dokumentow):
    dokument = input().strip()
    dokumenty.append(dokument)

liczba_zapytan = int(input())

zapytania = []
for zap in range(liczba_zapytan):
    zapytanie = input().strip()
    zapytania.append(zapytanie)

dokumenty_licz_slowa = []

for dokument in dokumenty:
    slowa = wyczysc_dokument(dokument)
    licznik_slow = defaultdict(int) # uzycie kodu z prezentacji
    for slowo in slowa:
        licznik_slow[slowo] += 1 
    dokumenty_licz_slowa.append(licznik_slow)

# sprawdzenie zapytan oraz ustalenie kolejnosci
wyniki = []

for zapytanie in zapytania:
    dokumenty_zapytania = []
    for index, licznik_slow in enumerate(dokumenty_licz_slowa):
        liczba_wystapien = licznik_slow.get(zapytanie.lower(), 0)
        if liczba_wystapien > 0:
            dokumenty_zapytania.append((index, liczba_wystapien))
    
    
    dokumenty_zapytania.sort(key=lambda x: (-x[1], x[0]))
    
    indeksy = [] 
    
    for dokument in dokumenty_zapytania:
        indeks_dokumentu = dokument[0]  
        indeksy.append(str(indeks_dokumentu))  
    
    wynik = "[" + ", ".join(indeksy) + "]"
    wyniki.append(wynik)

# prezentacja wyniku 
for wynik in wyniki:
    print(wynik)

