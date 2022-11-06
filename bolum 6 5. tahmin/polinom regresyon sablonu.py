# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 10:25:08 2022

@author: beyza
"""

# 1. Kutuphane ekleme
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# veri yukleme 
veriler = pd.read_csv("maaslar.csv")
print(veriler)


# dataframe dilimleme (slice)
x = veriler.iloc[:,1:2]
y = veriler.iloc[:,2:]

# numpy array dizi donusumu
X = x.values
Y = y.values

# lineer regresyon
# dogrusal model olusturma
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

# gorselleştirme
plt.scatter(X, Y, color = "red")
plt.plot(x, lin_reg.predict(X))
plt.show()


# polinomal regresyon
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 2)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

# gorselleştirme
plt.scatter(X, Y, color ="red")
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = "blue")
plt.show()


# 4. dereceden polinom
poly_reg = PolynomialFeatures(degree = 4)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, y)

# gorselleştirme
plt.scatter(X, Y, color = "red")
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color = "blue")
plt.show()
































