# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:25:08 2022

@author: beyza
"""

# 1. Kutuphane ekleme
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


 # 2. Veri onişleme
# 2.1 veri yukleme 
veriler = pd.read_csv("satislar.csv")
print(veriler)

aylar = veriler[["Aylar"]]
print(aylar)
satislar = veriler[["Satislar"]]
print(satislar)


# veri on isleme


# ulke boy ve yası ayrı bi data frame de cinsiyeti ayrı bi data frame de bolecegiz
# verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(aylar, satislar, test_size = 0.33, random_state = 0)


# verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

Y_train = sc.fit_transform(x_train)
Y_test = sc.fit_transform(x_test)

#birbirlerine yakın duruma getirilmiş oldu



# model insası (linear regression)
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train) # x_trainden y_traini öğren

tahmin = lr.predict(X_test) 


x_train = x_train.sort_index()
y_train = y_train.sort_index()   # indexe gore sıralayacak


plt.plot(x_train, y_train)
plt.plot(x_test, lr.predict(x_test))

plt.title("Aylara Göre Satış")
plt.xlabel("Aylar")
plt.ylabel("Satislar")




















