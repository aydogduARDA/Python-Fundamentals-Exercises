#1- 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
#    buldurmaya çalışın. (hak = 5)
#
#    ** "random modülü" için "python random" şeklinde arama yapın.
#    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
#    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
#       üzerinden hesaplansın.

# --- Proje 6: Sayı Tahmin Oyunu ---
# AUTHOR: İbrahim Arda Aydogdu
#
# AÇIKLAMA:
# Bu proje, şu ana kadar öğrendiğim her şeyi kullandım:
# - 'random' modülü (yeni bir şey öğreneceğiz)
# - 'while' döngüsü (oyunun ana motoru)
# - 'if/elif/else' (aşağı/yukarı yönlendirmesi)
# - 'break' (oyun bitince döngüyü kırmak için)
# - 'input' ve 'int' (kullanıcıdan veri almak için)
# - Matematik operatörleri (puan hesaplamak için)

# random modülünü çağırıyoruz. Bu, bilgisayara rastgele sayı ürettirir.
import random 




tutulan_sayi = random.randint(1, 100)

print("\n" + "="*40)
print("--- SAYI TAHMİN OYUNUNA HOŞ GELDİN YEĞENİM ---")
print("Aklımda 1-100 arasında bir sayı tuttum. Bakalım bulabilecek misin?")
print("="*40)


toplam_hak = int(input("Kaç denemede bilirsin? (Can sayısını gir): "))
kalan_hak = toplam_hak


deneme_sayisi = 0


kazandi_mi = False


while kalan_hak > 0:
    
    print(f"\n--- {deneme_sayisi + 1}. DENEME ---") 
    print(f"Kalan Can: {kalan_hak}")
    
    
    tahmin = int(input("Tahminin nedir?: "))
    
    
    deneme_sayisi = deneme_sayisi + 1
    
    
    
    if tahmin == tutulan_sayi:
        print("*"*40)
        print(f"TEBRİKLER!BİLDİN!")
        print(f"Sayıyı {deneme_sayisi}. denemede buldun.")
        print("*"*40)
        kazandi_mi = True  
        break
    
    elif tahmin < tutulan_sayi:
        print(">>> DAHA YUKARI ÇIK!")
        kalan_hak = kalan_hak - 1 
        
    else: 
        print(">>> DAHA AŞAĞI İN!")
        kalan_hak = kalan_hak - 1 



print("\n" + "="*40)
print("--- OYUN BİTTİ ---")
print("="*40)


if kazandi_mi == True:
    
    
    puan_kaybi_per_hata = 100 / toplam_hak
    yanlis_sayisi = deneme_sayisi - 1 
    kaybedilen_puan = yanlis_sayisi * puan_kaybi_per_hata
    
    son_puan = 100 - kaybedilen_puan
    

    if son_puan < 0:
        son_puan = 0
        
    print(f"Toplam Puanın: {son_puan:.2f}") 

else:
    
    print("Bütün canlarını  KAYBETTİN.")
    print(f"Aklımda tuttuğum  sayı şuydu: {tutulan_sayi}")
    print("Puanın: 0")