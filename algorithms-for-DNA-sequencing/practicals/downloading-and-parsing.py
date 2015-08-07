import collections

def readGenome(filename):
  genome = ''
  with open('fastq/' + filename, 'r') as f:
    for line in f:
      if not line[0] == '>':
        genome += line.rstrip()
  return genome

genome = readGenome('lambda_virus.fa')

# counts = {'A': 0, 'C': 0, 'G': 0, 'T':0}
# for base in genome:
#   counts[base] += 1

counts = collections.Counter(genome)

print counts