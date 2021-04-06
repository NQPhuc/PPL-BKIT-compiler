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

program  : FUNCTION COLON ID BODY COLON exp SEMI ENDBODY DOT EOF ;

exp: ID '(' exp ')' | INTLIT ;

ID: [a-z][A-Za-z0-9_]* ;

SEMI: ';' ;

COLON: ':' ;

DOT: '.';

FUNCTION: 'Function' ;

BODY: 'Body';

ENDBODY: 'EndBody';

INTLIT: [0-9]+; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;