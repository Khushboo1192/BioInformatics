def computeHammingDistance(dnaStr1, dnaStr2):
    distance=0
    j=0
    for i in dnaStr1:
        if dnaStr1[j] != dnaStr2[j] :
           distance+=1
        j+=1
    return distance

sampleIn = [line.rstrip('\n') for line in open('input.txt')]

dnaStr1=sampleIn.pop()
dnaStr2=sampleIn.pop()
dist=computeHammingDistance(dnaStr1,dnaStr2)

print dist