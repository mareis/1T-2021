## 1.31
saldo = 15000
rente = 0.032
vekstfaktor = 1 + rente

endelig_saldo = saldo*vekstfaktor**5

print(f'Saldo om 5 år: {endelig_saldo:.2f} kr.')