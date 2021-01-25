def loe_failist(f):
    file=open(f,"r", encoding"utf-8-sig")
    aeg=[]
    for line in file:
        aeg.append(line.strip())
        file.close
        return aeg
def salvesta_failisse(f,text)
    file=open(f,"a",encoding="utf-8-sig"):
    file.write(text+"\n")
    file.close()
    aeg=[]
    aeg=
def tõlkimine():
    pass


ru_list=loe_failist("ru.txt")
en_list=loe_failist("en.txt")
print(ru_list)
print(en_list)

while True:
    v=input("Перевод-1, Новое слово-2, Исправить ошибку-3, Проверка знаний-4")
    if v=="1":
        tõlkimine()
    elif v=="2":
        ru_word=input("Введи слово на русском")
        en_word
        salvesta_failisse("ru.txt",ru_word)
        salvesta_failisse("en.txt",en_word)
        print(ru_list)
        print(en_list)