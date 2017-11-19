def LiczbaOdw(x, y):
    if x > y:
        wieksza = x
    else:
        wieksza = y

    while True :
        if wieksza % x == 0 and wieksza % y == 0 :
            nwd = wieksza
            return nwd
        wieksza += 1

print(LiczbaOdw(4,6))