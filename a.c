#include<stdio.h>
//This is a single line comment
void main(){
    float a=10.0, b=12.0;
    if(a!=b)
        printf("Not equal!");
    helper(a);
}

void helper(float num){
    //This is also a single line comment
    printf("%d", num);
    main();
}
