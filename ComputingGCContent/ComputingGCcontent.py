def computingGCcontent(sampleDNAString):
    count = len(sampleDNAString)
    ratio = 0;
    for c in sampleDNAString:
        if c == 'C' or c == 'G':
            ratio += 1

    ratio = ratio * 100;
    var = float(ratio) / count
    return var;


# read the input file
lines = [line.rstrip('\n') for line in open('rosalind_gc.txt')]

# convert the input to the desired output
f = open('output.txt', 'w')
f.write(lines.pop(0))
f.write('\n')
temp2 = ''
for tempstr in lines:
    tempstr.__str__()
    if tempstr[0] == '>':
        f.write(temp2)
        f.write('\n')
        f.write(tempstr)
        f.write('\n')
        temp2 = ''
    else:
        temp2 += tempstr
f.write(temp2)

f.close()
listofDNA = [line.rstrip('\n') for line in open('output.txt')]
maxGCcontent = 0.0
j = 0
ans = 0
info = ''

for i in listofDNA:
    if j % 2 != 0:
        ans = computingGCcontent(i)
    if ans > maxGCcontent:
        info=listofDNA.__getitem__(j-1)
        maxGCcontent=ans
    j+=1

print info[1:];
print maxGCcontent;

