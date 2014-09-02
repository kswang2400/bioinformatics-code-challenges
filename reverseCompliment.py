# Given a nucleotide p, we denote its complementary nucleotide as p. 
# The reverse complement of a string Pattern = p1…pn is the string 
# Pattern = pn … p1 formed by taking the complement of each nucleotide 
# in Pattern, then reversing the resulting string. We will need the 
# solution to the following problem throughout the book:

# Reverse Complement Problem: Reverse complement a nucleotide pattern.
#      Input: A DNA string Pattern.
#      Output: Pattern, the reverse complement of Pattern.

# CODE CHALLENGE: Solve the Reverse Complement Problem.

# Sample Input:
#      AAAACCCGGT

# Sample Output:
#      ACCGGGTTTT

dataset = input("What is the DNA string pattern? ")

forwardString = list(str(dataset.upper()))

def complement(DNAstring):
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
	print(" ")
	print(answer)
	return None

complement(forwardString)
