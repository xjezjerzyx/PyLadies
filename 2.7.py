import  json
import operator
from collections import  OrderedDict
with open('py1.2zd.json') as f:
    a = json.load(f)
    #a = dict(a)
    b = {}

    for q in a :
        if q['cost_in_credits'].isdigit():
            None
        else:
            a.pop()

    #b = sorted(a, key=lambda x: x['cost_in_credits'] )
    #b = sorted(a, key=lambda x: int(x['cost_in_credits']))
    for i in b :
        print(i)

    #b = sorted(a[0].items(), key=operator.itemgetter(0))

    #sorted(a, key=lambda x:sorted(x.keys()))
    #a = OrderedDict(sorted(a.items['cost_in_credits'], key=lambda k: k[0]))
    #sorted(a, key=lambda x: sorted(x.keys()))

