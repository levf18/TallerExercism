def to_rna(dna_strand):
    hebra = {
        'G': 'C', 'C': 'G',
        'T': 'A', 'A': 'U'
        }
    acum = ''
    for i in dna_strand:
        acum += hebra[i]
    return acum
