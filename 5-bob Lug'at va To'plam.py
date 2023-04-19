# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 18:08:45 2023

@author: xudoy
"""

#lugat=dictionary  to'plam= set
#key-value pair=kalit-qiymat juftligi

#car={'model':'ferrari', 'rang':'qizil','uzatma':'avtomat'}
#bu yerda model va rang mos ravishda kalit so'zlar ferrari va qizil so'zlari
# mos ravishda kalit so'zlarning qiymatlari

#5.2 Lug'at bilan ishlash
#car={'model':'ferrari','rang':'qizil'}
#print(car['model'])
#print(car['rang'])

#talaba={'ism':'morod olimov', 'yosh':20,'t_yil':2000}
#print(f"{talaba['ism'].title()},\
#      {talaba['t_yil']}-yilda tug'ilgan,\
 #         {talaba['yosh']} yoshda")


#car={
#     'manufacturer':'GM',
#     'model':'Malibu',
#     'color':'Black',
#     'gear':'Automatic',
#     'year':2023,
#     'price':40000
#     }

#talaba={'ism':'murod olimov','yosh':20,'t_yil':2000}
#print(f"{talaba['ism'].title()},\
#      {talaba['t_yil']}-yilda tug'ilgan,\
#          {talaba['yosh']} yoshda")

#murabbiy={'ism':'asliddin','yosh':30,'t_yil':1993}
#print(f"{murabbiy['ism'].title()},\
#      {murabbiy['t_yil']}-yilda tug'ilgan,\
#          {murabbiy['yosh']} yoshda")


#shifokor={'ism':'a.xalikulov','mutaxassislik':'travmotolog','faoliyati':'5 yil'}
#print(f"{shifokor['ism'].title()},\
#      {shifokor['mutaxassislik']} sohasida mutaxassis,\
#          {shifokor['faoliyati']} dan beri shu sohada faoliyat yuritadi")

#car={'name':'mercedes','price':'65000 usd','year of manufactured':2020}
#print(f"{car['name'].title()},\
#      {car['price']} you should pay,\
#          {car['year of manufactured']} is the the time the car made")

#president={'name':'j.biden','country':'usa','age':'79 years old','governing period':'4 year'}
#print(f"{president['name'].title()},\
#      {president['country']} come from,\
#          {president['age']} man")



#get() metodi
#place={'name':'tashkent','republic':'uzbekistan','continent':'central asia'}
#print(f"{place['name'].title()},\
#      located in {place['republic'].title()},\
#      located in {place['continent'].title()}")
#weather=place.get('weather','Bunday kalit mavjud emas')

#car={'make':'gm','color':'black','price':30000,'gear':'automatic',
#     'model':'malibu','year':'automatic'}
#print(f"{car['model'].title()},\
#      made by {car['make'].title()},\
 #         rangi {car['color']},\
#              narxi {car['price']} USD,\
#                  uzatmasi {car['gear']}")
#salon=car.get('salon','Bunday kalit mavjud emas')
#disk=car.get('disk','Bunday kalit mavjud emas')


#YANGI JUFTLIK qo'shish
#talaba={'ism':'Allayev Feruz','yosh':20,'t_yil':2000}
#print(f"{talaba['ism'].title()},\
#      {talaba['t_yil']}-yilda tug'ilgan,\
#       {talaba['yosh']} yoshda")
#talaba['kurs']=4
#talaba['fakultet']='informatika'
#print(talaba)

#qishloq={'nom':'Nurli yo\'l', 'aholisi':2000,'mahallalar soni':7,'maydoni':'800 ga'  }
#print(f"{qishloq['nom'].title()},\
#      {qishloq['aholisi']} miqdorida odam yashaydi,\
#          {qishloq['mahallalar soni']} dona mahalladan iborat,\
#              {qishloq['maydoni']} hududni o'z ichiga oladi")


car={'name':'bmw','color':'blue','gear':'automatic','max_speed':'360 kmph'}
print(f"{car['name'].title()},\
      {car['color']} ray,\
          {car['gear']} type,\
              {car['max_speed']} is the max speed of this bmw")




















