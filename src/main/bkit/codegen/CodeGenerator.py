'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

from AST import * #NEWLY ADDED
from functools import reduce #NEWLY ADDED

class MethodEnv():
    def __init__(self, frame, sym, isLeft = False):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        
class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
    def __str__(self): 
        return "Symbol(" + self.name + ", " + str(self.mtype) + ", " + str(self.value) + ")"
    def __repr__(self): return self.__str__()    
        
class CName:
    def __init__(self,n):
        self.value = n
    def __str__(self): return "class=" + self.value
    def __repr__(self): return self.__str__()
    
class Index:
    def __init__(self,n):
        self.value = n
    def __str__(self): return "index=" + str(self.value)
    def __repr__(self): return self.__str__()      
        
class Type(ABC): pass

class IntType(Type):
    def __str__(self): return "Int"
    def __repr__(self): return "Int"
    
class FloatType(Type):
    def __str__(self): return "Float"
    def __repr__(self): return "Float"
    
class VoidType(Type):
    def __str__(self): return "Void"
    def __repr__(self): return "Void"
    
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
        
class StringType(Type):
    def __str__(self): return "String"
    def __repr__(self): return "String"  
    
class BoolType(Type):
    def __str__(self): return "Bool"
    def __repr__(self): return "Bool"
    
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type
    def __str__(self): return "MType(" + str(self.partype) + ", " + str(self.rettype) + ")"
    def __repr__(self): return self.__str__()
        
class ArrayType(Type):
    def __init__(self,et, s = None): #modified
        self.eleType = et #Type
        self.dimen = s   #List[int]  
    def __str__(self): return "Array(" + str(self.eleType) + ", " + str(self.dimen) + ")"
    def __repr__(self): return self.__str__()

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
        #Symbol("read", MType([], StringType()), CName(self.libName)),
                   # Symbol("printLn", MType([], VoidType()), CName(self.libName)),
                  #  Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
                  #  Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
		 #   Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName))
Symbol("int_of_float",MType([FloatType()],IntType()), CName(self.libName)), 
Symbol("float_to_int",MType([IntType()],FloatType()), CName(self.libName)), #change from float_of_int to float_to_int
Symbol("int_of_string",MType([StringType()],IntType()), CName(self.libName)),
Symbol("string_of_int",MType([IntType()],StringType()), CName(self.libName)),
Symbol("float_of_string",MType([StringType()],FloatType()), CName(self.libName)),
Symbol("string_of_float",MType([FloatType()],StringType()), CName(self.libName)),
Symbol("bool_of_string",MType([StringType()],BoolType()), CName(self.libName)),
Symbol("string_of_bool",MType([BoolType()],StringType()), CName(self.libName)),
Symbol("read",MType([],StringType()), CName(self.libName)),
Symbol("printLn",MType([],VoidType()), CName(self.libName)), 
Symbol("print",MType([StringType()],VoidType()), CName(self.libName)), #change from printStr to print
Symbol("printStrLn",MType([StringType()],VoidType()), CName(self.libName))
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)


class CodeGenVisitor(BaseVisitor): #inherite Visitor.py in scr/main/bkit/utils
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        
        self.typeInferer = StaticChecker(astTree, env)
        self.env = self.typeInferer.check()

    # decl : List[Decl]
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))      
                     
        self.clinitFrame = Frame("<clinit>", VoidType())
        self.clinitFrame.enterScope(True)
                
        #We already used the old type checker to build global evnviroment, so only code generation is required in program
        clinitCode = list(map(lambda x: x.accept(self, MethodEnv(None, self.env))[0], ast.decl))
        clinitCode = ''.join(clinitCode)           
        
        #generate REAL class entry main function
        self.genMain(MethodEnv(None, self.env))
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.genClInit(clinitCode, self.clinitFrame)
        self.clinitFrame.exitScope() #redundant, I added this to make this file have the same number of enter and exit, so that I can debug easier
        
        self.emit.emitEPILOG() #SUPER IMPORTANT
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope() #redundant, I added this to make this file have the same number of enter and exit, so that I can debug easier
        
    def genClInit(self, clinitCode, frame):
        methodname, methodtype = frame.name, MType([],frame.returnType)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(clinitCode)
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        #return frame

    # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,o):
    #our 'main' function in BKIT is actually renamed to 'Main' in java bytecode
    #this function will call our 'Main' in bytecode
        methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()

        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        
        mainSym = next(filter(lambda s: 'main' == s.name, o.sym)) #get main function symbol        
        #generate dummy value on stack for main's parameter
        for p in mainSym.mtype.partype:
            if type(p) is IntType or type(p) is BoolType:
                self.emit.printout(self.emit.emitPUSHICONST(0, frame))
            elif type(p) is FloatType:
                self.emit.printout(self.emit.emitPUSHFCONST("0", frame))
            elif type(p) is StringType:
                self.emit.printout(self.emit.emitPUSHCONST("", frame))
            elif type(p) is ArrayType:
                self.emit.printout(self.emit.emitPUSHICONST(1, frame)) #put dummy dimension
                self.emit.printout(self.emit.emitPUSHARRAY_SHALLOW(p, frame))
            else: print("Something wrong in genMain")
        
        realMainCall = self.emit.emitINVOKESTATIC(mainSym.value.value + "/" + "Main", mainSym.mtype, frame)
        self.emit.printout(realMainCall)
        if not type(mainSym.mtype.rettype ) is VoidType:
            self.emit.printout(self.emit.emitPOP(frame))
            
        ''' example code
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        '''
        
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope() #redundant, I added this to make this file have the same number of enter and exit, so that I can debug easier

    #1852668 - assignment 4   
    
    # name : str
    def visitId(self, ctx, o): #DONE
    #print nothing
    #return code, type
        symbol = next(filter(lambda s: ctx.name == s.name, o.sym))
        
        if o.isLeft:
            if isinstance(symbol.value, Index):
                return self.emit.emitWRITEVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame), symbol.mtype
            else:
                return self.emit.emitPUTSTATIC(symbol.value.value + "." + symbol.name, symbol.mtype, o.frame), symbol.mtype        
        else: #on right hand side
            if isinstance(symbol.value, Index):
                return self.emit.emitREADVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame), symbol.mtype
            elif type(symbol.mtype) is MType:
                realName = symbol.name
                if realName == 'main': realName = 'Main' #this is the java bytecode real main function name
                return self.emit.emitINVOKESTATIC(symbol.value.value + "/" + realName, symbol.mtype, o.frame), symbol.mtype
            else:
                return self.emit.emitGETSTATIC(symbol.value.value + "." + symbol.name, symbol.mtype, o.frame), symbol.mtype
    
    #arr:Expr
    #idx:List[Expr]
    def visitArrayCell(self, ctx, o): #DONE
    #print nothing
    #return code, type
        temp = o.isLeft
        o.isLeft = False
        jCode, exprType = ctx.arr.accept(self, o) #put address of array onto stack -> stack + 1
              
        returnType = ArrayType(exprType.eleType, exprType.dimen) #copying to revent mutate id symbol type
        
        eCode, eType = ctx.idx[0].accept(self, o)
        jCode += eCode #put index on stack -> stack+1       
        
        returnType.dimen = returnType.dimen[1:] #pop 1 dimension from the top after each indexing
        if len(returnType.dimen) < 1: returnType = returnType.eleType #no dimension array
        
        for i in range(1, len(ctx.idx)): #for every additional dimension, we need to load the child address first
            jCode += self.emit.emitALOAD(returnType, o.frame) #load ref of child array -> stack-1
            eCode, eType = ctx.idx[i].accept(self, o) #We need to be careful where to call accept (because it changes the frame's stack)
            jCode += eCode #put index on stack -> stack+1
                
            returnType.dimen = returnType.dimen[1:] #pop 1 dimension from the top after each indexing
            if len(returnType.dimen) < 1: returnType = returnType.eleType#no dimension array
        
        o.isLeft = temp
        if not o.isLeft:           
            jCode += self.emit.emitALOAD(returnType, o.frame) #Put value at arraycell on to stack -> stack - 1
        
        return jCode, returnType                
    
    # variable : Id
    # varDimen : List[int] # empty list for scalar variable
    # varInit  : Literal   # null if no initial
    def visitVarDecl(self, ctx, o, paramType=None): #DONE
    #print declareCode
    #return initilizeCode, Symbol
        if o.frame: #local declaration + initilization
            newIndex = o.frame.getNewIndex()    
            
            if ctx.varInit is None: #this mean that this is a param => paramType != None
                self.emit.printout(self.emit.emitVAR(newIndex, ctx.variable.name, paramType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
                return "", Symbol(ctx.variable.name, paramType, Index(newIndex))
                
            else:
                initValueCode, initType = ctx.varInit.accept(self, o)
                self.emit.printout(self.emit.emitVAR(newIndex, ctx.variable.name, initType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame))
                jCode = initValueCode + self.emit.emitWRITEVAR(ctx.variable.name, initType, newIndex, o.frame)
                return jCode, Symbol(ctx.variable.name, initType, Index(newIndex))
                
        else: #global declaration + initilization
            globalEnv = MethodEnv(self.clinitFrame, o.sym) #hope we can modify clinitFrame
            initValueCode, initType = ctx.varInit.accept(self, globalEnv)
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.variable.name, initType, False))
            jCode = initValueCode + self.emit.emitPUTSTATIC(self.className + "." + ctx.variable.name, initType, globalEnv.frame)           
            return jCode, Symbol(ctx.variable.name, initType, CName(self.className))
    
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ctx, o): #DONE?
    #print functionCode
    #return initilizeCode, Symbol - actually this return only to keep it the same as VarDecl. The return value is not used
        fSym = next(filter(lambda s: ctx.name.name == s.name, o.sym))
        
        fFrame = Frame(ctx.name.name, fSym.mtype.rettype)
        
        realName = ctx.name.name
        if realName == 'main': realName = 'Main' #this is the java bytecode real main function name
        self.emit.printout(self.emit.emitMETHOD(realName, fSym.mtype, True, fFrame)) #print method declare directive
        
        message = MethodEnv(fFrame, o.sym.copy()) #need to copy o.sym to preserve the global list
        message.frame.enterScope(True) #generate start & end label for this function's scope
        
        #we are assuming there's no Redeclared Variable error here. Else this won't work
        #paraSymbolList = list(map(lambda x, y: x.accept(self, message, y)[1], ctx.param, fSym.mtype.partype)) #call accept to print var declare directive and receive a list of para symbol       
        paraSymbolList = list(map(lambda x, y: self.visitVarDecl(x, message, y)[1], ctx.param, fSym.mtype.partype))
        message.sym[:0] = paraSymbolList #append list of para symbol into the beginning of message.sym list
    
        #we are assuming there's no Redeclared Variable error here. Else this won't work
        varInitCode, varSymbolList = [], []
        if len(ctx.body[0]) > 0:
            varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ctx.body[0]))) #call accept to print var declare directive and receive a list of local method's variable symbol
        message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
        #print(message.sym)
        
        #mark the start of method label
        self.emit.printout(self.emit.emitLABEL(message.frame.getStartLabel(), message.frame)) #the second parameter message.frame is redundant (emitter didn't use them)
        self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter        
        [st.accept(self, message) for st in ctx.body[1]] #print function body statements code
        
        
        self.emit.printout(self.emit.emitLABEL(message.frame.getEndLabel(), message.frame)) #mark the end of method label 

        #If a method doesn't return at the end of their bytecode, 
        #jvm will raise java.lang.VerifyError: ( Falling off the end of the code) error
        #So we add this return instruction at the end of any function to ensure that it won't happens.
        #putting dummy return value on stack
        if type(fSym.mtype.rettype) is IntType or type(fSym.mtype.rettype) is BoolType:
            self.emit.printout(self.emit.emitPUSHICONST(0, message.frame))
        elif type(fSym.mtype.rettype) is FloatType:
            self.emit.printout(self.emit.emitPUSHFCONST("0", message.frame))
        elif type(fSym.mtype.rettype) is StringType:
            self.emit.printout(self.emit.emitPUSHCONST("", message.frame))
        elif type(fSym.mtype.rettype) is ArrayType:
            self.emit.printout(self.emit.emitPUSHICONST(1, message.frame)) #put dummy dimension
            self.emit.printout(self.emit.emitPUSHARRAY_SHALLOW(fSym.mtype.rettype, message.frame))
        self.emit.printout(self.emit.emitRETURN(fSym.mtype.rettype, message.frame)) #Make sure to print return
            
        self.emit.printout(self.emit.emitENDMETHOD(message.frame)) #print out end method directive
        
        message.frame.exitScope() #redundant, I added this to make this file have the same number of enter and exit, so that I can debug easier
        
        return "", Symbol(ctx.name, fSym.mtype, CName(self.className))
    
    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ctx, o):#DONE #location to call accept is VERY IMPORTANT (it change the frame's stack immediately)
    #print nothing
    #return jCode, type
        #temp = o.isLeft #not need?
        #o.isLeft = False #not need?
        #lhsCode, lhsType = ctx.left.accept(self, o)
        #rhsCode, rhsType = ctx.right.accept(self, o)
        #o.isLeft = temp #not need?
        
        if ctx.op in ['+', '-', '+.', '-.']:
            lex = ctx.op
            if len(lex) > 1: lex = lex[0] #remove dot if necessary
            lhsCode, lhsType = ctx.left.accept(self, o)
            rhsCode, rhsType = ctx.right.accept(self, o)
            return lhsCode + rhsCode + self.emit.emitADDOP(lex, lhsType, o.frame), lhsType
        elif ctx.op in ['*', '\\', '*.', '\\.']:
            lex = ctx.op
            if len(lex) > 1: lex = lex[0] #remove dot if necessary
            lhsCode, lhsType = ctx.left.accept(self, o)
            rhsCode, rhsType = ctx.right.accept(self, o)
            return lhsCode + rhsCode + self.emit.emitMULOP(lex, lhsType, o.frame), lhsType
        elif ctx.op in ['%']:
            lhsCode, lhsType = ctx.left.accept(self, o)
            rhsCode, rhsType = ctx.right.accept(self, o)
            return lhsCode + rhsCode + self.emit.emitMOD(o.frame), lhsType
        elif ctx.op in ['>', '<', '==', '>=', '<=', '!=']:
            lhsCode, lhsType = ctx.left.accept(self, o)
            rhsCode, rhsType = ctx.right.accept(self, o)
            return lhsCode + rhsCode + self.emit.emitREOP(ctx.op, lhsType, o.frame), BoolType()
        elif ctx.op in ['>.', '<.', '>=.', '<=.', '=/=']:
            lhsCode, lhsType = ctx.left.accept(self, o)
            rhsCode, rhsType = ctx.right.accept(self, o)
            return lhsCode + rhsCode + self.emit.emitREFOP(ctx.op, lhsType, o.frame), BoolType()
        elif ctx.op in ['&&']: #short-circuit evaluation
            labelF = o.frame.getNewLabel()
            labelO = o.frame.getNewLabel()
            
            lhsCode, lhsType = ctx.left.accept(self, o)
            jCode = lhsCode #put left expr boolean value on to stack
            jCode += self.emit.emitIFFALSE(labelF, o.frame)#conclude false when left is false  
            
            rhsCode, rhsType = ctx.right.accept(self, o)
            jCode += rhsCode #put right expr boolean value on to stack
            
            jCode += self.emit.emitIFFALSE(labelF, o.frame)
            
            jCode += self.emit.emitPUSHICONST(1, o.frame)
            o.frame.pop()
            jCode += self.emit.emitGOTO(labelO, o.frame)
            
            jCode += self.emit.emitLABEL(labelF, o.frame)
            jCode += self.emit.emitPUSHICONST(0, o.frame)
            jCode += self.emit.emitLABEL(labelO, o.frame)
            return jCode, BoolType()
            
        elif ctx.op in ['||']: #short-circuit evaluation
            labelT = o.frame.getNewLabel()
            labelO = o.frame.getNewLabel()
            
            lhsCode, lhsType = ctx.left.accept(self, o)
            jCode = lhsCode #put left expr boolean value on to stack
            jCode += self.emit.emitIFTRUE(labelT, o.frame)#conclude false when left is false  
            
            rhsCode, rhsType = ctx.right.accept(self, o)
            jCode += rhsCode #put right expr boolean value on to stack
            
            jCode += self.emit.emitIFTRUE(labelT, o.frame)
            
            jCode += self.emit.emitPUSHICONST(0, o.frame)
            o.frame.pop()
            jCode += self.emit.emitGOTO(labelO, o.frame)
            
            jCode += self.emit.emitLABEL(labelT, o.frame)
            jCode += self.emit.emitPUSHICONST(1, o.frame)
            jCode += self.emit.emitLABEL(labelO, o.frame)
            return jCode, BoolType()
    
    # op:str
    # body:Expr
    def visitUnaryOp(self, ctx, o):#DONE
        temp = o.isLeft #not need?
        o.isLeft = False #not need?

        operandCode, operandType = ctx.body.accept(self, o)

        o.isLeft = temp #not need?
        if ctx.op in ['-', '-.']:
            return operandCode + self.emit.emitNEGOP(operandType, o.frame), operandType
        elif ctx.op in ['!']:
            return operandCode + self.emit.emitNOT(operandType, o.frame), BoolType()
    
    #method:Id
    #param:List[Expr]
    def visitCallExpr(self, ctx, o):#DONE #location to call accept is VERY IMPORTANT (it change the frame's stack immediately)
    #print nothing
    #return jCode, type  
        temp = o.isLeft #not need?
        o.isLeft = False #not need?
        
        #paramCodeList = list(map(lambda x: x.accept(self.o)[0], funcType.mtype.partype))

        paramCodeList = list(map(lambda x: x.accept(self, o)[0], ctx.param)) #put actual parameter value onto stack       

        callCode, funcType = ctx.method.accept(self, o)       
        jCode = reduce(lambda x,y: x + y, paramCodeList, "") + callCode
        
        o.isLeft = temp #not need?                                   
        return jCode, funcType.rettype
       
    #lhs: LHS
    #rhs: Expr
    def visitAssign(self, ctx, o):#DONE #location to call accept is VERY IMPORTANT (it change the frame's stack immediately)
    #print assignCode
    #return nothing        
        #The order in which we call accept is VERY important
        if type(ctx.lhs) is Id:
            o.isLeft = False
            rhsCode, rhsType = ctx.rhs.accept(self, o)            
            o.isLeft = True
            lhsCode, lhsType = ctx.lhs.accept(self, o)
            o.isLeft = False
            
            self.emit.printout(rhsCode + lhsCode)
            return
        
        #Else: lhs is arrayCell => lhs will load address and index onto stack first, then rhs load value to be stored, lastly we exceute store instruction
        o.isLeft = True
        lhsCode, lhsType = ctx.lhs.accept(self, o)
        o.isLeft = False
        rhsCode, rhsType = ctx.rhs.accept(self, o)
        self.emit.printout(lhsCode + rhsCode + self.emit.emitASTORE(lhsType, o.frame))
    
    
    """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """
    #ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    #elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    def visitIf(self, ctx, o):#DONE #location to call accept is VERY IMPORTANT (it change the frame's stack immediately)
    #print ifCode
    #return nothing    
        labelO = o.frame.getNewLabel()
        for ifThenAST in ctx.ifthenStmt:
            expCode, expType = ifThenAST[0].accept(self, o) #used outer scope
            
            o.frame.enterScope(False)
            #we need to store the start and end lable immediately because there might be other inner statement trying to enter Scope again
            labelS = o.frame.getStartLabel() 
            labelE = o.frame.getEndLabel()
            
            message = MethodEnv(o.frame, o.sym.copy()) #copy o.sym to preserve the original symbol list
                    
            self.emit.printout(expCode) #put expression-value on stack
            self.emit.printout(self.emit.emitIFFALSE(labelE, message.frame)) #compare top of stack, if false then jump to end label
            
            varInitCode, varSymbolList = [], []
            #we are assuming there's no Redeclared Variable error here. Else this won't work
            varInitCode, varSymbolList = [], []
            if len(ifThenAST[1]) > 0:
                varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ifThenAST[1]))) #call accept to print var declare directive and receive a list of local method's variable symbol
            message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
            
            #mark the start of if label
            self.emit.printout(self.emit.emitLABEL(labelS, message.frame)) #the second parameter message.frame is redundant (emitter didn't use them)
            
            self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter                                  
            [st.accept(self, message) for st in ifThenAST[2]]#if body statements
            
            self.emit.printout(self.emit.emitGOTO(labelO, message.frame)) #goto out of ifThenElse
            self.emit.printout(self.emit.emitLABEL(labelE, message.frame)) #mark exit out of current if body label    
            
            o.frame.exitScope()
        
        if len(ctx.elseStmt[0]) + len(ctx.elseStmt[1]) > 0:
            o.frame.enterScope(False)
            #we need to store the start and end lable immediately because there might be other inner statement trying to enter Scope again
            labelS = o.frame.getStartLabel()
            labelE = o.frame.getEndLabel()
            
            message = MethodEnv(o.frame, o.sym.copy()) #copy o.sym to preserve the original symbol list
            
            varInitCode, varSymbolList = [], []
            if len(ctx.elseStmt[0]) > 0:
                varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ctx.elseStmt[0]))) #call accept to print var declare directive and receive a list of local method's variable symbol
            message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
            
            #mark the start of else label
            self.emit.printout(self.emit.emitLABEL(labelS, message.frame)) #the second parameter message.frame is redundant (emitter didn't use them)

            self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter
            [st.accept(self, message) for st in ctx.elseStmt[1]]#if body statements
            
            self.emit.printout(self.emit.emitLABEL(labelE, message.frame)) #mark exit out of current if body label            
            o.frame.exitScope()
            
        self.emit.printout(self.emit.emitLABEL(labelO, o.frame)) #mark exit out of current if body label
    
    
    #idx1: Id
    #expr1:Expr
    #expr2:Expr
    #expr3:Expr
    #loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ctx, o):#DONE #order and location of accept call is VERY IMPORTANT
    #print loopCode
    #return nothing
        message = MethodEnv(o.frame, o.sym.copy()) #need to copy o.sym to preserve the global list
        
        message.frame.enterLoop()
        #we need to store the loop lables immediately because there might be other loop statement trying to enter Scope again
        labelBrk = message.frame.getBreakLabel()
        labelCont = message.frame.getContinueLabel()
        
        message.frame.enterScope(False)
        #we need to store the start and end lable immediately because there might be other inner statement trying to enter Scope again
        labelStart = message.frame.getStartLabel() 
        labelEnd = message.frame.getEndLabel()
        
        o.isLeft = False
        rhsCode, rhsType = ctx.expr1.accept(self, o) #used outer scope
        o.isLeft = True
        indexAddressCode, lhsType = ctx.idx1.accept(self, o) #used outer scope
        o.isLeft = False
        self.emit.printout(rhsCode + indexAddressCode) #print idx variable init assignment instuction
        
        labelCondition = message.frame.getNewLabel() 
        self.emit.printout(self.emit.emitLABEL(labelCondition, message.frame)) #mark condition label
        
        condCode, condType = ctx.expr2.accept(self, o) #used outer scope
        self.emit.printout(condCode) #put expression-value on stack
        self.emit.printout(self.emit.emitIFFALSE(labelBrk, message.frame)) #compare top of stack, if false then jump to end label
        
        varInitCode, varSymbolList = [], []
        if len(ctx.loop[0]) > 0:
            varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ctx.loop[0]))) #call accept to print var declare directive and receive a list of local method's variable symbol
        message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
        self.emit.printout(self.emit.emitLABEL(labelStart, message.frame)) #mark the start of local VarDecl label
        
        self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter
        [st.accept(self, message) for st in ctx.loop[1]]#for body statements
        
        self.emit.printout(self.emit.emitLABEL(labelEnd, message.frame)) #mark the end of local VarDecl label 
                
        self.emit.printout(self.emit.emitLABEL(labelCont, message.frame)) #mark continue point
        
        #update index variable
        o.isLeft = False
        indexValueCode, indexValueType = ctx.idx1.accept(self, o) #used outer scope
        incrementCode, incrementType = ctx.expr3.accept(self, o) #used outer scope

        self.emit.printout(indexValueCode + incrementCode) #put value of index and increment value on to stack -> stack + 2
        self.emit.printout(self.emit.emitADDOP("+", IntType(), message.frame)) #integer addition them together -> stack - 1
        self.emit.printout(indexAddressCode) #store result into index variable -> stack - 1
        message.frame.pop() #THIS IS EXTREMLY IMPORTANT, I WATSED 2 HOURS OF MY LIFE DEBUGGING BECAUSE OF THIS SINGLE LINE

        self.emit.printout(self.emit.emitGOTO(labelCondition, message.frame)) #go back to condition Check
        
        self.emit.printout(self.emit.emitLABEL(labelBrk, message.frame)) #mark break point
        
        message.frame.exitScope()
        
        message.frame.exitLoop()
    
    
    def visitContinue(self, ctx, o):#DONE
    #print continueCode
    #return nothing
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))
    
    
    def visitBreak(self, ctx, o):#DONE
    #print breakCode
    #return nothing
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    
    
    #expr:Expr # None if no expression
    def visitReturn(self, ctx, o):#DONE
    #print breakCode
    #return nothing
        expType = VoidType()
        if ctx.expr:
            expCode, expType = ctx.expr.accept(self, o)
            self.emit.printout(expCode)       
        self.emit.printout(self.emit.emitRETURN(expType, o.frame))
    
    
    #sl:Tuple[List[VarDecl],List[Stmt]]
    #exp: Expr
    def visitDowhile(self, ctx, o):
    #print DowhileCode
    #return nothing
        message = MethodEnv(o.frame, o.sym.copy()) #need to copy o.sym to preserve the global list
        
        message.frame.enterLoop()
        #we need to store the loop lables immediately because there might be other loop statement trying to enter Scope again
        labelBrk = message.frame.getBreakLabel()
        labelCont = message.frame.getContinueLabel()
        
        message.frame.enterScope(False)
        #we need to store the start and end lable immediately because there might be other inner statement trying to enter Scope again
        labelStart = message.frame.getStartLabel() 
        labelEnd = message.frame.getEndLabel()
        
        varInitCode, varSymbolList = [], []
        if len(ctx.sl[0]) > 0:
            varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ctx.sl[0]))) #call accept to print var declare directive and receive a list of local method's variable symbol
        message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
        self.emit.printout(self.emit.emitLABEL(labelStart, message.frame)) #mark the start of local VarDecl label
        
        self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter
        [st.accept(self, message) for st in ctx.sl[1]]#for body statements
        
        self.emit.printout(self.emit.emitLABEL(labelEnd, message.frame)) #mark the end of local VarDecl label
        
        self.emit.printout(self.emit.emitLABEL(labelCont, message.frame)) #mark continue label
        
        condCode, condType = ctx.exp.accept(self, o) #exp used outer scope symbol
        self.emit.printout(condCode) #put expression-value on stack
        self.emit.printout(self.emit.emitIFTRUE(labelStart, message.frame)) #compare top of stack, if true then jump to start label
        
        self.emit.printout(self.emit.emitLABEL(labelBrk, message.frame)) #mark break point
        
        message.frame.exitScope()
        
        message.frame.exitLoop()
        

    #exp: Expr
    #sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ctx, o):
    #print WhileCode
    #return nothing
        message = MethodEnv(o.frame, o.sym.copy()) #need to copy o.sym to preserve the global list
        
        message.frame.enterLoop()
        #we need to store the loop lables immediately because there might be other loop statement trying to enter Scope again
        labelBrk = message.frame.getBreakLabel()
        labelCont = message.frame.getContinueLabel()
        
        message.frame.enterScope(False)
        #we need to store the start and end lable immediately because there might be other inner statement trying to enter Scope again
        labelStart = message.frame.getStartLabel() 
        labelEnd = message.frame.getEndLabel()
        
        self.emit.printout(self.emit.emitLABEL(labelCont, message.frame)) #mark continue label
        
        condCode, condType = ctx.exp.accept(self, o) #used outer scope
        self.emit.printout(condCode) #put expression-value on stack
        self.emit.printout(self.emit.emitIFFALSE(labelBrk, message.frame)) #compare top of stack, if false then jump to break label
        
        varInitCode, varSymbolList = [], []
        if len(ctx.sl[0]) > 0:
            varInitCode, varSymbolList = zip(*list(map(lambda x: x.accept(self, message), ctx.sl[0]))) #call accept to print var declare directive and receive a list of local method's variable symbol
        message.sym[:0] = varSymbolList #append list of var symbol into the beginning of message.sym list
        self.emit.printout(self.emit.emitLABEL(labelStart, message.frame)) #mark the start of local VarDecl label
        
        self.emit.printout(''.join(varInitCode)) #init all local variables, except for parameter
        [st.accept(self, message) for st in ctx.sl[1]]#for body statements
        
        self.emit.printout(self.emit.emitLABEL(labelEnd, message.frame)) #mark the end of local VarDecl label

        self.emit.printout(self.emit.emitGOTO(labelCont, message.frame)) #go back to condition Check
        
        self.emit.printout(self.emit.emitLABEL(labelBrk, message.frame)) #mark break point
        
        message.frame.exitScope()
        
        message.frame.exitLoop()

    #method:Id
    #param:List[Expr]
    def visitCallStmt(self, ctx, o): #DONE
    #print CallStmtCode
    #return nothing
        temp = o.isLeft #not need?
        o.isLeft = False #not need?

        #paramCodeList = list(map(lambda x: x.accept(self.o)[0], funcType.mtype.partype))
        paramCodeList = list(map(lambda x: x.accept(self, o)[0], ctx.param)) #put actual parameter value onto stack 

        callCode, funcType = ctx.method.accept(self, o) #pop actual param value from stack and generate call code
   
        jCode = reduce(lambda x,y: x + y, paramCodeList, "") + callCode  
        
        o.isLeft = temp #not need?

        self.emit.printout(jCode)
        
    #value:int
    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()
    
    #value:float
    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(str(ctx.value), o.frame), FloatType()
    
    #value:bool
    def visitBooleanLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST("true" if ctx.value else "false", o.frame), BoolType()
    
    #value:string
    def visitStringLiteral(self, ctx, o): #enclosing double-quotes? Not sure
        return self.emit.emitPUSHCONST('"' + ctx.value + '"', StringType(), o.frame), StringType() 

    
    #value:List[Literal]
    #This code is not optimized and contain alot of redundancy
    #shallow array version (multi-dimensional array is created using anewarray of multiple anewarray)
    def visitArrayLiteral(self, ctx, o):
        jCode = ""        
        
        returnType, dc1, dc2, dc3, dc4 = ctx.accept(self.typeInferer, None)
        dimension = returnType.dimen

        """ OLD CODE - replaced by assignment-3's visitor to get the ArrayType
        dimension = [len(ctx.value)]
        dummyFrame = Frame("", VoidType())
        dontCare, theType = ctx.value[0].accept(self, MethodEnv(dummyFrame, o.sym))
        
        if isinstance(theType, ArrayType):
            dimension += theType.dimen
            theType = theType.eleType
        """   
        
        #print(returnType)
        jCode += self.emit.emitPUSHICONST(dimension[0], o.frame) # -> stack+1
        jCode += self.emit.emitPUSHARRAY_SHALLOW(returnType, o.frame) # -> stack+0
                
        for i in range(0, dimension[0]):            
            jCode += self.emit.emitDUP(o.frame) #duplicate the Parent Array address ->stack+1
            jCode += self.emit.emitPUSHICONST(i, o.frame) #push the current index for iterating through parent array -> stack+2
            
            #print(ctx.value[i])
            eleCode, eleType = ctx.value[i].accept(self, o)
            jCode += eleCode #push the literal onto the stack ->stack+3
             
            jCode += self.emit.emitASTORE(eleType, o.frame)  # -> stack-3
                    
        return jCode, returnType
    
    
    
    #This code is not optimized and contain alot of redundancy
    #I write this for fun, in reality JDK 15 compiler use the shallow version because they're faster (multianewarray is poorly optimized, though they used less stack size)
    #To use this, just change to shallow version's name to something else and rename this function to visitArrayLiteral 
    #deep version (multi-dimensional array is created using multianewarray)
    def visitArrayLiteral_deep(self, ctx, o):
        jCode = ""
        
        returnType, dc1, dc2, dc3, dc4 = ctx.accept(self.typeInferer, None)
        
        for d in returnType.dimen: 
            jCode += self.emit.emitPUSHICONST(d, o.frame)
        
        jCode += self.emit.emitPUSHARRAY_DEEP(returnType, o.frame)
        jCode += self.emit.emitDUP(o.frame)
        
        arrayBodyCode, dc5 = self.buildArrayType(ctx, o)
                       
        return jCode + arrayBodyCode, returnType    
        
    def buildArrayType(self, ast, o):
        jCode = ""
        
        returnType, dc1, dc2, dc3, dc4 = ast.accept(self.typeInferer, None)
        dimension = returnType.dimen
        
        if not type(ast.value[0]) is ArrayLiteral:
            for i in range(0, dimension[0]):
                if i < dimension[0] - 1: #if this is not the last element
                    jCode += self.emit.emitDUP(o.frame) #duplicate the Parent Array address, except for the last element
                
                jCode += self.emit.emitPUSHICONST(i, o.frame) #push the current index for iterating through parent array 
                
                eleCode, eleType = ast.value[i].accept(self, o)                
                jCode += eleCode #push the literal onto the stack
                jCode += self.emit.emitASTORE(eleType, o.frame)
            return jCode, returnType
        
        
        for i in range(0, dimension[0]):            
            if i < dimension[0] - 1: #if this is not the last element
                jCode += self.emit.emitDUP(o.frame)
            
            jCode += self.emit.emitPUSHICONST(i, o.frame)
            
            childType = ArrayType(returnType.eleType, returnType.dimen[1:])
            jCode += self.emit.emitALOAD(childType, o.frame)
           
            eleCode, eleType = self.buildArrayType(ast.value[i], o)
            jCode += eleCode #push the literal onto the stack    
                
        return jCode, returnType
      


#################REUSING TYPE INFERER################
#I have a feeling that these classes will cause troubles for me in the future... they might have been already declared somewhere outside of my control
class Kind(ABC):
    pass
class Function(Kind):
    def __str__(self):
        return "Function"
class Parameter(Kind):
    def __str__(self):
        return "Parameter"
class Variable(Kind):
    def __str__(self):
        return "Variable"
class Identifier(Kind):
    def __str__(self):
        return "Identifier"

#I have a feeling that these exceptions will cause troubles for me in the future...they might have been already declared somewhere outside of my control
class StaticError(Exception):
    pass    
class Undeclared(StaticError):  
    def __init__(self, k, n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n
class Redeclared(StaticError):
    def __init__(self, k, n):
        self.k = k
        self.n = n
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n
class TypeMismatchInExpression(StaticError):
    def __init__(self, e):
        self.exp = e
    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)
class TypeMismatchInStatement(StaticError):
    def __init__(self, s):
        self.stmt = s
    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)
class TypeCannotBeInferred(StaticError):
    def __init__(self, s):
        self.stmt = s
    def __str__(self):
        return "Type Cannot Be Inferred: "+ str(self.stmt)
class NoEntryPoint(StaticError):
    def __str__(self):
        return "No Entry Point"
        

class OldSymbol:
    def __init__(self, *arg):
        if(len(arg) == 2): #arg[0]: Symbol; arg[1]: Kind
            self.name = arg[0].name
            self.mtype = arg[0].mtype
            self.kind = arg[1]
            self.value = arg[0].value
            return None
        elif(len(arg) == 4): 
            self.name = arg[0]
            self.mtype = arg[1]
            self.kind = arg[2]
            self.value = arg[3]
            return None
    
    def purgeUnknownType(self): #turn all uninfered type into int (or void for func return) - just to be sure,.. my type inferer is not perfect
        #I make this mostly to match the 2 initial test cases: this will purge main() return type
        purged = False
        if type(self.mtype) is Unknown: #This should never happen
            self.mtype = VoidType()
            purged = True
        elif type(self.mtype) is ArrayType and type(self.mtype.eleType) is Unknown: #This should never happen
            self.mtype.eleType = VoidType() #Not sure - might need to turn the whole array into VoidType
            purged = True
        elif type(self.mtype) is MType:
            if type(self.mtype.rettype) is Unknown: 
                self.mtype.rettype = VoidType()
                purged = True
            elif type(self.mtype.rettype) is ArrayType and type(self.mtype.rettype.eleType) is Unknown: #This should never happen
                self.mtype.rettype.eleType = IntType() #Not sure - might need to turn the whole array into VoidType   
                purged = True
            for i in range(0, len(self.mtype.partype)):
                if type(self.mtype.partype[i]) is Unknown:
                    self.mtype.partype[i] = IntType() #auto infer unknown param to be int - just to be sure
                    purged = True
                elif type(self.mtype.partype[i]) is ArrayType and type(self.mtype.partype[i].eleType) is Unknown:
                    self.mtype.partype[i].eleType = IntType() #Not sure - might need to turn the whole array into VoidType
                    purged = True
        return purged
        
    def toSymbol(self):
        res = self.purgeUnknownType();
        #if res: print("Something is purged!") #remove when done
        return Symbol(self.name, self.mtype, self.value)
    
    def __str__(self): 
        return "OldSymbol(" + self.name + ", " + str(self.mtype) + ", " + str(self.kind) + ", " + str(self.value) + ")"
    def __repr__(self): return self.__str__()   
    
class Unknown(Type):
    def __str__(self): return "UNKNOWN"
    def __repr__(self): return "UNKNOWN"

class StaticChecker(BaseVisitor): #inherite Visitor.py in scr/main/bkit/utils
    #copied and modified from assignment 3
    def __init__(self,ast, gl):
        self.ast = ast
        self.global_envi = list(map(lambda x: OldSymbol(x, Function()), gl))  
        self.className = "MCClass" #NEWLY ADDED
   
    #1852668 - assignment 3
    def check(self): #entry method
        #return self.visit(self.ast,self.global_envi)
        res = self.visit(self.ast,self.global_envi)
        
        #self.printOldSymbolTable(res) #remove this when done
            
        returnList = list(map(lambda x: x.toSymbol(), res['scope'][0])) 
        
        #self.printSymbolTable(returnList) #remove this when done
        
        return returnList
        
    def printOldSymbolTable(self, res):
        if res:
            print("--------------------OldSymbol Table---------------------")
            i = 0
            for s in res['scope']:
                print("Scope:", i)
                i += 1
                for sym in s:
                    print("\t", str(sym))    
            print("-------------------END OldSymbol Table-------------------")
            
    def printSymbolTable(self, returnList):
        print("------------------------Symbol Table------------------------")
        for sym in returnList:
            print("\t", str(sym))
        print("----------------------END Symbol Table----------------------")
    
    # decl : List[Decl]
    def visitProgram(self,ast, param):
        #[self.visit(x,c) for x in ast.decl]
        
        message = {}
        message['currentFuncIndex'] = -1 #positive index of the current function symbol in the message['scope'][0] list - used to let returnStatement remember its father - also used to update parameterType
        message['scope'] = [param]
        message['FunctionKind'] = False
        
        mainNotFound = True
        #first loop: name checking, visit global VarDecl, scout FuncDecl, build global scope.
        for d in ast.decl:
            if isinstance(d, VarDecl):
                message['scope'][0].append(d.accept(self, message))
            else: #AST:FuncDecl - no vist because we only scout the function number of param (and dimension if it's ARRAY), not type check inside it
                # name: Id
                # param: List[VarDecl]
                # body: Tuple[List[VarDecl],List[Stmt]]
                funcName = d.name.name
                
                if any(funcName == x.name for x in message['scope'][0]): raise Redeclared(Function(), funcName)
                
                paramTypeList = []
                for p in d.param:
                    theType = Unknown()
                    if len(p.varDimen) > 0:
                        theType = ArrayType(Unknown(), p.varDimen)
                    paramTypeList.append(theType)
                
                message['scope'][0].append(OldSymbol(funcName, MType(paramTypeList, Unknown()), Function(), CName(self.className)))
                if funcName == 'main': mainNotFound = False
        
        if mainNotFound: raise NoEntryPoint()
        
        #second loop: type inference and checking - top down, first usage policy => parameter and return type can change midway through the function's AST - THIS IS HARD.
        #message['mode'] = 1
        for d in ast.decl:
            if isinstance(d, FuncDecl):
                for i in range(0, len(message['scope'][0])): #not efficient but I'm too tire
                    if message['scope'][0][i].name == d.name.name:
                        message['currentFuncIndex'] = i
                        break;
                d.accept(self, message)
        
        return message #to see the scope in res
    
    # variable : Id
    # varDimen : List[int] # empty list for scalar variable
    # varInit  : Literal   # null if no initial
    def visitVarDecl(self, ast, param): #DONE
        #Scala equivalent of exist: https://docs.python.org/3/library/functions.html#any
        if any(ast.variable.name == x.name for x in param['scope'][-1]): 
            raise Redeclared(Variable(), ast.variable.name) #we only care about the most local scope => -1 index
        else:
            theType = Unknown()
            if ast.varInit:
                theType, dontCare1, dontCare2, dontCare3, dontCare4 = ast.varInit.accept(self, param)
                #if isinstance(theType, ArrayType): #No TypeMismatchInVarDecl in case of a[5] = {{1}}? 
                #    if theType.dimen != ast.varDimen: raise...
            #if there's varInit, we don't care about its dimension, because we were not asked to check for that here(there's no way to raise exception here)
            elif len(ast.varDimen) > 0:
                theType = ArrayType(Unknown(), ast.varDimen)
            
            return OldSymbol(ast.variable.name, theType, Variable(), CName(self.className))         
    
    def visitParam(self, ast, param, theType): #mimicking visitVarDecl..now I know the reason for Kind()
        #Scala equivalent of exist: https://docs.python.org/3/library/functions.html#any
        if any(ast.variable.name == x.name for x in param['scope'][-1]): 
            raise Redeclared(Parameter(), ast.variable.name) #we only care about the most local scope => -1 index
        else:
            return OldSymbol(ast.variable.name, theType, Parameter(), CName(self.className))
    
    # name: Id
    # param: List[VarDecl]
    # body: Tuple[List[VarDecl],List[Stmt]]
    def visitFuncDecl(self, ast, param):
        funcName = ast.name.name
        param['scope'].append([])
        for i in range(0, len(ast.param)):           
            param['scope'][-1].append(self.visitParam(ast.param[i], param, param['scope'][0][param['currentFuncIndex']].mtype.partype[i])) #I regret my SymbolTable design....
        
        for vd in ast.body[0]:
            param['scope'][-1].append(vd.accept(self, param))
            
        for st in ast.body[1]:
            st.accept(self, param) # to be changed
        
        #assignment pdf didn't mention about checking for return type Void in case of no return statement, which make sense because how can we raise TypeMisMatch in FuncDecl
        #beside that, checking for no return would that imply a Void return is unrealistic, since that mean all function scope exit branch of if, else,... must be checked as well 
        #thisFuncIndex = param['currentFuncIndex']
        #if type(param['scope'][0][thisFuncIndex].mtype.rettype) is Unknown: #there's no return statement
        #    param['scope'][0][thisFuncIndex].mtype.rettype = VoidType()
        
        param['scope'].pop() #return to global enviroment original state
        
    # op:str
    # left:Expr
    # right:Expr
    def visitBinaryOp(self, ast, param):
        lhs, indexL1, indexL2, fromFuncExp_L, fromArrayCell_L = ast.left.accept(self, param)
        rhs, indexR1, indexR2, fromFuncExp_R, fromArrayCell_R = ast.right.accept(self, param)
        if lhs is None or rhs is None: return None, None, None, None, None
        
        if ast.op in ["-", "+", "*", "\\", "%"]:
            if type(lhs) is Unknown:
                lhs = IntType() #1 change here when copy
                if fromFuncExp_L and fromArrayCell_L: param['scope'][indexL1][indexL2].mtype.rettype.eleType = lhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_L: param['scope'][indexL1][indexL2].mtype.rettype = lhs #infer function return basic type
                elif fromArrayCell_L: 
                    param['scope'][indexL1][indexL2].mtype.eleType = lhs #infer array basic type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = lhs
                else: 
                    param['scope'][indexL1][indexL2].mtype = lhs #infer symbol type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = lhs
            if type(rhs) is Unknown:
                rhs = IntType() #1 change here when copy
                if fromFuncExp_R and fromArrayCell_R: param['scope'][indexR1][indexR2].mtype.rettype.eleType = rhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_R: param['scope'][indexR1][indexR2].mtype.rettype = rhs #infer function return basic type
                elif fromArrayCell_R: 
                    param['scope'][indexR1][indexR2].mtype.eleType = rhs #infer array basic type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs
                else: 
                    param['scope'][indexR1][indexR2].mtype = rhs #infer symbol type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs
            if type(lhs) is IntType and type(rhs) is IntType: return IntType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        
        if ast.op in ["-.", "+.", "*.", "\\."]:
            if type(lhs) is Unknown:
                lhs = FloatType() #1 change here when copy
                if fromFuncExp_L and fromArrayCell_L: param['scope'][indexL1][indexL2].mtype.rettype.eleType = lhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_L: param['scope'][indexL1][indexL2].mtype.rettype = lhs #infer function return basic type
                elif fromArrayCell_L: 
                    param['scope'][indexL1][indexL2].mtype.eleType = lhs #infer array basic type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = lhs
                else: 
                    param['scope'][indexL1][indexL2].mtype = lhs #infer symbol type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = lhs
            if type(rhs) is Unknown:
                rhs = FloatType() #1 change here when copy
                if fromFuncExp_R and fromArrayCell_R: param['scope'][indexR1][indexR2].mtype.rettype.eleType = rhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_R: param['scope'][indexR1][indexR2].mtype.rettype = rhs #infer function return basic type
                elif fromArrayCell_R: 
                    param['scope'][indexR1][indexR2].mtype.eleType = rhs #infer array basic type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs
                else: 
                    param['scope'][indexR1][indexR2].mtype = rhs #infer symbol type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs
            if type(lhs) is FloatType and type(rhs) is FloatType: return FloatType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
    
        if ast.op in ["==", "!=", "<", ">", "<=", ">="]:
            if type(lhs) is Unknown:
                lhs = IntType() #1 change here when copy
                if fromFuncExp_L and fromArrayCell_L: param['scope'][indexL1][indexL2].mtype.rettype.eleType = lhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_L: param['scope'][indexL1][indexL2].mtype.rettype = lhs #infer function return basic type
                elif fromArrayCell_L: 
                    param['scope'][indexL1][indexL2].mtype.eleType = lhs #infer array basic type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = lhs
                else: 
                    param['scope'][indexL1][indexL2].mtype = lhs #infer symbol type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = lhs
            if type(rhs) is Unknown:
                rhs = IntType() #1 change here when copy
                if fromFuncExp_R and fromArrayCell_R: param['scope'][indexR1][indexR2].mtype.rettype.eleType = rhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_R: param['scope'][indexR1][indexR2].mtype.rettype = rhs #infer function return basic type
                elif fromArrayCell_R: 
                    param['scope'][indexR1][indexR2].mtype.eleType = rhs #infer array basic type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs
                else: 
                    param['scope'][indexR1][indexR2].mtype = rhs #infer symbol type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs
            if type(lhs) is IntType and type(rhs) is IntType: return BoolType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        
        if ast.op in ["=/=", "<.", ">.", "<=.", ">=."]:
            if type(lhs) is Unknown:
                lhs = FloatType() #1 change here when copy
                if fromFuncExp_L and fromArrayCell_L: param['scope'][indexL1][indexL2].mtype.rettype.eleType = lhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_L: param['scope'][indexL1][indexL2].mtype.rettype = lhs #infer function return basic type
                elif fromArrayCell_L: 
                    param['scope'][indexL1][indexL2].mtype.eleType = lhs #infer array basic type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = lhs
                else: 
                    param['scope'][indexL1][indexL2].mtype = lhs #infer symbol type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = lhs
            if type(rhs) is Unknown:
                rhs = FloatType() #1 change here when copy
                if fromFuncExp_R and fromArrayCell_R: param['scope'][indexR1][indexR2].mtype.rettype.eleType = rhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_R: param['scope'][indexR1][indexR2].mtype.rettype = rhs #infer function return basic type
                elif fromArrayCell_R: 
                    param['scope'][indexR1][indexR2].mtype.eleType = rhs #infer array basic type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs
                else: 
                    param['scope'][indexR1][indexR2].mtype = rhs #infer symbol type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs
            if type(lhs) is FloatType and type(rhs) is FloatType: return BoolType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        
        if ast.op in ["&&", "||"]:
            if type(lhs) is Unknown:
                lhs = BoolType() #1 change here when copy
                if fromFuncExp_L and fromArrayCell_L: param['scope'][indexL1][indexL2].mtype.rettype.eleType = lhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_L: param['scope'][indexL1][indexL2].mtype.rettype = lhs #infer function return basic type
                elif fromArrayCell_L: 
                    param['scope'][indexL1][indexL2].mtype.eleType = lhs #infer array basic type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = lhs
                else: 
                    param['scope'][indexL1][indexL2].mtype = lhs #infer symbol type
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = lhs
            if type(rhs) is Unknown:
                rhs = BoolType() #1 change here when copy
                if fromFuncExp_R and fromArrayCell_R: param['scope'][indexR1][indexR2].mtype.rettype.eleType = rhs #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp_R: param['scope'][indexR1][indexR2].mtype.rettype = rhs #infer function return basic type
                elif fromArrayCell_R: 
                    param['scope'][indexR1][indexR2].mtype.eleType = rhs #infer array basic type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs
                else: 
                    param['scope'][indexR1][indexR2].mtype = rhs #infer symbol type
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs
            if type(lhs) is BoolType and type(rhs) is BoolType: return BoolType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        
    # op:str
    # body:Expr
    def visitUnaryOp(self, ast, param):
        opd, index1, index2, fromFuncExp, fromArrayCell = ast.body.accept(self, param)
        if opd is None: return None, None, None, None, None
        
        if ast.op == "-":
            if type(opd) is Unknown:
                opd = IntType() #1 change here when copy
                if fromFuncExp and fromArrayCell: param['scope'][index1][index2].mtype.rettype.eleType = opd #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp: param['scope'][index1][index2].mtype.rettype = opd #infer function return basic type
                elif fromArrayCell: 
                    param['scope'][index1][index2].mtype.eleType = opd #infer array basic type
                    if type(param['scope'][index1][index2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2].eleType = opd
                else: 
                    param['scope'][index1][index2].mtype = opd #infer symbol type
                    if type(param['scope'][index1][index2].kind) is Parameter: #the inferred id is also parameter of this function
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2] = opd
            if type(opd) is IntType: return IntType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        if ast.op == "-.":
            if type(opd) is Unknown:
                opd = FloatType() #1 change here when copy
                if fromFuncExp and fromArrayCell: param['scope'][index1][index2].mtype.rettype.eleType = opd #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp: param['scope'][index1][index2].mtype.rettype = opd #infer function return basic type
                elif fromArrayCell: 
                    param['scope'][index1][index2].mtype.eleType = opd #infer array basic type
                    if type(param['scope'][index1][index2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2].eleType = opd
                else: 
                    param['scope'][index1][index2].mtype = opd #infer symbol type
                    if type(param['scope'][index1][index2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2] = opd
            if type(opd) is FloatType: return FloatType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
        if ast.op == "!":
            if type(opd) is Unknown:
                opd = BoolType() #1 change here when copy
                if fromFuncExp and fromArrayCell: param['scope'][index1][index2].mtype.rettype.eleType = opd #infer function that return an array but become basic type after gone through index op
                elif fromFuncExp: param['scope'][index1][index2].mtype.rettype = opd #infer function return basic type
                elif fromArrayCell: 
                    param['scope'][index1][index2].mtype.eleType = opd #infer array basic type
                    if type(param['scope'][index1][index2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2].eleType = opd
                else: 
                    param['scope'][index1][index2].mtype = opd #infer symbol type
                    if type(param['scope'][index1][index2].kind) is Parameter:
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[index2] = opd
            if type(opd) is BoolType: return BoolType(), -1, -1, False, False  # 3 change here when copy 
            else: raise TypeMismatchInExpression(ast)
    
    #method:Id
    #param:List[Expr]
    def visitCallExpr(self, ast, param):
        param['FunctionKind'] = True
        functionType, index1, index2, fromFuncExp, fromArrayCell = ast.method.accept(self, param)
        param['FunctionKind'] = False
        if functionType is None: return None, None, None, None, None
        
        if not type(param['scope'][index1][index2].mtype) is MType: raise Undeclared(Function(), ast.method.name)#TypeMismatchInExpression(ast)
        
        symbolInputType = param['scope'][index1][index2].mtype.partype
        if len(symbolInputType) != len(ast.param): raise TypeMismatchInExpression(ast)
        
        for i in range(0, len(symbolInputType)):
            argType, argIndex1, argIndex2, argFromFuncExp, argFromArrayCell = ast.param[i].accept(self, param)
            if argType is None: return None, None, None, None, None
            
            if type(symbolInputType[i]) is VoidType or type(argType) is VoidType: raise TypeMismatchInExpression(ast)
            
            if type(symbolInputType[i]) is Unknown: #parameter is unknown prim
                if type(argType) is Unknown: 
                    return None, None, None, None, None # this will tell the outer statements to raise TypeCannotBeInferred 
                    
                elif type(argType) is ArrayType:
                    if type(argType.eleType) is Unknown: 
                        return None, None, None, None, None #raise TypeMismatchInExpression(ast)? not sure
                    
                elif type(argType) is not VoidType(): 
                    symbolInputType[i] = argType #infer prim type for parameter
                    
                    param['scope'][index1][index2].mtype.partype[i] = symbolInputType[i] #update called function signature
                    if index1 == 0 and index2 == param['currentFuncIndex']: #recursive call => need to update local parameter type (because we are also visiting that function)
                        #current function parameter represented as local variable is always in the the top of the second list
                        #this make the job easier since we don't need to track nested function and their respective parameter in local list
                        param['scope'][1][i] = symbolInputType[i]
                
            elif type(symbolInputType[i]) is ArrayType:#parameter is unknown prim
                if type(symbolInputType[i].eleType) is Unknown:
                    if type(argType) is Unknown: 
                        return None, None, None, None, None #raise TypeMismatchInExpression(ast)? not sure
                        
                    elif type(argType) is ArrayType:
                        if type(argType.eleType) is Unknown: 
                            return None, None, None, None, None
                        elif symbolInputType[i].dimen == argType.dimen: 
                            symbolInputType[i] = argType #infer array type for parameters
                            if index1 == 0 and index2 == param['currentFuncIndex']: #recursive call => need to update local parameter type (because we are also visiting that function)
                                param['scope'][1][i] = symbolInputType[i]
                
            else:#argument is unknown  #My head hurt
                if type(argType) is Unknown:#argument is unknown prim
                    if argFromFuncExp and argFromArrayCell:#ex: calledFunc(foo()[1])
                        print("This should not HAPPEND")
                    #    if type(symbolInputType[i]) is ArrayType: 
                    #        if symbolInputType[i].dimen == param['scope'][argIndex1][argIndex2].mtype.rettype.dimen
                    #            argType = symbolInputType[i]
                    #            param['scope'][argIndex1][argIndex2].mtype.rettype = symbolInputType[i]
                    elif argFromFuncExp:#ex: calledFunc(foo())
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype.rettype = symbolInputType[i]
                    elif argFromArrayCell: #ex: calledFunc(foo[1])
                        if not type(symbolInputType[i]) in [ArrayType, VoidType, Unknown]: 
                            argType = symbolInputType[i]
                            param['scope'][argIndex1][argIndex2].mtype.eleType = symbolInputType[i]
                            if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                                param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2].eleType = symbolInputType[i]
                    else: #ex: calledFunc(foo)
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype = symbolInputType[i]
                        if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                            param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2] = symbolInputType[i]
                            
                    #if type(param['scope'][argIndex1][argIndex2].mtype) is MType:
                                    
                elif type(argType) is ArrayType and type(argType.eleType) is Unknown and type(symbolInputType[i]) is ArrayType and symbolInputType[i].dimen == argType.dimen:#argument is unknown  array
                    if argFromFuncExp and argFromArrayCell:#ex: calledFunc(foo()[1]) #should not happened, unknown array going through index op MUST return an primitive type (assignment pdf 2.5 and http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=130386)
                        print("Function with index op should never return a unknown array (function can only return unknown prim or known array)")
                    elif argFromFuncExp:
                        print("Function should never return a unknown array (function can only return unknown prim or known array)")
                    elif argFromArrayCell: #should not happened, unknown array going through index op MUST return an primitive type (assignment pdf 2.5 and http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=130386)
                        '''
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype.eleType = symbolInputType[i].eleType
                        if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                            param['scope'][0][param['currentFuncIndex']].mtypey.partype[argIndex2].eleType = symbolInputType[i].eleType
                        '''
                    else:
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype = symbolInputType[i]
                        if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                            param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2] = symbolInputType[i]
            
            if not self.typeCompare(symbolInputType[i], argType): raise TypeMismatchInExpression(ast)        
        
        return functionType.rettype, index1, index2, True, fromArrayCell
        
    # name : str
    def visitId(self, ast, param):
        for i in range(len(param['scope']) - 1, -1, -1):
            for j in range(len(param['scope'][i]) - 1, -1, -1):
                if param['scope'][i][j].name == ast.name: 
                    if param['FunctionKind']: 
                        if type(param['scope'][i][j].mtype) is MType: return param['scope'][i][j].mtype, i, j, False, False
                        else: raise Undeclared(Function(), ast.name)
                    else:
                        if not type(param['scope'][i][j].mtype) is MType: return param['scope'][i][j].mtype, i, j, False, False
                        else: raise Undeclared(Identifier(), ast.name)
        raise Undeclared(Function() if param['FunctionKind'] else Identifier(), ast.name)
          
    #arr:Expr
    #idx:List[Expr]
    def visitArrayCell(self, ast, param):
        theType, index1, index2, fromFuncExp, fromArrayCell = ast.arr.accept(self, param)
        
        if theType is None: return None, None, None, None, None
        
        if not type(theType) is ArrayType: raise TypeMismatchInExpression(ast)
        
        #array going through index op MUST return an primitive type or else raise exception (assignment pdf 2.5 and http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=130386)
        #if len(theType.dimen) != len(ast.idx): raise TypeMismatchInExpression(ast) #I will relaxed this constraint for assignment 4
        #if len(theType.dimen) < len(ast.idx): raise TypeMismatchInExpression(ast)
        #if isinstance(ast.arr, ArrayLiteral): raise TypeMismatchInExpression(ast) # is {1,2}[1] allowed?
        
        returnType = ArrayType(theType.eleType, theType.dimen.copy()) #copying ArrayType
        for e in ast.idx:
            eType, eIndex1, eIndex2, eFromFuncExp, eFromArrayCell = e.accept(self, param)
            
            if type(eType) is Unknown:
                eType = IntType()
                if eFromFuncExp and eFromArrayCell:
                    print("This should not happened")
                elif eFromFuncExp:
                    param['scope'][eIndex1][eIndex2].mtype.rettype = eType
                elif eFromArrayCell:
                    param['scope'][eIndex1][eIndex2].mtype.eleType = eType
                    #the inferred id is also parameter of this function =>
                    #need to update current function input type at the corresponding index (same as index of parameter in second scope)
                    if type(param['scope'][eIndex1][eIndex2].kind) is Parameter: 
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[eIndex2].eleType = eType
                else:
                    param['scope'][eIndex1][eIndex2].mtype = eType
                    #the inferred id is also parameter of this function =>
                    #need to update current function input type at the corresponding index (same as index of parameter in second scope)
                    if type(param['scope'][eIndex1][eIndex2].kind) is Parameter: 
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[eIndex2] = eType
            if not type(eType) is IntType: raise TypeMismatchInExpression(ast)
            returnType.dimen = returnType.dimen[1:] #pop 1 dimension from the top after each indexing
            
        if len(returnType.dimen) < 1: returnType = returnType.eleType #no dimension array
        
        return returnType, index1, index2, fromFuncExp, True
    
    #lhs: LHS
    #rhs: Expr
    def visitAssign(self, ast, param):
        #infer left hand side first, http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=131000
        lhs, indexL1, indexL2, fromFuncExp_L, fromArrayCell_L = ast.lhs.accept(self, param)  
        rhs, indexR1, indexR2, fromFuncExp_R, fromArrayCell_R = ast.rhs.accept(self, param)
        
        if lhs is None or rhs is None: raise TypeCannotBeInferred(ast)       
        #if fromFuncExp_L: raise TypeMismatchInStatement(ast) #lhs is from a function call, this may be wrong in the future
        if type(lhs) is VoidType or type(rhs) is VoidType: raise TypeMismatchInStatement(ast)
        
        if type(lhs) is Unknown:
            if fromFuncExp_L and fromArrayCell_L: #should not happend
                #pass #left for future
                if type(rhs) is Unknown: raise TypeCannotBeInferred(ast)
                elif type(rhs) is ArrayType:
                    if type(rhs.eleType) is Unknown: raise TypeCannotBeInferred(ast)#not sure
                    else: raise TypeMismatchInStatement(ast) #not sure
                elif type(rhs) is VoidType: raise TypeMismatchInStatement(ast) #redundant
                else: 
                    lhs = rhs
                    param['scope'][indexL1][indexL2].mtype.rettype.eleType = rhs
                        
            elif fromFuncExp_L:
                #pass #left for future
                if type(rhs) is Unknown: raise TypeCannotBeInferred(ast)
                elif type(rhs) is ArrayType:
                    if type(rhs.eleType) is Unknown: raise TypeCannotBeInferred(ast)#not sure
                    else: raise TypeMismatchInStatement(ast) #not sure
                elif type(rhs) is VoidType: raise TypeMismatchInStatement(ast) #redundant
                else: 
                    lhs = rhs
                    param['scope'][indexL1][indexL2].mtype.rettype = rhs
                
            elif fromArrayCell_L:
                if type(rhs) is Unknown: raise TypeCannotBeInferred(ast)
                elif type(rhs) is ArrayType:
                    if type(rhs.eleType) is Unknown: raise TypeCannotBeInferred(ast)#not sure
                    else: raise TypeMismatchInStatement(ast) #not sure
                elif type(rhs) is VoidType: raise TypeMismatchInStatement(ast) #redundant
                else: 
                    lhs = rhs
                    param['scope'][indexL1][indexL2].mtype.eleType = rhs
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter: 
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = rhs
                        
            else:
                if type(rhs) is Unknown: raise TypeCannotBeInferred(ast)
                elif type(rhs) is ArrayType:
                    if type(rhs.eleType) is Unknown: raise TypeCannotBeInferred(ast)#not sure
                else: 
                    lhs = rhs
                    param['scope'][indexL1][indexL2].mtype = rhs
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter: 
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2] = rhs
                        
        elif type(lhs) is ArrayType and type(lhs.eleType) is Unknown:
            if type(rhs) is Unknown: raise TypeCannotBeInferred(ast) #not sure
            
            elif type(rhs) is ArrayType:
                if type(rhs.eleType) is Unknown: raise TypeCannotBeInferred(ast)
                elif lhs.dimen == rhs.dimen: 
                    lhs = rhs
                    param['scope'][indexL1][indexL2].mtype.eleType = rhs.eleType
                    if type(param['scope'][indexL1][indexL2].kind) is Parameter: 
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexL2].eleType = rhs.eleType
                        
            elif type(rhs) is VoidType: raise TypeMismatchInStatement(ast) #redundant
            
            else: # Unknown Array = scalar type
                raise TypeMismatchInStatement(ast) #not sure
        
        elif type(rhs) is Unknown:
            if fromFuncExp_R and fromArrayCell_R:
                print("Function with index op should never return a unknown array (function can only return unknown prim or known array)")
            elif fromFuncExp_R:
                rhs = lhs
                param['scope'][indexR1][indexR2].mtype.rettype = rhs
            elif fromArrayCell_R: #primitive = a[3]::Unknown =>infer a.eleType = primitive
                rhs = lhs
                param['scope'][indexR1][indexR2].mtype.eleType = rhs
                if type(param['scope'][indexR1][indexR2].kind) is Parameter: #inferred variable is also an parameter
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2].eleType = rhs #infer the input type of current function
            else:
                rhs = lhs
                param['scope'][indexR1][indexR2].mtype = rhs
                if type(param['scope'][indexR1][indexR2].kind) is Parameter: #inferred variable is also an parameter
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs #infer the input type of current function
                        
        elif type(rhs) is ArrayType and rhs.eleType is Unknown:
            if fromFuncExp_R and fromArrayCell_R: #should not happend
                pass
            elif fromFuncExp_R: #should not happend
                pass
            elif fromArrayCell_R: #should not happend
                pass
            else:
                if type(lhs) is ArrayType and lhs.dimen == rhs.dimen:
                    rhs = lhs
                    param['scope'][indexR1][indexR2].mtype = rhs
                    if type(param['scope'][indexR1][indexR2].kind) is Parameter: #inferred variable is also an parameter
                        param['scope'][0][param['currentFuncIndex']].mtype.partype[indexR2] = rhs #infer the input type of current function
                else: raise TypeMismatchInStatement(ast)
        
        if not self.typeCompare(lhs, rhs): raise TypeMismatchInStatement(ast)
    
    
    """Expr is the condition, 
        List[VarDecl] is the list of declaration in the beginning of Then branch, empty list if no declaration
        List[Stmt] is the list of statement after the declaration in Then branch, empty list if no statement
    """
    #ifthenStmt:List[Tuple[Expr,List[VarDecl],List[Stmt]]]
    #elseStmt:Tuple[List[VarDecl],List[Stmt]] # for Else branch, empty list if no Else
    def visitIf(self, ast, param):
        for ifThen in ast.ifthenStmt:
            
            condType, condI, condJ, condFromFuncExp, condFromArrayCell =  ifThen[0].accept(self, param)
            
            if type(condType) is Unknown:
                condType = BoolType()
                if condFromFuncExp and condfromArrayCell: #should not happen, function only return known/unknown primitive or known array. Cannot return unknown array
                    param['scope'][condI][condJ].mtype.rettype.eleType = condType
                
                elif condFromFuncExp:#infer function return type
                    param['scope'][condI][condJ].mtype.rettype = condType
                
                elif condFromArrayCell:#infer eletype of a variable after going through array indexing operation
                    param['scope'][condI][condJ].mtype.eleType = condType
                    if type(param['scope'][condI][condJ].kind) is Parameter:
                        parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                        param['scope'][0][parentFunctionIndex].mtype.partype[condJ].eleType = condType
                
                else:#infer variable ID -> must also check if that ID is parameter
                    param['scope'][condI][condJ].mtype = condType
                    if type(param['scope'][condI][condJ].kind) is Parameter:
                        parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                        param['scope'][0][parentFunctionIndex].mtype.partype[condJ] = condType
            
            if condType is None: raise TypeCannotBeInferred(ast) #somewhere deep inside the condExpre, a type cannot be infer (maybe due to unresolved CallExpr)
            
            if not type(condType) is BoolType: raise TypeMismatchInStatement(ast) #careful here (assignment pdf 2.4)
            
            param['scope'].append([]) #enter a new local scope
            
            for vd in ifThen[1]:
                param['scope'][-1].append(vd.accept(self, param))                
            for st in ifThen[2]:
                st.accept(self, param) # could be changed

            param['scope'].pop() #exit the current local scope
        
        #Else Scope   
        param['scope'].append([]) #enter a new local scope
        
        for vd in ast.elseStmt[0]:
            param['scope'][-1].append(vd.accept(self, param))                
        for st in ast.elseStmt[1]:
            st.accept(self, param) # could be changed

        param['scope'].pop() #exit the current local scope

    #idx1: Id
    #expr1:Expr
    #expr2:Expr
    #expr3:Expr
    #loop: Tuple[List[VarDecl],List[Stmt]]
    def visitFor(self, ast, param):
    
        e1Type, e1I, e1J, e1FromFuncExp, e1FromArrayCell = ast.expr1.accept(self, param) #infer right hand side first, should not matter much because there's only at most 1 error       
        if e1Type is None: raise TypeCannotBeInferred(ast)
        
        idType, idI, idJ, idFromFuncExp, idFromArrayCell = ast.idx1.accept(self, param) #infer left hand side
        if e1Type is None: raise TypeCannotBeInferred(ast) 
        
        if type(idType) is MType: raise TypeMismatchInStatement(ast) #should not happend
        
        if type(idType) is Unknown:
            idType = IntType()
            if idFromFuncExp and idFromArrayCell: print("should not happend") #should not happend            
            elif idFromFuncExp: print("should not happend") #should not happen
            elif idFromArrayCell: print("should not happend") #should not happend, only Id allowed (no array cell)
            else:
                param['scope'][idI][idJ].mtype = idType
                if type(param['scope'][idI][idJ].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[idJ] = idType
        
        if type(e1Type) is Unknown:
            e1Type = IntType()
            if e1FromFuncExp and e1FromArrayCell: print("should not happend") #should not happend            
            elif e1FromFuncExp: #infer function return type
                param['scope'][e1I][e1J].mtype.rettype = e1Type
            elif e1FromArrayCell:#infer eletype of a variable after going through array indexing operation
                param['scope'][e1I][e1J].mtype.eleType = e1Type
                if type(param['scope'][e1I][e1J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e1J].eleType = e1Type
            else:
                param['scope'][e1I][e1J].mtype = e1Type
                if type(param['scope'][e1I][e1J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e1J] = e1Type
                    
        if not (type(idType) is IntType and type(e1Type) is IntType): raise TypeMismatchInStatement(ast)


        e2Type, e2I, e2J, e2FromFuncExp, e2FromArrayCell = ast.expr2.accept(self, param)
        if e2Type is None: raise TypeCannotBeInferred(ast)
        
        if type(e2Type) is Unknown:
            e2Type = BoolType()
            if e2FromFuncExp and e2FromArrayCell: print("should not happend") #should not happend            
            elif e2FromFuncExp: #infer function return type
                param['scope'][e2I][e2J].mtype.rettype = e2Type
            elif e2FromArrayCell:#infer eletype of a variable after going through array indexing operation
                param['scope'][e2I][e2J].mtype.eleType = e2Type
                if type(param['scope'][e2I][e2J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e2J].eleType = e2Type
            else:
                param['scope'][e2I][e2J].mtype = e2Type
                if type(param['scope'][e2I][e2J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e2J] = e2Type
                    
        if not type(e2Type) is BoolType: raise TypeMismatchInStatement(ast)
        
        
        e3Type, e3I, e3J, e3FromFuncExp, e3FromArrayCell = ast.expr3.accept(self, param)
        if e3Type is None: raise TypeCannotBeInferred(ast)
        
        if type(e3Type) is Unknown:
            e3Type = IntType()
            if e3FromFuncExp and e3FromArrayCell: print("should not happend") #should not happend            
            elif e3FromFuncExp: #infer function return type
                param['scope'][e3I][e3J].mtype.rettype = e3Type
            elif e3FromArrayCell:#infer eletype of a variable after going through array indexing operation
                param['scope'][e3I][e3J].mtype.eleType = e3Type
                if type(param['scope'][e3I][e3J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e3J].eleType = e3Type
            else:
                param['scope'][e3I][e3J].mtype = e3Type
                if type(param['scope'][e3I][e3J].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[e3J] = e3Type
                    
        if not type(e3Type) is IntType: raise TypeMismatchInStatement(ast)
        
        #Vardecls and Statements part
        param['scope'].append([]) #enter a new local scope
        
        for vd in ast.loop[0]:
            param['scope'][-1].append(vd.accept(self, param))                
        for st in ast.loop[1]:
            st.accept(self, param) # could be changed

        param['scope'].pop() #exit the current local scope
    
    def visitContinue(self, ast, param):
        return None #No job for you
    
    def visitBreak(self, ast, param):
        return None #No job for you
    
    #expr:Expr # None if no expression
    def visitReturn(self, ast, param):
        if ast.expr is None: #empty return statements
            funcJ = param['currentFuncIndex']
            if type(param['scope'][0][funcJ].mtype.rettype) is Unknown: #infer the return type of current function to VoidType
                param['scope'][0][funcJ].mtype.rettype = VoidType()
            
            if not type(param['scope'][0][funcJ].mtype.rettype) is VoidType: raise TypeMismatchInStatement(ast)
            
        else:
            eType, eI, eJ, eFromFuncExp, eFromArrayCell = ast.expr.accept(self, param)
            funcJ = param['currentFuncIndex']
            
            if eType is None: raise TypeCannotBeInferred(ast)
            
            if type(param['scope'][0][funcJ].mtype.rettype) is VoidType: raise TypeMismatchInStatement(ast) #void return MUST be empty (last clause in pdf 2.4)
            
            if type(eType) is VoidType: raise TypeMismatchInStatement(ast) #void return MUST be empty (last clause in pdf 2.4)
            
            if type(param['scope'][0][funcJ].mtype.rettype) is Unknown: #current function return type is unknown
                if type(eType) is Unknown: raise TypeCannotBeInferred(ast)
                
                elif type(eType) is ArrayType:
                    if type(eType.eleType) is Unknown: raise TypeCannotBeInferred(ast)
                    else: 
                        param['scope'][0][funcJ].mtype.rettype = eType
                else:
                    param['scope'][0][funcJ].mtype.rettype = eType
                    
            elif type(eType) is Unknown:
                eType = param['scope'][0][funcJ].mtype.rettype
                if eFromFuncExp and eFromArrayCell:
                    print("should not happend")
                elif eFromFuncExp:
                    param['scope'][eI][eJ].mtype.rettype = eType
                elif eFromArrayCell:
                    param['scope'][eI][eJ].mtype.eleType = eType
                    if type(param['scope'][eI][eJ].mtype.kind) is Parameter:
                        param['scope'][0][funcJ].mtype.partype[eJ].eleType = eType
                else:
                    param['scope'][eI][eJ].mtype = eType
                    if type(param['scope'][eI][eJ].mtype.kind) is Parameter:
                        param['scope'][0][funcJ].mtype.partype[eJ] = eType
            
            elif type(eType) is ArrayType and type(eType.eleType) is Unknown:
                if eFromFuncExp and eFromArrayCell:
                    print("should not happend")
                elif eFromFuncExp:
                    print("should not happend")
                elif eFromArrayCell:
                    print("should not happend")
                else:
                    if type(param['scope'][0][funcJ].mtype.rettype) is ArrayType and param['scope'][0][funcJ].mtype.rettype.dimen == eType.dimen:
                        eType = param['scope'][0][funcJ].mtype.rettype
                        param['scope'][eI][eJ].mtype = eType
                        if type(param['scope'][eI][eJ].mtype.kind) is Parameter:
                            param['scope'][0][funcJ].mtype.partype[eJ] = eType
            
            if not self.typeCompare(param['scope'][0][funcJ].mtype.rettype, eType): raise TypeMismatchInStatement(ast)#param['scope'])
                
    
    #sl:Tuple[List[VarDecl],List[Stmt]]
    #exp: Expr
    def visitDowhile(self, ast, param): #basically the same as While, only difference is that we read the statementsList first
        #Vardecls and Statements part
        param['scope'].append([]) #enter a new local scope
        
        for vd in ast.sl[0]:
            param['scope'][-1].append(vd.accept(self, param))                
        for st in ast.sl[1]:
            st.accept(self, param) # could be changed
            
        eType, eI, eJ, eFromFuncExp, eFromArrayCell = ast.exp.accept(self, param)
        if eType is None: raise TypeCannotBeInferred(ast)
        
        if type(eType) is Unknown:
            eType = BoolType()
            if eFromFuncExp and eFromArrayCell: print("should not happend") #should not happend            
            elif eFromFuncExp: #infer function return type
                param['scope'][eI][eJ].mtype.rettype = eType
            elif eFromArrayCell:#infer eletype of a variable after going through array indexing operation
                param['scope'][eI][eJ].mtype.eleType = eType
                if type(param['scope'][eI][eJ].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[eJ].eleType = eType
            else:
                param['scope'][eI][eJ].mtype = eType
                if type(param['scope'][eI][eJ].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[eJ] = eType
                    
        if not type(eType) is BoolType: raise TypeMismatchInStatement(ast)

        param['scope'].pop() #exit the current local scope

    #exp: Expr
    #sl:Tuple[List[VarDecl],List[Stmt]]
    def visitWhile(self, ast, param): #basically the same as DoWhile
        eType, eI, eJ, eFromFuncExp, eFromArrayCell = ast.exp.accept(self, param)
        if eType is None: raise TypeCannotBeInferred(ast)
        
        if type(eType) is Unknown:
            eType = BoolType()
            if eFromFuncExp and eFromArrayCell: print("should not happend") #should not happend            
            elif eFromFuncExp: #infer function return type
                param['scope'][eI][eJ].mtype.rettype = eType
            elif eFromArrayCell:#infer eletype of a variable after going through array indexing operation
                param['scope'][eI][eJ].mtype.eleType = eType
                if type(param['scope'][eI][eJ].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[eJ].eleType = eType
            else:
                param['scope'][eI][eJ].mtype = eType
                if type(param['scope'][eI][eJ].kind) is Parameter:
                    parentFunctionIndex = param['currentFuncIndex'] #only the current function that we are visiting have parameter symbol exist in local scope
                    param['scope'][0][parentFunctionIndex].mtype.partype[eJ] = eType
                    
        if not type(eType) is BoolType: raise TypeMismatchInStatement(ast)
        
        #Vardecls and Statements part
        param['scope'].append([]) #enter a new local scope
        
        for vd in ast.sl[0]:
            param['scope'][-1].append(vd.accept(self, param))                
        for st in ast.sl[1]:
            st.accept(self, param) # could be changed

        param['scope'].pop() #exit the current local scope

    #method:Id
    #param:List[Expr]
    def visitCallStmt(self, ast, param):
        param['FunctionKind'] = True
        functionType, index1, index2, fromFuncExp, fromArrayCell = ast.method.accept(self, param)
        param['FunctionKind'] = False
        if functionType is None: raise TypeCannotBeInferred(ast)
        
        if not type(param['scope'][index1][index2].mtype) is MType: raise Undeclared(Function(), ast.method.name)#TypeMismatchInStatement(ast)
        
        symbolInputType = param['scope'][index1][index2].mtype.partype
        if len(symbolInputType) != len(ast.param): raise TypeMismatchInStatement(ast)
        
        for i in range(0, len(symbolInputType)):
            argType, argIndex1, argIndex2, argFromFuncExp, argFromArrayCell = ast.param[i].accept(self, param)
            
            if argType is None: raise TypeCannotBeInferred(ast)
            
            if type(symbolInputType[i]) is VoidType or type(argType) is VoidType: raise TypeMismatchInStatement(ast)
            
            if type(symbolInputType[i]) is Unknown: #parameter is unknown prim
                if type(argType) is Unknown: 
                    raise TypeCannotBeInferred(ast)
                    
                elif type(argType) is ArrayType:
                    if type(argType.eleType) is Unknown: 
                       raise TypeCannotBeInferred(ast) #raise TypeMismatchInExpression(ast)? not sure
                    elif type(argType.eleType) is not VoidType():
                        symbolInputType[i] = argType #infer prim type for parameter
                    
                        param['scope'][index1][index2].mtype.partype[i] = symbolInputType[i] #update called function signature
                        if index1 == 0 and index2 == param['currentFuncIndex']: #recursive call => need to update local parameter type (because we are also visiting that function)
                            #current function parameter represented as local variable is always in the the top of the second list
                            #this make the job easier since we don't need to track nested function and their respective parameter in local list
                            param['scope'][1][i] = symbolInputType[i]
                    
                elif type(argType) is not VoidType(): 
                    symbolInputType[i] = argType #infer prim type for parameter
                    
                    param['scope'][index1][index2].mtype.partype[i] = symbolInputType[i] #update called function signature
                    if index1 == 0 and index2 == param['currentFuncIndex']: #recursive call => need to update local parameter type (because we are also visiting that function)
                        #current function parameter represented as local variable is always in the the top of the second list
                        #this make the job easier since we don't need to track nested function and their respective parameter in local list
                        param['scope'][1][i] = symbolInputType[i]
                
            elif type(symbolInputType[i]) is ArrayType:#parameter is unknown prim
                if type(symbolInputType[i].eleType) is Unknown:
                    if type(argType) is Unknown: 
                        raise TypeCannotBeInferred(ast) #raise TypeMismatchInExpression(ast)? not sure
                        
                    elif type(argType) is ArrayType:
                        if type(argType.eleType) is Unknown: 
                            raise TypeCannotBeInferred(ast)
                        elif symbolInputType[i].dimen == argType.dimen: 
                            symbolInputType[i] = argType #infer array type for parameters
                            if index1 == 0 and index2 == param['currentFuncIndex']: #recursive call => need to update local parameter type (because we are also visiting that function)
                                param['scope'][1][i] = symbolInputType[i]
                
            else:#argument is unknown  #My head hurt
                if type(argType) is Unknown:#argument is unknown prim
                    if argFromFuncExp and argFromArrayCell:#ex: calledFunc(foo()[1])
                        print("This should not HAPPEND")

                    elif argFromFuncExp:#ex: calledFunc(foo())
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype.rettype = symbolInputType[i]
                    elif argFromArrayCell: #ex: calledFunc(foo[1])
                        if not type(symbolInputType[i]) in [ArrayType, VoidType, Unknown]: 
                            argType = symbolInputType[i]
                            param['scope'][argIndex1][argIndex2].mtype.eleType = symbolInputType[i]
                            if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                                param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2].eleType = symbolInputType[i]
                    else: #ex: calledFunc(foo)
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype = symbolInputType[i]
                        if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                            param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2] = symbolInputType[i]
                            
                    #if type(param['scope'][argIndex1][argIndex2].mtype) is MType:
                                    
                elif type(argType) is ArrayType and type(argType.eleType) is Unknown and type(symbolInputType[i]) is ArrayType and symbolInputType[i].dimen == argType.dimen:#argument is unknown  array
                    if argFromFuncExp and argFromArrayCell:#ex: calledFunc(foo()[1]) #should not happened, unknown array going through index op MUST return an primitive type (assignment pdf 2.5 and http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=130386)
                        print("Function with index op should never return a unknown array (function can only return unknown prim or known array)")
                    elif argFromFuncExp:
                        print("Function should never return a unknown array (function can only return unknown prim or known array)")
                    elif argFromArrayCell: #should not happened, unknown array going through index op MUST return an primitive type (assignment pdf 2.5 and http://e-learning.hcmut.edu.vn/mod/forum/discuss.php?d=130386)
                        print("should not happend")
                    else:
                        argType = symbolInputType[i]
                        param['scope'][argIndex1][argIndex2].mtype = symbolInputType[i]
                        if type(param['scope'][argIndex1][argIndex2].kind) is Parameter: #the inferred id is also parameter of this function
                            param['scope'][0][param['currentFuncIndex']].mtype.partype[argIndex2] = symbolInputType[i]                 
            
            if not self.typeCompare(symbolInputType[i], argType): raise TypeMismatchInStatement(ast)
        
        returnType = functionType.rettype
        if type(returnType) is Unknown:
            returnType = VoidType()
            param['scope'][index1][index2].mtype.rettype = returnType
            
        if not type(returnType) is VoidType: raise TypeMismatchInStatement(ast) 
        
        #return returnType, index1, index2, True, fromArrayCell we don't do return in CallStmt
        
    #value:int
    def visitIntLiteral(self, ast, param):
        return IntType(), -1, -1, False, False
        
    #value:float
    def visitFloatLiteral(self, ast, param):
        return FloatType(), -1, -1, False, False
        
    #value:bool  
    def visitBooleanLiteral(self, ast, param):
        return BoolType(), -1, -1, False, False
        
    #value:string
    def visitStringLiteral(self, ast, param):
        return StringType(), -1, -1, False, False
    
    #value:List[Literal]
    def visitArrayLiteral(self, ast, param):
        dimension = [len(ast.value)]
        theType, dontCare1, dontCare2, dontCare3, dontCare4 = ast.value[0].accept(self, param)
        
        if isinstance(theType, ArrayType):
            dimension += theType.dimen
            theType = theType.eleType #going deep into theType           
        return ArrayType(theType, dimension), -1, -1, False, False
        
    def typeCompare(self, t1, t2):
        if type(t1) is type(t2):
            if type(t1) in [IntType, FloatType, BoolType, StringType, VoidType]: return True
            if type(t1) is ArrayType:
                return self.typeCompare(t1.eleType, t2.eleType) and t1.dimen == t2.dimen
            if type(t1) is MType:
                if len(t1.partype) == len(t2.partype):
                #Scala equivalent of forall: https://docs.python.org/3/library/functions.html#any
                    return all(list(map(lambda x, y: self.typeCompare(x, y), t1.partype, t2.partype))) and self.typeCompare(t1.rettype, t2.rettype)
        return False
