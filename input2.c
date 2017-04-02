// 2017 Team NULL1 

#include<stdio.h>
#include<stdint.h>
#include<ctype.h>
#include<iomanip.h>

int first(int i)
{
  	return first(i-1);
}

union pair
{
  	int first; 
	int second;
};

int main()
{
	float f = 5.0;
	volatile register inline int i = f;	
		
	signed int i = 45;
	
	int n = 10;
  	switch(n){        
	    case 1:
	      	printf("1\n");
	      	break;
	    case 10:
	      	printf("10\n");
	      	break;
 	 }
 	 :LOOP
 	 for(int i =0;i<10;++i){
 	 	if( i == 5 )
 	 		goto LOOP;
 	 	else
 	 		continue;
 	 }

  	 int *i = malloc(sizeof(int));

  	 switch(n == 0){        
	    case 1:
	      	printf("1\n");
	      	break;
	    case 10:
	      	printf("10\n");
	      	break;
	    default:
 	 }

}
