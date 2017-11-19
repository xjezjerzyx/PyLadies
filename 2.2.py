

with open("py1.2.txt") as file:
    data = file.readlines()
    swdata = {}
    for line in data :
        name = line[line.find('.') + 2: line.find(' has')]
        eyes = line[line.find('has ') + 4:]
        eyes = eyes[:eyes.find(' and')]
        height = int(line[line.find(' is ') + 3: line.find(' cm')])
        swdata[name] = {'height': height, 'eyes': eyes}

    hero_short = []
    hero_200_plus = []

    hero_200_plus = open('hero_200_plus.txt', 'w')
    hero_200_minus = open('hero_200_minus.txt', 'w')

    for osoba in swdata :
        if swdata[osoba]['height'] > 200:
            hero_200_plus.write(osoba)
            hero_200_plus.write('\n')
        else :
            hero_200_minus.write(osoba)
            hero_200_minus.write('\n')

    hero_200_minus.close()
    hero_200_plus.close()

