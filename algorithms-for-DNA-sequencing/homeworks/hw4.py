import itertools
from collections import defaultdict

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

def overlap(a, b, min_length=3):
  start = 0
  while True:
    start = a.find(b[:min_length], start)
    if start == -1:
      return 0
    if b.startswith(a[start:]):
      return len(a) - start
    start += 1

def pick_maximal_overlap(index, k):
  reada, readb = None, None
  best_olen = 0
  for kmer, reads in index.items():
    for a,b in itertools.permutations(reads, 2):
      if a != b:
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
          reada, readb = a, b
          best_olen = olen

  return reada, readb, best_olen

def greedy_scs(reads):
  reada, readb, olen = None, None, None
  k = 100
  while k > 0:
    index = indexReadKmers(reads, k)
    reada, readb, olen = pick_maximal_overlap(index, k)
    if olen == 0:
      k -= 1
    else:
      reads.remove(reada)
      reads.remove(readb)
      reads.append(reada + readb[olen:])
  return ''.join(reads)

def getReadOverlaps(index, reads, k):
  overlaps = []
  for ind, read in enumerate(reads):
    suf = read[-k:]
    readIndexes = index[suf]
    for rIndex in readIndexes:
      if ind != rIndex:
        olap = overlap(read, reads[rIndex], k)
        if olap != 0:
          overlaps.append((ind, rIndex, olap))
  return overlaps

def indexReadKmers(reads, k):
  index = defaultdict(list)
  for i, read in enumerate(reads):
    for j in range(len(read)-k):
      kmer = read[j:(j+k)]
      index[kmer].append(read)
  return index

reads, quals = readFastQ('ads1_week4_reads.fq')

DNA = greedy_scs(reads)
print DNA

print 'Question 1'
print DNA.count('A')

print 'Question 2'
print DNA.count('T')

# k = 100
# index = None
# overlaps = None
# while(k > 0):
#   index = indexReadKmers(reads, k)
#   overlaps = getReadOverlaps(index, reads, k)
#   if len(overlaps) == 0:
#     k -= 1
#     print k
#   else:
#     overlaps.sort(key=lambda tup: tup[2], reverse=True)
#     # if len(overlaps) > 1:
#     #   topOlap = overlaps[0] if overlaps[0][2] != overlaps[1][2] else overlaps[1]
#     # else:
#     #   topOlap = overlaps[0]
#     topOlap = overlaps[0]
#     print topOlap[0]
#     print topOlap[1]
#     print reads[topOlap[0]] + reads[topOlap[1]][topOlap[2]:]
#     reads.append(reads[topOlap[0]] + reads[topOlap[1]][topOlap[2]:])
#     del reads[topOlap[0]]
#     del reads[topOlap[1]]

# print reads
# final = ''.join(reads)
# print len(final)
