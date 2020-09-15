
apple_aksje_2008 = 10000
årlig_økning = 0.3
vekstfaktor = 1 + årlig_økning

#apple_aksje_2009 = apple_aksje_2008*vekstfaktor
#print(f'verdi i 2009: {apple_aksje_2009:.2f} kr.')
#apple_aksje_2010 = apple_aksje_2009*vekstfaktor
#print(f'verdi i 2010: {apple_aksje_2010:.2f} kr.')
#apple_aksje_2011 = apple_aksje_2010*vekstfaktor
#print(f'verdi i 2011: {apple_aksje_2011:.2f} kr.')

saldo = apple_aksje_2008
for antall_år in range(12):
    saldo = saldo*vekstfaktor
    print(f'Verdi i {2008+antall_år+1}: {saldo:.2f}')


print(apple_aksje_2008*vekstfaktor**12)









