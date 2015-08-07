

def readGenome(filename):
  genome = ''
  with open('fastq/' + filename, 'r') as f:
    for line in f:
      if not line[0] == '>':
        genome += line.rstrip()
  return genome

def readFastQ(filename):
  sequences = []
  qualities = []
  with open('fastq/' + filename) as fh:
    while True:
      fh.readline()
      seq = fh.readline().rstrip()
      fh.readline()
      qual = fh.readline().rstrip()
      if len(seq) == 0:
        break
      sequences.append(seq)
      qualities.append(qual)
  return sequences, qualities

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

phix_reads, _ = readFastQ('ERR266411.1.fastq')

numMatched = 0
n = 0
for r in phix_reads:
	r = r[:30] # To adjust for the fact that there are more errors later on in the read
	matches = naive(r, genome)
	n += 1
	if len(matches) > 0:
		numMatched += 1

print('%d / %d reads matched the genome!' % (numMatched, n))

# Reads not matching very well - why?
# Well you have some errors so it's difficult to get an exact match
# But also some of the reads are coming from complementary base pairs - need to check those too!

def reverseComplement(s):
  complement = {'A': 'T',
                'C': 'G',
                'G': 'C',
                'T': 'A',
                'N': 'N'}
  t = ''
  for base in s:
    t = complement[base] + t
  return t

numMatched = 0
n = 0
for r in phix_reads:
	r = r[:30] # To adjust for the fact that there are more errors later on in the read
	matches = naive(r, genome)
	matches.extend(naive(reverseComplement(r), genome))
	n += 1
	if len(matches) > 0:
		numMatched += 1

print('%d / %d reads matched the genome with complements!' % (numMatched, n))