# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:32:34 2018

@author: user
"""

# %%
# variable (degisken)
# variable
var1 = 10 # integer = int
var2 = 15 
gun = "pazartesi" # string
var3 = 10.0 # double (float)
var5 = 10
# 5var = 10  # hata verir
var6 = 10
Var7 = 19  # standart convention of python'a gore buyuk harfle baslamasi uygun degil

# %%
# string 

s = "bugun gunlerden pazartesi"

variable_type = type(s)   # str = string

print(s)

var1 = "ankara"
var2 = "ist"
var3 = var1+var2

var4 = "100"
var5 = "200"
var6 = var4+var5

uzunluk = len(var6) 

# var6[3]

# %% numbers
# int
integer_deneme = -50
# double = float = ondalikli sayi
float_deneme = -30.7


# %% built in functions
str1= "deneme"
float1 = 10.6 
# float(10)
# int(float1)
# round(float1)
str2 = "1005"

# %% user defined functions

var1 = 20
var2 = 50

output = (((var1+var2)*50)/100.0)*var1/var2

# fonksiyon parametresi = input
def benim_ilk_func(a,b):
    
    """
    bu benim ilk denemem
    
    parametre: 
        
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    
    return output
    
sonuc = benim_ilk_func(var1,var2)
sonuc2 = benim_ilk_func(var1,var2,)

def deneme1():
    print("bu benim ikinci denemem")
    
    
    
def ilkFonk(ilk,son):
      print("hadi inş ty22 olursun") 
           
ilkFonk("",1)      
ilkFonk("","") 
#ilkFonk("",) hata verir
ilkFonk("","",)  

# %% default ve flexible functionları

# default f: cemberin cevre uzunlugu = 2*pi*r
    
def cember_cevresi_hesapla(r,pi=3.14):
    
    """
    cember cevresi hesapla
    input(parametre): r,pi
    output = cemberin cevresi
    """
    
    output = 2*pi*r
    return output

# flexible

   
def hesapla(boy,kilo,*args):
    print(args)
    print(len(args))
    print(type(args))
    output = (boy+kilo)*args[0]
    
    for each in range(0,len(args)):
          print("args ",each,"= ", args[each])
    
    args_values = [args[each] for each in range(0,len(args))]  #yukardaki for ile aynı işi yapıyor
          
    return output,args_values

sonuc, args_sonucu = hesapla(1,2,10,11,12)
print("\nsonuc = ",sonuc)
print("\nargs değerleri = ", args_sonucu)

#def hesapla(boy,kilo,yas):
#    output = (boy+kilo)*yas
#    return output
    
#%%

def x(y):

    #y = y + [2]
    y.append(2) #ekleme böyle olur , yukardaki sadece aritmetik işlem bastırır

    print(y)

c = [1,2,3]
# d = c + 2   hata verir list+int olmaz
x(c)
len(c)


# %% QUIZ
    
# int variable yas
# string name isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float()) 
# *args soyisim
# default parametre ayakkabi numarasi
    
yas = 10
name = "ali"
soyisim = "veli"

def function_quiz(yas,name,*args,ayakkabi_numarasi=35):
    print("Cocugun ismi: ",name, " yasi: ",yas," ayak numarasi: ",ayakkabi_numarasi)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    
    return output

sonuc = function_quiz(yas,name,soyisim)

print("args[0]*yas: ",sonuc)


# %% 
# lambda function         // sadece ufak aritmetik yapcaksan mantıklı

def hesapla(x):
    return x*x
sonuc = hesapla(3)


sonuc2 = lambda abc: abc**2 + 0
print(sonuc2(3))
print(sonuc2(4))

# %% 
# lambda function 2
l = [lambda x:x*2, lambda x:x**2,lambda x:x+2]

for i in l:
    print(i(5))
    print(i(6))


def funcdf():
      return
#%%


x = [a for a in range(10) if a % 2 == 0]
print(x)


y = []
for each in range(0,10):
      y.append(each)
print(y)















