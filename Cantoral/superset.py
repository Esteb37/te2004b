
powerset = input("Set: ").split()

sets = []


def add(zet, index):
    sets.append(zet)
    for i, num in enumerate(powerset[index:]):
        add(zet+[num], index + i + 1)


add([], 0)
print(sets)
