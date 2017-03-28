#include <stdio.h>

/*
 * This is very simple example of switch statement in c
 */

int main(){
  int n = 10;
  switch(n){
    case 1:
      printf("1\n");
      break;
    case 10:
      printf("10\n");
      break;
    default:
      printf("Nothing\n");
  }
  return 0;
}
