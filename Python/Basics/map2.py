temps_celcius = [("Berlin", 29), ("Cairo", 36),
                 ("Dubai", 45), ("Los Angeles", 26)]


def cel_to_fahr(cel):
    fahr = []
    for data in cel:
        fahr.append((data[0], (9/5)*data[1]+32))
    return fahr


temps_farenheit = cel_to_fahr(temps_celcius)
print(temps_farenheit)


def cel1_to_fahr1(cel):
    return (9/5)*cel+32


temps_farenheit = []
for data in temps_celcius:
    temps_farenheit.append((data[0], cel1_to_fahr1(data[1])))
print(temps_farenheit)


def cel2_to_fahr2(cel):
    fahr = []
    fahr.append(cel[0])
    fahr.append((9/5)*cel[1]+32)
    return tuple(fahr)


temps_farenheit = list(map(cel2_to_fahr2, temps_celcius))
print(temps_farenheit)

cel3_to_fahr3 = lambda data: (data[0], (9/5)*data[1]+32)
temps_farenheit = list(map(cel3_to_fahr3, temps_celcius))
print(temps_farenheit)