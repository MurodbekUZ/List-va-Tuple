# # 1-Masala: Haftaning kunlari
# kunlar = ('Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma')
#
# # 1. Tuple uzunligini toping
# uzunlik = len(kunlar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 2. 'Juma' elementi mavjudligini tekshirish
# print(f"'Juma' mavjudmi?: {'Juma' in kunlar}")
#
# # 3. 'Chorshanba' ning indeksini toping
# indeks_chorshanba = kunlar.index('Chorshanba')
# print(f"'Chorshanba' indeksi: {indeks_chorshanba}")
#
# # 4. 2-chi elementni oling (indeks 1)
# ikkinchi_kun = kunlar[1]
# print(f"2-chi kun: {ikkinchi_kun}")
#
# # 5. Faqat oxirgi 2 ta kunni kesib oling
# oxirgi_2_kun = kunlar[-2:]
# print(f"Oxirgi 2 kun: {oxirgi_2_kun}")
#
# # 6. Tuple ni ro'yxatga aylantiring
# kunlar_royxat = list(kunlar)
# print(f"Ro'yxatga aylantirilgan: {kunlar_royxat}")
#
# # 7. Ro'yxatga 'Shanba' va 'Yakshanba' qo'shing
# kunlar_royxat.append('Shanba')
# kunlar_royxat.append('Yakshanba')
# print(f"Hafta kunlari qo'shilgan ro'yxat: {kunlar_royxat}")
#
# # 8. Ro'yxatni qayta tuple’ga aylantiring
# kunlar_yangi = tuple(kunlar_royxat)
# print(f"Yangi tuple: {kunlar_yangi}")
#
# # 9. Yakuniy tuple uzunligini toping
# uzunlik_yangi = len(kunlar_yangi)
# print(f"Yakuniy tuple uzunligi: {uzunlik_yangi}")
#
# # 10. Yakuniy tuple’ni chop eting
# print(f"Yakuniy hafta kunlari tuple: {kunlar_yangi}")

# # 2-Masala: Ranglar to‘plami
# ranglar = ('qizil', 'yashil', "ko'k", 'sariq')
#
# # 1. 'yashil' mavjudligini tekshirish
# print(f"'yashil' mavjudmi?: {'yashil' in ranglar}")
#
# # 2. 'qora' mavjud emasligini tekshirish
# print(f"'qora' mavjud emasmi?: {'qora' not in ranglar}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(ranglar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. 'ko\'k' ning indeksini topish
# indeks_kok = ranglar.index("ko'k")
# print(f"'ko\\'k' indeksi: {indeks_kok}")
#
# # 5. Tuple ni ro'yxatga aylantirib 'pushti' qo'shing
# ranglar_royxat = list(ranglar)
# ranglar_royxat.append('pushti')
# print(f"Ro'yxatga 'pushti' qo'shildi: {ranglar_royxat}")
#
# # 6. Ro'yxatni qayta tuple’ga aylantirish
# ranglar_yangi = tuple(ranglar_royxat)
# print(f"Yangi tuple: {ranglar_yangi}")
#
# # 7. Tuple ichidagi 2-3 elementlarni kesib oling
# kesilgan_ranglar = ranglar_yangi[1:3]
# print(f"2-3 elementlar: {kesilgan_ranglar}")
#
# # 8. Tuple’ni 2 marta takrorlash
# ranglar_takror = ranglar_yangi * 2
# print(f"2 marta takrorlangan tuple: {ranglar_takror}")
#
# # 9. Yangi tuple uzunligini topish
# uzunlik_yangi = len(ranglar_takror)
# print(f"Takrorlangan tuple uzunligi: {uzunlik_yangi}")
#
# # 10. Natijani chop etish
# print(f"Yakuniy tuple: {ranglar_takror}")

# # 3-Masala: Shaharlar haqida ma'lumot
# shaharlar = ('Toshkent', 'Buxoro', 'Xiva', 'Samarqand')
#
# # 1. 'Buxoro' ning indeksini topish
# indeks_buxoro = shaharlar.index('Buxoro')
# print(f"'Buxoro' indeksi: {indeks_buxoro}")
#
# # 2. Tuple uzunligini topish
# uzunlik = len(shaharlar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 3. 'Navoiy' tuple’da mavjud emasligini tekshirish
# print(f"'Navoiy' mavjud emasmi?: {'Navoiy' not in shaharlar}")
#
# # 4. Faqat 1-2-3 elementlarni kesib olish
# kesilgan_shaharlar = shaharlar[0:3]
# print(f"1-2-3 elementlar: {kesilgan_shaharlar}")
#
# # 5. Tuple ni ro'yxatga o‘tkazib 'Navoiy' qo'shish
# shaharlar_royxat = list(shaharlar)
# shaharlar_royxat.append('Navoiy')
# print(f"Ro'yxatga 'Navoiy' qo'shildi: {shaharlar_royxat}")
#
# # 6. Ro'yxatni qayta tuple’ga aylantirish
# shaharlar_yangi = tuple(shaharlar_royxat)
# print(f"Yangi tuple: {shaharlar_yangi}")
#
# # 7. Har bir elementni for orqali chop etish
# print("Shaharlar:")
# for shahar in shaharlar_yangi:
#     print(shahar)
#
# # 8. Tuple’dan oxirgi elementni olish
# oxirgi_shahar = shaharlar_yangi[-1]
# print(f"Oxirgi shahar: {oxirgi_shahar}")
#
# # 9. Tuple ni 2 marta takrorlash
# shaharlar_takror = shaharlar_yangi * 2
# print(f"2 marta takrorlangan tuple: {shaharlar_takror}")
#
# # 10. Yakuniy natijani chop etish
# print(f"Yakuniy tuple: {shaharlar_takror}")

# # 4-Masala: Talabalar ballari
# ballar = (78, 92, 65, 88, 100)
#
# # 1. Eng katta ballni topish
# eng_katta = max(ballar)
# print(f"Eng katta ball: {eng_katta}")
#
# # 2. Eng kichik ballni topish
# eng_kichik = min(ballar)
# print(f"Eng kichik ball: {eng_kichik}")
#
# # 3. Ballar o‘rtacha qiymatini topish
# ortalama = sum(ballar) / len(ballar)
# print(f"Ballar o'rtachasi: {ortalama}")
#
# # 4. 92 mavjudligini tekshirish
# print(f"92 ball mavjudmi?: {92 in ballar}")
#
# # 5. Tuple uzunligini topish
# uzunlik = len(ballar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 6. Tuple’ni ro‘yxatga o‘tkazib, 85 ball qo‘shish
# ballar_royxat = list(ballar)
# ballar_royxat.append(85)
# print(f"Ro'yxatga 85 qo'shildi: {ballar_royxat}")
#
# # 7. Ro‘yxatni qayta tuple’ga aylantirish
# ballar_yangi = tuple(ballar_royxat)
# print(f"Yangi tuple: {ballar_yangi}")
#
# # 8. 80 dan katta ballarni ajratish
# katta_ballar = tuple([b for b in ballar_yangi if b > 80])
# print(f"80 dan katta ballar: {katta_ballar}")
#
# # 9. 3-chi elementni olish
# uchinchi_ball = ballar_yangi[2]
# print(f"3-chi ball: {uchinchi_ball}")
#
# # 10. Yakuniy tuple’ni chop etish
# print(f"Yakuniy tuple: {ballar_yangi}")

# # 5-Masala: Filmlar
# filmlar = ('Titanic', 'Avatar', 'Inception', 'Joker')
#
# # 1. 'Avatar' mavjudligini tekshirish
# print(f"'Avatar' mavjudmi?: {'Avatar' in filmlar}")
#
# # 2. 'Matrix' yo'qligini tekshirish
# print(f"'Matrix' mavjud emasmi?: {'Matrix' not in filmlar}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(filmlar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. 'Joker' ning indeksini topish
# joker_index = filmlar.index('Joker')
# print(f"'Joker' indeksi: {joker_index}")
#
# # 5. Tuple ni ro'yxatga aylantirib 'Matrix' qo'shish
# filmlar_royxat = list(filmlar)
# filmlar_royxat.append('Matrix')
# print(f"Ro'yxatga 'Matrix' qo'shildi: {filmlar_royxat}")
#
# # 6. Ro'yxatni qayta tuple'ga aylantirish
# filmlar_yangi = tuple(filmlar_royxat)
# print(f"Yangi tuple: {filmlar_yangi}")
#
# # 7. 2-dan 4-elementgacha qismini olish
# qisqa_filmlar = filmlar_yangi[1:4]
# print(f"2-dan 4-elementgacha: {qisqa_filmlar}")
#
# # 8. Tuple'ni 2 marta takrorlash
# takrorlangan_filmlar = filmlar_yangi * 2
# print(f"Takrorlangan tuple: {takrorlangan_filmlar}")
#
# # 9. Tuple ichidagi barcha elementlarni for bilan chiqarish
# print("Barcha filmlar:")
# for film in filmlar_yangi:
#     print(film)
#
# # 10. Yakuniy natijani chop etish
# print(f"Yakuniy tuple: {filmlar_yangi}")

# # 6-Masala: Restoran menyusi
# menyu = ('osh', "lag'mon", 'shashlik', 'somsa')
#
# # 1. 'somsa' mavjudligini tekshirish
# print(f"'somsa' mavjudmi?: {'somsa' in menyu}")
#
# # 2. 'manti' yo'qligini tekshirish
# print(f"'manti' mavjud emasmi?: {'manti' not in menyu}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(menyu)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. 'lag'mon' ning indeksini topish
# lagmon_index = menyu.index("lag'mon")
# print(f"'lag'mon' indeksi: {lagmon_index}")
#
# # 5. Tuple ni ro'yxatga aylantirib 'manti' qo'shish
# menyu_royxat = list(menyu)
# menyu_royxat.append('manti')
# print(f"Ro'yxatga 'manti' qo'shildi: {menyu_royxat}")
#
# # 6. 'osh' ni ro'yxatdan o'chirish
# menyu_royxat.remove('osh')
# print(f"'osh' o'chirildi: {menyu_royxat}")
#
# # 7. Ro'yxatni qayta tuple'ga aylantirish
# menyu_yangi = tuple(menyu_royxat)
# print(f"Yangi tuple: {menyu_yangi}")
#
# # 8. Tuple'ni 2 marta takrorlash
# takrorlangan_menyu = menyu_yangi * 2
# print(f"Takrorlangan tuple: {takrorlangan_menyu}")
#
# # 9. 1-dan 3-elementgacha bo‘lgan qismini olish
# qisqa_menyu = menyu_yangi[0:3]
# print(f"1-dan 3-elementgacha: {qisqa_menyu}")
#
# # 10. Yakuniy natijani chop etish
# print(f"Yakuniy tuple: {menyu_yangi}")

# # 7-Masala: Musiqa janrlari
# janrlar = ('pop', 'rap', 'rock', 'jazz', 'classic')
#
# # 1. 'rock' indeksini topish
# rock_index = janrlar.index('rock')
# print(f"'rock' indeksi: {rock_index}")
#
# # 2. 'blues' mavjud emasligini tekshirish
# print(f"'blues' mavjud emasmi?: {'blues' not in janrlar}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(janrlar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. Tuple ni ro'yxatga aylantirish
# janrlar_royxat = list(janrlar)
# print(f"Ro'yxatga aylantirildi: {janrlar_royxat}")
#
# # 5. 'blues' va 'electro' janrlarini qo'shish
# janrlar_royxat.append('blues')
# janrlar_royxat.append('electro')
# print(f"Janrlar qo'shildi: {janrlar_royxat}")
#
# # 6. Ro'yxatni qayta tuple'ga aylantirish
# janrlar_yangi = tuple(janrlar_royxat)
# print(f"Yangi tuple: {janrlar_yangi}")
#
# # 7. Tuple'ni alifbo tartibida chiqarish
# sorted_janrlar = sorted(janrlar_yangi)
# print(f"Alifbo tartibida: {sorted_janrlar}")
#
# # 8. 3-chi elementni olish
# uchinchi_element = janrlar_yangi[2]
# print(f"3-chi element: {uchinchi_element}")
#
# # 9. Tuple'ni 3 marta takrorlash
# takrorlangan_janrlar = janrlar_yangi * 3
# print(f"3 marta takrorlangan tuple: {takrorlangan_janrlar}")
#
# # 10. Natijani chop etish
# print(f"Yakuniy tuple: {janrlar_yangi}")

# # 8-Masala: Telefon modellari
# telefonlar = ('iPhone', 'Samsung', 'Nokia', 'Xiaomi', 'Huawei')
#
# # 1. 'Samsung' indeksini topish
# samsung_index = telefonlar.index('Samsung')
# print(f"'Samsung' indeksi: {samsung_index}")
#
# # 2. 'LG' mavjudligini tekshirish
# print(f"'LG' mavjudmi?: {'LG' in telefonlar}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(telefonlar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. Tuple ni ro'yxatga aylantirish va 'Realme' qo'shish
# telefonlar_royxat = list(telefonlar)
# telefonlar_royxat.append('Realme')
# print(f"Ro'yxatga qo'shildi: {telefonlar_royxat}")
#
# # 5. 'Nokia' ni olib tashlash
# telefonlar_royxat.remove('Nokia')
# print(f"'Nokia' o'chirildi: {telefonlar_royxat}")
#
# # 6. Ro'yxatni qayta tuple'ga aylantirish
# telefonlar_yangi = tuple(telefonlar_royxat)
# print(f"Yangi tuple: {telefonlar_yangi}")
#
# # 7. Tuple’dan 2-dan oxirigacha kesib olish
# kesilgan_telefonlar = telefonlar_yangi[1:]
# print(f"2-dan oxirigacha: {kesilgan_telefonlar}")
#
# # 8. Tuple’ni 2 marta takrorlash
# takrorlangan_telefonlar = telefonlar_yangi * 2
# print(f"2 marta takrorlangan tuple: {takrorlangan_telefonlar}")
#
# # 9. Har bir elementni for bilan chiqarish
# print("Har bir telefon:")
# for telefon in telefonlar_yangi:
#     print(telefon)
#
# # 10. Yakuniy tuple’ni chop etish
# print(f"Yakuniy tuple: {telefonlar_yangi}")

# # 9-Masala: Kitoblar to‘plami
# kitoblar = ('1984', 'Shaytanat', 'Alkimyogar', "O'tkan kunlar")
#
# # 1. '1984' mavjudligini tekshirish
# print(f"'1984' mavjudmi?: {'1984' in kitoblar}")
#
# # 2. 'Sariq devni minib' yo‘qligini tekshirish
# print(f"'Sariq devni minib' yo'qmi?: {'Sariq devni minib' not in kitoblar}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(kitoblar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. 'Shaytanat' indeksini topish
# shaytanat_index = kitoblar.index('Shaytanat')
# print(f"'Shaytanat' indeksi: {shaytanat_index}")
#
# # 5. Tuple ni ro'yxatga aylantirish
# kitoblar_royxat = list(kitoblar)
#
# # 6. 'Sariq devni minib' qo'shish
# kitoblar_royxat.append('Sariq devni minib')
# print(f"Ro'yxatga qo'shildi: {kitoblar_royxat}")
#
# # 7. Ro'yxatni qayta tuple'ga aylantirish
# kitoblar_yangi = tuple(kitoblar_royxat)
# print(f"Yangi tuple: {kitoblar_yangi}")
#
# # 8. Oxirgi 2 elementni olish
# oxirgi_kitoblar = kitoblar_yangi[-2:]
# print(f"Oxirgi 2 element: {oxirgi_kitoblar}")
#
# # 9. Tuple’ni 3 marta takrorlash
# takrorlangan_kitoblar = kitoblar_yangi * 3
# print(f"3 marta takrorlangan tuple: {takrorlangan_kitoblar}")
#
# # 10. Yakuniy natijani chop etish
# print(f"Yakuniy tuple: {kitoblar_yangi}")

# # 10-Masala: Avtomobillar
# avtomobillar = ('BMW', 'Chevrolet', 'Hyundai', 'Toyota')
#
# # 1. 'BMW' indeksini topish
# bmw_index = avtomobillar.index('BMW')
# print(f"'BMW' indeksi: {bmw_index}")
#
# # 2. 'Kia' mavjud emasligini tekshirish
# kia_yoq = 'Kia' not in avtomobillar
# print(f"'Kia' mavjud emasmi?: {kia_yoq}")
#
# # 3. Tuple uzunligini topish
# uzunlik = len(avtomobillar)
# print(f"Tuple uzunligi: {uzunlik}")
#
# # 4. Tuple ni ro'yxatga aylantirib 'Kia' qo'shish
# avtomobillar_royxat = list(avtomobillar)
# avtomobillar_royxat.append('Kia')
# print(f"Ro'yxatga qo'shildi: {avtomobillar_royxat}")
#
# # 5. 'Hyundai' ni olib tashlash
# avtomobillar_royxat.remove('Hyundai')
# print(f"'Hyundai' olib tashlandi: {avtomobillar_royxat}")
#
# # 6. Ro'yxatni qayta tuple'ga aylantirish
# avtomobillar_yangi = tuple(avtomobillar_royxat)
# print(f"Yangi tuple: {avtomobillar_yangi}")
#
# # 7. 2-elementdan boshlab kesish
# kesilgan_avtomobillar = avtomobillar_yangi[1:]
# print(f"2-elementdan boshlab: {kesilgan_avtomobillar}")
#
# # 8. Tuple’ni 2 marta takrorlash
# takrorlangan_avtomobillar = avtomobillar_yangi * 2
# print(f"2 marta takrorlangan tuple: {takrorlangan_avtomobillar}")
#
# # 9. Tuple’ni sorted() bilan tartiblash
# tartiblangan_avtomobillar = tuple(sorted(avtomobillar_yangi))
# print(f"Tartiblangan tuple: {tartiblangan_avtomobillar}")
#
# # 10. Yakuniy tuple’ni chop etish
# print(f"Yakuniy tuple: {avtomobillar_yangi}")



