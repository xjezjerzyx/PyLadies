import  json
with open('py1.2.json') as f:
    a = json.load(f)
    sw_all_heroes = open('sw_all_heroes.txt', 'w')
    for y in a:
        str = '{} wazy {} kg jest {} i pochodzi z {} '.format(y['name'], y['mass'], y['gender'], y['homeworld'])
        sw_all_heroes.write(str)
        sw_all_heroes.write('\n')

sw_all_heroes.close()