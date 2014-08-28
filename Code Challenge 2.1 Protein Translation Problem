# Protein Translation Problem: Translate an RNA string into an amino acid string.
#      Input: An RNA string Pattern.
#      Output: The translation of Pattern into an amino acid string Peptide.

# CODE CHALLENGE: Solve the Protein Translation Problem.

# Notes:

# The “Stop” codon should not be translated, as shown in the sample below.
# For your convenience, we provide a downloadable RNA codon table indicating 
# which codons encode which amino acids.

f = open('codon.txt', 'r')
f1 = open('../Downloads/dataset_18_3.txt', 'r')

s = f.readlines()
# print(s)

RNA = f1.read()

codon = {}

for pair in s:
	if codon[pair[:3]] in codon:
		codon[pair[:3]].append(pair[4])
	else:
		codon[pair[:3]] = pair[4]

# print(codon)

answer = []

for i in range(0, len(RNA), 3):
	triplet = RNA[i:i+3]
	if triplet in codon:
		answer.append(codon[triplet])

# print(answer)

output = ''.join(answer)
print(output)
