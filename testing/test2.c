#include <stdio.h>

#define ll long long

const int N = 1e5+1;

int array[N];


struct node{
  int val;
  node* child;
};

typedef struct node Node;

int first_function(int a, int b){
  printf("This function is supposed to take two integers as parameters, and add them up and return the sum\n");
  int sum = a + b;
  return sum;
}

int first_function(int a, int b){
  printf("This function is supposed to take two integers as parameters, and add them up and return the sum\n");
  int sum = a + b;
  return sum;
}

int main(){
  int a, b;
  a = 3, b = 8;
  printf("the summation is %d\n",first_function(a,b));
}
