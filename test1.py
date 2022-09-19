def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague


def goals1(*args):
    return sum(args)


print(goals1(1, 2, 3))
print(goals1(2, 5, 7, 11))

