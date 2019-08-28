d = {1: "one", 3: "three"}
d1 = {2: "two"}
dic = {}
for l in (d, d1): dic.update(l)
print(dic)