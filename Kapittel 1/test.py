lån = 125000                # Forbrukslån (kr)
terminbeløp = 20000         # Årlige terminbeløp (kr)
rente = 0.15                # Renter på lånet
renteutgift = 0
år = 0

while lån > 0:
    renter = lån*rente
    renteutgift += renter
    avdrag = terminbeløp-renter
    lån = lån - avdrag
    år = år + 1

print(år)
print(lån)
print(renteutgift)