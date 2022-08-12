'''
	We know that we can get the exons i.e. the coding regions of a gene by solving finding the ORF in 6 different ways. Let n1,n2,...,n6 be the no of exons we could find in 6 different ways. Suppose k exons combine to form a protien. So the no of possible protiens from 'ni' possible exons in a way of reading a sequence are k!*C(ni, k), where C(x, y) is ways 'x choose y'. Extending this to for our given problem, no of different proteins would be when k exons are required:
		k!*(C(n1, k) + C(n2, k) + C(n3, k) + C(n4, k) + C(n5, k) + C(n6, k))

	Now given below is the program for different values of k in different parts
'''
import math

#the below values were found for the code of part (iii)
n1=215
n2=204
n3=190
n4=200
n5=198
n6=213

def permute(n, k):
	ans=1
	while k>0:
		ans*=n
		n-=1
		k-=1

	return ans

def find(k):
	x1 = permute(n1, k)
	x2 = permute(n2, k)
	x3 = permute(n3, k)
	x4 = permute(n4, k)
	x5 = permute(n5, k)
	x6 = permute(n6, k)
	return x1+x2+x3+x4+x6




print("a) When 5 exons combine to form protein:",find(5), "possible structures")
print("b) When 3 exons combine to form protein:",find(3), "possible structures")
print("c) When 10 exons combine to form protein:",find(10), "possible structures")
print("d) When 6 exons combine to form protein:",find(6), "possible structures")