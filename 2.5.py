import  json
with open('py1.2.json') as f:
    a = json.load(f)
    sw_women = open('sw_women.txt', 'w')
    sw_men = open('sw_men.txt', 'w')
    for y in a:
        if y["gender"] == "female":
            sw_women.write(y['name'])
            sw_women.write('\n')
            print(y['name'])
        else:
            sw_men.write(y['name'])
            sw_men.write('\n')



#"gender": "female"

sw_men.close()
sw_women.close()