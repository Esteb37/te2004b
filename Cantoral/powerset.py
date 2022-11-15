

def add(superset, subset, index, sets):
    sets.append(subset)
    for i, num in enumerate(superset[index:]):
        add(superset, subset+[num], index + i + 1, sets)


def powerset(superset):
    sets = []
    add(superset, [], 0, sets)
    return sets


superset = input("Set: ").split()

print(powerset(superset))
