# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 01:56:43 2021

@author: Samed
"""

a = "        Suyu israf etmeyin! "
print(a.strip()) # metinin başındaki ve sonundaki boşlukları temizlemek için strip()

#%%
b = "Ağaçlar ciğerlerimizdir"
print(b.upper()) # metini tamamen büyük harflere çevirmek istiyorsanız upper()

#%%
a = "AĞAÇLAR CİĞERLERİMİZDİR"
print(a.lower()) # ağaçlar ciğerlerimizdir
#%%
a = "Muz tatlı bir meyvedir"

print(a.replace("Muz", "Çilek"))
#%%
a = "Kayseri,Nevşehir,Kırşehir İç Anadolu bölgesindedir"

print(a.split("e")) # ['Kayseri', 'Nevşehir', 'Kırşehir İç Anadolu bölgesindedir']
print(a.split(","))
#%%
txt = "En sevdiğim hava yağmurlu havadır"

x = "mur" in txt

print(x)            # True
#%%
txt = "En sevdiğim hava yağmurlu havadır"

x = "mur" not in txt 

print(x) # False
#%%
a = "Kerteriz"
b = " "
c = "Blog"

print(a+b+c)                     # Kerteriz Blog
print(c + "yazmak düzeldir")     # Blog yazmak güzeldir
#%%
a = "elma"
print(a*3)        # elmaelmaelma
#%%
yas = 24
hava = "Yağmurlu"
hedef = "Okula"

metin = "Dün akşam {} yaşlarında bir genç {} havada yürüyerek {} gidiyordu"

print(metin.format(yas,hava,hedef))       # Dün akşam 24 yaşlarında bir genç Yağmurlu havada yürüyerek Okula gidiyordu
#%%
metin = "Bu aralar "Şeker Portakalı" kitabını okuyorum"
print(metin) # !! HATA !!
#%%
metin = "Bu aralar 'Şeker Portakalı' kitabını okuyorum"
print(metin) # Bu aralar 'Şeker Portakalı' kitabını okuyorum
#%%
metin = "Bu aralar \"Şeker Portakalı\" kitabını okuyorum"
print(metin) # Bu aralar "Şeker Portakalı" kitabını okuyorum
#%%

a = [1]
b = tuple(a)
print(b)
b=type(b)
print(b)
#%%
tpl = (1)
ary = list(tpl)   # bu hata verir, bir şey tuple'a dönüşebilir ama tuple bir şeye dönüşemez
# print(type(ary))
#%%

myDict = {"name": "John", "country": "Norway"}
test = "TEST"
samed = "samed"
x = test.join(myDict)

print(x)
print(samed.join(test))
#%%
