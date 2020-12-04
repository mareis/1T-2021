verdi = 0
innskudd = 20000
rente = 0.08
vf = 1 + rente

for mnd in range(5):
    verdi = verdi + innskudd
    verdi = verdi * vf
    innskudd = innskudd + 20000

print(f"Verdi etter 5 år med sparing: {verdi:.2f} kr.")
