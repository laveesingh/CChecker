#include<stdio.h>

int *pnt;

int main() {
  // implicit type conversion
  int a=10, b = 3, c, d;
  float e=10, f = 3, g, h;
  a = b;
  a = e;
  f = a;
  g = d;
  c = h;
  pnt = new int[10];
  memset(pnt, 0, sizeof(int)*10);
	return 0;
}
