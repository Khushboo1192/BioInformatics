def count_nucleotides(word,countArr):
  count = 0
  for c in word:
    if c == 'A':
      countArr[0] += 1
    elif c == 'C':
      countArr[1] += 1
    elif c == 'G':
      countArr[2] += 1
    elif c == 'T':
      countArr[3] += 1

  return countArr

f = open("input.txt")
samplestring = f.read()
countArr=[0,0,0,0]
ans=count_nucleotides(samplestring, countArr)
print ans.__getitem__(0),ans.__getitem__(1),ans.__getitem__(2),ans.__getitem__(3)