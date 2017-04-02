#include <stdio.h>
int main()
{
  double  d;
  long    l;
  int     i=0;
  i=0.0;
  int j=0;
  j=i;
  i=j;
  for(i=0;i<10;i++)
  {
    printf("%d\n",i);
  }
  if (d > i)      d = i;
  if (i > l)      l = i;
  if (d == l)     d *= 2;
  int * pYour = max(2,5);
  void * pv = pYour;
  return 0;
}
