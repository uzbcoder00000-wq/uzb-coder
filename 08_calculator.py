# 08_calculator.py
# Oddiy kalkulyator (funksiya ishlatmasdan)

print("Kalkulyator")
print("Amallar: 1 - Qo‘shish, 2 - Ayirish, 3 - Ko‘paytirish, 4 - Bo‘lish")

tanlov = input("Amalni tanlang (1/2/3/4): ")
a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))

if tanlov == "1":
    print("Natija:", a + b)
elif tanlov == "2":
    print("Natija:", a - b)
elif tanlov == "3":
    print("Natija:", a * b)
elif tanlov == "4":
    if b != 0:
        print("Natija:", a / b)
    else:
        print("❌ 0 ga bo‘lish mumkin emas!")
else:
    print("Noto‘g‘ri tanlov!")
