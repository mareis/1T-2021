saldo = 0
innskudd = 1000
rente = 0.001
vf = 1 + rente
ant_mnd = 10*12


for mnd in range(ant_mnd):
    saldo = saldo + 1000
    saldo = saldo*vf
    #print(saldo)

# Skriv ut endelig saldo der du svarer på spørsmålet over
print(f'Saldo etter 10 år med sparing: {saldo:.2f} kr.')