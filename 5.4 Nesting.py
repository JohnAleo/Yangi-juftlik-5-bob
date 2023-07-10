# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 04:55:35 2023

@author: xudoy
"""

#car0={'model':'lacetti', 'rang':'oq',
#      'yil':2018, 'narx':13000,
 #     'km':50000, 'korobka':'avtomat'}

#car1={'model':'nexia3','rang':'qora',
#      'yil':2015,'narx':13000,
#      'km':50000}

#car2={'model':'gentra', 'rang':'qizil',
#      'yil':2019, 'narx':15000,
#      'km':20000,'korobka':'mexanika'}




#car=car0
#print(f"{car['model'].title()},\
#      {car['rang'].title()},\
#          {car['yil']}-yil, {car['narx']}$")

#car=car1
#print(f"{car['model'].title()},\
#      {car['rang'].title()},\
#          {car['yil']}-yil, {car['narx']} $ ")

#car=car2
#print(f"{car['model'].title()},\
#      {car['rang'].title()},\
#         {car['yil']}-yil,{car['narx']} $ ")




#cars=[car0, car1, car2] # lug'atlar ro'yxati
#for car in cars:
#    print(f"{car['model'].title()},"
#          f"{car['rang']} rang,"
#          f"{car['yil']}-yil, {car['narx']} $")


#print(cars[0])
# BIROR LUG'ATDAGI ELEMENTGA MUROJAAT QILISH USULI
#print(cars[0]['model'])
#print(f"{cars[1]['rang'].title()}  "
#      f"{cars[0]['model'].title()}")

# for sikli yordamida bo'sh lug'atlar ham yaratib olishimiz mumkin

#malibus=[]# malibu mashinalari uchun bo'sh ro'yxat yaratdik
#for n in range(10):
#    new_car={# HAR BIR YANGI AVTO UCHUN LUG'AT YARATAMIZ
#        'model':'malibu',
#        'rang':None,#rangi noaniq
#        'yil':2020,
#        'narx':None,#narxi belgilanmagan
#        'km':0,
#        'korobka':'avto'}
#    malibus.append(new_car)#lug'atni ro'yxatga qo'shamiz)
#for malibu in malibus[:3]:
#    malibu['rang']='qizil'
#    #keyingi uchtasiga esa qora
#for malibu in malibus[3:6]:
#    malibu['rang']='qora'
#for malibu in malibus[6:]:
#        malibu['rang']='qora'
#        malibu['korobka']='mexanika'
#for malibu in malibus:
#    if malibu['korobka']=='avto':
#                malibu['narx']=40000
#    else:
#                malibu['narx']=35000
#for malibu in malibus:
#    print(malibu.values())
    
    
    
#laptops=[]
#for n in range(10):    
#    new_laptop={#  HAR BIR YANGI NOUTBOOOK UCHUN LUG'AT YARATAMIZ
#        'model':'macbook',
#        'rang':None,#rangi noaniq
#        'yil':2022,
#        'narx':None,
#        'ishlagan soati':0,
#        'materiali':'carbon fibre'}
#    laptops.append(new_laptop)# RO'YXATNI LUG'ATGA QO'SHAMIZ
#for laptop in laptops[:3]:   
#    laptop['rang']='qora'
   # keyingi uchtasiga esa oq
#for laptop in laptops[3:6]:    
#   laptop['rang']='oq'
#for laptop in laptops[6:]:    
#   laptop['rang']='kulrang'
#   laptop['materiali']='carbon fibre' 
#for laptop in laptops:
#    if laptop['materiali']=='carbon fibre':
#        laptop['narx']=3000
#    else:
#        laptop['narx']=2500
#for laptop in laptops:
#    print(laptop.values())    
   
    
#books=[]
#for n in range(10):
#    new_book={#HAR BIR YANGI KITOB UCHUN LUG'AT YARATAMIZ
#        'genre':'novel',
#        'book cover':'thick',
#        'year':2023,
#        'narx':None,
#        'translated from':'English',
#        'author':'T.Nassem'}
#    books.append(new_book)# RO'YXATNI LUG'ATGA QO'SHAMIZ
#for book in books[:3]:
#    book['rang']='oddiy muqovada'
    #keyingi ikkitasi esa RANGLI MUQOVADA
#for book in books[3:5]:
#    book['rang']='rangli muqovada'
#for book in books[5:]:
#    book['rang']='rasmli muqovada'           
#    book['author']='T.Nassem'
#for book in books:
#    if book['author']=='T.Nassem':
#        book ['narx']=75
#    else:
#        book['narx']=35
#for book in books:
#    print(book.values())
            


#houses=[]
#for n in range(10):
#    new_house={ #HAR BIR YANGI UY UCHUN LUG'AT YARATAMIZ
#        'type':'detached',
#        'area':'400 m sqr',
 #       'location':None,
  #      'price':None,
   #     'rooms':8,
    #    'public transport':'available'
    #}
    #houses.append(new_house)#RO'YXATNI LUG'ATGA QO'SHAMIZ
#for house in houses[:3]:
#    house['location']='suburban'
#for house in houses[3:8]:
#    house['location']='outskirt'
#for house in houses[8:]:
#    house['location']='village'
#    if house['location']=='city center':
#               house['price']=520000
#    else:
#               house['price']=400000
#               print(house.values())
    

pens=[]
for n in range(10):
    new_staff={#HAR BIR YANGI RUCHKA UCHUN LUG'AT YARATAMIZ
    'color':None,
    'price':None,
    'year':2022,
    'manufacturer':'Dip impeks',
    'model':'OOS ALpha',
    'type':'auto'}
    pens.append(new_staff)#RO'YXATNI LUG'ATGA QO'SHAMIZ
for pen in pens[:3]:
    pen['color']='red'
for pen in pens[3:5]:
    pen['color']='black'
    pen['type']='simple'
for pen in pens[5:]:
    pen['color']='green'
    pen['type']='auto'    
for pen in pens:
    if pen['type']=='auto':
        pen['price']=4
    else:
        pen['price']=3
        
for pen in pens:
    print(pen.values())        

juices=[]
for n in range(10):
    new_brand={#HAR BIR YANGI ICHIMLIK UCHUN LUG'AT YARATAMIZ
    'volume':1.5,
    'type':'fizzy',
    'components':None,
    'alcoholic rate':'non alcoholic',
     'manufacturer':'dinay',
     'price':None
     }
    juices.append(new_brand)
for juice in juices[:2]:
    juice['components']='organic'
    juice['price']=5000
for juice in juices[2:7]:
    juice['components']='chemical'
    juice['price']=3000
for juice in juices[7:]:
    juice['components']='organic'
    if juice['components']=='probiotic':    
        juice['alcoholic rate']='non alcoholic'
        juice ['price']=3200
    else:
      juice['price']=3500
for juice in juices:
    print(juice.values())      
   
    
   
    
   
    
    
    
    
    
    
    
    
    
    
    
    



