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


#car={'name':'bmw','color':'blue','gear':'automatic','max_speed':'360 kmph'}
#print(f"{car['name'].title()},\
#      {car['color']} ray,\
#          {car['gear']} type,\
 #             {car['max_speed']} is the max speed of this bmw")

#Bo'sh lug'at 
#student={}
#student['name']='andrew'
#student['age']=19
#student['faculty']='economy'
#student['university']='Harvard business school'
#print(f"{student['name'].title()} {student['age']}, {student['university'].upper()}")

#cinema={}
#cinema['name']='titanic'
#cinema['genre']='romance,drama'
#cinema['director']='james cameron'
#cinema['imdb rate']='8.7 out of 10'
#cinema['stars']='leonardo di caprio,kate winslet'
#print(f"{cinema['name'].title()},\
#      {cinema['genre']},\
#          {cinema['director'].title()},\
#             {cinema['imdb rate']},\
#                {cinema['stars'].title()}")


# Qiymatni O'zgartirish
#car={}
#car['price']=35000
#car['color']='green'
#car['company']='chevrolet'
#print(f"{car['color']}, {car['price']}, {car['company']} $")

#Kalit So'z-Qiymat Juftligini O'chirish
#car={'company':'Porsche','model':'cayenne','speed':320,'type':'crossover'}
#print(car)
#del car['company']
#print(car)


#engineer={'name':'Pol','speciality':'AI engineering','age':'28','company':'google'}
#print(engineer)

#Amaliyot
#otam={'ism':'akrom','yosh':55,'kasb':'muhandis','mashinasi':'prado'}
#print(otam)
#onam={'ismi':'nargiza','kasbi':'shifokor','biznesi':'meva,gul'}
#print(onam)
#opam={'ismi':'Zebiniso','qiziqishi':'dizaynerlik'}
#print(opam)
#sevimli_taomlar={}
#sevimli_taomlar['jahongir']='jahongir xalimga ishqiboz'
#sevimli_taomlar['zebiniso']='zebiniso uchun manti yaxshi'
#sevimli_taomlar['akrom']='dadamga tandir yoqadi'
#sevimli_taomlar['nargiza']='onam oshni yaxshi pishiradi va istemol qiladi'
#sevimli_taomlar['muzaffar']='muzaffarga shirguruch yoqadi'
#sevimli_taomlar={'jahongir':'xalim','Zebiniso':'manti','akrom':'tandir','nargiza':'osh',\
                 #'muzaffar':'shirguruch'}
#print(f"{sevimli_taomlar['jahongir'].title()}, {sevimli_taomlar['zebiniso'].title()},\
     # {sevimli_taomlar['akrom'].title()}, {sevimli_taomlar['nargiza'].title()},\
     #     {sevimli_taomlar['muzaffar'].title()}")





#dictionary={}
#dictionary['int']="o'zgaruvchining qiymatini butun sonligini ko'rsatadi"
#dictionary['title']='kiritilyotgan qiymatni bosh harfda beradi'
#dictionary['upper']='kiritilayotgan qiymatlarni faqat katta harflarda beradi'
#dictionary['lower']='kiritilayotgan qiymatlarni faqat kichik harflarda beradi'
#dictionary['for']="shart berayotganda uchun ma'nosida keladi"
#dictionary['or']='shart bajarilayotganda 2tadan birortasi bajarilishini anglatadi'
#dictionary['and']='shart bajarilayotganda 2tadan shartning ikkalasi bajarilganda ishlaydi'
#dictionary['float']="integerdan farqli ravishda matnli o'zgaruvchilarni oladi"
#dictionary['sort']='qiymatlarni turlarga ajratadi'
#dictionary['not in']="berilgan qiymatni ro'yxat ichida bo'lmagandagi holatda ishlatiladi"

#print(f"{dictionary['int']},\
#      {dictionary['title']},\
#          {dictionary['upper']},\
#              {dictionary['lower']},\
#                  {dictionary['for']},\
#                      {dictionary['or']},\
#                          {dictionary['and']},\
#                              {dictionary['float']},\
#                                  {dictionary['sort']},\
#                                      {dictionary['not in']}")

#royhat=dictionary
#royhat=['int','title','upper','lower','for','or','and','float','sort','not in']
#soz=input("Biror so'z kiriting : ")
#if soz not in royhat:
# print("Kechirasiz bunday so'z mavjud emas")
#else:
#    print(f"So'z tarjimasi {dictionary}")



#python_izohli_lugati = {
#    'integer':"Butun son",
#    'float':"O'nlik son",
#    'string':"Matn",
#    'list':"Ro'yxat",
#    'tuple':"O'zgarmas ro'yxat"}

#kalit = input("Kalit so'z kiriting:").lower()
#print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

#kalit = input("Kalit so'z kiriting:").lower()
#tarjima = python_izohli_lugati.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


#car_engineering_words={
#    'speedometr':"Tezlikni o'lchovchi asbob",
#    'tire':'shina',
#    'gear':'uzatma',
#    'engine':'dvigatel',
#    'baggage':'yukxona',
#    'break':'tormoz',
#    }

#kalit=input("Kalit so'z kiriting :").lower()
#print(car_engineering_words.get(kalit,"Bunday so'z mavjud emas"))

#kalit=input("Kalit so'zni kiriting :").lower()
#tarjima=car_engineering_words.get(kalit)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f'{kalit.title()} {tarjima} deb tarjima qilinadi')



#math_words={
#    'cosinus':'sonning cosinis qiymati',
#    'sinus':'sonning sinus qiymati',
#    'pi':'3.14 soni',
#    'ln':'natural logarifm',
#    'sqrt':'ildiz'}
    
#key=input("Kalit so'zni kiriting :").lower()
#print(math_words.get(key,"Bunday so'z mavjud emas"))

#key=input("Kalit so'zni kiriting:")
#tarjima=math_words.get(key)
#if tarjima==None:
 #   print("Bunday so'z mavjud emas")    
#else:
#    print(f"{key.title()} {tarjima} deb tarjima qilinadi")



#physics_words={
#    'electron':'manfiy zarra',
#    'ptoton':'musbat zarra',
#    'volt':'kuchlanish belgisi',
#    'amper':'tok kuchi',
#    'atom':"bo'linmas zarra",
#    'neytron':'neytral zarra',
#    'tok':"zaryadli zarrachalarning tartibli harakati"}

#kalit=input("Kalit so'zni kiriritng :").lower()
#print(physics_words.get(key,"Bunday so'z mavjud emas"))

#kalit=input("Kalit so'zni kiriting :")
#manosi=physics_words.get(key)
#if manosi==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit.title()} {manosi} deb tarjima qilinadi")


#politics={
#    'freedom':'ozodlik',
#    'evolution':'inqilob',
#    'liberalism':'liberalizm',
#    'democracy':'xalq hokimiyati',
#    'free market':'ochiq bozor',
#    'realism':'realizm',
#    }

#kalit=input("Kalit so'zni kiriting").lower()
#print(politics.get(key,"Bunday so'z mavjud emas"))

#kalit=input("Kalit so'zni kiriting :")
#tarjima=politics.get(key)
#if tarjima==None:
#    print("Bunday so'z mavjud emas")
#else:
#    print(f"{kalit}tite() {tarjima} deb tarjima qilinadi")


airway={
    'regional get':'mahalliy uchoq',
    'airbus':'fransiya kompaniyasi',
    'loucoster':'kam chiqimli parvoz',
    'helicopter':'vertolyot',
    'charter reys':'maxsus reys',
    'board supervisor':'bord kuzatuvchisi',
    'airplane':'samolyot',
    }

kalit=input("Kalit so'zni kiriting  : ")
print(airway.get(kalit,"Bunday so'z mavjud emas"))
tarjima=airway.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit}title() {tarjima} deb tarjima qilinadi")

























#dictionary={'integer':'butun son',
#            'float':"o'nlik son",
#            'title':"qiymatni bosh harfda beradi",
#            'string':'matn',
#            'or':'yoki'}
#kalit=input("Kalit so'z kiriting :").lower
#manosi=dictionary.get(kalit,"Bunday lug'at mavjud emas")
#if tarjima==None:
#    print("Bunday lug'at mavjud emas")
#else:
#    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")




#taomlar = {
#    'ali':'osh',
#    'vali':'shashlik',
#    'hasan':"lag'mon",
#    'husan':"mastava",
#    'olim':"somsa"
 #   }

#taom = taomlar['ali']
#print(f"Alining sevimli taomi {taom}")





