# Peptide Encoding Problem: Find substrings of a genome encoding a 
# given amino acid sequence.
#      Input: A DNA string Text and an amino acid string Peptide.
#      Output: All substrings of Text encoding Peptide (if any such 
# 		substrings exist).

# CODE CHALLENGE: Solve the Peptide Encoding Problem.

# Sample Input:
#      ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
#      MA

# Sample Output:
#      ATGGCC
#      GGCCAT
#      ATGGCC

# Note: The solution may contain repeated strings if the same string 
# occurs more than once as a substring of Text and encodes Peptide.

def complementD(DNAstring):
	for n, i in enumerate(DNAstring):
		if i == "A":
			DNAstring[n] = "T"
		elif i == "T":
			DNAstring[n] = "A"
		elif i == "C":
			DNAstring[n] = "G"
		elif i == "G":
			DNAstring[n] = "C"

	DNAstring.reverse()
	answer = ''.join(DNAstring)
	return answer

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

def checkMatch(answer, peptide, dataset):
	checkPosition = []
	output = []

	for i in range(0, len(answer) - len(peptide) + 1):
		sample = answer[i:i + len(peptide)]
		if sample == peptide:
			checkPosition.append(i * 3)

	for i in checkPosition:
		r = dataset[:3 * len(peptide)]
		output.append(r)
	return output

def stringAmino(n, Rdataset):
	stringAmino = []
	for i in range(n, len(Rdataset), 3):
		triplet = Rdataset[i:i+3]
		if triplet in codonToAmino:
			stringAmino.append(codonToAmino[triplet])
	answer = ''.join(stringAmino)
	return answer

def revert(strand):
	output = []
	for i in strand:
		x = complementD(list(i))
		output.append(x)
	answer = ' '.join(output)
	return answer

# Input DNA pattern and sample peptide

dataset = input("What is the DNA pattern? ")
peptide = input("What is the peptide pattern? ")

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

# print(aminoToCodon)
# print(" ")
# print(codonToAmino)

# Transcribe DNA dataset into RNA Rdataset; reverse complement Rdataset

Rdataset = dataset.replace("T", "U")
RRdataset = complementR(list(Rdataset))
# print(Rdataset)
# print(RRdataset)

# convert dataset into string of amino acids to compare with peptide strand
# with different frame shifts (optimize?!)

a = stringAmino(0, Rdataset)
b = stringAmino(1, Rdataset)
c = stringAmino(2, Rdataset)
d = stringAmino(0, RRdataset)
e = stringAmino(1, RRdataset)
f = stringAmino(2, RRdataset)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# look through peptide strands to find amino acid string matches
# checkMatch will be list with positions in RNA where peptide matches amino strings

a1 = checkMatch(a, peptide, dataset)
b1 = checkMatch(b, peptide, dataset)
c1 = checkMatch(c, peptide, dataset)
d1 = checkMatch(d, peptide, dataset)
e1 = checkMatch(e, peptide, dataset)
f1 = checkMatch(f, peptide, dataset)

# Need to join as list and revert back the reverse strands

a1x = ' '.join(a1)
b1x = ' '.join(b1)
c1x = ' '.join(c1)
d1x = revert(d1)
e1x = revert(e1)
f1x = revert(f1)

print(a1x)
print(b1x)
print(c1x)
print(d1x)
print(e1x)
print(f1x)

