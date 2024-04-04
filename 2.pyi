
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

class bialy():
    def pionek_bialy(w, k):
        #mozliwosci ruchu
        if w == plansza[1]:
            pola_ruchu_pionka = plansza[w+1][k], plansza[w+2][k]
        else:
            pola_ruchu_pionka = plansza[w+1][k]
        #mozliwosci bicia
        pola_bicia_pionka = plansza[w+1][k-1], plansza[w+1][k+1]


class czarny():
    def pionek_czarny(w, k):
        #mozliwosci ruchu
        if w == plansza[6]:
            pola_ruchu_pionka = plansza[w-1][k], plansza[w-2][k]
        else:
            pola_ruchu_pionka = plansza[w-1][k]
        #mozliwosci bicia
        pola_bicia_pionka = plansza[w-1][k-1], plansza[w-1][k+1]

