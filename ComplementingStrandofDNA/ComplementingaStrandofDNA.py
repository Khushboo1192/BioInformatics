
def complementStrand(sampleDNA,complementDNA):

  for c in sampleDNA:
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
  return complementDNA;

f = open("input.txt")
sampleDNA = f.read()
sampleDNA=sampleDNA[::-1]
complementDNA=''
complementDNA=complementStrand(sampleDNA,complementDNA)
f = open('output.txt','w')
f.write(complementDNA) # python will convert \n to os.linesep
f.close()
print complementDNA
