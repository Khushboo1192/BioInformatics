def transcribetoRNA(word, newString):

 for c in word:
    if c == 'T':
        cnew ='U'
        newString+=cnew
    else:
        newString+=c

 return newString

f = open("input.txt")
samplestring = f.read()
newString=''
ans=transcribetoRNA(samplestring, newString)
f = open('output.txt','w')
f.write(ans) # python will convert \n to os.linesep
f.close()
print ans