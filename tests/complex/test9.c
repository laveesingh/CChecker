 #include <bits/stdc++.h>
using namespace std;
int diff(pair<int,int> a,pair<int,int> b)
{
	return abs(a.first-b.first)+abs(a.second-b.second);
}

int main() {
	map < int, pair<int,int> > A;
	int T,N=0,x;
	cin>>T;
	while(T--)
	{
	cin>>N;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			cin>>x;
			A[x]=make_pair(i+1,j+1);
		}
	}
	int cnt=0;
	for(int i=1;i<N*N;i++)
	{
	//	cout<<i<<endl;
		cnt+=diff(A[i+1],A[i]);
	}
	cout<<cnt<<endl;
	A.clear();
	}
	// your code goes here
	return 0;
}

