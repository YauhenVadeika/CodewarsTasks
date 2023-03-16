# my task solution
def dna_to_rna(dna):
    return "".join([i.replace('T', 'U') for i in dna])


print(dna_to_rna("TTTT"))


# codewars task best solution
def DNAtoRNA(dna):
    return dna.replace('T', 'U')


# codewars task best solution
def DNAtoRNA(dna):
    RNA = ""
    i = 0
    for i in dna:
        if i == "T":
            RNA = RNA + "U"
        else:
            RNA = RNA + i
    return RNA


# codewars task best solution
def DNAtoRNA(dna):
    rna = dna.replace("T", "U")
    return rna


# codewars task best solution
DNAtoRNA = lambda d: d.replace("T", "U")


# codewars task best solution
def DNAtoRNA(dna):
    return "".join(["U" if c == "T" else c for c in dna])


# codewars task best solution
dna_dict = {'T': 'U', 'A': 'A', 'C': 'C', 'G': 'G'}


def DNAtoRNA(dna):
    rna = []
    for letter in dna:
        rna.append(dna_dict[letter])
    return "".join(rna)