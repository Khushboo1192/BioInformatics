def complementStrand(sampleDNA):

  complementDNA=''
  sampleDNAtemp=sampleDNA[::-1]
  flag=False

  for c in sampleDNAtemp:
    if c == 'A':
        cnew ='T'
        complementDNA+=cnew
    elif c == 'C':
        cnew ='G'
        complementDNA+=cnew
    elif c == 'G':
        cnew ='C'
        complementDNA+=cnew
    elif c == 'T':
        cnew ='A'
        complementDNA+=cnew

  if sampleDNA == complementDNA:
      flag=True
  else :
      flag=False

  return flag;

sampleIn = [line.rstrip('\n') for line in open('input.txt')]
print sampleIn
i=0
dnaStr2=''
for s in sampleIn :
    if i == 0 :
        i+=1
    else :
       dnaStr2+=s
       i+=1
print dnaStr2

lencheck=len(dnaStr2)
f = open('output1.txt', 'w')
flag=4
while flag < 13 :
  j=0
  for c in dnaStr2:
    x=j+flag

    if x-1 < lencheck :
        temp=dnaStr2[j:x]

        ans=complementStrand(temp)
        if ans == True :
            print j+1,flag
            a=j+1
            f.write(a.__str__())
            f.write(' ')
            f.write(flag.__str__())
            f.write('\n')
    j+=1
  flag+=1