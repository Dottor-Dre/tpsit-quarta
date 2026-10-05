#es1
def conta_unici(nomi):
    return len(set(nomi))

nomi = ["Luca", "Sara", "Marco", "Luca", "Giulia", "Sara", "Luca"]
print(conta_unici(nomi))
#----------------------------------------------------------------------------------------
#es2
capitali = {"Italia": "Roma", "Francia": "Parigi", "Spagna": "Madrid"}
def capitale(paese):
    return capitali.get(paese, "paese non in elenco")
print(capitale("Italia"))
#----------------------------------------------------------------------------------------
#es3
def sufficiente(voti):
    return [v for v in voti if v >= 6]

print(sufficiente([4, 7, 5, 8, 6, 3]))
print(sufficiente([]))

#----------------------------------------------------------------------------------------
#es4
def senza_duplicati(elementi):
    visti = set()
    risultato = []
    for e in elementi:
        if e not in visti:
            visti.add(e)
            risultato.append(e)
    return risultato

nomi = ["Sara", "Luca", "Sara", "Marco", "Luca", "Giulia"]
print(senza_duplicati(nomi))
print(sorted(set(nomi)))
#----------------------------------------------------------------------------------------
#es5
def conta_parole(frase):
    conteggio = {}
    for parola in frase.lower().split():
        conteggio[parola] = conteggio.get(parola, 0) + 1
    return conteggio

frase = "il gatto dorme il cane dorme il topo corre"
risultato = conta_parole(frase)
print(risultato)

piu_frequente = max(risultato, key=risultato.get)
print(piu_frequente, risultato[piu_frequente])