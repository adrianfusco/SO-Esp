import urllib.request
import json

URL_ADDRESS = 'https://dinahosting.com/dominios/ajax-precios-por-categoria?categoria=top100&pagina='

responses = []

for i in range(1, 15+1):
    responses.append(urllib.request.urlopen(URL_ADDRESS+str(i)))

contents = [response.read().decode('UTF-8') for response in responses]

tldsInformation = [json.loads(content) for content in contents]

total = 0

for tlds in tldsInformation:
    for tld in tlds:
        total += 1
        print("TLD:", tld['tld'], "-", "Precio Alta:", tld['precioAltaParteEntera']+tld['precioAltaParteDecimal']+tld['precioAltaMoneda'])

print("Total of TLDs:", total)

# Result:

#   TLD: gal - Precio Alta: 8'95€
#   TLD: eus - Precio Alta: 20'99€
#   TLD: cat - Precio Alta: 8'95€
#   TLD: es - Precio Alta: 8'99€
#   TLD: pt - Precio Alta: 12'49€
#   TLD: it - Precio Alta: 12'95€
#   TLD: fr - Precio Alta: 11'99€
#   TLD: co.uk - Precio Alta: 10'95€
#   ...
#   Total of TLDs: X