# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:25:08 2022

@author: beyza
"""

# 1. Kutuphane ekleme
import pandas as pd
import numpy as np
import matplotlib as plt

 # 2. Veri onişleme
# 2.1 veri yukleme 
veriler = pd.read_csv("veriler.csv")
print(veriler)

# veri on isleme
# sadece boyu yazdırmak istersek
boy = veriler[["boy"]]
print(boy)

# boy ve kiloyu yazdırmak istersek 
boykilo = veriler[["boy","kilo"]]
print(boykilo)

# eksik veriler
from sklearn.impute import SimpleImputer
imputer= SimpleImputer(missing_values=np.nan, strategy="mean")
Yas = veriler.iloc[:,1:4].values
# butun satırlardaki 1 den 4 e kadar olan degerler
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
# fit fonk ogrenilecek olan deger
# yasın 1 den 4 e kadar olan kolonlarını ogrenmesini saglıyorz
# imputer sayısal kolonlar uzerinde ogrenme işlemi yapar. 
# simpleImputerdaki strategy mean oldugu icin kolonların ortalama degerini ogrenir.
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)



# encoder: Kategorik -> Numeric e donus saglıyor
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing 

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)




# encoder: Kategorik -> Numeric e donus saglıyor
c = veriler.iloc[:,-1:].values
print(c)

from sklearn import preprocessing 

le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(veriler.iloc[:,-1])
print(c)

ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()
print(c)


# numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data = ulke, index = range(22), columns = ["fr", "tr", "us"])
print(sonuc)


sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ["boy", "kilo", "yas"])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1]
print(cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ["cinsiyet"])
print(sonuc3)

# dataframe birleştirme işlemi
s = pd.concat([sonuc, sonuc2], axis = 1)
print(s)

s2 = pd.concat([s, sonuc3], axis = 1)
print(s2)



# ulke boy ve yası ayrı bi data frame de cinsiyeti ayrı bi data frame de bolecegiz
# verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)

# verilerin olceklenmesi
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

#birbirlerine yakın duruma getirilmiş oldu




from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train ,y_train)

y_pred = regressor.predict(x_test)


boy = s2.iloc[:,3:4].values  # bagımlı degiskenler iceren boy kumesi
print(boy)

sol = s2.iloc[:,:3]
sag = s2.iloc[:,4:]


veri = pd.concat([sol, sag], axis = 1)  #bagımsız degiskenler iceren veri kumesi 
print(veri)

x_train, x_test, y_train, y_test = train_test_split(veri, boy, test_size = 0.33, random_state = 0)
# bagımsız degisken olan verileri kullanarak bagımlı deisken olan boya gore bol


# tahmin etmesini isteyecegiz
r2 = LinearRegression()
r2.fit(x_train ,y_train)

y_pred = r2.predict(x_test)


import statsmodels.api as sm

X = np.append(arr = np.ones((22,1)).astype(int), values = veri, axis = 1)
X_l = veri.iloc[:,[0,1,2,3,4,5]].values
X_l = np.array(X_l, dtype= float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())


X = np.append(arr = np.ones((22,1)).astype(int), values = veri, axis = 1)
X_l = veri.iloc[:,[0,1,2,3,5]].values
X_l = np.array(X_l, dtype= float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())


X = np.append(arr = np.ones((22,1)).astype(int), values = veri, axis = 1)
X_l = veri.iloc[:,[0,1,2,3]].values
X_l = np.array(X_l, dtype= float)
model = sm.OLS(boy,X_l).fit()
print(model.summary())














