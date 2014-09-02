# Generating Theoretical Spectrum Problem: Generate the theoretical spectrum 
# of a cyclic peptide.
#      Input: An amino acid string Peptide.
#      Output: Cyclospectrum(Peptide).

# CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.

# Sample Input:
#      LEQN

# Sample Output:
#      0 113 114 128 129 227 242 242 257 355 356 370 371 484

def peptideCombo(peptide):
	linPepCombo = []
	cycPepCombo = []
	for a in range(0, len(peptide)): #linear subpeptides
		for b in range(a, len(peptide)):
			linPepCombo.append(peptide[a:b + 1])
	for c in range(2, len(peptide)): #cyclic subpeptides
		for d in range(0, c - 1):
			cycPepCombo.append(peptide[c:len(peptide)] + peptide[0:d + 1])
	totalPepCombo = linPepCombo + cycPepCombo
	# print(linPepCombo)
	# print(cycPepCombo)
	# print(totalPepCombo)
	return totalPepCombo

def calcSpectrum(peptideCombo):
	count = {}
	for i, a in enumerate(peptideCombo):
		count[i] = 0
		for p in a:
			count[i] += int(massTable[p])
	return count


# COPY PASTE: create dictionary of mass of peptide

f = open('masstable.txt', 'r')

s = f.readlines()
# print(s)

massTable = {} # key, value = amino acid, list of codons

for line in s:
	massTable[line[0]] = line[2:5]

# print(massTable)
# a = massTable["A"]
# print(int(a))

peptide = input("What is the peptide string? ")

massList1 = []

for n in peptide:
	massList1.append(massTable[n])
# print(massList1)

pep = peptideCombo(peptide)
dictCount = calcSpectrum(pep)
counts = list(dictCount.values())
counts = sorted(counts)
answer = ' '.join(str(i) for i in counts)
print(answer)
