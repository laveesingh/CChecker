#include <stdio.h>

int first(int i){
  if(i<=0)
    return 0;
  return first(i-1) + i;
}

int main(void){
  int a = 10;
  printf("%d\n",first(10));
}
