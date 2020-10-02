# Antall løsninger i en andregradslikning
# Vi bruker diskriminenten, D = b**2 - 4*a*c
# Form på likning: a*x**2 + b*x + c = 0

a = 1
b = 0
c = 4

D = b**2 - 4*a*c

# Ingen løsning:
#Hvis D<0 så har vi ingen løsning
if D < 0:
    print("Likningen har ingen løsning.")

#Ellers hvis D = 0 så har vi én løsning.
elif D == 0:
    print("Likningen har én løsning.")

#Ellers hvis D > 0 så har vi to løsning.
elif D > 0:
    print("Likningen har to løsninger.")


