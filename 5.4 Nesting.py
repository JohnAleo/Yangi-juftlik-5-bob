# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 04:55:35 2023

@author: xudoy
"""

car0={'model':'lacetti', 'rang':'oq',
      'yil':2018, 'narx':13000,
      'km':50000, 'korobka':'avtomat'}

car1={'model':'nexia3','rang':'qora',
      'yil':2015,'narx':13000,
      'km':50000}

car2={'model':'gentra', 'rang':'qizil',
      'yil':2019, 'narx':15000,
      'km':20000,'korobka':'mexanika'}




car=car0
print(f"{car['model'].title()},\
      {car['rang'].title()},\
          {car['yil']}-yil, {car['narx']}$")

car=car1
print(f"{car['model'].title()},\
      {car['rang'].title()},\
          {car['yil']}-yil, {car['narx']} $ ")

car=car2
print(f"{car['model'].title()},\
      {car['rang'].title()},\
         {car['yil']}-yil,{car['narx']} $ ")




cars=[car0, car1, car2] # lug'atlar ro'yxati
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rang']} rang,"
          f"{car['yil']}-yil, {car['narx']} $")


print(cars[0])
# BIROR LUG'ATDAGI ELEMENTGA MUROJAAT QILISH USULI
print(cars[0]['model'])
print(f"{cars[1]['rang'].title()}  "
      f"{cars[0]['model'].title()}")

# for sikli yordamida bo'sh lug'atlar ham yaratib olishimiz mumkin

malibus=[]# malibu mashinalari uchun bo'sh ro'yxat yaratdik
for in range(5)



























