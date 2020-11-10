import numpy.random as rn


def get_ant_kron(n):
    ant_kron = 0
    for i in range(n):
        kast = rn.randint(0, 1)
        if kast == 0:
            ant_kron += 1

    return ant_kron


print(get_ant_kron(1000))

