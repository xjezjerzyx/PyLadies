with open("py1.2.txt") as file:
    data = file.readlines()
    swdata = {}
    for line in data :
        name = line[line.find('.') + 2: line.find(' has')]
        eyes = line[line.find('has ') + 4:]
        eyes = eyes[:eyes.find(' and')]
        height = int(line[line.find(' is ') + 3: line.find(' cm')])
        swdata[name] = {'height': height, 'eyes': eyes}

    print(swdata)