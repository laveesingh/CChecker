#include<stdio.h>
int main(){
	float f=5.0;
	volatile register inline int i=f;
	printf("%d",i);

}
