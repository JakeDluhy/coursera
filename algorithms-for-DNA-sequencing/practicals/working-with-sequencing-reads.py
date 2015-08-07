import matplotlib.pyplot as plt

def readFastQ(filename):
  sequences = []
  qualities = []
  print 'fastq/' + filename
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

seqs, quals = readFastQ('SRR835775_1.first1000.fastq')

# print(seqs[:5])
# print(quals[:5])

# print(phred33ToQ('#'))
# print(phred33ToQ('J'))

h = createHist(quals)

plt.bar(range(len(h)), h)
plt.show()