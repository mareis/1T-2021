# Vekstfaktor
# Øker:     V = (1 + p)
# Minker:   V = (1 - p)
# Formel:   G*V = N

lønn = 170      # Lønn på bring i kr
overtid = 0.5   # Prosentvis overtidsbetaling

G = lønn
V = 1 + overtid # Vekstfaktor 1 + p = 1 + 0.5 = 1.5
N = G*V         # Ny lønn = Gammel lønn GANGER Vekstfaktor

print(f'Ovrtidslønn: {N:.2f} kr.')