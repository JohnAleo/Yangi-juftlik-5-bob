# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:50:10 2023

@author: xudoy
"""

#sonlar={1,2,3}
#print(sonlar)

#ismlar={'Azamat','laziz','javohir'}
#print(ismlar)

#sonlar1={4,4,1,1,1,1,3,5,45,48,78,95,95}# 1xil solarni faqat bir marta oladi
#print(sonlar1)

#a=set() # bo'sh to'plam 

#mevalar=['olma','anjir','olma','uzum','olma','uzum',]
#mevalar=set(mevalar)
#print(mevalar)
#mevalar=list(mevalar)
#print(mevalar)

#  {}-to'plam belgisi
#  []-ro'yxat belgisi

#To'plamga element qo'shish
#Bitta element qo'shish uchun add metodidan foydalaniladi
# Bir nechta element qo'shish uchun update metodidan foydalaniladi


mevalar={'anjir', 'olma','uzum'}
mevalar.add('banan')
print(mevalar)
mevalar.update(['ananas','kiwi'])
print(mevalar)

car={'bmw','nexia','porsche'}
car.update(['supra','fiat','camaro'] )
print(car)

fruits={'apple','banana','melon','peach'}
fruits.add('lime')
print(fruits)






