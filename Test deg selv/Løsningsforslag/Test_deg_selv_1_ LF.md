## Test deg selv - uke 35

#### Løsningsforslag

### Informasjon om test-deg-selv

Dette er oppgaver som er ment som mengdetrening i programmering. Det legges ut løsningsforslag etter at vi har gått gjennom og løst oppgavene i webinaret. Se Blackboard for mer informasjon om tidspunkt for dette.

Oppgavene er strukturert på samme måte som i øvingene: Det er tre kategorier: 1(grunnleggende), 2(forventet), 3(avansert). Kategori 1 og 3 har én oppgave hver, imens kategori 2 har fire oppgaver. Oppgavene i kategori 2 er det forventet at man klarer å løse.

Står du fast? Prøv å google problemet, eller spør om tips eller hjelp på Slack :)

Temaene disse ukene er:

- Variabler
- Datatyper
- Print

## 1) Variabler

## 1.1

Hva er feil eller dårlig med variabelnavnene under? Gi en kort forklaring og gi dem til bedre variabelnavn.

a) Et tall = 123

b) 3variabelen = 3

c) Variabel1 = "teksten skal hit"

d) detførstetallet = "1"

e) %AvTallet = 15

f) SummenAvRegnestykketEr = 16

```python
# a)
etTall = 123 # Variabelnavn kan ikke inneholde andre tegn enn bokstaver, tall eller under/bindestrek
# b)
tre = 3 # Variabelnavn kan ikke starte med tall
# c)
forst = 123 # Langt navn, tallene er definert som tekst, noe som kan gi problemer senere hvis man skal bruke tallene
# d)
prst = 15 # Spesialtegn er ikke tillatt i variabelnavn
# e)
summen = 18 # Unødvendig langt navn
```

## 2) Datatyper

## 2.1

Skriv et program som skriver "5 ganger 10 er 50" til konsoll ved å bruke variabler for tallene 5, 10 og 50.

```python
tall1 = 5
tall2 = 10
produkt = 5*10

print(f'{tall1} ganger {tall2} er {produkt}.')
```

## 2.2

Skriv et program som bruker variablene under (erstatt variabelnavnene med mer passende navn) til å skrive forslag til e-post adresser til konsoll.

Kriterier:

- Epostadressene skal bestå av fornavn og etternavn, separert med punktum, etterfulgt av @ og et valgfritt domene, for eksempel "test.testesen@bedrift.no".

- Epostadressene som skrives ut skal være uten mellomrom.

- Variabelen som inneholder "domene" skal ikke inneholde "@".

- Epostadressen skal lagres i en egen variabel, og denne nye variabelen skal printes ut

var1 = fornavn

var2 = etternavn

var3 = domene

```python
fornavn = 'mads'
etternavn = 'reistadbakk'
domene = 'mrfylke.no'

print(f'{fornavn}.{etternavn}@{domene}')
```

## 2.3

a) Hvorfor blir ikke regnestykket under regnet ut når print-setningen kjøres?

print("4 + 6")

b) Skriv et program som lagrer tallet 42 i en variabel, og skriver "Svaret på alt er 42" til konsoll ved å bruke variabelen med tallet 42.

c) Hvorfor blir to forskjellige tall printet når koden under kjøres?

a = 3.4

b = 20.5

total = a \* b

print(total)

print(int(total))

```python
# a)
# Fordi tallene i print-setningen er definert som tekst.

# b)
alt = 42
print(f'Svaret på alt er {alt}.')

# c)
# i den andre print-setningen er tallet definert som en int, som er heltall. Da printes bare det hele tallet uten desimaler.
```

## 3) Sammensatte datatyper

## 3.1

Skriv et program som lager romkoder i en kontorbygning ved å bruke informasjonen under. Romkoden er satt sammen slik: (etasjenummer)(romtype-forkortelse)(romnummer), for eksempel 03K03, som betyr etasje nr 3, K for Kontor og 03 for kontor nr 3.

Mulige verdier i variablene:

Etg: 1-6

Romtype: Kontor, møterom, lager, samtalerom

Romnummer: 1-25

Skriv ut tre eksempler på romnummer, kalt rom1, rom2 og rom3 ved å lage tre variabler som har verdier fra listen over.

```python
etg1 = 2
type1 = 'K'
romnr1 = 20

etg2 = 6
type2 = 'L'
romnr2 = 1

etg3 = 1
type3 = 'M'
romnr3 = 4

print(f'Rom 1: {etg1}{type1}{romnr1}')
print(f'Rom 2: {etg2}{type2}{romnr2}')
print(f'Rom 3: {etg3}{type3}{romnr3}')
```
