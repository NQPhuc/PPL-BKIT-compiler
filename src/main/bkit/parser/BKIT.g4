//1852668
//assignment 2
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : (var_declare SEMI)* func_declare* EOF ; //start symbol
		
//variable: ID (SBRACKET_L expression SBRACKET_R)*; not used
all_literal: basic_literal | array_lit;
basic_literal: INT_LIT | OCT_LIT | HEX_LIT | FLOAT_LIT | BOOL_LIT |STRING_LIT;	   
array_lit: CBRACKET_L  (all_literal (COMMA all_literal)*)? CBRACKET_R  ;// the ? is for empty array


func_declare: FUNC COLON ID func_para? func_body;

func_para: PARA COLON init_variable (COMMA init_variable)*; 
func_body: BODY COLON statement_list ENDBODY DOT;

statement_list: (var_declare SEMI)* statement*;
statement: (assignment | BREAK | CONT | funcCall | ret_stmt) SEMI
		 | (if_stmt | for_stmt | while_stmt | do_stmt); //these stmt don't end with semicolon


var_declare: VAR COLON id_init (COMMA id_init)*;
id_init: init_variable (ASS all_literal)?;
init_variable: ID (SBRACKET_L (INT_LIT|HEX_LIT|OCT_LIT) SBRACKET_R)*; //new

assignment: (ID | index_exp) ASS expression; //variable ASS expression;

if_stmt: IF expression THEN statement_list (ELSEIF expression THEN statement_list)* (ELSE statement_list)? ENDIF DOT;

for_stmt: FOR RBRACKET_L ID ASS expression COMMA expression COMMA expression RBRACKET_R DO statement_list ENDFOR DOT;

while_stmt: WHILE expression DO statement_list ENDWHILE DOT;

do_stmt: DO statement_list WHILE expression ENDDO DOT;

funcCall: ID RBRACKET_L (expression(COMMA expression)*)? RBRACKET_R;

ret_stmt: RETURN expression?;

/*Best version, work exactly like how the specs said*/
expression: exp2 (EQUAL | NEQUAL | SMALLER | LARGER | SEQUAL | LEQUAL | NEQUALF | SMALLERF | LARGERF | SEQUALF | LEQUALF) exp2
		  | exp2;
exp2: RBRACKET_L expression RBRACKET_R
	| funcCall
	| index_exp
	| <assoc=right> (SUB|SUBF) exp2 //might be naturally right-assoc, just to be sure since this is antlr parser, not a pure BNF parser
	| <assoc=right> (NOT) exp2 //might be naturally right-assoc, just to be sure since this is antlr parser, not a pure BNF parser
	| exp2(MUL|MULF|DIV|DIVF|MOD)exp2
	| exp2(ADD|ADDF|SUB|SUBF)exp2
	| exp2(AND|OR)exp2
	| ID
	| all_literal;

//Indexing OP, naturally left-assoc
index_exp: (ID | funcCall) (SBRACKET_L expression SBRACKET_R)+ ;		  
 

//3.3.1 Identifiers
ID: [a-z][a-zA-Z0-9_]* ;

//3.3.2 Keywords
BODY: 'Body' ; 
BREAK: 'Break' ;
CONT: 'Continue' ;
DO: 'Do' ;
ELSE: 'Else' ; 
ELSEIF: 'ElseIf' ;
ENDBODY: 'EndBody' ; 
ENDIF: 'EndIf' ;
ENDFOR: 'EndFor' ;
ENDWHILE: 'EndWhile' ;
FOR: 'For' ;
FUNC: 'Function' ;
IF: 'If' ;
PARA: 'Parameter' ;
RETURN: 'Return' ;
THEN: 'Then' ;
VAR: 'Var' ;
WHILE: 'While' ;
fragment TRUE: 'True' ;
fragment FALSE: 'False' ;
ENDDO: 'EndDo' ;

//3.3.3 Operators
ADD: '+' ;
ADDF: '+.' ;
SUB: '-' ;
SUBF: '-.' ;
MUL: '*' ;
MULF: '*.' ;
DIV: '\\' ;
DIVF: '\\.' ;
MOD: '%' ;
ASS: '='; //not mentioned in 3.3.3 but mentioned in 7.2

NOT: '!' ;
AND: '&&' ;
OR: '||' ;

EQUAL: '==' ;
NEQUAL: '!=' ;
SMALLER: '<' ;
LARGER: '>' ;
SEQUAL: '<=' ;
LEQUAL: '>=' ;

NEQUALF: '=/=' ;
SMALLERF: '<.' ;
LARGERF: '>.' ;
SEQUALF: '<=.' ;
LEQUALF: '>=.' ;

//3.3.4 Seperators
RBRACKET_L: '(' ;
RBRACKET_R: ')' ;
SBRACKET_L: '[' ;
SBRACKET_R: ']' ;
CBRACKET_L: '{' ;
CBRACKET_R: '}' ;
SEMI: ';' ;
DOT: '.' ;
COMMA: ',' ;
COLON: ':' ;

//3.3.5 Literals

/*
edge case: 0123 -> 0,123
*/
INT_LIT: ( '0' | [1-9][0-9]* ); 
HEX_LIT: '0'[xX][1-9A-F][0-9A-F]* ;
OCT_LIT: '0'[oO][1-7][0-7]* ;

fragment DecimalPart: ('.'[0-9]*) ;
fragment Digits: [0-9]+ ;
fragment SciNotation: [eE] [+-]? Digits ;
FLOAT_LIT: Digits (DecimalPart SciNotation? | SciNotation) ; 
BOOL_LIT:	(TRUE|FALSE) ;

fragment LegalEscape: [bfrnt'\\] ;
fragment StringElement:  '\'"' | [\\] LegalEscape | ~['\\\n\r"] ;
STRING_LIT:  //greedy match
	'"' StringElement* '"' //look filmsy, might need EOF in ~()
	{self.text = self.text[1:-1]}; //This action seem unavoidable in order to remove quote
	
//Whitespace
WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//3.2  Block Comments
CMT: '**' .*? '**' -> skip ; //skip comment - lazy match

//Errors Tokens
UNCLOSE_STRING: //because newlines before closing quote led to error, we don't need to keep checking
	'"' StringElement* ('\r'|'\n'|EOF) //greedy match
	{self.text = self.text[1:]};
	
ILLEGAL_ESCAPE: // match until encounter wrong escape sequence, greedy match
	'"'  StringElement* ( [\\]~[bfrnt'\\] | [']~["]) //look filmsy, might need EOF in ~()
	{self.text = self.text[1:]};
	
UNTERMINATED_COMMENT: '**' ( (~'*') | '*'(~'*') )*  ;  //match from ** then (not* or *not*)repeat 


ERROR_CHAR: .; //this work better than the below, basicallly, when all other token fail, this will match
/*every character not in the specification is detected,
only strings, string errors, comments, comment errors can overide this token*/
//ERROR_CHAR: ( ~([ a-zA-Z0-9_!%&*()\-=+/{}\\|;:'",<.>] | '[' | ']' ) );
