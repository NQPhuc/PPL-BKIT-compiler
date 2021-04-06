from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    #1852668
    #assignment 2

    #1 program  : (var_declare SEMI)* func_declare* EOF ;
    # This context represent a AST.Program node
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        declareList = []
        for varDecl in ctx.var_declare(): #this parse tree is actually a list inside a list of AST:VarDecl. This gonna get ugly...
            declareList += varDecl.accept(self) #concat VarDecl list with accumulating list
        for decl in ctx.func_declare():
            declareList.append(decl.accept(self)) #appending a single element to the accumulating list
        return Program(declareList)
        #return Program([VarDecl(Id(ctx.ID().getText()),[],None)])
        
 
    #2 This context represent a AST.Literal abtract node
    # all_literal: basic_literal | array_lit;
    def visitAll_literal(self, ctx:BKITParser.All_literalContext):
        return ctx.getChild(0).accept(self)


    #3 This context represent a AST.IntLiteral/ FloatLiteral/ StringLiteral/ BooleanLiteral concrete node
    # basic_literal: INT_LIT | OCT_LIT | HEX_LIT | FLOAT_LIT | BOOL_LIT |STRING_LIT;
    def visitBasic_literal(self, ctx:BKITParser.Basic_literalContext):
        lit = ctx.getChild(0).getText()
        if ctx.INT_LIT(): return IntLiteral(int(lit))
        if ctx.OCT_LIT(): return IntLiteral(int(lit, 0))
        if ctx.HEX_LIT(): return IntLiteral(int(lit, 0))
        if ctx.FLOAT_LIT(): return FloatLiteral(float(lit))
        if ctx.BOOL_LIT(): return BooleanLiteral(lit == 'True') #result inside bracket is a boolean
        return StringLiteral(lit)

    #4 This context represent a AST.ArrayLiteral node
    # array_lit: CBRACKET_L  (all_literal (COMMA all_literal)*)? CBRACKET_R  ;// the ? is for empty array
    def visitArray_lit(self, ctx:BKITParser.Array_litContext):
        re = []
        if ctx.all_literal(): re = list(map(lambda x: x.accept(self), ctx.all_literal()))
        return ArrayLiteral(re)

    #5 This context represent a AST.FuncDecl node
    # func_declare: FUNC COLON ID func_para? func_body;
    def visitFunc_declare(self, ctx:BKITParser.Func_declareContext):
        para = [] #List[VarDecl] with no init value
        if ctx.func_para(): para = ctx.func_para().accept(self)
        return FuncDecl(Id(ctx.ID().getText()), para, ctx.func_body().accept(self))

    #6 This context represent a LIST[AST.VarDecl]
    # func_para: PARA COLON init_variable (COMMA init_variable)*; 
    def visitFunc_para(self, ctx:BKITParser.Func_paraContext):
        return list(map(lambda x: VarDecl(*x.accept(self), None), ctx.init_variable())) #syntax: *tupple is for unpacking


    #7 This context represent a Tuple[List[AST.VarDecl],List[AST.Stmt]]
    # func_body: BODY statement_list ENDBODY DOT;
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return ctx.statement_list().accept(self)

    #8 This context represent a Tuple[List[AST.VarDecl],List[AST.Stmt]]
    # statement_list: (var_declare SEMI)* statement*;
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        varDeclList = []
        for vd in ctx.var_declare():
            varDeclList += vd.accept(self)
        stmtList = list(map(lambda x: x.accept(self), ctx.statement()))
        return (varDeclList, stmtList)


    #9 This context represent a AST.Stmt abtract node
    # statement: (assignment | BREAK | CONT | funcCall | ret_stmt) SEMI
	#	       | (if_stmt | for_stmt | while_stmt | do_stmt); //these stmt don't end with semicolon
    def visitStatement(self, ctx:BKITParser.StatementContext):
        if ctx.BREAK(): return Break()
        if ctx.CONT(): return Continue()
        return ctx.getChild(0).accept(self)


    #10 This context represent a LIST[AST.VarDecl]
    # var_declare: VAR COLON id_init (COMMA id_init)*;
    def visitVar_declare(self, ctx:BKITParser.Var_declareContext):
        return list(map(lambda x: x.accept(self), ctx.id_init()))


    #11 This context represent a AST.VarDecl node
    # id_init: init_variable (ASS all_literal)?;
    def visitId_init(self, ctx:BKITParser.Id_initContext):
        id, dimensions = ctx.init_variable().accept(self)
        lit = ctx.all_literal()
        return VarDecl(id, dimensions, None if not lit else lit.accept(self))


    #12 doesn't represent any AST node (but is made up of an AST:ID and an list[int])
    # init_variable: ID (SBRACKET_L (INT_LIT|HEX_LIT|OCT_LIT) SBRACKET_R)*;
    def visitInit_variable(self, ctx:BKITParser.Init_variableContext):
        dimensions = []
        dimensionsSize = len(ctx.SBRACKET_L()) #count number of '['
        for i in range(0, dimensionsSize):
            dimensions.append(int(ctx.getChild(i * 3 + 2).getText(), 0)) #LIT index is 2,5,8,11,... might need to parse HEX/OCT manually          
        return Id(ctx.ID().getText()), dimensions


    #13 This context represent a AST.Assign node
    # assignment: (ID | index_exp) ASS expression; //variable ASS expression;
    def visitAssignment(self, ctx:BKITParser.AssignmentContext):
        if ctx.ID(): return Assign(Id(ctx.ID().getText()), ctx.expression().accept(self))
        return Assign(ctx.index_exp().accept(self), ctx.expression().accept(self))


    #14 This context represent a AST.If node
    # if_stmt: IF expression THEN statement_list (ELSEIF expression THEN statement_list)* (ELSE statement_list)? ENDIF DOT;
    def visitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        elseTuple = ([],[])
        size = len(ctx.statement_list())
        if ctx.ELSE():  
            elseTuple = ctx.statement_list(size - 1).accept(self)
            size -= 1
        ifList = list(map(lambda x,y: (x.accept(self), y.accept(self)), ctx.expression(), ctx.statement_list()[:size]))
        ifList = [(a, b, c) for a, (b, c) in ifList] #tupple unpacking
        return If(ifList, elseTuple)


    #15 This context represent a AST.For node
    # for_stmt: FOR RBRACKET_L ID ASS expression COMMA expression COMMA expression RBRACKET_R DO statement_list ENDFOR DOT;
    def visitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        return For(Id(ctx.ID().getText()), ctx.expression(0).accept(self), ctx.expression(1).accept(self)
                    , ctx.expression(2).accept(self), ctx.statement_list().accept(self))


    #16 This context represent a AST.While node
    # while_stmt: WHILE expression DO statement_list ENDWHILE DOT;
    def visitWhile_stmt(self, ctx:BKITParser.While_stmtContext):
        return While(ctx.expression().accept(self), ctx.statement_list().accept(self))


    #17 This context represent a AST.Dowhile node
    # do_stmt: DO statement_list WHILE expression ENDDO DOT;
    def visitDo_stmt(self, ctx:BKITParser.Do_stmtContext):
        return Dowhile(ctx.statement_list().accept(self), ctx.expression().accept(self))


    #18 This context represent a AST.CallStmt node
    # funcCall: ID RBRACKET_L (expression(COMMA expression)*)? RBRACKET_R;
    def visitFuncCall(self, ctx:BKITParser.FuncCallContext):
        return CallStmt(Id(ctx.ID().getText()), list(map(lambda x: x.accept(self), ctx.expression())))


    #19 This context represent a AST.Return node
    # ret_stmt: RETURN expression?;
    def visitRet_stmt(self, ctx:BKITParser.Ret_stmtContext):
        temp = ctx.expression() #so that we don't make 2 call
        return Return(None if not temp else temp.accept(self))


    #20 This context represent a AST.BinaryOp node or a AST.Expr abstract node
    # expression: exp2 (EQUAL | NEQUAL | SMALLER | LARGER | SEQUAL | LEQUAL | NEQUALF | SMALLERF | LARGERF | SEQUALF | LEQUALF) exp2
	#	        | exp2;
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        if len(ctx.exp2()) == 2:
            return BinaryOp(ctx.getChild(1).getText(), ctx.exp2(0).accept(self), ctx.exp2(1).accept(self))
        return ctx.exp2(0).accept(self)


    #21 This context represent a AST.Expr abstract node
    # exp2: RBRACKET_L expression RBRACKET_R //not sure 
	#     | funcCall                          #AST.CallExpr
	#     | index_exp                         #AST.ArrayCell
	#     | <assoc=right> (SUB|SUBF) exp2     #AST.UnaryOp
	#     | <assoc=right> (NOT) exp2          #AST.UnaryOp
	#     | exp2(MUL|MULF|DIV|DIVF|MOD)exp2   #AST.BinaryOp
	#     | exp2(ADD|ADDF|SUB|SUBF)exp2       #AST.BinaryOp
	#     | exp2(AND|OR)exp2                  #AST.BinaryOp
	#     | ID                                #AST.Id
	#     | all_literal;                      #AST.Literal abtract node
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        if ctx.RBRACKET_L(): return ctx.expression().accept(self) #(...)
        if ctx.funcCall(): #func()
            callStmt = ctx.funcCall().accept(self) 
            return CallExpr(callStmt.method, callStmt.param)
        if ctx.index_exp(): return ctx.index_exp().accept(self) #var[5]
        if ctx.ID(): return Id(ctx.ID().getText()) #var
        if ctx.all_literal(): return ctx.all_literal().accept(self) #15
        if len(ctx.exp2()) == 1: return UnaryOp(ctx.getChild(0).getText(), ctx.exp2(0).accept(self)) #-a
        
        return BinaryOp(ctx.getChild(1).getText(), ctx.exp2(0).accept(self), ctx.exp2(1).accept(self)) #a+b   
    
    #22 This context represent a AST.ArrayCell node
    # index_exp: (ID | funcCall) (SBRACKET_L expression SBRACKET_R)+ ;
    def visitIndex_exp(self, ctx:BKITParser.Index_expContext):
        exprList = list(map(lambda x: x.accept(self), ctx.expression()))
        if ctx.ID(): return ArrayCell(Id(ctx.ID().getText()), exprList)
        callStmt = ctx.funcCall().accept(self)
        callExp = CallExpr(callStmt.method, callStmt.param)
        return ArrayCell(callExp, exprList)
