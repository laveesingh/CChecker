 #include <bits/stdc++.h>
using namespace std;
struct node
{
	int index;
	int prev=0;
	float area;
}B[100001];
int cmp(node A,node B)
{
	return A.area<B.area;
}
int cmp1(node A,node B)
{
	return A.index<B.index;
}

int main() {
	long long int T,N,V,A[100001][2],suml,sumr;
	cin>>T;
	while(T--)
	{
		cin>>N;
		for(int i=0;i<N;i++)
		{
			suml=0;
			sumr=0;
			cin>>V;
			for(int j=0;j<V;j++)
			{
				cin>>A[j][0]>>A[j][1];
			}
			A[V][0]=A[0][0];
			A[V][1]=A[0][1];
			for(int j=0;j<V;j++)
			{
				sumr+=(A[j][0]*A[j+1][1]);
				suml+=(A[j][1]*A[j+1][0]);
			}
			B[i].area=abs((sumr-suml)/2);
			B[i].index=i;
		}
		sort(B,B+N,cmp);
		for(int i=0;i<N;i++)
		{
			B[i].prev=i;
		}
		sort(B,B+N,cmp1);
		for(int i=0;i<N;i++)
		{
			cout<<B[i].prev<<" ";
		}
		cout<<endl;
	}
	// your code goes here
	return 0;
}

