#include "table.h"
#include <deque>
#include <iostream>
#include <string>

#define DEBUG 1

extern int yylex();
extern int yylineno;
extern char *yytext;

std::string getTokenName(int token) {
  switch (token) {
  case UNEXPECTED:
    return "UNEXPECTED";
  case KEYWORD:
    return "KEYWORD";
  case SOURCE:
    return "SOURCE";
  case PARAMETER:
    return "PARAMETER";
  case VARIABLE:
    return "VARIABLE";
  case STRING:
    return "STRING";
  case NUMBER:
    return "NUMBER";
  case COMMENT:
    return "COMMENT";
  case OPERATOR:
    return "OPERATOR";
  case FUNCTION:
    return "FUNCTION";
  case EOQ:
    return "EOQ";
  case FIELD:
    return "FIELD";
  case SEPERATOR:
    return "SEPERATOR";
  case SELECT:
    return "SELECT";
  case FROM:
    return "FROM";
  case WHERE:
    return "WHERE";
  case AND:
    return "AND";
  case OR:
    return "OR";
  case PARENTHESIS_OPEN:
    return "PARENTHESIS";
  case PARENTHESIS_CLOSE:
    return "PARENTHESIS";
  case BRACKET_OPEN:
    return "BRACKET";
  case BRACKET_CLOSE:
    return "BRACKET";
  case CURLY_BRACKET_OPEN:
    return "CURLY_BRACKET";
  case CURLY_BRACKET_CLOSE:
    return "CURLY_BRACKET";
  case LIMIT:
    return "LIMIT";
  case START:
    return "START";
  default:
    return "UNEXPECTED";
  }
}

struct Token {
  int type;
  std::string value;
  int position;
};

struct Counter {
  int paren;
  int bracket;
  int curly;
};

void print_token(Token token) {
  std::clog << ">>> [" << token.position << "]"
            << ":" << getTokenName(token.type) << "::" << '"' << token.value
            << '"' << std::endl;
}
void print_paren_open(Token token, int counter) {
  if (token.type == AND && counter == 0) {
    std::cout << "\n";
  }
  if (token.type == AND && counter != 0) {
    std::cout << " ";
  }
}
void print_paren_close(Token token, int counter) {
  if (token.type == AND && counter == 0) {
    std::cout << "\t\t";
  }
  if (token.type == AND && counter != 0) {
    std::cout << " ";
  }
}
void print_paren(Token token, int counter, bool open) {
  if (open == true) {
    print_paren_open(token, counter);
  }
  if (open == false) {
    print_paren_close(token, counter);
  }
}
void print_before(Token token, Counter counter) {
  if (token.type == COMMENT || token.type == SELECT) {
    std::cout << "\n";
  }
  print_paren(token, counter.paren, true);
  if (token.type == FROM || token.type == WHERE || token.type == LIMIT ||
      token.type == START || token.type == EOQ) {
    std::cout << "\n";
  }
  if (token.type == OPERATOR) {
    std::cout << " ";
  }
}
void print_after(Token token, Counter counter) {
  if (token.type == OPERATOR || token.type == FROM || token.type == LIMIT ||
      token.type == START) {
    std::cout << " ";
  }
  if (token.type == SELECT || token.type == SEPERATOR) {
    std::cout << "\n\t";
  }
  if (token.type == WHERE) {
    std::cout << "\t";
  }
  print_paren(token, counter.paren, false);
  if (token.type == EOQ) {
    std::cout << "\n";
  }
}
void calc_paren(Token token, int &counter) {
  if (token.type == PARENTHESIS_OPEN) {
    counter = counter + 1;
  }
  if (token.type == PARENTHESIS_CLOSE) {
    counter = counter - 1;
  }
}

int main() {
  std::deque<Token> tokens;

  int ntoken = yylex();
  int count = 0;
  while (ntoken) {
    Token token = {ntoken, yytext, count};
    tokens.push_back(token);
    if (DEBUG == 1) {
      print_token(token);
    }
    ntoken = yylex();
    count = count + 1;
  }

  int paren_counter = 0;
  Counter counter = {0, 0, 0};
  for (auto it = tokens.begin(); it != tokens.end(); ++it) {
    Token token = *it;
    calc_paren(token, counter.paren);
    print_before(token, counter);
    std::cout << token.value;
    print_after(token, counter);
  }
}
