import json

#
#
#
#
#
#
#

d = {}
x = ''
a= {}
b = {}
k = {}
yyy = {}
xxx = {}

with open("py1.2.txt") as file:
    x = file.readlines()
    keys = ['name']#, 'height', 'eyes']
    values = ['']
    for a in x:
       # d = dict([(a.split('has'),a.split('is') )])
        q = a.find('. ') + 2
        w = a.find('has')
        e = a.find('has') + 3
        d = a[q:w] # name
        m = a.find('and')
        p = a[e:m]  #eyes
        i = a.find('is') + 2
        o = a.find('is') + 2
        n = a.find('cm')
        k = a[i:n] # height
        values.extend(d)#, k, p)
        print(d, k, p)
        # xxx = dict(d, k, p)
        xxx = dict(zip(keys, values))

        print(xxx)

       # d['height'] = a.split('is')
       # dict(zip(d['name'], d['height']))

       # for i in b :
       #     print(i)
       # for a in d:
       #     print(a)

