import re

def validar_senha(senha, comprimento_min=8, usar_maiusculas=True, usar_numeros=True, usar_especiais=True):
    if len(senha) < comprimento_min:
        return False, "Senha muito curta"

    if usar_maiusculas and not re.seach(r"[A-Z]", senha):
        return False, "A senha deve conter ao menos uma letra maiuscula."
    
    if usar_numeros and not re.search(r"0-9", senha):
        return False, "A senha deve conter ao menos um numero."
    
    if usar_especiais and not re.search(r"[!@#$%^&*(),.{}\|<>], senha"):
        return False, "A senha deve conter ao menos um caractere especial."
    
    return True, "A senha 'e valida."
       