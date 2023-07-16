# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 20:43:55 2023

@author: xudoy
"""

#LUG'AT ICHIDA LUG'AT

dasturchilar={
    'ali':['python',  'c++'],
    'vali':['html',  'css',  'js'],
    'hasan':['php',  'sql'],
    'husan':['python',  'php'],
    'maryam':['c++',  'c#']
    }
for ism,tillar in dasturchilar.items():
    print(f"\n{ism.title()}:",end='')
    for til in tillar:
        print(f'{til.upper()}',end='')
        
        
#LUG'AT ICHIDA LUG'AT
hamkasblar={
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']},
    
    'vali':{'familiya':'aliyev',
            'tyil':2001 ,
            'malumot':"o'rta maxsus",
            'tillar':['html','css','js']},
    
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['pyhton','php']}}
for ism,info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan. \n"
          f"Ma'lumoti: {info['malumot']}.\n"
          "Quyidagi dasturlash tilllarini biladi:")
for til in info['tillar']:
    print(til.upper())

# AMALIYOT
mashhurlar={
    'leonardo di caprio':{"americada tug'ilgan aktyor.Titanic va boshqalarda bosh rol ijrochisi"},
    'c ronaldo':{'38 yosh portugaliyada tavallud topgan futbolchi},
    'zaha hadid':['arxitektor','lvianda tugilgan','the best architect'],
    'eynshteyn':['fizik','atom energiya ixtirochisi','nobel sohibi']}
for ism, tariflar in mashhurlar.items():
    print(f"\n{ism.title()}:",end='')
    for tarif in tariflar:
        print(f'{tarif.upper()}',end='')
































