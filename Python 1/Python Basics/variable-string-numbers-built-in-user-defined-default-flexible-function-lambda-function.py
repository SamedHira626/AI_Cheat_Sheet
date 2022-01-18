# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 12:32:34 2018

@author: Samed
"""
def func(a,b):
    
    """
    bu benim ilk denemem
    
    parametre: 
        
    return: 
    """
    output = (((a+b)*50)/100.0)*a/b
    
    return output
    
sonuc = func(var1,var2)
sonuc2 = func(var1,var2,)

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















