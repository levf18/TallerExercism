def is_isogram(string):
    palabra = string.lower()
    for i in palabra:
        if i != "-" and i != " ":
            letra = palabra.count(i)
            if letra > 1:
                return False
    return True
