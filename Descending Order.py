# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:58:42 2020

@author: Rebeca
"""

def descending_order(y):
    lis1 = []
    for i in str(y):
        lis1.append(int(i))

    lis2=[]
    for times in range(len(lis1)):
        biggest=lis1[0]
        b_num=0
        for i in range(len(lis1)):
            if lis1[i] > biggest :
                biggest = lis[i]
            if lis1[i] == biggest :
                b_num += 1
        lis2.append(biggest)
        lis1.remove(biggest)
    ll = ''
    for i in lis2:
        l=str(i)
        ll=ll+ l
    return ll
