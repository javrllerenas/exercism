DNA_TO_RNA = {
    'A': 'U',
    'C': 'G',
    'G': 'C',
    'T': 'A'
}

KEYS = set(DNA_TO_RNA.keys())

def dna_nucleotide_compliment(letter):
    return DNA_TO_RNA[letter]

def to_rna(dna_strand):
    '''Return the RNA complement of a DNA string'''
    rna = ''
    for nucleotide in dna_strand:
        if nucleotide not in KEYS:
            raise Exception('The string you passed is an invalid DNA strand')
        rna += DNA_TO_RNA[nucleotide]
    
    return rna

    
