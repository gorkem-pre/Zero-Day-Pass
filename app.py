import random # rastgele üretici kütüphanesi klasik
import string
YESIL='\033[92m'
KIRMIZI='\033[91m'
SARI='\033[93m'
MAVI='\033[94m'
SIFIRLA='\033[0m'

while True:
    print(f"\n{MAVI}======================================={SIFIRLA}")
    print(f"\n{MAVI}--- SİBER GÜVENLİK SİSTEMİ{SIFIRLA}----")
    print(f"\n{SARI}1.Parola Güvenlik Analizi{SIFIRLA}")
    print(f"\n{SARI}2.Kırılmaz Parola Üretici{SIFIRLA}")
    print(f"\n{KIRMIZI}3.Sistemden Çıkış{SIFIRLA}")
    secim=input(f"\n{YESIL}Lütfen bir işlem seçin (1/2/3): {SIFIRLA}")
    if secim=='1':
        print(f"\n{MAVI}[+]Parola Analiz Modülü Başlatıldı...{SIFIRLA}")
        parola=input("Lütfen analiz edilecek parolayı girin: ")#kullanıcıdan parola istendi


        uzunluk=len(parola)#parolanın uzunluk ölçüldü.

        kucuk_harf_var=False
        buyuk_harf_var=False
        rakam_var=False
        ozel_karakter_var=False #1. Yeni bayrak(flag)

        #2. Hangi özel karakterleri kabul edeceğimizi bir değişkene atıyoruz
        ozel_karakterler = "!@#$%^&*()-_=+."


        #Parolanın içindeki her bir karakteri tek tek tarayan döngü
        for karakter in parola:
            if karakter.islower():
                kucuk_harf_var=True
            elif karakter.isupper():
                buyuk_harf_var=True
            elif karakter.isdigit():
                rakam_var=True    
            elif karakter in ozel_karakterler:
                ozel_karakter_var=True    
        puan=0 #puan sistemi
        if uzunluk >= 8:
            puan += 1
        if kucuk_harf_var:
            puan += 1
        if buyuk_harf_var:
            puan += 1
        if rakam_var:
            puan += 1
        if ozel_karakter_var:
            puan += 1    


        print(f"\n{SARI}--- ANALİZ SONUCU ---{SIFIRLA}")
        print(f"Güvenlik Puanınız (0-5 arasında olacaktır):{puan}")

        if uzunluk < 8:
            print("Durum: ZAYIF - Parolanız çok kısa! Siber saldırlara karşı en az 8 karakter olmalıdır.")#Uzunluk kontrol edildi
        else:
            print("Durum: BAŞARILI - Uzunluk kriterleri sağlandı.")
        #Puan durumuna göre kullanıcıya mesaj

        #mesaj verelim
        if puan == 5:
            print(f"{YESIL}Durum: GÜÇLÜ - Brute Force ile şifreniz yaklaşık  1 milyar yılda bulunacaktır ;){SIFIRLA}")
        elif puan >= 3:
            print(f"{SARI}Durum: ORTA - Fena değil ama daha güçlü bi zırhın neden olmasın ki ?{SIFIRLA}")    
        else:
            print(f"{KIRMIZI}Durum: ZAYIF - Parolanız siber saldırılara karşı çok savunmasız!{SIFIRLA}")
            print("Girdiğiniz parolanın uzunluğu: ",uzunluk, "karakter.")
    elif secim == '2':
        print(f"\n{MAVI}[+] Parola Üretici Modülü Başlatıldı...{SIFIRLA}")
        uzunluk = int(input("Kaç karakterlik bir parola oluşturulsun?(önerilen en az 12):"))
        tum_karakterler=string.ascii_letters+string.digits+string.punctuation 
        yeni_parola = ""

        for i in range(uzunluk):
            yeni_parola += random.choice(tum_karakterler)
        print(f"\n{YESIL}Oluşturulan Kırılması Zor Parolanız:{SIFIRLA} {SARI} {yeni_parola}{SIFIRLA}")


    elif secim == '3':
        print(f"\n{KIRMIZI}Sistem kapatılıyor. Güvende kalın{SIFIRLA}\n")
        break
    else:
        print(f"\n{KIRMIZI}[!]Hatalı giriş yaptınız. Lütfen 1,2 veya 3 tuşlayın")                    



    
    


    
