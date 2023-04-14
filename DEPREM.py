admin= "yetkili"
sifre= "123456"

user=  "pearl"
password="3001"

adsoyList=[]
usernameList=[]
parolaList=[]


print("""
      *******Deprem Acil Uygulamasına Hoşgeldiniz.*******
      Uygulama adminiyseniz 1i kullanıcıysanız 2yi üye olmak için 3ü tuşlayınız.""")

giris= input("Tuşlama yapınız:")

if giris=="1":
        print("Admin girisine hosgeldiniz.")
       
        kullanici = input("Kullanıcı adınızı giriniz.")
        parola = input("Şifrenizi giriniz:")    
    
        if kullanici == admin and parola == sifre:
            print("Sistem girişi başarılı hoşgeldiniz.")
    
 #listeden veri kullanmayı ogrendigimde kullanıcı girisi
 #liste elemanları kullanılarak gerceklestirilecektir.
   
elif giris=="2":
        print("Kullanıcı girisine hosgeldiniz.")
            
        kullanici = input("Kullanıcı adınızı giriniz:")
        parola = input("Şifrenizi giriniz:") 
            
        if kullanici == user and parola == password:
            print("Kullanıcı girişi başarılı hoşgeldiniz.")

    
elif giris=="3":
        print("Kayıt olma girisine hosgeldiniz.")
        
AdSoyad=input("Adınızı ve Soyadınızı giriniz:")
username=input("İstediğiniz kullanıcı adını giriniz:")
parola=input("Parolanızı giriniz:")
adsoyList.append(AdSoyad)
usernameList.append(username)
parolaList.append(parola)
print("Kayıt gerçekleştirildi.")             
    