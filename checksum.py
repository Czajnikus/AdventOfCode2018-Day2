podw = []
potr = []

with open('checksum.txt', 'r') as f:
    ident = [lista.rstrip() for lista in f]

for wyraz in ident:
    for litera in wyraz:
        if wyraz.count(litera) == 2:
            podw.append(wyraz)

        elif wyraz.count(litera) == 3:
            potr.append(wyraz)

print(len(set(podw))*len(set(potr)))
