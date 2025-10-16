
#FILE: project_1_grocery_store.py
# AUTHOR: Arda Aydoğdu
# DESCRIPTION: A simple command-line grocery simulation.
# Allows an administrator to stock products with a code, name, and price,
# then allows a customer to purchase a single product using their code.










meyveler = {

}
meyverafkodu = int(input("Meyve alan kodunu giriniz: "))
meyvead = input("Eklemek stedğiniz meyvenin ismi: ")
meyvekg = int(input("Eklemek isteidğiniz meyvenin 1 kilogram fiyatını yazınız:"))

meyveler.update({
    meyverafkodu:{
        "meyve adı": meyvead,
        "meyvekg": meyvekg,
    
    }
})

meyverafkodu = int(input("Meyve alan kodunu giriniz: "))
meyvead = input("Eklemek stedğiniz meyvenin ismi: ")
meyvekg = int(input("Eklemek isteidğiniz meyvenin 1 kilogram fiyatını yazınız:"))

meyveler.update({
    meyverafkodu:{
        "meyve adı": meyvead,
        "meyvekg": meyvekg,
    
    }

})

meyverafkodu = int(input("Meyve alan kodunu giriniz: "))
meyvead = input("Eklemek stedğiniz meyvenin ismi: ")
meyvekg = int(input("Eklemek isteidğiniz meyvenin 1 kilogram fiyatını yazınız:"))

meyveler.update({
    meyverafkodu:{
        "meyve adı": meyvead,
        "meyvekg": meyvekg,
    
    }

})


print(meyveler)

# Müşteriden  RAF KODUNU isteyelim.
alinacak_urun_kodu = int(input("Hangi meyvenin raf kodunu istiyorsunuz?: "))
kac_kilo = float(input("Kaç kilogram alacaksınız?: "))

# Fiyatı hesaplayalım
# Önce o raf koduna ait olan iç sözlüğü bulalım
urun_bilgileri = meyveler[alinacak_urun_kodu]

# Şimdi o iç sözlükten fiyatı ('meyvekg') çekelim
birim_fiyat = urun_bilgileri['meyvekg']

# Toplam tutarı hesaplayalım
toplam_tutar = birim_fiyat * kac_kilo

# Sonucu yazdıralım
print(f"Ödemeniz gereken tutar: {toplam_tutar} TL")













