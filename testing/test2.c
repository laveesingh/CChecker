#include <stdio.h>
#include <stdlib.h>

#define ll long long

const int N = 1e5+1;

struct node{
  int val;
  struct node* child;
};

typedef struct node Node;

int first_function(int a, int b){
  printf("This function is supposed to take two integers as parameters, and add them up and return the sum\n");
  int sum = a + b;
  return sum;
}

int second_function(int a, int b){
  printf("This function is supposed to take two integers as parameters, and add them up and return the sum\n");
  int sum = a + b;
  return sum;
}

Node* third_function(int a){
  Node *root;
  root = (Node *)malloc(sizeof(Node));
  root->val = a;
  root->child = NULL;
  return root;
}

int main(){
  int a, b;
  a = 3, b = 8;
  printf("the summation is %d\n",first_function(a,b));
}
