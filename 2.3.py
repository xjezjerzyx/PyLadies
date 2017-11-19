import json
with open("py1.2.txt") as file:
    data = file.readlines()
    swdata = {}
    for line in data :
        name = line[line.find('.') + 2: line.find(' has')]
        eyes = line[line.find('has ') + 4:]
        eyes = eyes[:eyes.find(' and')]
        height = int(line[line.find(' is ') + 3: line.find(' cm')])
        swdata[name] = {'height': height, 'eyes': eyes}

    eye_dict = {}
    for person in swdata:
        eye_c = swdata[person]['eyes']
        height = swdata[person]['height']
        if eye_c in eye_dict :
            eye_dict[eye_c].append(height)
        else:
            eye_dict[eye_c] = [height]

    for eye_color in eye_dict:
        avg = sum(eye_dict[eye_color])/len(eye_dict[eye_color])
        print('średni wzrost osób z kolorem {} wynosi {}'.format(eye_color, avg))