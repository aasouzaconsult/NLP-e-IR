import re
from unicodedata import normalize

def remover_acentos(txt, codif='latin-1'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII', 'ignore')

# Texto Completo
with open("bases/Iracema-jose-de-alencar.txt") as f:
	text = f.read()

text = remover_acentos(text)

# Capitulo I
with open("bases/Iracema-jose-de-alencar-Cap1.txt") as c1:
	Cap1 = c1.read()

Cap1 = remover_acentos(Cap1)
	
# Remove os espaços em branco
# Capítulo I
Cap1SE = re.sub(r'\s', '', Cap1)

# Voltar os espaços