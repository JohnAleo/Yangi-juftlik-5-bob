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

#laptops={'hp','samsung','mac'}
#laptops.add('imac')
#print(laptops)


# TO'PLAMDAN ELEMENT O'CHIRISH
# To'plamdan element o'chirish uchun .discard() va .remove() metodlaridan 
#foydalanamiz

#mevalar={'anjir','uzum','anor','banan','olcha','apelsin','gilos'}
#mevalar.remove('uzum')
#print(mevalar)
#mevalar.discard('banan')
#print(mevalar)

#daraxt={'terak','tol','jiyda','olma','mahogany','popplar','oak','eman'}
#daraxt.remove('majnuntol') # remove metodi ro'yxatda yo'q qiymat bo'ganda Key error chiqaradi
#daraxt.discard('tol')
#daraxt.discard('pooplar')
#daraxt('bodom')
#print(daraxt)

#sonlar={1,2,3,4,5,6,7,89,87,54,65,24,28,36,9,7,4,52,6,5,2,4,45,522,3,36}
#son=sonlar.pop()
#print(son) # pop elementi to'plamdan ixtiyoriy elementni sug'urib oladi chunki indeks aniq bo'maydi
#print(sonlar)

#products={'meat','water','onion','banan','bread','juice','sugar','salt'}
#product=products.pop()
#print(product)
#print(products)

# TO'PLAMLAR USTIDA AMALLAR
# IKKI TO'PLAMNI BIRLASHTIRISH
#A={1,2,3,4}
#B={3,4,5,6}
#C=A|B
#print(C)
#D=A.union(B)
#print(D)

#chevrolet={'lacetti','nexia','suburman','tahoe','equinox'}
#ford={'rapter','taaurus','explorer','shalby'}
#american_cars=chevrolet|ford
#print(american_cars)

#hunarmandlar={'kulol','haykaltarosh','usta','stomatolog','rassom','sartarosh'}
#kasb_egalari={'ustoz','dasturchi','stomatolog','dizayner','sartaarosh','shifokor'}
#mehnatga_layoqatlilar=(hunarmandlar|kasb_egalari)
#print(mehnatga_layoqatlilar)

#kompyuter={'lg','samsung','microfoft','apple','msi'}
#laptop={'lenovo','apple','sony','hp','samsung','acer'}
#print(kompyuter|laptop)

#qiziqchilar={'erik haydar','bravo','million','mirshakar fayzulloyev'}
#reperlar={'shaka','erik haydar','shoxrux','shaxriyor','konsta'}
#sanatkorlar=qiziqchilar|reperlar
#print(sanatkorlar)

#kompozitorlar={'bax','motsart','shopenhauer'}
#olimlar={'nyuton','galiley','paskal','amper','eynshteyn'}
#ziyolilar=kompozitorlar|olimlar
#print(ziyolilar)

# IKKI TO'PLAMNING BIR XIL ELEMENTLAINI TOPISH
#goshtli_taomlar={'manti','norin','shashlik','osh','lagmon','qizilcha'}
#xamir_taomlar={'manti','norin','xonim','yupqa','quymoq','lagmon','gilmindi'}
#(goshtli_taomlar&xamir_taomlar)
#print(goshtli_taomlar&xamir_taomlar)
#print(goshtli_taomlar.intersection(xamir_taomlar))


#A={'olma','uzum','gilos','banan','shaftoli','behi'}
#B={'ananas','behi','kiwi','anjir','banan','qulupnay','mandarin'}
#print(A&B)
#print(A-B)# print(A.difference(B)) kabi ham beriladi A ning B da farqi yoki ayirmasi
#print(B-A)# print(B.difference(A)) kabi ham beriladi B ning A dan farqi yoki ayirmasi
#print(A^B)# bir vaqtda ikkalasida mavjuda umumiy el ni sug'urib olgandagi holat


# AMALIYOT
#rang={'qizil','kulrang','yashil'}
#rang.add('zangori')
#print(rang)
#rang.update(['yashil','sariq','binafsha','pushti'])
#print(rang)

#tumanlar={'yakkabog','kitob','shahrisabz','qarshi'}
#tumanlar.add('qamashi')
#print(tumanlar)
#tumanlar.update(['zangiota','sergeli','yangihayot'])
#print(tumanlar)

#brand={'gucci','dolce gabbana','versace'}
#brand.add('chanel')
#print(brand)
#brand.update(['prada','valenciaga','louis vuitton'])
#print(brand)

#set1={10,20,30,40,50}
#set2={30,40,50,60,70}
#set3=set1&set2
#print(set3)
#print(set1^set2)
#print(set1|set2)
#print(set1-set2)



#phone1={'iphone','samsung','sony','toshiba','siemens'}
#phone2={'iphone','nokia','motorola','google','samsung'}
#phone3=phone1.intersection(phone2)
#print(phone3)
#print(phone1^phone2) #yoki print(phone1.symmetric_difference(B))
#print(phone1|phone2)
#print(phone1-phone2)# yoki print(phone1.difference(phone2))



#laptop1={'hp','acer','asus','msi','toshiba','mac'}
#laptop2={'lenovo','mac','genius','hp','samsung','msi'}
#laptop3=laptop1.intersection(laptop2)
#print(laptop3)


#AMALIYOT
#a={'yashil','qizil','malla'}
#a.add('binafsha')
#print(a)

#a.update(['siyoh','pushti','zangori'])
#print(a)

#set1={10,20,30,40,50}
#set2={30,40,50,60,70}
#print(set1&set2)
#print(set1.intersection(set2))
#print(set1-set2)
#print(set1.difference(set2))
#print(set2-set1)
#print(set2.difference(set1))
#print(set1^set2)
#print(set1.symmetric_difference(set2))







bozorlik={'choy','non','kartoshka','tuxum','sut'} # SOTIB OLINISSHI KERAK MAHSULOTLAR
mahsulotlar=['non','sut','tuxum','olma','un','tuz'] # DO'KONDA BOR MAHSULOTLAR
yoq_mahsulotlar=bozorlik-mahsulotlar
print(yoq_mahsulotlar)

bor_mahsulotlar=bozorlik&mahsulotlar
print(bor_mahsulotlar)
input("Olmoqchi bo'lgan mahsulotingizni kiriting :")
buyurtmalar=[]
for n in range:
































