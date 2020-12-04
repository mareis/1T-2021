saldo = 34000
rente = 0.034
vf = 1 + rente
ant_år = 10

// Med formel
sluttsaldo = saldo*vf**ant_år
print(f'Etter {ant_år} år er saldoen {sluttsaldo:.2f} kr.')

// Med for-løkke
for år in range(1, ant_år+1):
    saldo = saldo*vf
    print(f'Saldo etter {år:2} år: {saldo:.2f}')
