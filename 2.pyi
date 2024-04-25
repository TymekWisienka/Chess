
# -*- coding: utf-8 -*-

import sys
sys.stdout.reconfigure(encoding='utf-8')

plansza = [['♜','♞','♝','♛','♚','♝','♞','♜'],
           ['♟','♟','♟','♟','♟','♟','♟','♟'],
           ['♙','♙','♙','♙','♙','♙','♙','♙'],
           ['♖','♘','♗','♕','♔','♗','♘','♖']]

for i in range(4):
    plansza.insert(i+2,['G']* 8)

for i in plansza:
    chwila = []
    for j in i:
        chwila.append(j)
for i in plansza:
    print(i)



#print(plansza[wiersze][kolumna])
def przekladanie(wiersze1,kolumna1,wiersze2,kolumna2):

    plansza[wiersze2-1][kolumna2-1] = plansza[wiersze1-1][kolumna1-1]
    plansza[wiersze1-1][kolumna1-1] = 'G'
    kolumna1 = chr(kolumna1)
    print(kolumna1)
przekladanie(wiersze1 = 0, kolumna1 = 1, wiersze2 = 2, kolumna2 = 2)

class bialy(): #Tymek
    #w = wiersz
    #k = kolumna
    def pionek_bialy(w, k):
        #mozliwosci ruchu
        if w == plansza[1]:
            pola_ruchu_pionka = plansza[w+1][k], plansza[w+2][k]
        else:
            pola_ruchu_pionka = plansza[w+1][k]
        #mozliwosci bicia
        pola_bicia_pionka = plansza[w+1][k-1], plansza[w+1][k+1]

    def skoczek_bialy(w, k):
        pola_dla_skoczka = plansza[w+2][k-1], plansza[w+2][k+1], plansza[w+1][k-2], plansza[w+1][k-2], plansza[w-2][k-1], plansza[w-2][k+1], plansza[w-1][k-2], plansza[w-1][k+2]

    def goniec_bialy(w, k):
        pola_gonca = []
        i = j = m = n = 1
        while w + i < 8 and k + i < 8:
            pola_gonca.append(plansza[w+i][k+i])
            i += 1
        while w + j < 8 and k - j >= 0:
            pola_gonca.append(plansza[w+j][k-j])
            j += 1
        while w - m >= 0 and k + m < 8:
            pola_gonca.append(plansza[w-m][w+m])
            m += 1
        while w - n >= 0 and k - n >= 0:
            pola_gonca.append(plansza[w-n][k-n])
            n += 1

    def wierza_biala(w, k):
        pola_wiezy = []
        i = j = m = n = 1
        while w + i < 8:
            pola_wiezy.append(plansza[w+i][k])
            i += 1
        while w - j >= 0:
            pola_wiezy.append(plansza[w-j][k])
            j += 1
        while k + m < 8:
            pola_wiezy.append(plansza[w][k+m])
            m += 1
        while k - n >= 0:
            pola_wiezy.append(plansza[w][k-n])
            n += 1





class czarny(): #Karol
    def pionek_czarny(w, k):
        #mozliwosci ruchu
        if w == plansza[6]:
            pola_ruchu_pionka = plansza[w-1][k], plansza[w-2][k]
        else:
            pola_ruchu_pionka = plansza[w-1][k]
        #mozliwosci bicia
        pola_bicia_pionka = plansza[w-1][k-1], plansza[w-1][k+1]

