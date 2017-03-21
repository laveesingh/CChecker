%{
  #include <math.h>
  #include <stdio.h>
  #include <stdlib.h>
  int yylex(void);
  void yyerror(char const *);
%}

%define api.value.type (double)

%token NAME
%start input


%%

input:

%%

void yyerror(char const *x){
  printf("Error %s\n", x);
}
