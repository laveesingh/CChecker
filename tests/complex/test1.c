#include<stdio.h>
#include<stdlib.h>
int cmp(const int *a,const int *b);
int main()
{
    int n,count=1;
    scanf("%d",&n);
    int a[n],b[n];
    for(int i=0;i<n;i++)scanf("%d",&a[i]);
    qsort(a,n,sizeof(int),cmp);
    //for(int i=0;i<n;i++)printf("%d ",a[i]);
    for(int i=0;i<n-1;i++){
        b[i]=a[i+1]-a[i];
    }
    qsort(b,n-1,sizeof(int),cmp);
    for(int i=1;i<n;i++){
        if(b[0]==b[i])count++;
    }
    printf("%d %d",b[0],count);
    return 0;
}
int cmp(const int *a,const int *b)
{
    return(*a-*b);
}
