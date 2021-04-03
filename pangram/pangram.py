def is_pangram(oracion):
    abecedario = 'abcdefghijklmnopqrstuvwxyz'
    for i in abecedario:
        if i not in oracion.lower():
            return False
    return True
