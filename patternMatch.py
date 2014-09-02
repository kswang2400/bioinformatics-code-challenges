# Solve the Pattern Matching Problem (restated below).

# Pattern Matching Problem: Find all occurrences of a pattern in a string.
#      Input: Two strings, Pattern and Genome.
#      Output: All starting positions where Pattern appears as a substring
#      of Genome.

# Note: Throughout this chapter, we will use 0-based indexing in problem 
# implementations, meaning that we count starting at 0 instead of 1. 
# For example, the starting positions of ATA in CGATATATCCATAG are 2, 4, 
# and 10 instead of 3, 5, and 11.

# Sample Input:
#      ATAT
#      GATATATGCATATACTT

# Sample Output:
#      1 3 9

sequence = input("What is the genetic sequence? ")
pattern = input("What is the pattern? ")

DNA = str(sequence.upper())
kmer = str(pattern.upper())
k = len(kmer)
output = list()

for i in range(0, len(DNA) - k + 1):
	substring = DNA[i:i + k]
	if substring == kmer:
		output.append(str(i))

answer = ' '.join(output)
print(answer)
