# -*- coding: utf-8 -*-
"""
Bu skript test.html'dagi barcha savollarni arabcha ovozli mp3 fayllarga aylantiradi.
Ishlatish: shu faylni bot.py bilan bir papkaga (Desktop) qo'ying va terminalda ishga tushiring:

    python generate_audio.py

Kerak bo'lsa kutubxonani o'rnating (odatda bot.py uchun allaqachon o'rnatilgan):

    pip install gtts

Natijada shu skript joylashgan joyda "audio" nomli papka paydo bo'ladi,
uning ichida 36 ta mp3 fayl bo'ladi. Shu "audio" papkasini test.html bilan
birga GitHub'ga yuklashingiz kerak bo'ladi.
"""

import os
import sys
import time

try:
    from gtts import gTTS
except ImportError:
    print("XATOLIK: gtts kutubxonasi topilmadi.")
    print("Terminalda mana buni ishga tushiring: pip install gtts")
    sys.exit(1)

# Har bir mavzu uchun savollar, test.html dagi savollarDB bilan BIR XIL TARTIBDA.
# "→" belgisi va emoji rasmlar olib tashlangan — faqat sof arabcha matn ovozga aylantiriladi.
savollar = {
    "harflar": [
        "مَا هَذَا الحَرْفُ؟ ب",
        "مَا هَذَا الحَرْفُ؟ ت",
        "مَا هَذَا الحَرْفُ؟ س",
        "مَا هَذَا الحَرْفُ؟ ج",
        "مَا هَذَا الحَرْفُ؟ د",
        "مَا هَذَا الحَرْفُ؟ ر",
        "مَا هَذَا الحَرْفُ؟ ش",
        "مَا هَذَا الحَرْفُ؟ ص",
        "مَا هَذَا الحَرْفُ؟ ع",
        "مَا هَذَا الحَرْفُ؟ م",
    ],
    "mevalar": [
        "مَا اسْمُ هَذِهِ الخَضْرَاء؟",
        "مَا اسْمُ هَذِهِ الخَضْرَاء؟",
        "مَا اسْمُ هَذِهِ الخَضْرَاء؟",
        "مَا اسْمُ هَذِهِ الخَضْرَاء؟",
        "مَا اسْمُ هَذِهِ الفَاكِهَة؟",
        "مَا اسْمُ هَذِهِ الفَاكِهَة؟",
    ],
    "gaplar": [
        "الأُمُّ تَشْتَرِي",
        "تَطْبُخُ الأُمُّ",
        "المَانجُو",
        "يَزِنُ البَائِعُ",
    ],
    "joylashuv": [
        "أَيْنَ هَانِي؟",
        "أَيْنَ سَامِي؟",
        "أَيْنَ تَامِرٌ؟",
        "أَيْنَ الكَلْبُ الكَبِيرُ؟",
        "أَيْنَ الكَلْبُ الصَّغِيرُ؟",
    ],
    "felllar": [
        "هُوَ يَجْرِي، هُمَا",
        "هُوَ يَجْرِي، هُمْ",
        "هُوَ يَلْعَبُ، هُمَا",
        "هُوَ يَلْعَبُ، هُمْ",
        "هُوَ يَكْتُبُ، هُمَا",
        "هُوَ يَكْتُبُ، هُمْ",
    ],
    "kunlar": [
        "مَا هُوَ أَوَّلُ أَيَّامِ الأُسْبُوعِ؟",
        "مَا هُوَ اليَوْمُ بَعْدَ الاثْنَيْنِ؟",
        "مَا هُوَ آخِرُ أَيَّامِ الأُسْبُوعِ؟",
        "مَا هُوَ اليَوْمُ قَبْلَ الأَرْبِعَاءِ؟",
        "مَا هُوَ اليَوْمُ بَعْدَ الخَمِيسِ؟",
    ],
}

chiqish_papka = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")
os.makedirs(chiqish_papka, exist_ok=True)

jami = sum(len(v) for v in savollar.values())
hozir = 0

print(f"Jami {jami} ta ovoz fayli yaratiladi. Internet kerak, biroz vaqt olishi mumkin...\n")

for mavzu, matnlar in savollar.items():
    for i, matn in enumerate(matnlar):
        hozir += 1
        fayl_nomi = f"{mavzu}_{i}.mp3"
        fayl_yuli = os.path.join(chiqish_papka, fayl_nomi)
        print(f"[{hozir}/{jami}] {fayl_nomi} yaratilmoqda...  ({matn})")
        try:
            tts = gTTS(text=matn, lang='ar')
            tts.save(fayl_yuli)
            time.sleep(0.3)  # Google serveriga tez-tez so'rov yubormaslik uchun kichik pauza
        except Exception as e:
            print(f"   XATOLIK: {fayl_nomi} yaratilmadi -> {e}")

print("\nTayyor! 'audio' papkasida barcha ovoz fayllari yaratildi.")
print("Endi shu 'audio' papkasini test.html bilan birga GitHub'ga yuklang.")
