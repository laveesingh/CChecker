#include<stdio.h>
int main()
{
	int a;
	int *c;
	int b=0;
	if(a==b)
	{
		printf("There is no assignment in this if");
		b=0;
	}
	if(a==b)
	{
	b=a==b;
	}

	if(a==b){
	printf("Another format");
	}

	for(a=0;a<10;a++)
	{
		printf("Hello this is also fine");
	}
	for (;(a==35);i++)
	{
		printf("There is a bug :P");
	}
	do{
		printf("This does nothing _/\\_");
	}while(a==4);
	if(a==1||a==250)
	{
		printf("This is also wrong.");
	}
	else printf("Hello");
	for(int i = 0; i < 10; i ++){
		if(i==5)
				printf("i=%d\n",i);
	}


	return 0;
}
