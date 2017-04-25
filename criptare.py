n = raw_input("Ciffre cle pour le cryptage: ")
text = raw_input("Votre texte: ")
alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
nou_text = []
nou1_text = []

def codcaesar (text,n):
    for x in text:
        for y in alfabet:
            if(x == y):
                a = alfabet.find(y) + int(n)
                nou_text.append(alfabet[a])
    return nou_text

def decodcaesar (n, text1):
    for x in text1:
        for y in alfabet:
            if(x == y):
                a = alfabet.find(y) - int(n)
                nou1_text.append(alfabet[a])
    return nou1_text


codcaesar(text, n)
print "Mesajul introdus este: "+text   
nou = "".join(nou_text)
print "Mesajul codificat este: "+nou
decodcaesar(n, nou)
nou2 = "".join(nou1_text)
print "Mesajul decodificat este: " + nou2

