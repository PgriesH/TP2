BASE = 4

fromage = 800.0

eau = 2

ail = 2

pain = 400


nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue :"))

nvfromage = fromage * nbConvives/BASE

nveau = eau * nbConvives / BASE

nvail = ail * nbConvives / BASE

nvpain = pain * nbConvives / BASE

print('Pour faire une fondue fribourgeoise pour' , nbConvives , 'personnes , il vous faut :')

print('-' , nvfromage , 'gr de fromage')
print('-' , nveau ,  "dl d' eau")
print('-', nvail ,  "gousse(s) d' ail")
print('-', nvpain , 'gr de pain')





           
