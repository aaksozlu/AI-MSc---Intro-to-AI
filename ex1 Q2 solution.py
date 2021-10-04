#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:05:25 2021

@author: aziz
"""

import os
import pandas as pd

path = "/home/aziz/Desktop/City AI MSc Files/Intro to AI INM701/Week 1"

filename_read = os.path.join(path, "iris.csv")
df = pd.read_csv(filename_read, na_values=['NA', '?'])

print(df)

df_wo_petal = df[df.petal_w <1.0]

print(df_wo_petal)

df = df.sort_values(by='sepal_l', ascending=True)

print(df)

df.to_csv('/home/aziz/Desktop/City AI MSc Files/Intro to AI INM701/Week 1/Iris_Sepal_sorted.csv')
print("Export Succesful")

print("Variance of sepal_l is ", df.loc[:,"sepal_l"].var())