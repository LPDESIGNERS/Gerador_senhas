import random
import string

def gerar_senha(comprimento=12,usar_maiusculas=True,usar_numeros=True,usar_especiais=True):
        caracteres = string.ascii_lowercase
        if usar_maiusculas:
            caracteres += string.ascii_uppercase
        if usar_numeros:
            caracteres += string.digits
        if usar_especiais:
            caracteres += string.punctuation

        senha =''.join(random.choice(caracteres for _ in range(comprimento)))
        return senha