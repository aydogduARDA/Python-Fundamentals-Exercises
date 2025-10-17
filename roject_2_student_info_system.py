# --- Mini Proje 2: Öğrenci Bilgi Sistemi (Okul Numarası ile Arama) ---
# AUTHOR: Arda Aydogdu
# DESCRIPTION: A simple script to store student data in a list of dictionaries
# and search for a student using their unique ID number.

# --- 1. VERİ KURULUMU: Öğrenci kartlarını ve sınıf listesini oluşturuyoruz ---

ogrenci1 = {
    "ad": "Ahmet",
    "soyad": "Yıldız",
    "no": 101
}

ogrenci2 = {
    "ad": "Yusuf",
    "soyad": "Kaya",
    "no": 202
}

ogrenci3 = {
    "ad": "Arda",
    "soyad": "Aydogan",
    "no": 303
}

# 3 öğrenci kartını tek bir sınıf listesine koyuyoruz.
ogrenciler = [ogrenci1, ogrenci2, ogrenci3]

print("--- Öğrenci Bilgi Sistemine Hoş Geldiniz ---")
print("Mevcut Öğrenci Numaraları: 101, 202, 303")


# --- 2. KULLANICIDAN BİLGİ ALMA: Hangi öğrenciyi aradığını soruyoruz ---

aranan_okul_no = int(input("Bilgilerini görmek istediğiniz öğrencinin OKUL NUMARASINI giriniz: "))


# --- 3. ARAMA ALGORİTMASI: Listenin içini tarayıp doğru öğrenciyi buluyoruz ---

# Başlangıçta öğrenciyi bulamadığımızı varsayıyoruz. Bu bizim bayrağımız (flag).
ogrenci_bulundu = False

# "for" döngüsü ile "ogrenciler" listesindeki her bir kartı tek tek geziyoruz.
for ogrenci_karti in ogrenciler:
    
    # "if" koşulu ile o anki kartın içindeki "no"nun, bizim aradığımız no'ya eşit olup olmadığını kontrol ediyoruz.
    if ogrenci_karti["no"] == aranan_okul_no:
        
        # Eğer eşitse:
        print("\n>>> Öğrenci Bulundu! Bilgiler getiriliyor...")
        
        # Bilgileri ekrana yazdırıyoruz.
        print(f"Adı: {ogrenci_karti['ad']}")
        print(f"Soyadı: {ogrenci_karti['soyad']}")
        print(f"Numarası: {ogrenci_karti['no']}")
        
        # Bayrağımızı "bulduk" olarak değiştiriyoruz.
        ogrenci_bulundu = True
        
        # Aradığımızı bulduğumuz için döngüyü daha fazla çalıştırmaya gerek yok, kırıp çıkıyoruz.
        break


# --- 4. SONUÇ: Arama bittikten sonra sonucu değerlendiriyoruz ---

# Eğer döngü bittiğinde bayrağımız hala "bulamadık" (False) durumundaysa...
if not ogrenci_bulundu:
    print(f"\n>>> HATA: Sistemde {aranan_okul_no} numaralı bir öğrenci kaydı bulunamadı.")