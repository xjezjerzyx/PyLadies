tekst = 'Pies psu niedzwiedziem'
def policz_slowa(tekst):
    list(tekst)
print(len(tekst))
aaa = tekst.split( )
print(len(aaa))
print(policz_slowa(tekst))

tekst = 'Pies psu niedzwiedziem'
def policz_slowa(tekst):
    aaa = tekst.split()
    return len(aaa)

print(policz_slowa( tekst))
#
tekst = 'Pies psu niedzwiedziem'
def policz_samogloski(tekst):
    liczba_sam = 0
    samogloski = ['a','e','u','i','o']
    for yyy in tekst :
        if yyy in samogloski:
            liczba_sam = liczba_sam +1
    return liczba_sam
    #return 1

print(policz_samogloski(tekst))
#
# inp_str = 'xxxoooxaaaaaxxxxxxo'
# def xo_checker(inp_str):
#     cntx = 0
#     cnto = 0
#     cnto = inp_str.count('o', 0, len(inp_str))
#     cntx = inp_str.count('x', 0, len(inp_str))
#
#     if (cntx == cnto) :
#         return True
#     elif len(inp_str) > cntx + cnto:
#         return 'Illegal letters in text'
#     else :
#         return False
#
#
#
# print(xo_checker(inp_str))
#
#
# dane = 'password12345'
#
# def cenzura_cyfr(dane):
#     outpt = ''
#     for x in dane:
#         if x.isdigit():
#             x = x.replace(x,'#')
#             outpt += x
#         else:
#             outpt += x
#     return outpt
#
# print(cenzura_cyfr(dane))



txtAla = 'ala ma kota a kot ma aids'
print(txtAla[0])
print(txtAla[0:])
print(txtAla[3:])
print(txtAla[0:10])
print(txtAla[:8])
print(txtAla[::8])
print(txtAla[::-1])
print(txtAla[::])