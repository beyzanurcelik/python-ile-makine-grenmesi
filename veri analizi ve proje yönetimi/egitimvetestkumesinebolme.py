# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:25:08 2022

@author: beyza
"""


import pandas as pd
import numpy as np
import matplotlib as plt


veriler = pd.read_csv("eksikveriler.csv")
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


# eksik veriler
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan, strategy="mean")

Yas = veriler.iloc[:,1:4].values
# butun satırlardaki 1 den 4 e kadar olan degerler
print(Yas)
print("XXXXXXXXXXXXXXXXXXX")
imputer = imputer.fit(Yas[:,1:4])
# fit fonk ogrenilecek olan deger
# yasın 1 den 4 e kadar olan kolonlarını ogrenmesini saglıyorz
# imputer sayısal kolonlar uzerinde ogrenme işlemi yapar. 
# simpleImputerdaki strategy mean oldugu icin kolonların ortalama degerini ogrenir.
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)


ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing 

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)


print(list(range(22)))
sonuc = pd.DataFrame(data = ulke, index = range(22), columns = ["fr", "tr", "us"])
print(sonuc)


sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ["boy", "kilo", "yas"])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1]
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ["cinsiyet"])
print(sonuc3)


s = pd.concat([sonuc, sonuc2], axis = 1)
print(s)

s2 = pd.concat([s, sonuc3], axis = 1)
print(s2)



# ulke boy ve yası ayrı bi data frame de cinsiyeti ayrı bi data frame de bolecegiz
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)


























