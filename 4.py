# print(chr(96))
# print(chr(122))
# print(ord("A")) # 65
# print(ord("Z")) # 95
#
#
# przesuniecie = 0
# tekst = ""
# tekst = input("Podaj tekst do zaszyfrowania: ")
# przesuniecie = int(input("Podaj przesunięcie: "))
#
#
#
# def szyfruj(tekst, przesuniecie):
#     wynik = ""
#     for i in range(len(tekst)):
#         if przesuniecie > 0:
#             if ord(tekst[i]) > 122 - przesuniecie :
#                 wynik += chr(ord(tekst[i]) + (przesuniecie - 26))
#             else:
#                 wynik += chr(ord(tekst[i]) + przesuniecie)
#         # else :
#         #     if ord(tekst[i]) > 122 + przesuniecie :
#         #         wynik += chr(ord(tekst[i]) + (przesuniecie - 26))
#         #     else:
#         #         wynik += chr(ord(tekst[i]) + przesuniecie)
#     return wynik
#
# print(szyfruj(tekst, przesuniecie))

vs = 0
czas = int(input("Podaj czas:"))
przysp = int(input("Podaj przyspieszenie:"))
vs = int(input("Podaj predk pocz:"))


def licz_droge(czas, przysp, vs=0):
    droga = 0
    if vs == 0:
        droga = (przysp * czas*czas)/2
    else:
        droga = vs*czas + (przysp * czas*czas)/2
    return droga

print(licz_droge(czas, przysp, vs))
#print(ord("_"))