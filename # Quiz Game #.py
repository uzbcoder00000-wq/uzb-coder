# Quiz Game # 

savollar = [
    {"savol": "5 * 6 nechga teng ?" , "javob": "30"},   
    {"savol" : "pythonda royhat qaysi belgilar bilan yoziladi?","javob":"[]"},
    {"savol":"pythonda yaratgan kim?","javob":"guido van rossum"},
]


bal = 0

print("Salom Quiz Gamega  hush kelibsiz!\n")

for s in savollar:
    javob = input(s["savol"] + " >>> ").lower()
    if javob == s["javob"]:
        print("javob tog`ri !")
        bal += 1
    else:
        print("Notog`ri, Tog`ri javob:", s['javob'])

print("O`yin tugadi ! Sizning natijanggiz:", bal, "/", len(savollar))
