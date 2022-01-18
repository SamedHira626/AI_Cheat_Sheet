# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:46:00 2018

@author: user
"""

s = "abcdef"
print(s[::-1] )
print(s[::-2])
print(s[::-3])
print(s[::-4])


print("-------------")
print(s[::1])
print(s[::2])
print(s[::3])
print(s[::4])
 

print("-------------")
a = "123456789"
print(a[1::2])
print(a[:-1])
print(a[:-2])
print(a[-1])
print(a[-2])
print(a[2:8:3])


# %%
# list

liste = [1,2,3,4,5,6]
type(liste)

liste_str = ["ptesi","sali","cars"]
type(liste_str)



last_value = liste[-1]

liste_divide = liste[0:3]

liste.append(7)
liste.remove(7) # bu 7 yi siler, pop(7) 7. indeksi siler
liste.reverse()
liste2 = [1,5,4,3,6,7,2]
liste2.sort()

print(len(liste2))
liste2.insert(7,8) # 7.indekse 8'i ekle
print(len(liste2))
liste2.insert(10,9) # 8 9 olmasa bile en sona ekler
print(liste2)
print(len(liste2))
string_int_liste = [1,2,3,"aa","bb"]

liste2.clear()
print("silinmiş liste = " , liste2)
#%%

sum([1,2,3]) 
sum([1,2,3,4])
t = [1]
y = [2]
s = [3]
sum(t)
#sum(1,2,3)      bu HATA verir
a = list("dataiteam") 
print(a[0])
print(list("dataiteam")) 
#%%
liste = ["a","b","c","d"]
yeniliste = liste.copy()
print(yeniliste) # ["a","b","c","d"]
#%%
liste1 = ["A","B","C"] 
liste2 = ["D","E"]
liste3 = liste1 + liste2
print(liste3) # ["A","B","C","D","E"]

#%%
liste1 = ["A","B","C"] 
liste2 = ["D","E"]
liste1.extend(liste2)
print(liste1) # ["A","B","C","D","E"]

#%%
liste1 = ["A","B","C"] 
liste2 = ["D","E"]
for x in liste2: liste1.append(x)
print(liste1) # ["A","B","C","D","E"]
#%%
liste = [14,36,2,95,43,0,66]
liste2 = liste.copy()
liste.sort(reverse=True)
liste2.sort()

print(liste) # [95, 66, 43, 36, 14, 2, 0]
print(liste2)
#%%
liste = [14,36,2,95,43,0,66,95]
print(liste.index(95)) # 3
#%%

# %% tuple           DEĞİŞMEZ

t = (1,2,3,3,4,5,6)
t.count(3)
t.index(3)

abc = 3,33,33,"abc"
a_b=33,333,333

print(abc)
print(type(abc))
print(a_b)
print(type(a_b))
#%%
demet1 = ("A","B","C") 
demet2 = ("D","E")

demet3 = demet1 + demet2

print(demet3) # ("A","B","C","D","E")

    
# %% dictionary

dictionary = {"ali":32,"veli":45,"ayse":13}
# dictionary["ali"] , 32 verir
print(dictionary["ali"])
print(dictionary.get("ali"))
# ali ,veli ,ayse = keys
# 32,45,13 = values
#%%
sozluk = {
         "ulke" : "Türkiye",
         "sehir" : "Ankara",
         "ilce"   : "Yenimahalle"
         }

print(sozluk.items(),"\n")
for x,y in sozluk.items():
    print("key: " + x + " -- " + "value: " + y)

# Anahtar: ulke -- Değer: Türkiye
# Anahtar: sehir -- Değer: Ankara
# Anahtar: ilce -- Değer: Yenimahalle
#%%
sozluk = {
         "marka" : "BMW",
         "model" : "i8",
         "yil"   : 2019
         }

sozluk.pop("yil")

print(sozluk)       # {'marka': 'BMW', 'model': 'i8'}
#%%
sozluk = {
         "marka" : "BMW",
         "model" : "i8",
         "yil"   : 2019
         }

sozluk.popitem()

print(sozluk)       # {'model': 'i8', 'yil': 2019}
#%%
sozluk = {
          "sehir1" : {
                      "sehir" : "Ankara",
                      "plaka" : 6
                     },
          "sehir2" : {
                      "sehir" : "İstanbul",
                      "plaka" : 34
                     },
         "sehir3" : {
                      "sehir" : "Kayseri",
                      "plaka" : 38
                     },
         }
print(sozluk["sehir1"]["plaka"])

#%%
def deneme():
    dictionary = {"ali":32,"veli":45,"ayse":13}
    return dictionary

dic = deneme()

print(dic.values())
print(dic.keys(),"\n")

a = {"x":2,"y":3}
b = dict(zip(a.values(),a.keys()))
print(b)
print(tuple(b))
print(b.keys())
print(b.values(),"\n")

# zip lediğin şeyi tuple veya dict'e çevir

c = ("John", "Charles", "Mike")
d = ("Jenny", "Christy", "Monica")

x = zip(c, d)
print(x,"\n")
print(type(x))
#use the tuple() function to display a readable version of the result:

print(tuple(x))
x = tuple(x)
print(x)
print("--------")

a = [1,2]
b = [3,4]
d = [5,6]
c = zip(a,b)
print(c)
c = list(c)
print(c)
print(c[0])
print(c[0][1])
e = list(zip(c,d))
print(e)
#%%
x = ('anahtar1', 'anahtar2', 'anahtar3') 
y = 0

sozluk = dict.fromkeys(x, y)

print(sozluk) # {'anahtar2': 0, 'anahtar3': 0, 'anahtar1': 0}
#%%
x = ('anahtar1', 'anahtar2', 'anahtar3') 
print(type(x))
y = [1,2,3]
print(type(y))

sozluk = dict.fromkeys(x, y)

print(sozluk) # {'anahtar2': 0, 'anahtar3': 0, 'anahtar1': 0}
print(type(sozluk))
print(sozluk['anahtar1'][1])
# %% conditionals
# if else statement

var1 = 10
var2 = 20

if(var1 > var2):
    print("var1 buyuktur var2")
elif(var1 == var2):
    print("var and var2 esitler")
else:
    print("var1 kucuktur var2")


liste = [1,2,3,4,5]

value = 3
value2 = 4
if value in liste:
    print("evet {} {} degeri listenin icinde".format(value,value2))
else:
    print("hayir")


keys = dictionary.keys()  # ali veli ve ayşe keys oluyor
turler = type(keys)
if "can" in keys:
    print("evet")
else:
    print("hayir")


# %% 

# 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005
    
def year2Century(year):
    """
    year to century
    """
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year) == 3):
        if(str_year[1:3] == "00"):  # 100 ,200 300, 400 ... 900
            return int(str_year[0])
        else:                       # 190, 250, 450
            return int(str_year[0])+1
    else:                           # 1750, 1700, 1805
        if(str_year[2:4]=="00"):    # 1700, 1900, 1100
            return int(str_year[:2])
        else:                       # 1705, 1645, 1258
            return int(str_year[:2])+1

# %% loops
# for loop
    
    
for each in "ankara ist":
    print(each)
print("-------------")    
for each in "ankara ist".split(): 
    print(each)
print("-------------")    
   
liste = [1,4,5,6,8,3,3,4,67]
 
summation = sum(liste)    

count = 0
for each in liste:
    count = count + each
print(count)
    
# while loop
    
i = 0
while(i <4):
    print(i)
    i = i + 1


sinir = len(liste)   
each = 0
count = 0
while(each < sinir):
    count = count + liste[each]
    each = each + 1 

 
# %%


# liste verecegim
#sizden bu listenin icindeki en kucuk sayiyi bulmanizi istiyorum

liste = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

mini = 100000
for each in liste:
    if(each < mini):
        mini = each
    else:
        continue
print(mini)


#%%

a = (1,2)
print(a)
print(type(a))

strin = str(a)
print(strin)
print(type(strin))








