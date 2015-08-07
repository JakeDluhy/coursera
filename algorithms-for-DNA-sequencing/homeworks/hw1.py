import matplotlib.pyplot as plt

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

def baseNaive(p, t):
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

def reverseNaive(p, t):
  occurances = []
  reverseP = reverseComplement(p)
  if p == reverseP:
    return baseNaive(p, t)
  else:
    occurances.extend(baseNaive(p, t))
    occurances.extend(baseNaive(reverseP, t))
    return occurances

def naive2(p, t):
  occurances = []
  for i in range(len(t) - len(p) + 1):
    match = True
    mismatches = 0
    for j in range(len(p)):
      if t[i+j] != p[j]:
        if mismatches >= 2:
          match = False
          break
        else:
          mismatches += 1
    if match:
      occurances.append(i)
  return occurances

genome = readGenome('lambda_virus.fa')

print 'Problem 1'
AGGTOccurances = reverseNaive('AGGT', genome)
print len(AGGTOccurances)

print 'Problem 2'
TTAAOccurances = reverseNaive('TTAA', genome)
print len(TTAAOccurances)

print 'Problem 3'
ACTAAGTOccurances = reverseNaive('ACTAAGT', genome)
# print ACTAAGTOccurances
print min(ACTAAGTOccurances)

print 'Problem 4'
AGTCGAOccurances = reverseNaive('AGTCGA', genome)
# print AGTCGAOccurances
print min(AGTCGAOccurances)

print 'Problem 5'
TTCAAGCCOccurances = naive2('TTCAAGCC', genome)
print len(TTCAAGCCOccurances)

print 'Problem 6'
AGGAGGTTOccurances = naive2('AGGAGGTT', genome)
# print AGGAGGTTOccurances
print min(AGGAGGTTOccurances)

print 'Problem 7'
reads, quals = readFastQ('ERR037900_1.first1000.fastq')

def phred33ToQ(qual):
  return ord(qual) - 33

totalQuals = []
histogram = [0] * 100
for qual in quals:
  for i in range(len(qual)):
    q = phred33ToQ(qual[i])
    if q == 2:
      histogram[i] += 1

plt.bar(range(len(histogram)), histogram)
plt.show()

print histogram.index(max(histogram))

# for val in totalQuals:
#   if val > 50:
#     print val
# nCount = []
# for read in reads:
#   nCounter = 0
#   for base in read:
#     if base == 'N':
#       nCounter += 1
#   nCount.append(nCounter)
# for val in nCount:
#   if val > 2:
#     print val
#     print nCount.index(val)