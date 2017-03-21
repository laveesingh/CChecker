%option noyywrap
%{
  #include "grammar.tab.h"
%}

name \w([0-9]\w)+
whitespace [ \r\t\v\f]
linefeed  \n
%%

{name}        { return name; }
":"           { return COLON; }
"->"          { return  RIGHT_ARROW; }
"{"           { return  LEFT_BRACE; }
"}"           { return RIGHT_BRACE; }

{whitespace}
{linefeed}    ++yylineno;

%%

