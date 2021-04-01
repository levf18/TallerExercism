def convert(number):
    respuesta1 = "Pling"
    respuesta2 = "Plang"
    respuesta3 = "Plong"
    acum = ""
    if number % 3 == 0:
        acum += respuesta1
    if number % 5 == 0:
        acum += respuesta2
    if number % 7 == 0:
        acum += respuesta3
    if acum == "":
        acum += str(number)
    return acum
