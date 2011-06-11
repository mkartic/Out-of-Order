#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
#define MAX 999999999999
int hh=sqrt(MAX)+10000;
vector<int> v(hh,1);
vector<int> primes;
void sieve()
{
	v[0]=v[1]=0;
	for(int i=2;i<=sqrt(hh);i++)
		if(v[i]==1)
			for(int j=i*i;j<hh;j+=i)
				v[j]=0;
	for(int i=0;i<hh;i++)
		if(v[i]==1)
			primes.push_back(i);
}
int main()
{
	//int *a=new int[999999999999];
	sieve();
	int max=0;
//	int n=13195;
	long long n=600851475143;
	
	for(int i=0;i<primes.size() && n>=primes[i];i++)
	{
		int prime=primes[i];

		if(n%prime==0)
			if(prime>max)
				max=prime;
	}
	cout<<max<<endl;
}


