# d = {}
#
# with open("countries.py") as f:
#     keys = f.readline().split(":")
#     values = f.readline().split()
# d = dict(zip(keys, values))
#
# print(d)

from countries import countries
d = {}
print(type(d))
d = dict(countries)
v = "region"
k = "Asia"

#mydict = {'george':16,'amber':19}
#print(list(mydict.keys())[list(mydict.values()).index(16)])
print(type(d))
print(list(d.keys())[list(d.values()).index(v)])

# for v, k in d.items():
#     if v == k:
#         print(v)

#for key in d:
    # print(key)
    # print(key.items())
    # print(key.keys())
#print(countries["name"])