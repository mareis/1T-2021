# Oblig 1
---
I denne innlevering skal du implementere Hangman. Du får utdelt en funksjon (trekk_ord()) som returnerer et tilfeldig ord fra en liste når den blir kalt på. Du trenger filen <a href='https://github.com/mareis/ProMod-1920/blob/master/02_Oppgaver/02_Innleveringer/ord.py'>ord.py</a> som må legges i samme mappen som hangman.py-filen din. For å bruke den kan du benytte følgende kode i hangman.py-filen din.


```python
import ord

tilfeldig_ord = ord.trekk_ord()
```

Utgaven vår av spillet skal fungere på følgende måte:

 - Vi får et ord fra funksjonen `lag_ord()` som skal gjettes av brukeren i terminalen. I koden over    lagres ordet i variabelen `tilfeldig_ord`
 - Den første bokstaven i ordet skal skrives ut med etterfølgende __ ut fra antall resterende bokstaver det er ordet. Hvis ordet er Byte så skal B  __  __  __ skrives ut til brukeren.
 - Deretter vil du spørre brukeren taste inn en bokstav. 
   - Hvis bokstaven er i ordet skal bokstav settes inn og erstatte den riktige __ For eksempel hvis brukeren gjetter t skal programmet skrive ut B __ t __ 
   - Hvis bokstaven ikke er i ordet skal programmet skrive ut hvor mange forsøk brukeren har igjen. I dette spillet er 10 maks. Skriv også ut bokstavene som er gjettet feil.
 - Hvis ordet er komplett skal programmet skrive ut: Du vant, gratulerer! 😀
 
Denne innleveringen er obligatorisk og må leveres senest Torsdag 15/10


Det er lov til å prøve seg med asci-grafikk og gjøre litt mer ut av spillet. 

<img src='https://gieseanw.files.wordpress.com/2010/03/hangman_banner.jpg'>

Kode for å tømme terminal før du skriver ut på nytt:
```python
import os
os.system('cls' if os.name == 'nt' else 'clear')
```