# Peptide Encoding Problem: Find substrings of a genome encoding a given 
# amino acid sequence.
#      Input: A DNA string Text and an amino acid string Peptide.
#      Output: All substrings of Text encoding Peptide (if any such substrings 
# exist).

# CODE CHALLENGE: Solve the Peptide Encoding Problem.

# Sample Input:
#      ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
#      MA

# Sample Output:
#      ATGGCC
#      GGCCAT
#      ATGGCC

# Note: The solution may contain repeated strings if the same string occurs 
# more than once as a substring of Text and encodes Peptide.


# stringAmino takes a start position (n) and a RNA string dataset.  It then
# translates the RNA string into a peptide string

def stringAmino(n, Rdataset):
        stringAmino = []
        for i in range(n, len(Rdataset), 3):
                triplet = Rdataset[i:i+3]
                if triplet in codonToAmino:
                        stringAmino.append(codonToAmino[triplet])

        answer = ''.join(stringAmino)
        return answer

# findW looks through pep string for w and prints first index where w is found
# starting at index i

def findW(w, pep, i):
	a = pep.find(w, i)
	return a

# findAllW starts at position 0 and finds first match.  Append position to list 
# and then search again starting at 

def findAllW(w, pep, i):
	positions = []
	while i < len(pep):
		a = findW(w, pep, i)
		if a >= 0:
			positions.append(a)
			i = a + 1
		else:
			break
	return(positions)

# complementR gives the reverse complement of RNA string

def complementR(RNAstring):
        for n, i in enumerate(RNAstring):
                if i == "A":
                        RNAstring[n] = "U"
                elif i == "U":
                        RNAstring[n] = "A"
                elif i == "C":
                        RNAstring[n] = "G"
                elif i == "G":
                        RNAstring[n] = "C"

        RNAstring.reverse()
        answer = ''.join(RNAstring)
        return answer

# revertF and revertR finds the substrings in DNA based on found positions

def revertF(positions, DNA, i):
	DNAsub = []
	for a in positions:
		b = a * 3 + i
		sub = DNA[b:b + 3 * len(w)]
		DNAsub.append(sub)
	return DNAsub

def revertR(positions, DNA, i):
	DNAsub = []
	for a in positions:
		b = a * 3 + i
		c = len(DNA) - b - 1
		d = c - 3 * len(w)
		sub = DNA[d:d + 3 * len(w)]
		DNAsub.append(sub)
	return DNAsub


DNA = input("What is the DNA string? ")
w = input("What is the peptide string? ")


# COPY PASTE: create two dictionaries to translate amino acids to codons
# and vice versa

f = open('codon.txt', 'r')

s = f.readlines()
# print(s)

aminoToCodon = {} # key, value = amino acid, list of codons

for line in s:
        if line[4] in aminoToCodon:
                aminoToCodon[line[4]].append(line[:3])
        else:
                aminoToCodon[line[4]] = [line[:3]]

codonToAmino = {} # key, value = codon, amino acid

for pair in s:
        if pair[:3] in codonToAmino:
                codonToAmino[pair[:3]].append(pair[4])
        else:
                codonToAmino[pair[:3]] = pair[4]

RNA = DNA.replace("T", "U")
revRNA = complementR(list(RNA))
# print(RNA)
# print(revRNA)

pep0 = stringAmino(0, RNA)
pep1 = stringAmino(1, RNA)
pep2 = stringAmino(2, RNA)
rpep0 = stringAmino(0, revRNA)
rpep1 = stringAmino(1, revRNA)
rpep2 = stringAmino(2, revRNA)
# print(pep0)
# print(pep1)
# print(pep2)
# print(rpep0)
# print(rpep1)
# print(rpep2)

a = findAllW(w, pep0, 0)
b = findAllW(w, pep1, 0)
c = findAllW(w, pep2, 0)
d = findAllW(w, rpep0, 0)
e = findAllW(w, rpep1, 0)
f = findAllW(w, rpep2, 0)
# print(a, b, c, d, e, f)

a1 = ' '.join(revertF(a, DNA, 0))
b1 = ' '.join(revertF(b, DNA, 1))
c1 = ' '.join(revertF(c, DNA, 2))
d1 = ' '.join(revertR(d, DNA, 0))
e1 = ' '.join(revertR(e, DNA, 1))
f1 = ' '.join(revertR(f, DNA, 2))
print(a1, b1, c1, d1, e1, f1)

