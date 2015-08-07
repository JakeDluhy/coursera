from collections import defaultdict

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

def editDist(x, y):
  # Init
  D = []
  for i in range(len(x)+1):
    D.append([0] * (len(y)+1))
  for i in range(len(x)+1):
    D[i][0] = i

  for i in range(1, len(x)+1):
    for j in range(1, len(y)+1):
      delta = 0 if x[i-1] == y[j-1] else 1
      case1 = D[i-1][j-1] + delta
      case2 = D[i-1][j] + 1
      case3 = D[i][j-1] + 1
      D[i][j] = min(case1, case2, case3)

  return min(D[-1])

def overlap(a, b, min_length=3):
  """ Return length of longest suffix of 'a' matching
      a prefix of 'b' that is at least 'min_length'
      characters long.  If no such overlap exists,
      return 0. """
  start = 0  # start all the way at the left
  while True:
    start = a.find(b[:min_length], start)  # look for b's suffx in a
    if start == -1:  # no more occurrences to right
      return 0
    # found occurrence; check for full suffix/prefix match
    if b.startswith(a[start:]):
      return len(a)-start
    start += 1  # move just past previous match

def indexReadKmers(reads, k):
  index = defaultdict(list)
  for i, read in enumerate(reads):
    for j in range(len(read)-k):
      kmer = read[j:(j+k)]
      index[kmer].append(i)
  return index

def getReadOverlaps(index, reads, k):
  overlaps = []
  for ind, read in enumerate(reads):
    suf = read[-k:]
    readIndexes = index[suf]
    for rIndex in readIndexes:
      if ind != rIndex:
        olap = overlap(read, reads[rIndex], k)
        if olap != 0:
          overlaps.append((ind, rIndex))
  return overlaps



genome = readGenome('chr1.GRCh38.excerpt.fasta')

print 'Question 1'
p = 'GCTGATCGATCGTACG'
print editDist(p, genome)


print 'Question 2'
p = 'GATTTACCAGATTGAG'
print editDist(p, genome)

# print 'Question 3'
# reads, quals = readFastQ('ERR266411_1.for_asm.fastq')
# index = indexReadKmers(reads, 30)
# overlaps = getReadOverlaps(index, reads, 30)
# print len(overlaps)

# print 'Question 4'
# nodeMap = defaultdict(list)
# for edge in overlaps:
#   nodeMap[edge[0]].append(edge[1])
# print len(nodeMap)