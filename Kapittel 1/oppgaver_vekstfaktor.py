## 1.31
saldo = 15000
rente = 0.035
vekstfaktor = 1 + rente
antall_år = 5

saldo_slutt = saldo*vekstfaktor**antall_år

print("Oppgave 1.31")
print(f"Saldoen til Line er {saldo_slutt:.2f} kr etter {antall_år} år.")

## 1.32
bank = (1.035**5-1)*100
fond = (1.03*1.07*1.01*1.02*1.04-1)*100
print("\nOppgave 1.32")
print(f"Bank: {bank:.2f} %")
print(f"Aksjefond: {fond:.2f} %")
print("Banken hadde best avkastning de siste 5 årene.")


