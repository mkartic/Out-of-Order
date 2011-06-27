import math
def fact(n):
	prod=1
	while(n>1):
		prod*=n
		n-=1
	return prod
facty=[math.factorial(x) for x in range(0,10)]
def digfacsum(n):
	sum=0
	while n:
		#sum+=math.factorial((n%10))
		sum+=facty[(n%10)]
		n/=10
	return sum

def factchain(n):
	vals=set([n])
	val=n
	while 1:
		val=digfacsum(val)
		if val in vals:
			break
		vals.add(val)
	#print vals
	return len(vals)

def altclen(n):
	#preprocessing upto 1000
	fin=dict.fromkeys(range(1,1000000),0)
	for i in range(1,1000):
		sol=factchain(i)
		fin[i]=sol
	for i in range(1000,n):
		num=i
		cl=0
		vals=set()
		while (num not in fin or fin[num]==0) and num not in vals:
			vals.add(num)
			cl+=1
			num=digfacsum(num)
		if num in fin and fin[num]!=0:
			cl+=fin[num]
		fin[i]=cl
	count=0
	for k,v in fin.iteritems():
		if v==60:
			count+=1
	return count
			
def solution(n):
	cl=0
	for i in range(1,n):
		sol=factchain(i)
		#print sol
		if sol==60:
			cl+=1
	return cl
	
if __name__=="__main__":
	print altclen(1000)