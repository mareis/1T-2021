rente = 0.032               # 3.2%
vekstfaktor = 1 + rente     # Siden saldo øker blir vekstfaktor 1+p
saldo = 15000               # Beløpet på kontoen
antall_år = 5

#--- Med formel ----
print(f'Saldo etter {antall_år} år: {saldo*vekstfaktor**antall_år:.2f} kr.\n')

#--- Med løkke ----
for i in range(antall_år):
    saldo = saldo*(1+rente)
    print(f'Saldo etter {i+1} år: {saldo:.2f} kr.')