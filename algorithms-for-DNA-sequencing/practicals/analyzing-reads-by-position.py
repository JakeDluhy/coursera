# Plotting G, C content to determine whether the mix of different bases changes throughout the read
# Also, different species have different G, C content

import matplotlib.pyplot as plt
import collections

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

def phred33ToQ(qual):
  return ord(qual) - 33

# def qToPhred33(Q):
  # return 

def createHist(qualities):
  hist = [0] * 50
  for qual in qualities:
    for phred in qual:
      q = phred33ToQ(phred)
      hist[q] += 1
  return hist

# Keeping track of total number of bases
# Keeping track of  number of gc bases at each position
# To get the fraction at each position in each read
def findGCByPos(reads):
	gc = [0] * 100
	totals = [0] * 100

	for read in reads:
		for i in range(len(read)):
			if read[i] == 'C' or read[i] == 'G':
				gc[i] += 1
			totals[i] += 1

	for i in range(len(gc)):
		if totals[i] > 0:
			gc[i] /= float(totals[i])

	return gc



seqs, quals = readFastQ('SRR835775_1.first1000.fastq')

gc = findGCByPos(seqs)
plt.plot(range(len(gc)), gc)
plt.show()

# Overall the fraction remains about content
# Greater than 0.5, because human genome has greater GC content

# Now look at distribution of bases in sequences

count = collections.Counter()
for seq in seqs:
	count.update(seq)
print(count)

# N shows up 18 times => means no confidence (sequencer was not able to figure out what was supposed to be there)