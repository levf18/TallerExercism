def abbreviate(palabra):
    palabras = palabra.replace('_', ' ').replace('-', ' ')
    vecPalabra = palabras.split()
    acronimo = ''
    for i in vecPalabra:
        acronimo += i[0].upper()
    return acronimo
