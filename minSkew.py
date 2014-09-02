# Minimum Skew Problem: Find a position in a genome minimizing the skew.
#      Input: A DNA string Genome.
#      Output: All integer(s) i minimizing Skew(Prefixi (Text)) among 
# 		all values of i (from 0 to |Genome|).

# CODE CHALLENGE: Solve the Minimum Skew Problem.

# Sample Input:
#      TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT

# Sample Output:
#      11 24

sequence = input("What is the DNA string genome? ")

DNA = str(sequence).upper()
DNAdict = {}

# Count the skew through the sequence

def findcount(DNA):
	count = 0
	for n, i in enumerate(DNA):
		if i == "C":
			count -= 1
			DNAdict[n] = count
		elif i == "G":
			count +=1
			DNAdict[n] = count
		else:
			DNAdict[n] = count

findcount(DNA)
print(DNAdict)

# Find minimum positions

skew = min(DNAdict.values())

answer = []
for s in DNAdict:
	if DNAdict[s] == skew:
		answer.append(s)

print(answer)

# my answer is one short
