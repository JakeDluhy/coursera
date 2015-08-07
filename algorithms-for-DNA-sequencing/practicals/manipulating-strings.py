def longestCommonPrefix(s1, s2):
  i = 0
  while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
    i+=1
  return s1[:i]

pre = longestCommonPrefix('ACCATGT', 'ACCAGAC')
print(pre)

def match(s1, s2):
  if not len(s1) == len(s2):
    return False

  for i in range(len(s1)):
    if not s1[i] == s2[i]:
      return False

  return True

result = match('ACCATGT', 'ACCATGT')
print(result)

#or

# s1 == s2

complement = {'A': 'T',
              'C': 'G',
              'G': 'C',
              'T': 'A'}

def reverseComplement(s):
  t = ''
  for base in s:
    t = complement[base] + t
  return t

reverse = reverseComplement('ACCGTCG')
print(reverse)