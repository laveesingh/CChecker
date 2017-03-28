#include<bits/stdc++.h>
#define PI 3.1415926535897932384626433832795028841971693993751058209749Lf
#define INF 2000000000
#define INFI 1e37
#define pb push_back
#define PRINT(x)           cout << #x << "  " << x << endl
#define MAX ((int)1e6+10)
#define MOD 1000000007
#define BUF 4096
char ibuf[BUF];
int ipt = BUF;

int readInt() {
	while (ipt < BUF && ibuf[ipt] < '0') ipt++;
	if (ipt == BUF) {
		fread(ibuf, 1, BUF, stdin);
		ipt = 0;
		while (ipt < BUF && ibuf[ipt] < '0') ipt++;
	}
	int n = 0;
	while (ipt < BUF && ibuf[ipt] >= '0') n = (n*10)+(ibuf[ipt++]-'0');
	if (ipt == BUF) {
		fread(ibuf, 1, BUF, stdin);
		ipt = 0;
		while (ipt < BUF && ibuf[ipt] >= '0') n = (n*10)+(ibuf[ipt++]-'0');
	}
	return n;
}



using namespace std;


int main()
{
    int T;
    int A[100001]={0};
    T=readInt();
    while(T--)
    {
    
    long long int N,sum=0;
    N=readInt();
    for(int i=0;i<N;i++)
    {
        A[i]=readInt();
    }
    sum=A[0];
    for(int i=0;i<N-1;i++)
    {
    if(A[i]<A[i+1])
    sum+=(A[i+1]-A[i]);
    }
    printf("%lld\n",sum);
    }
return 0;
}

