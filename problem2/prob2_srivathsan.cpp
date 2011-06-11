#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int f1=1,f2=2,f3,count=2;
	while(1)
	{
		f3=f1+f2;
		f1=f2;
		f2=f3;
		if(f3%2==0)
			count+=f3;
		if(f3>4000000)
			break;
	}
	cout<<count<<endl;
	return 0;
}
