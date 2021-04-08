#!/usr/bin/env python
# coding: utf-8

# In[10]:


giriş_bilgileri={"Kullanıcı adı":"Mert_Yardımcı",
                        "Şifre":"12345"}
kullanıcı_adı1=input("Kullanıcı Adınızı Giriniz:")
şifre1=input("Şifrenizi Giriniz:")
if (giriş_bilgileri["Kullanıcı adı"]!=kullanıcı_adı1 and giriş_bilgileri["Şifre"]!=şifre1 ):
  print("Kullanıcı Adınız ve Şifreniz Hatalı!")
elif (giriş_bilgileri["Kullanıcı adı"]!=kullanıcı_adı1 and giriş_bilgileri["Şifre"]==şifre1 ):
  print("Kullanıcı Adınız Hatalı!")
elif (giriş_bilgileri["Kullanıcı adı"]==kullanıcı_adı1 and giriş_bilgileri["Şifre"]!=şifre1 ):
  print("Şifreniz Hatalı!")
else:
  print("Giriş Başarılı")

