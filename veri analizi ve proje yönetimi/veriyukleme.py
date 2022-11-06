# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:25:08 2022

@author: beyza
"""


import pandas as pd
import numpy as np
import matplotlib as plt


veriler = pd.read_csv("veriler.csv")
print(veriler)

# sadece boyu yazdırmak istersek
boy = veriler[["boy"]]
print(boy)

# boy ve kiloyu yazdırmak istersek 
boykilo = veriler[["boy","kilo"]]
print(boykilo)

class insan:
    boy = 196
    def kosmak(self, a):
        return a+10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))

l = [1,2,3]  # listeler koseli parantezle gosterilir.
# herhangi bir liste elemanına indexle erişmek mumkun.
