s = ""

with open("BRC1sequence.fasta", "r") as file:
    readline=file.read().splitlines()
    for i in range (1,len(readline)):
        s =s+readline[i]


c1=0
c2=0
c3=0
c4=0
c5=0
c6=0


open = False
for x in range(0, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c1+=1


open = False
for x in range(1, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c2+=1


open = False
for x in range(2, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c3+=1

s1 = s[len(s)-1::-1]
s = ""
for x in range(len(s1)):
	if s1[x] == 'A':
		s = s+'T'
	elif s1[x] == 'T':
		s = s+'A'
	elif s1[x] == 'G':
		s = s+'C'
	elif s1[x] == 'C':
		s = s+'G'

open = False
for x in range(0, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c4+=1


open = False
for x in range(1, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c5+=1


open = False
for x in range(2, len(s), 3):
	if s[x:x+3] == 'ATG' and open==False:
		open = True
	elif (s[x:x+3] == 'TAA' or s[x:x+3] == 'TAG' or s[x:x+3] == 'TGA') and open==True:
		open = False
		c6+=1



print("No of ORF while reading from sequence in forward direction from 1st index:", c1)
print("No of ORF while reading from sequence in forward direction from 2nd index:", c2)
print("No of ORF while reading from sequence in forward direction from 3rd index:", c3)
print("No of ORF while reading from reverse complement from 1st index:", c4)
print("No of ORF while reading from reverse complement from 2nd index:", c5)
print("No of ORF while reading from reverse complement from 3rd index:", c6)

print("Total no of ORFs =", c1+c2+c3+c4+c5+c6)




