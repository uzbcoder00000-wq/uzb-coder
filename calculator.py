# Beginner uchun oddiy kalkulyator dasturi
def main():
    # Bu dastur oddiy kalkulyator, def funksiyagacha bo'lgan barcha bosqichlarni o'z ichiga oladi.
    print("Salom! Bu oddiy kalkulyator.")
    print("Siz quyidagi amallardan birini tanlashingiz mumkin:")
    print("1. Qo'shish (+)")
    print("2. Ayirish (-)")
    print("3. Ko'paytirish (*)")
    print("4. Bo'lish (/)")
    
    # Foydalanuvchidan amal tanlashni so'raymiz
    amal = input("Amal raqamini kiriting (1-4): ")
    
    # Sonlarni kiritamiz
    son1 = float(input("Birinchi sonni kiriting: "))
    son2 = float(input("Ikkinchi sonni kiriting: "))
    
    # Natijani hisoblaymiz va ekranga chiqaramiz
    if amal == "1":
        natija = son1 + son2
        print(f"Natija: {son1} + {son2} = {natija}")
    elif amal == "2":
        natija = son1 - son2
        print(f"Natija: {son1} - {son2} = {natija}")
    elif amal == "3":
        natija = son1 * son2
        print(f"Natija: {son1} * {son2} = {natija}")
    elif amal == "4":
        if son2 != 0:
            natija = son1 / son2
            print(f"Natija: {son1} / {son2} = {natija}")
        else:
            print("Xatolik: 0 ga bo'lish mumkin emas!")
    else:
        print("Xatolik: Noto'g'ri amal tanlandi.")

# Endi, dasturni def funksiyaga o'rab ishlatamiz
def kalkulyator():
    main()

# Dastur boshlanish nuqtasi
if __name__ == "__main__":
    kalkulyator()