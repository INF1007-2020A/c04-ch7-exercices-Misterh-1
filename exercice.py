#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import sys

from turtle import *
#sys.path.insert(1, "C:\Users\User\PycharmProjects\c04-ch6-exercices-Misterh-1" )

# TODO: Définissez vos fonction ici

#def calcul_volume(a, b, c, m_vol):
  #  volume = (4 * math.pi * a * b * c)/3
   # m = m_vol*volume
   # return volume, m

def tree_draw(dictionnaire, lenght, pensize):
    new_dict = dict()
    cle = 0
    red = 0
    if pensize > -1.5:
        width(pensize)
        for key, items in dictionnaire.items():
            penup()
            setx(items[0])
            sety(items[1])
            #setpos(items[0], items[1])
            if items[2] <= 90:
                red = items[2]/2

            setheading(items[2] - red)
            pendown()
            forward(lenght)
            cle += 1
            new_dict[cle] = [xcor(), ycor(), heading()]
            penup()
            setx(items[0])
            sety(items[1])
            #setpos(-items[0], items[1])
            setheading(items[2] + red)
            pendown()
            forward(lenght)
            cle += 1
            new_dict[cle] = [xcor(), ycor(), heading()]
            print(new_dict)
    else:
        done()
    tree_draw(new_dict, lenght - 10.5, pensize - 2.5)
    done()

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # Exo1
    #tuple = calcul_volume(a=2, b=4, c=2, m_vol=10)
    #print(f"Le volume est {tuple[0]} et la masse volumique est {tuple[1]}")
    penup()
    setpos(0, -100)
    pendown()
    color('green')
    width(10)
    setheading(90)
    forward(100)
    coordonnees = {1: [0, 0, 90]}
    tree_draw(coordonnees, 90, 10)
    pass
