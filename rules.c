%{
#include "table.h"
%}

%%
--.*|\/\/.*|\/\*.*\/|\#.*	return COMMENT;
\".*\"|\'.*\'			return STRING;
" "			;
"("			return PARENTHESIS_OPEN;
")"			return PARENTHESIS_CLOSE;
"["			return BRACKET_OPEN;
"]"			return BRACKET_CLOSE;
"{"			return CURLY_BRACKET_OPEN;
"}"			return CURLY_BRACKET_CLOSE;
"SELECT"		return SELECT;
"*"			return FIELD;
","			return SEPERATOR;
"FROM"			return FROM;
"WHERE"			return WHERE;
"AND"			return AND;
"OR"			return OR;
"="			return OPERATOR;
"LIMIT"			return LIMIT;
"START"			return START;
[0-9]*[_a-zA-Z]+[0-9]*[_a-zA-Z]+((\.?[0-9]*)[_a-zA-Z]*)+	return VARIABLE;
[0-9]+			return NUMBER;
[a-zA-Z]+		return VARIABLE;
[\n\t]			;
";"			return EOQ;
.			return UNEXPECTED;
%%
 
int yywrap(void){
	return 1;
}
