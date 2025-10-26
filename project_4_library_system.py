# # --- Project 5: Basic Library Management System ---
# AUTHOR: Ibrahım Arda Aydogdu
# DATE: 2025-10-25
#
# DESCRIPTION:
# A command-line interface (CLI) application to manage a simple library.
# This project demonstrates the use of core Python concepts including:
# - while loops (for the main application loop)
# - for loops (for iterating over the book list)
# - if/elif/else (for menu navigation and logic)
# - lists (to store the main library collection)
# - dictionaries (to store individual book details)
# - input/print (for user interaction)
#
# FEATURES:
# 1. Add new books (with title, author, and an initial status of 'rafta').
# 2. List all existing books (with a numbered index, details, and current status).
# 3. Update the status of a book (toggle between 'rafta' and 'ödünçte').
# 4. Exit the application.
# 
# 
# 
# 
# 
# 
# 
# PROJE: BASİT KÜTÜPHANE YÖNETİM SİSTEMİ
#
# AMAÇ:
# Bir kütüphanedeki kitapları yönetmek için komut satırı tabanlı bir uygulama oluşturmak.
# Kullanıcılar yeni kitap ekleyebilmeli, tüm kitapları listeleyebilmeli, bir kitabı
# ödünç alıp geri getirebilmeli (yani durumunu güncelleyebilmeli) ve programdan çıkış yapabilmelidir.
#
# GEREKSİNİMLER:
#
# 1- Veri Yapısı:
#    - Tüm kitaplar, 'kutuphane' adında bir ana liste içinde saklanmalıdır.
#    - Listedeki her bir kitap, bir dictionary olmalıdır.
#    - Her bir kitap dictionary'si üç anahtar içermelidir:
#      - 'ad': Kitabın adını içeren bir string.
#      - 'yazar': Kitabın yazarını içeren bir string.
#      - 'durum': Kitabın durumunu belirten bir string (başlangıçta 'rafta').
# 'ad': 'Fahrenheit 451', 'yazar': 'Ray Bradbury', 'durum': 'rafta'
#
# 2- Ana Döngü ve Menü:
#    - Program, kullanıcı 'Çıkış' seçeneğini seçene kadar 'while True:' ile sürekli çalışmalıdır.
#    - Her döngünün başında kullanıcıya aşağıdaki seçenekler sunulmalıdır:
#      "1: Yeni Kitap Ekle"
#      "2: Tüm Kitapları Listele"
#      "3: Kitap Durumunu Güncelle (Ödünç Ver / Geri Al)"
#      "4: Çıkış"
#    - Geçersiz bir seçim yapılırsa, kullanıcı uyarılmalıdır.
#
# 3- Yeni Kitap Ekleme (Seçim '1'):
#    - Kullanıcıdan yeni kitabın adını ve yazarını alın.
#    - Bu bilgilerle ve başlangıç durumu 'rafta' olarak yeni bir kitap dictionary'si oluşturun.
#    - Bu yeni dictionary'yi ana 'kutuphane' listesine ekleyin.
#    - "Kitap başarıyla eklendi." mesajı gösterin.
#
# 4- Tüm Kitapları Listeleme (Seçim '2'):
#    - Eğer 'kutuphane' listesi boşsa, "Kütüphanede hiç kitap yok." mesajı gösterin.
#    - Eğer kitaplar varsa, tüm kitaplar numaralandırarak
#      ve tüm bilgileriyle (ad, yazar, durum) ekrana yazdırın.
#      - Örnek Çıktı:
#        "1. Fahrenheit 451 - Ray Bradbury (Durum: rafta)"
#        "2. 1984 - George Orwell (Durum: ödünçte)"
#
# 5- Kitap Durumunu Güncelleme (Seçim '3'):
#    - Bu, projenin en önemli ve en zorlayıcı kısmı.
#    - Önce, mevcut kitapları numaralarıyla birlikte ekrana listeleyin ki kullanıcı hangi kitabı seçeceğini bilsin.
#    - Kullanıcıdan durumunu değiştirmek istediği kitabın SIRA NUMARASINI isteyin.
#    - Kullanıcının girdiği sıra numarasını kullanarak, 'kutuphane' listesinden doğru kitabı seçin.
#    - O kitabın mevcut durumunu kontrol edin:
#      - Eğer durum 'rafta' ise, durumu 'ödünçte' olarak GÜNCELLEYİN ve "Kitap ödünç verildi." deyin.
#      - Eğer durum 'ödünçte' ise, durumu 'rafta' olarak GÜNCELLEYİN ve "Kitap geri alındı." deyin.
#
# 6- Çıkış (Seçim '4'):
#    - Programı sonlandırın.




kutuphane = []

while True: 



    print("\n ********KÜTÜPHANE UYGULAMASI*********")
    print("\n 1-Kitap ekle")
    print("\n 2-Tüm kitapları Listele")
    print("\n 3-Kitapların durumunu güncelle (ÖDÜNÇ VER / GERİ AL )")
    print("\n 4-Çıkış.") 
    print("*"*30)

    secim = input("Lütfen görev numarası seçin:  ")


    if (secim == "1"): 
        print("Kitap ekleme menüsüne geldiniz ")
        yeni_kitap_ad = input("Eklemek istediğiniz kitabın adı: ")
        yeni_kitap_yazar = input("Eklemek istediğiniz kitabın yazarını giriniz: ")
        

        
        kutuphane.append({
            'ad': yeni_kitap_ad,
            'yazar':yeni_kitap_yazar,
            'durum': "rafta"
        })

    elif (secim == "2"):
        if not kutuphane:    
            print("Kütüphane içinde herhangi bir kitap bulunmamaktadır")
        else:
            sayac = 1
            for i in kutuphane:
                
                print(f"{sayac}. {i['ad']} - {i['yazar']} (Durum: {i['durum']})")

                sayac += 1
    

    elif (secim == "3"):
        
        print("\n--- Kitap Durumu Güncelleme ---")

        if not kutuphane:
            print("Kütüphanede güncellenecek hiç kitap yok.")
        
        else:
            print("Mevcut Kitaplar:")
            sayac = 1
            for kitap in kutuphane:
                print(f"{sayac}. {kitap['ad']} - {kitap['yazar']} (Durum: {kitap['durum']})")
                sayac = sayac + 1
            print("---------------------------------")

        sira_no = int(input("İstediğiniz kitabin sira numarasını yaziniz: "))
        index = sira_no - 1

        if 0 <= index <len(kutuphane):

            secilen_kitap = kutuphane[index]

            if secilen_kitap['durum'] == "rafta":
                secilen_kitap['durum'] = "ödünçte"
                print(f"{secilen_kitap['ad']} kıtabı ödünç verildi")

            else: 
                secilen_kitap['durum'] == "ödünçte"
                secilen_kitap['durum'] = "rafa geri bırakıldı"
                print(f"{secilen_kitap['ad']} kıtabı yerine geri bırakıldı")

        else:
            print("Lütfen geçerli index numarasına sahip kitap sırasını giriniz")
    

    elif (secim == "4"):
        print("Sitem menüsünden çıkılıyor. Tekrar bekleriz")

        break

    


        
        
             
             

            
    
        





    
        
