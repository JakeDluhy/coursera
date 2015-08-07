import random

def generateRead(genome, numReads, readLen):
	''' Generate reads from random positions in the given genom. '''

	reads = []
	for _ in range(numReads):
		start = random.randint(0, len(genome) - readLen) - 1
		reads.append(genome[start : start+readLen])
	return reads

def readGenome(filename):
  genome = ''
  with open('fastq/' + filename, 'r') as f:
    for line in f:
      if not line[0] == '>':
        genome += line.rstrip()
  return genome

def naive(p, t):
	occurances = []
	for i in range(len(t) - len(p) +1):
		match = True
		for j in range(len(p)):
			if t[i+j] != p[j]:
				match = False
				break
		if match:
			occurances.append(i)
	return occurances

genome = readGenome('phix.fa')

reads = generateRead(genome, 100, 100)

numMatched = 0
for r in reads:
	matches = naive(r, genome)
	if len(matches) > 0:
		numMatched += 1

print('%d / %d reads matched exactly!' % (numMatched, len(reads)))