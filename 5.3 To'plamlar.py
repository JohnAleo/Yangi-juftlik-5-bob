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


#mevalar={'anjir', 'olma','uzum'}
#mevalar.add('banan')
#print(mevalar)
#mevalar.update(['ananas','kiwi'])
#print(mevalar)

#car={'bmw','nexia','porsche'}
#car.update(['supra','fiat','camaro'] )
#print(car)

#fruits={'apple','banana','melon','peach'}
#fruits.add('lime')
#print(fruits)


#phone={'iphone','samsung','nokia'}
#phone.update(['sony','goggle','sm'])
#print(phone)

laptops={'hp','samsung','mac'}
laptops.add('imac')
print(laptops)


# TO'PLAMDAN ELEMENT O'CHIRISH
# To'plamdan element o'chirish uchun .discard() va .remove() metodlaridan 
#foydalanamiz

mevalar={'anjir','uzum','anor','banan','olcha','apelsin','gilos'}
mevalar.remove('uzum')
print(mevalar)
mevalar.discard('banan')
print(mevalar)

#daraxt={'terak','tol','jiyda','olma','mahogany','popplar','oak','eman'}
#daraxt.remove('majnuntol') # remove metodi ro'yxatda yo'q qiymat bo'ganda Key error chiqaradi
#daraxt.discard('tol')
#daraxt.discard('pooplar')
#daraxt('bodom')
#print(daraxt)

sonlar={1,2,3,4,5,6,7,89,87,54,65,24,28,36,9,7,4,52,6,5,2,4,45,522,3,36}
son=sonlar.pop()
print(son) # pop elementi to'plamdan ixtiyoriy elementni sug'urib oladi chunki indeks aniq bo'maydi
print(sonlar)

products={'meat','water','onion','banan','bread','juice','sugar','salt'}
product=products.pop()
print(product)
print(products)





































