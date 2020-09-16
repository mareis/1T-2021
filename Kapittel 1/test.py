saldo = 46890
avdrag = 2028.42
rente = 0.15
ant_år = 10
renteutgift = 0

for år in range(ant_år):
    saldo = saldo - avdrag
    renter = saldo*rente
    renteutgift += renter
    saldo = saldo - renter

    print(renteutgift, saldo)