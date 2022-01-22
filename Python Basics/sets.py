# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 02:30:24 2021

@author: Samed
"""

#%% kümeler
kume = {"elma","armut","çilek"}
#%%
kume = set()

kume = set(("Ankara","İstanbul","Kayseri"))
print(type(kume)) # <class 'set'>
#%%
kume = {1,2,"a"}

kume.add("g")

print(kume) # {"b","c","g","a"}

#%%
kume = {} # !!! Küme değil Sözlük veri tipi !!!

print(type(kume)) # <class 'dict'>
#%%
kume = {"elma","armut","çilek"}

for x in kume:           # indeks numarası ile erişilemez, mecbur for ile 
    print(x)
#%%
kume = {"a","b","c"}

kume.add("g")

print(kume) # {"b","c","g","a"}
#%%
kume = {"a","b","c"}

kume.update(["x","y","z"])

print(kume) # {'y', 'c', 'b', 'x', 'z', 'a'}
#%%
kume = {"a","b","c"}
liste = ["x","y","z"] 
demet = (1,2,3)

kume.update(liste) 
kume.update(demet)

print(kume) # {1, 2, 3, 'y', 'a', 'x', 'c', 'b', 'z'}
#%%
kume = {"a","b","c","d"}

kume.remove("b")

print(kume) # {'a', 'c', 'd'}
#%%
kume = {"a","b","c","d"}

kume.discard("b")

print(kume) # {'d', 'c', 'a'}    
#%%
kume1 = {"A","B","C"} 
kume2 = {"D","E"}

kume3 = kume1.union(kume2)

print(kume3) # {'E', 'C', 'D', 'B', 'A'}
#%%
kume1 = {"A","B","C"} 
kume2 = {"D","E"}

kume1.update(kume2)

print(kume1) # {'D', 'C', 'E', 'B', 'A'}
#%%
kume1 = {"A","B","C"} 
kume2 = {"A"}

kume3 = kume1.union(kume2)

print(kume3) # {"A","B","C"}
#%%
 kume1 = {"A","B","C"} 
 kume2 = {"A","D"} 
 kume3 = {"F","G"}
 
print(kume1.isdisjoint(kume2)) # False 
print(kume1.isdisjoint(kume3)) # True
#%%
kume1 = {"A","B","C"} 
kume2 = {"A","D"}

kesisim= kume1.intersection(kume2)

print(kesisim) # {"A"}
#%%
kume1 = {"A","B","C"} 
kume2 = {"A","D"}

kume1.intersection_update(kume2)

print(kume1) # {"A"}
#%%
kume1 = {"A","D","G"} 
kume2 = {"A","B","C","D"}

# kume1 in kume2 den farkı
fark = kume1.difference(kume2)

print(fark) # {"G"}
#%%
kume1 = {"A","D","G"} 
kume2 = {"A","B","C","D"}

#kume1 in kume2 den farkı
kume1.difference_update(kume2)

print(kume1) # {"G"}
#%%
kume1 = {"A","B"} 
kume2 = {"A","B","C","D"}

print(kume1.issubset(kume2)) # True
#%%
kume1 = {"A","B"} 
kume2 = {"A","B","C","D"}

print(kume2.issuperset(kume1)) # True
#%%
kume = frozenset()

kume = frozenset(("Ankara","İstanbul",1))
kume.add("g")
print(type(kume)) # <class 'frozenset'>
