import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    #1852668 - assignment 4

    #given test cases
    def test_000_int(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_001_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,501))
    
    #-------SELF MADE
    #def test_002(self):
    #    #SIMPLE TEST
    #    input = """Function: main
    #               Parameter: a
    #               Body: 
    #                    print(string_of_int(13));
    #               EndBody."""
    #    expect = "13"
    #    self.assertTrue(TestCodeGen.test(input,expect,502))

#VarDecl Test
    
    #global init test
    
    def test_003(self):
    #test init global integer var 
        input = """
            Var: a = 1;
            Function: main
            Body:
                print(string_of_int(a));
            EndBody.
        """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,503))
    def test_004(self):
    #test init global integer var 2
        input = """
            Var: a = 2;
            Function: main
            Body:
                print(string_of_int(a));
                Return;
            EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,504))
    def test_005(self):
    #test init global float var 
        input = """
            Var: b = 5.0;
            Function: main
            Body:
                print(string_of_float(b));
                Return;
            EndBody.
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,505))
    def test_006(self):
    #test init global bool var 
        input = """
            Var: c = True;
            Function: main
            Body:
                print(string_of_bool(c));
                Return;
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,506))
    def test_007(self):
    #test init global String var 
        input = """
            Var: d = "Hello";
            Function: main
            Body:
                print(d);
                Return;
            EndBody.
        """
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input,expect,507))
    def test_008(self):
    #test init global Single dimension int array var 
        input = """
            Var: x[3] = {1,2,3};
            Function: main
            Body:
                print(string_of_int(x[1]));
                Return;
            EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,508))
    def test_009(self):
    #test init global multi dimension int array var 
        input = """
            Var: x[2][3] = {{1,2,3}, {4,5,6}};
            Function: main
            Body:
                print(string_of_int(x[1][1]));
                Return;
            EndBody.
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,509))
    def test_010(self):
    #test init global multiple primitive var 
        input = """
            Var: x = 100;
            Var: y = 1.0, s = "Phuc";
            Var: z = 5, b = True;
            Function: main
            Body:
                printStrLn(string_of_int(x));
                printStrLn(string_of_float(y));
                printStrLn(string_of_int(z));
                printStrLn(s);
                print(string_of_bool(b));
                Return;
            EndBody.
        """
        expect = "100\n1.0\n5\nPhuc\ntrue"
        self.assertTrue(TestCodeGen.test(input,expect,510))
    def test_011(self):
    #test init global Single dimension float array var 
        input = """
            Var: x = {1.1, 2.2, 3.3};
            Function: main
            Body:
                print(string_of_float(x[0]));
                print(string_of_float(x[1]));
                print(string_of_float(x[2]));
                Return;
            EndBody.
        """
        expect = "1.12.23.3"
        self.assertTrue(TestCodeGen.test(input,expect,511))
    def test_012(self):
    #test init global Single dimension bool array var 
        input = """
            Var: x[2] = {True, False};
            Function: main
            Body:
                print(string_of_bool(x[0]));
                print(string_of_bool(x[1]));
                Return;
            EndBody.
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input,expect,512))
    def test_013(self):
    #test init global Multi dimension float array var 
        input = """
            Var: x = {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}, {7.7, 8.8, 9.9}};
            Function: main
            Body:
                print(string_of_float(x[0][0]));
                print(string_of_float(x[1][1]));
                print(string_of_float(x[2][2]));
                Return;
            EndBody.
        """
        expect = "1.15.59.9"
        self.assertTrue(TestCodeGen.test(input,expect,513))
    def test_014(self):
    #test init global Multi dimension bool array var 
        input = """
            Var: x = {{True, False}, {False,True}};
            Function: main
            Body:
                print(string_of_bool(x[0][0]));
                print(string_of_bool(x[1][1]));
                Return;
            EndBody.
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input,expect,514))
    def test_015(self):
    #test init global Multi dimension string array var 
        input = """
            Var: x = {{"This", " is"}, {" a"," random sentence."}};
            Function: main
            Body:
                print(x[0][0]);
                print(x[0][1]);
                print(x[1][0]);
                print(x[1][1]);
                Return;
            EndBody.
        """
        expect = "This is a random sentence."
        self.assertTrue(TestCodeGen.test(input,expect,515))
    def test_016(self):
    #test init global multi dimension int array var (complex case)
        input = """
            Var: x[2][3] = {{1,2,3}, {4,5,6}};
            Function: main
            Body:
                Var: y[3] = {0, 0, 0};
                y = x[0];
                print(string_of_int(x[1][1]));
                print(string_of_int(y[1]));
                Return;
            EndBody.
        """
        expect = "52"
        self.assertTrue(TestCodeGen.test(input,expect,516))
     
     
    #Local function variable test
    
    def test_017(self):
    #test local int var
        input = """
            Function: main
            Body:
                Var: x = 300;
                print(string_of_int(x));
                Return;
            EndBody.
        """
        expect = "300"
        self.assertTrue(TestCodeGen.test(input,expect,517))
    def test_018(self):
    #test local float var
        input = """
            Function: main
            Body:
                Var: x = 99.75;
                print(string_of_float(x));
                Return;
            EndBody.
        """
        expect = "99.75"
        self.assertTrue(TestCodeGen.test(input,expect,518))
    def test_019(self):
    #test local bool var
        input = """
            Function: main
            Body:
                Var: x = False;
                print(string_of_bool(x));
                Return;
            EndBody.
        """
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,519))
    def test_020(self):
    #test local string var
        input = """
            Function: main
            Body:
                Var: x = "Local var";
                print(x);
                Return;
            EndBody.
        """
        expect = "Local var"
        self.assertTrue(TestCodeGen.test(input,expect,520))
    def test_021(self):
    #test mixed primitive type variable
        input = """
            Function: main
            Body:
                Var: x = "Local var";
                Var: y = 1;
                Var: z = 5.7;
                print(x);
                print(string_of_int(y));
                print(string_of_float(z));
                Return;
            EndBody.
        """
        expect = "Local var15.7"
        self.assertTrue(TestCodeGen.test(input,expect,521))
    def test_022(self):
    #test single dimension int array type local var
        input = """
            Function: main
            Body:
                Var: x = {1,2,3};
                print(string_of_int(x[1]));
                print(string_of_int(x[2]));
                Return;
            EndBody.
        """
        expect = "23"
        self.assertTrue(TestCodeGen.test(input,expect,522))
    def test_023(self):
    #test single dimension float array type local var
        input = """
            Function: main
            Body:
                Var: x = {1e-2,2.0,3.8e7};
                printStrLn(string_of_float(x[0]));
                printStrLn(string_of_float(x[1]));
                print(string_of_float(x[2]));
                Return;
            EndBody.
        """
        expect = "0.01\n2.0\n3.8E7"
        self.assertTrue(TestCodeGen.test(input,expect,523))
    def test_024(self):
    #test single dimension bool array type local var
        input = """
            Function: main
            Body:
                Var: x = {True, False};
                print(string_of_bool(x[0]));
                print(string_of_bool(x[1]));
                Return;
            EndBody.
        """
        expect = "truefalse"
        self.assertTrue(TestCodeGen.test(input,expect,524))
    def test_025(self):
    #test single dimension string array type local var
        input = """
            Function: main
            Body:
                Var: x = {"aaa", "bbb"};
                print(x[0]);
                print(x[1]);
                Return;
            EndBody.
        """
        expect = "aaabbb"
        self.assertTrue(TestCodeGen.test(input,expect,525))
    def test_026(self):
    #test mixed many single dimension array type local var 
        input = """
            Function: main
            Body:
                Var: x = {"aaa", "bbb"};
                Var: y = {1,2,3};
                print(x[0]);
                print(x[1]);
                print(string_of_int(y[1]));
                print(string_of_int(y[2]));
                Return;
            EndBody.
        """
        expect = "aaabbb23"
        self.assertTrue(TestCodeGen.test(input,expect,526))
    def test_027(self):
    #test init multi dimension int array local var 
        input = """          
            Function: main
            Body:
                Var: x = {{200, 5}, {6, 80}};
                print(string_of_int(x[0][0]));
                print(string_of_int(x[0][1]));
                print(string_of_int(x[1][0]));
                print(string_of_int(x[1][1]));
                Return;
            EndBody.
        """
        expect = "2005680"
        self.assertTrue(TestCodeGen.test(input,expect,527))
    def test_028(self):
    #test init Multi dimension float array local var 
        input = """
            Function: main
            Body:
                Var: x = {{1.1, 2.2, 3.3}, {4.4, 5.5, 6.6}, {7.7, 8.8, 9.9}};
                print(string_of_float(x[0][0]));
                print(string_of_float(x[1][1]));
                print(string_of_float(x[2][2]));
                Return;
            EndBody.
        """
        expect = "1.15.59.9"
        self.assertTrue(TestCodeGen.test(input,expect,528))
    def test_029(self):
    #test init Multi dimension bool array local var 
        input = """
            Function: main
            Body:
                Var: x = {{True, False}, {False,True}};
                print(string_of_bool(x[0][0]));
                print(string_of_bool(x[1][1]));
                Return;
            EndBody.
        """
        expect = "truetrue"
        self.assertTrue(TestCodeGen.test(input,expect,529))
    def test_030(self):
    #test init Multi dimension string array local var 
        input = """
            Function: main
            Body:
                Var: x = {{"This", " is"}, {" a"," random sentence."}};
                print(x[0][0]);
                print(x[0][1]);
                print(x[1][0]);
                print(x[1][1]);
                Return;
            EndBody.
        """
        expect = "This is a random sentence."
        self.assertTrue(TestCodeGen.test(input,expect,530))
    def test_031(self):
    #test mixed Multi dimension string array local var 
        input = """
            Function: main
            Body:
                Var: x = {{"This", " is"}, {" a"," random sentence."}};
                Var: y[2][3] = {{200, 5}, {6, 80}};
                
                print(x[0][0]);
                print(x[0][1]);
                print(x[1][0]);
                print(x[1][1]);
                
                print(string_of_int(y[0][0]));
                print(string_of_int(y[0][1]));
                print(string_of_int(y[1][0]));
                print(string_of_int(y[1][1]));
                Return;
            EndBody.
        """
        expect = "This is a random sentence.2005680"
        self.assertTrue(TestCodeGen.test(input,expect,531))
        
    #combined local and global variable tests
    def test_032(self):
    #test mixed primitive type variable
        input = """
            Var: x = "Local var";
            Function: main
            Body:               
                Var: y = 1;
                Var: z = 5.7;
                print(x);
                print(string_of_int(y));
                print(string_of_float(z));
                Return;
            EndBody.
        """
        expect = "Local var15.7"
        self.assertTrue(TestCodeGen.test(input,expect,532))
    def test_033(self):
    #test local scope variable
        input = """
            Var: x = "Local var";
            Function: main
            Body:               
                Var: y = 1;
                Var: x = 5.7;
                print(string_of_int(y));
                print(string_of_float(x));
                Return;
            EndBody.
        """
        expect = "15.7"
        self.assertTrue(TestCodeGen.test(input,expect,533))
    
    def test_063(self):
        #test VERY COMPLEX int array
        input = """          
            Function: main
            Body:
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                print(string_of_int(x[0][0][0]));
                print(string_of_int(x[0][0][1]));
                print(string_of_int(x[0][0][2]));
                print(string_of_int(x[0][1][0]));
                print(string_of_int(x[0][1][1]));
                print(string_of_int(x[0][1][2]));
                print(string_of_int(x[0][2][0]));
                print(string_of_int(x[0][2][1]));
                print(string_of_int(x[0][2][2]));
                
                print(string_of_int(x[1][0][0]));
                print(string_of_int(x[1][0][1]));
                print(string_of_int(x[1][0][2]));
                print(string_of_int(x[1][1][0]));
                print(string_of_int(x[1][1][1]));
                print(string_of_int(x[1][1][2]));
                print(string_of_int(x[1][2][0]));
                print(string_of_int(x[1][2][1]));
                print(string_of_int(x[1][2][2]));
                Return;
            EndBody.
        """
        expect = "20051868079101112915287496081161024"
        self.assertTrue(TestCodeGen.test(input,expect,563))
        
        
#Binary expression test
    def test_034(self):
    #test simple +
        input = """
            Function: main
            Body:               
                print(string_of_int(1+2));
                Return;
            EndBody.
        """
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,534))
    def test_035(self):
    #test simple -
        input = """
            Function: main
            Body:               
                print(string_of_int(4-6));
                Return;
            EndBody.
        """
        expect = "-2"
        self.assertTrue(TestCodeGen.test(input,expect,535))
    def test_036(self):
    #test simple *
        input = """
            Function: main
            Body:               
                print(string_of_int(5*6));
                Return;
            EndBody.
        """
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,536))
    def test_037(self):
    #test simple \
        input = """
            Function: main
            Body:               
                print(string_of_int(101\\20));
                Return;
            EndBody.
        """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,537))
    def test_038(self):
    #test simple +.
        input = """
            Function: main
            Body:               
                print(string_of_float(1.0+.2.0));
                Return;
            EndBody.
        """
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,538))
    def test_039(self):
    #test simple -.
        input = """
            Function: main
            Body:               
                print(string_of_float(4.0-.6.0));
                Return;
            EndBody.
        """
        expect = "-2.0"
        self.assertTrue(TestCodeGen.test(input,expect,539))
    def test_040(self):
    #test simple *.
        input = """
            Function: main
            Body:               
                print(string_of_float(5.0*.6.0));
                Return;
            EndBody.
        """
        expect = "30.0"
        self.assertTrue(TestCodeGen.test(input,expect,540))
    def test_041(self):
    #test simple \.
        input = """
            Function: main
            Body:               
                print(string_of_float(100.0\\.20.0));
                Return;
            EndBody.
        """
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,541))
    def test_042(self):
    #test simple %
        input = """
            Function: main
            Body:               
                print(string_of_int(102%20));
                Return;
            EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,542))
    def test_043(self):
    #test simple ==
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x == 2));
                print(string_of_bool(2 == 2));
                print(string_of_bool(3 == 2));
                Return;
            EndBody.
        """
        expect = "falsetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,543))
    def test_044(self):
    #test simple !=
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x != 2));
                print(string_of_bool(2 != 2));
                print(string_of_bool(3 != 2));
                Return;
            EndBody.
        """
        expect = "truefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,544))
    def test_045(self):
    #test simple <
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x < 2));
                print(string_of_bool(2 < 2));
                print(string_of_bool(3 < 2));
                Return;
            EndBody.
        """
        expect = "truefalsefalse"
        self.assertTrue(TestCodeGen.test(input,expect,545))
    def test_046(self):
    #test simple >
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x > 2));
                print(string_of_bool(2 > 2));
                print(string_of_bool(3 > 2));
                Return;
            EndBody.
        """
        expect = "falsefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,546))
    def test_047(self):
    #test simple <=
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x <= 2));
                print(string_of_bool(2 <= 2));
                print(string_of_bool(3 <= 2));
                Return;
            EndBody.
        """
        expect = "truetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,547))
    def test_048(self):
    #test simple >=
        input = """
            Function: main
            Body:
                Var: x = 1;
                print(string_of_bool(x >= 2));
                print(string_of_bool(2 >= 2));
                print(string_of_bool(3 >= 2));
                Return;
            EndBody.
        """
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,548))
    def test_049(self):
    #test simple =/=
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                print(string_of_bool(x =/= 2.0));
                print(string_of_bool(2e0 =/= 2.0));
                print(string_of_bool(3.0 =/= 2.0));
                Return;
            EndBody.
        """
        expect = "truefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,549))
    def test_050(self):
    #test simple <.
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                print(string_of_bool(x <. 2.0));
                print(string_of_bool(2.0 <. 2.0));
                print(string_of_bool(3.0 <. 2.0));
                Return;
            EndBody.
        """
        expect = "truefalsefalse"
        self.assertTrue(TestCodeGen.test(input,expect,550))
    def test_051(self):
    #test simple >.
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                print(string_of_bool(x >. 2.0));
                print(string_of_bool(2.0 >. 2.0));
                print(string_of_bool(3.0 >. 2.0));
                Return;
            EndBody.
        """
        expect = "falsefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,551))
    def test_052(self):
    #test simple <=.
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                print(string_of_bool(x <=. 2.0));
                print(string_of_bool(2.0 <=. 2.0));
                print(string_of_bool(3.0 <=. 2.0));
                Return;
            EndBody.
        """
        expect = "truetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,552))
    def test_053(self):
    #test simple >=.
        input = """
            Function: main
            Body:
                Var: x = 1.0;
                print(string_of_bool(x >=. 2.0));
                print(string_of_bool(2.0 >=. 2.0));
                print(string_of_bool(3.0 >=. 2.0));
                Return;
            EndBody.
        """
        expect = "falsetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,553))
        
    def test_054(self):
    #test simple &&
        input = """
            Function: main
            Body:
                Var: x = True, y = False;
                print(string_of_bool(x && x));
                print(string_of_bool(x && y));
                print(string_of_bool(y && x));
                print(string_of_bool(y && y));
                Return;
            EndBody.
        """
        expect = "truefalsefalsefalse"
        self.assertTrue(TestCodeGen.test(input,expect,554))
    def test_055(self):
    #test simple ||
        input = """
            Function: main
            Body:
                Var: x = True, y = False;
                print(string_of_bool(x || x));
                print(string_of_bool(x || y));
                print(string_of_bool(y || x));
                print(string_of_bool(y || y));
                Return;
            EndBody.
        """
        expect = "truetruetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,555))
    
    #SHORT CUIRCUIT EVALUATION TEST
    def test_056(self):
    #test short circuit evaluation of && 
        input = """
            Function: main
            Body:
                Var: x = False;
                print(string_of_bool(foo() && x));
                print(string_of_bool(x && foo()));
                Return;
            EndBody.
            
            Function: foo
            Body:
                print("TEST");
                Return True;
            EndBody.
        """
        expect = "TESTfalsefalse"
        self.assertTrue(TestCodeGen.test(input,expect,556))
    def test_057(self):
    #test short circuit evaluation of ||
        input = """
            Function: main
            Body:
                Var: x = True;
                print(string_of_bool(foo() || x));
                print(string_of_bool(x || foo()));
                Return;
            EndBody.
            
            Function: foo
            Body:
                print("TEST");
                Return False;
            EndBody.
        """
        expect = "TESTtruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,557))
    
    def test_058(self):
    #complex binary op test
        input = """
            Function: main
            Body:
                Var: x = 1, y = 2;
                printStrLn(string_of_int(10 + 2 - 3 * 4 \\ 2));
                print(string_of_int(10 + (2 - 3) * 4 \\ 2));
                Return;
            EndBody.
        """
        expect = "6\n8"
        self.assertTrue(TestCodeGen.test(input,expect,558))
    def test_059(self):
    #complex binary op test 2
        input = """
            Function: main
            Body:
                print(string_of_bool((foo2() && foo()) || (foo() && foo2())));
                Return;
            EndBody.
            
            Function: foo
            Body:
                print("foo(),");
                Return True;
            EndBody.
            Function: foo2
            Body:
                print("foo2(),");
                Return False;
            EndBody.
        """
        expect = "foo2(),foo(),foo2(),false"
        self.assertTrue(TestCodeGen.test(input,expect,559))


#Unary expression test
    def test_060(self):
    #test simple negate op
        input = """
            Function: main
            Body:
                Var: x = 99;
                print(string_of_int(-x));
                Return;
            EndBody.
        """
        expect = "-99"
        self.assertTrue(TestCodeGen.test(input,expect,560))
    def test_061(self):
    #test simple negate op float
        input = """
            Function: main
            Body:
                Var: x = 4.3;
                print(string_of_float(-.x));
                Return;
            EndBody.
        """
        expect = "-4.3"
        self.assertTrue(TestCodeGen.test(input,expect,561))
    def test_062(self):
    #test simple ! op
        input = """
            Function: main
            Body:
                Var: x = False;
                print(string_of_bool(!x));
                Return;
            EndBody.
        """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,562))
    def test_064(self):
    #test complex unary op test
        input = """
            Function: main
            Body:
                Var: x = False;
                print(string_of_bool(!(float_to_int(-7) >. -.7.5)));
                print(string_of_bool(!(float_to_int(-7) <. -.7.5)));
                Return;
            EndBody.
        """
        expect = "falsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,564))
    def test_065(self):
    #test simple array cell with expression index
        input = """
            Function: main
            Body:
                Var: x = {{1,2},{3,4}};
                print(string_of_int(x[2-1][--1]));
                Return;
            EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,565))
    def test_066(self):
    #test complex array cell
        input = """
            Function: main
            Body:
                Var: x = {{1,2},{3,4}};
                print(string_of_int(x[-int_of_float(-.1.0)][--1]));
                Return;
            EndBody.
        """
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,566))

#Assignment Test
    def test_067(self):
    #test simple assignment
        input = """
            Function: main
            Body:
                Var: x = 99;
                x = 10;
                print(string_of_int(x));
                Return;
            EndBody.
        """
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,567))
    def test_068(self):
    #test simple float assignment
        input = """
            Function: main
            Body:
                Var: x = 99.7;
                x = 10.1;
                print(string_of_float(x));
                Return;
            EndBody.
        """
        expect = "10.1"
        self.assertTrue(TestCodeGen.test(input,expect,568))
    def test_069(self):
    #test simple bool and string assignment
        input = """
            Function: main
            Body:
                Var: x = True, y = "";
                x = False;
                y = "Hello";
                print(string_of_bool(x));
                print(y);
                Return;
            EndBody.
        """
        expect = "falseHello"
        self.assertTrue(TestCodeGen.test(input,expect,569))
    def test_070(self):
    #test simple assignment lhs and rhs
        input = """
            Function: main
            Body:
                Var: x = 2, y = 3, temp = 0;
                temp = x;
                x = y;
                y = temp;
                print(string_of_int(x));
                print(string_of_int(y));
                Return;
            EndBody.
        """
        expect = "32"
        self.assertTrue(TestCodeGen.test(input,expect,570))
    def test_071(self):
    #test complex assignment increment expression
        input = """
            Function: main
            Body:
                Var: x = 64;
                x = x + 1;
                print(string_of_int(x));
                Return;
            EndBody.
        """
        expect = "65"
        self.assertTrue(TestCodeGen.test(input,expect,571))

#If statement Part
    def test_072(self):
    #test simple if
        input = """
            Function: main
            Body:
                If True Then
                    print("TRUE");
                EndIf.
                Return;
            EndBody.
        """
        expect = "TRUE"
        self.assertTrue(TestCodeGen.test(input,expect,572))
    def test_073(self):
    #test simple if else
        input = """
            Function: main
            Body:
                Var: x = True;
                If !x Then
                    print("1");
                Else
                    print("2");
                EndIf.
                Return;
            EndBody.
        """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,573))
    def test_074(self):
    #test simple if elseif else
        input = """
            Function: main
            Body:
                Var: x = 1, y = 2;
                If x != 1 Then
                    print("1");
                ElseIf y == 2 Then
                    print("HERE");
                Else
                    print("2");
                EndIf.
                Return;
            EndBody.
        """
        expect = "HERE"
        self.assertTrue(TestCodeGen.test(input,expect,574))
    def test_075(self):
    #test nested if
        input = """
            Function: main
            Body:
                Var: x = 1, y = 2;
                If x == 1 Then
                    print("1");
                    If y == 2 Then
                        print("HERE");
                    EndIf.
                Else
                    print("2");
                EndIf.
                Return;
            EndBody.
        """
        expect = "1HERE"
        self.assertTrue(TestCodeGen.test(input,expect,575))
    def test_076(self):
    #test if scope
        input = """
            Function: main
            Body:
                Var: x = 1, y = 2;
                If x == 1 Then
                    Var: x = 2;
                    print(string_of_int(x));
                    If x == 2 Then
                        print("HERE");
                    EndIf.
                Else
                    print("abc");
                EndIf.
                Return;
            EndBody.
        """
        expect = "2HERE"
        self.assertTrue(TestCodeGen.test(input,expect,576))
    def test_077(self):
    #test else scope
        input = """
            Function: main
            Body:
                Var: x = 3, y = 2;
                If x == 1 Then
                    Var: x = 2;
                    print(string_of_int(x));
                    If x == 2 Then
                        print("A");
                    EndIf.
                Else
                    Var: y = 3;
                    If y == 2 Then
                        print("B");
                    Else
                        print("C");
                    EndIf.
                    print("abc");
                EndIf.
                Return;
            EndBody.
        """
        expect = "Cabc"
        self.assertTrue(TestCodeGen.test(input,expect,577))
    def test_078(self):
    #test deep nested if scope
        input = """
            Function: main
            Body:
                Var: x = 1, y = 2;
                print(string_of_int(x));
                If x == 1 Then
                    Var: x = 2;
                    print(string_of_int(x));
                    If x == 2 Then
                        Var: x = 3;
                        print(string_of_int(x));
                        If x == 3 Then
                            Var: x = 4;
                            print(string_of_int(x));
                        EndIf.
                    EndIf.
                EndIf.
                Return;
            EndBody.
        """
        expect = "1234"
        self.assertTrue(TestCodeGen.test(input,expect,578))
        
#For statement Part
    def test_079(self):
    #test simple for
        input = """
            Function: main
            Body:
                Var: i = 1;
                For(i = 0, i < 10, 2) Do
                    print(string_of_int(i));
                EndFor.
                Return;
            EndBody.
        """
        expect = "02468"
        self.assertTrue(TestCodeGen.test(input,expect,579))
    def test_080(self):
        #test nested for
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 100;                
                For(i = 0, i < length, 1) Do
                    Var: j = 100;
                    For(j = 0, j < width, 1) Do
                        Var: k = 100;
                        For(k = 0, k < height, 1) Do
                            print(string_of_int(x[i][j][k]));
                        EndFor.
                    EndFor.
                EndFor.
                
                Return;
            EndBody.
        """
        expect = "20051868079101112915287496081161024"
        self.assertTrue(TestCodeGen.test(input,expect,580))
    def test_081(self):
        #test reversed for
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 100;                
                For(i = length - 1, i >= 0, -1) Do
                    Var: j = 100;
                    For(j = width - 1, j >= 0, -1) Do
                        Var: k = 100;
                        For(k = height - 1, k >= 0, -1) Do
                            print(string_of_int(x[i][j][k]));
                        EndFor.
                    EndFor.
                EndFor.
                
                Return;
            EndBody.
        """
        expect = "10241681604972815912111079806185200"
        self.assertTrue(TestCodeGen.test(input,expect,581))
    def test_082(self):
        #test nested for continue
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                Var: i = 100;                
                For(i = 0, i < length, 1) Do
                    Var: j = 100;
                    For(j = 0, j < width, 1) Do
                        Var: k = 100;
                        If j == 1 Then
                            Continue;
                        EndIf.
                        For(k = 0, k < height, 1) Do
                            If k == 1 Then
                                Continue;
                            EndIf.
                            print(string_of_int(x[i][j][k]));
                        EndFor.
                    EndFor.
                EndFor.
                
                Return;
            EndBody.
        """
        expect = "200181012928811024"
        self.assertTrue(TestCodeGen.test(input,expect,582))
    def test_083(self):
        #test nested for break
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                Var: i = 100;                
                For(i = 0, i < length, 1) Do
                    Var: j = 100;
                    For(j = 0, j < width, 1) Do
                        Var: k = 100;
                        If j == 2 Then
                            Break;
                        EndIf.
                        For(k = 0, k < height, 1) Do
                            If k == 1 Then
                                Break;
                            EndIf.
                            print(string_of_int(x[i][j][k]));
                        EndFor.
                    EndFor.
                EndFor.
                
                Return;
            EndBody.
        """
        expect = "200697"
        self.assertTrue(TestCodeGen.test(input,expect,583))
    def test_084(self):
        #test nested for combining continue and break
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                Var: i = 100;                
                For(i = 0, i < length, 1) Do
                    Var: j = 100;
                    For(j = 0, j < width, 1) Do
                        Var: k = 100;
                        If j == 1 Then
                            Break;
                        EndIf.
                        For(k = 0, k < height, 1) Do
                            If k == 1 Then
                                Continue;
                            EndIf.
                            print(string_of_int(x[i][j][k]));
                        EndFor.
                    EndFor.
                EndFor.
                
                Return;
            EndBody.
        """
        expect = "20018928"
        self.assertTrue(TestCodeGen.test(input,expect,584))
    def test_085(self):
    #test for local scope
        input = """
            Function: main
            Body:
                Var: i = 1;
                Var: j = 1;
                For(i = 0, i < 10, 2) Do
                    Var: i = 7;
                    print(string_of_int(i));
                    For(j = 0, j < 2, 1) Do
                        Var: j = 8;
                        print(string_of_int(j));
                    EndFor.                   
                EndFor.
                Return;
            EndBody.
        """
        expect = "788788788788788"
        self.assertTrue(TestCodeGen.test(input,expect,585))
        
#While statement Part
    def test_086(self):
    #test simple while
        input = """
            Function: main
            Body:
                Var: i = 0;
                While i < 10 Do
                    print(string_of_int(i));
                    i = i + 2;
                EndWhile.
                Return;
            EndBody.
        """
        expect = "02468"
        self.assertTrue(TestCodeGen.test(input,expect,586))
    def test_087(self):
        #test nested while
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 0;                
                While i < length Do
                    Var: j = 0;
                    i = i + 1;
                    While j < width Do
                        Var: k = 0;
                        j = j + 1;
                        While k < height Do
                            k = k + 1;
                            print(string_of_int(x[i-1][j-1][k-1]));
                        EndWhile.
                    EndWhile.
                EndWhile.
                
                Return;
            EndBody.
        """
        expect = "20051868079101112915287496081161024"
        self.assertTrue(TestCodeGen.test(input,expect,587))
    def test_088(self):
        #test nested while with continue and break
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 0;                
                While i < length Do
                    Var: j = 0;
                    i = i + 1;
                    While j < width Do
                        Var: k = 0;
                        j = j + 1;
                        If j == 1 Then
                            Continue;
                        EndIf.
                        While k < height Do
                            k = k + 1;
                            If k == 2 Then
                                Break;
                            EndIf.
                            print(string_of_int(x[i-1][j-1][k-1]));
                        EndWhile.
                    EndWhile.
                EndWhile.
                
                Return;
            EndBody.
        """
        expect = "610781"
        self.assertTrue(TestCodeGen.test(input,expect,588))
    def test_089(self):
    #test nested while local enviroment
        input = """
            Var: i = 0, j = 0;
            Function: main
            Body:                
                While i < 10 Do
                    Var: i = 6;
                    
                    print(string_of_int(i));
                    While j < 2 Do
                        Var: j = 8;
                        print(string_of_int(j));
                        jIncrease(1);
                    EndWhile.
                    
                    iIncrease(2);
                    j = 0;
                EndWhile.
                
                Return;
            EndBody.
            
            Function: iIncrease
            Parameter: n
            Body:
                i = i + n;
                Return;
            EndBody.
            
            Function: jIncrease
            Parameter: n
            Body:
                j = j + n;
                Return;
            EndBody.
        """
        expect = "688688688688688"
        self.assertTrue(TestCodeGen.test(input,expect,589))

#Dowhile statement Part
    def test_090(self):
    #test simple Dowhile
        input = """
            Function: main
            Body:
                Var: i = 0;
                Do
                    print(string_of_int(i));
                    i = i + 2;
                While i < 10
                EndDo.
                Return;
            EndBody.
        """
        expect = "02468"
        self.assertTrue(TestCodeGen.test(input,expect,590))
    def test_091(self):
    #test Dowhile must run atleast once
        input = """
            Function: main
            Body:
                Do
                    print("HERE");
                While False
                EndDo.
                Return;
            EndBody.
        """
        expect = "HERE"
        self.assertTrue(TestCodeGen.test(input,expect,591))
    def test_092(self):
        #test nested Dowhile
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 0;                
                Do
                    Var: j = 0;
                    i = i + 1;
                    
                    Do
                        Var: k = 0;
                        j = j + 1;
                        
                        Do
                            k = k + 1;
                            print(string_of_int(x[i-1][j-1][k-1]));
                        While k < height 
                        EndDo.
                        
                    While j < width 
                    EndDo.
                    
                While i < length 
                EndDo.
                
                Return;
            EndBody.
        """
        expect = "20051868079101112915287496081161024"
        self.assertTrue(TestCodeGen.test(input,expect,592))
    def test_093(self):
        #test nested Dowhile with Break and Continue
        input = """          
            Function: main
            Body:
                Var: length = 2, width = 3, height = 3;
                Var: x = {{{200, 5, 18}, {6, 80, 79}, {10, 11, 12}}, {{9, 15, 28}, {7, 49, 60}, {81, 16, 1024}}};
                
                Var: i = 0;                
                Do
                    Var: j = 0;
                    i = i + 1;                   
                    Do
                        Var: k = 0;                        
                        If j == 1 Then
                            j = j + 1;
                            Continue;
                        EndIf. 
                        j = j + 1;
                        Do
                            If k == 1 Then
                                Break;
                            EndIf.
                            k = k + 1;
                            print(string_of_int(x[i-1][j-1][k-1]));
                        While k < height 
                        EndDo.
                        
                    While j < width 
                    EndDo.
                    
                While i < length 
                EndDo.
                
                Return;
            EndBody.
        """
        expect = "20010981"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    def test_094(self):
    #test nested Dowhile local enviroment
        input = """
            Var: i = 0, j = 0;
            Function: main
            Body:                
                Do
                    Var: i = 6;
                    
                    print(string_of_int(i));
                    Do
                        Var: j = 8;
                        print(string_of_int(j));
                        jIncrease(1);
                    While j < 2 
                    EndDo.
                    
                    iIncrease(2);
                    j = 0;
                While i < 10 
                EndDo.
                
                Return;
            EndBody.
            
            Function: iIncrease
            Parameter: n
            Body:
                i = i + n;
                Return;
            EndBody.
            
            Function: jIncrease
            Parameter: n
            Body:
                j = j + n;
                Return;
            EndBody.
        """
        expect = "688688688688688"
        self.assertTrue(TestCodeGen.test(input,expect,594))
        

#FuncDecl, CallStmt, CallExpr, Return Part
    def test_095(self):
    #test recursive call
        input = """
        Function: main 
        Body:
            print(string_of_int(fac(6)));
            print(string_of_int(fac(0)));
            print(string_of_int(fac(1)));
            Return 0;
        EndBody.

        Function: fac
        Parameter: x
        Body:
            If x <= 1 Then
                Return 1;
            EndIf.
            Return x*fac(x-1);
        EndBody.
        """
        expect = "72011"
        self.assertTrue(TestCodeGen.test(input,expect,595))
    def test_096(self):
    #test primitive parameter pass-by-value
        input = """
        Function: main 
        Body:
            Var: iA = 5, iB = 7;
            Var: fA = 1.3, fB = 2.8;
            Var: bA = True, bB = False;
            Var: sA = "A", sB = "B";
            
            print("iA = ");
            print(string_of_int(iA));
            print(", iB = ");
            printStrLn(string_of_int(iB));
            
            print("bA = ");
            print(string_of_bool(bA));
            print(", bB = ");
            printStrLn(string_of_bool(bB));
            
            print("fA = ");
            print(string_of_float(fA));
            print(", fB = ");
            printStrLn(string_of_float(fB));
            
            print("sA = ");
            print(sA);
            print(", sB = ");
            printStrLn(sB);
            
            swapInt(iA, iB);
            swapBool(bA, bB);
            swapFloat(fA, fB);
            swapString(sA, sB);
            
            print("iA = ");
            print(string_of_int(iA));
            print(", iB = ");
            printStrLn(string_of_int(iB));
            
            print("bA = ");
            print(string_of_bool(bA));
            print(", bB = ");
            printStrLn(string_of_bool(bB));
            
            print("fA = ");
            print(string_of_float(fA));
            print(", fB = ");
            printStrLn(string_of_float(fB));
            
            print("sA = ");
            print(sA);
            print(", sB = ");
            printStrLn(sB);
            
            Return 0;
        EndBody.

        Function: swapInt
        Parameter: x, y
        Body:
            Var: temp = 0;
            temp = x;
            x = y;
            y = temp;
            Return;
        EndBody.
        
        Function: swapBool
        Parameter: x, y
        Body:
            Var: temp = False;
            temp = x;
            x = y;
            y = temp;
            Return;
        EndBody.
        
        Function: swapFloat
        Parameter: x, y
        Body:
            Var: temp = 0.0;
            temp = x;
            x = y;
            y = temp;
            Return;
        EndBody.
        
        Function: swapString
        Parameter: x, y
        Body:
            Var: temp = "";
            temp = x;
            x = y;
            y = temp;
            Return;
        EndBody.
        """
        expect = "iA = 5, iB = 7\nbA = true, bB = false\nfA = 1.3, fB = 2.8\nsA = A, sB = B\niA = 5, iB = 7\nbA = true, bB = false\nfA = 1.3, fB = 2.8\nsA = A, sB = B\n"
        self.assertTrue(TestCodeGen.test(input,expect,596))
        
    def test_097(self):
    #test array type parameter passing
        input = """
        Function: main 
        Body:
            Var: iA = {5, 7};
            Var: fA = {1.3, 2.8};
            Var: bA = {True, False};
            Var: sA = {"A", "B"};
            
            print("iA[0] = ");
            print(string_of_int(iA[0]));
            print(", iA[1] = ");
            printStrLn(string_of_int(iA[1]));
            
            print("bA[0] = ");
            print(string_of_bool(bA[0]));
            print(", bA[1] = ");
            printStrLn(string_of_bool(bA[1]));
            
            print("fA[0] = ");
            print(string_of_float(fA[0]));
            print(", fA[1] = ");
            printStrLn(string_of_float(fA[1]));
            
            print("sA[0] = ");
            print(sA[0]);
            print(", sA[1] = ");
            printStrLn(sA[1]);
            
            swapInt(iA, 0, 1);
            swapBool(bA, 0, 1);
            swapFloat(fA, 0, 1);
            swapString(sA, 0, 1);
            
            print("iA[0] = ");
            print(string_of_int(iA[0]));
            print(", iA[1] = ");
            printStrLn(string_of_int(iA[1]));
            
            print("bA[0] = ");
            print(string_of_bool(bA[0]));
            print(", bA[1] = ");
            printStrLn(string_of_bool(bA[1]));
            
            print("fA[0] = ");
            print(string_of_float(fA[0]));
            print(", fA[1] = ");
            printStrLn(string_of_float(fA[1]));
            
            print("sA[0] = ");
            print(sA[0]);
            print(", sA[1] = ");
            printStrLn(sA[1]);
            
            Return 0;
        EndBody.

        Function: swapInt
        Parameter: x[2], a, b
        Body:
            Var: temp = 0;
            temp = x[a];
            x[a] = x[b];
            x[b] = temp;
            Return;
        EndBody.
        
        Function: swapBool
        Parameter: x[2], a, b
        Body:
            Var: temp = False;
            temp = x[a];
            x[a] = x[b];
            x[b] = temp;
            Return;
        EndBody.
        
        Function: swapFloat
        Parameter: x[2], a, b
        Body:
            Var: temp = 0.0;
            temp = x[a];
            x[a] = x[b];
            x[b] = temp;
            Return;
        EndBody.
        
        Function: swapString
        Parameter: x[2], a, b
        Body:
            Var: temp = "";
            temp = x[a];
            x[a] = x[b];
            x[b] = temp;
            Return;
        EndBody.
        """
        expect = "iA[0] = 5, iA[1] = 7\nbA[0] = true, bA[1] = false\nfA[0] = 1.3, fA[1] = 2.8\nsA[0] = A, sA[1] = B\niA[0] = 7, iA[1] = 5\nbA[0] = false, bA[1] = true\nfA[0] = 2.8, fA[1] = 1.3\nsA[0] = B, sA[1] = A\n"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    def test_098(self):
    #Calculator
        input = """
        Var: a = 81;
        Var: b = 67;
        Function: main 
        Body: 
            print("a = ");
            printStrLn(string_of_int(a));
            print("b = ");
            printStrLn(string_of_int(b));
            print("a + b = ");
            print(string_of_int(sum(a, b)));
            Return 0;
        EndBody.
        
        ** Document
           input:
             a: int type
             b: int type
           return:
           sum of a + b: int type
        **
        Function: sum
        Parameter: x,y
        Body:
            Return x + y;
        EndBody.
        """
        expect = "a = 81\nb = 67\na + b = 148"
        self.assertTrue(TestCodeGen.test(input,expect,598))
    def test_099(self):
    #Power function
        input = """
        Var: a = 3;
        Var: b = 4;
        Function: main 
        Body: 
            print("a = ");
            printStrLn(string_of_int(a));
            print("b = ");
            printStrLn(string_of_int(b));
            print("a^b = ");
            print(string_of_int(power(a, b)));
            Return 0;
        EndBody.

        Function: power
        Parameter: x,y
        Body:
            Var: r = 1, i = 0;
            For(i = 0, i < y, 1) Do
                r = r * x;
            EndFor.
            Return r;
        EndBody.
        """
        expect = "a = 3\nb = 4\na^b = 81"
        self.assertTrue(TestCodeGen.test(input,expect,599))
    def test_099b(self):
    #2x2 matrix (test function returning an array)
        input = """
        Var: a = 3;
        Var: b = 4;
        Var: c = 5;
        Var: d = 6;
        Function: main 
        Body: 
            Var: matrix = {{0, 0},{0, 0}};
            print("Creating 2x2 matrix:\\n");
            print("a\\tb\\nc\\td\\n");
            print("a = ");
            printStrLn(string_of_int(a));
            print("b = ");
            printStrLn(string_of_int(b));
            print("c = ");
            printStrLn(string_of_int(c));
            print("d = ");
            printStrLn(string_of_int(d));
            
            matrix = matrix_2x2(a, b, c, d);
            print("m[0][0] = ");
            printStrLn(string_of_int(matrix[0][0]));
            print("m[0][1] = ");
            printStrLn(string_of_int(matrix_2x2(a, b, c, d)[0][1]));
            print("m[1][0] = ");
            printStrLn(string_of_int(matrix[1][0]));
            print("m[1][1] = ");
            print(string_of_int(matrix_2x2(a, b, c, d)[1][1]));
            
            Return;
        EndBody.
        
        Function: matrix_2x2
        Parameter: a00, a01, a10, a11
        Body:
        Var: m[2][2] = {{0,0},{0,0}};
            m[0][0] = a00;
            m[0][1] = a01;
            m[1][0] = a10;
            m[1][1] = a11;
            Return m;
        EndBody.
        """
        expect = "Creating 2x2 matrix:\na\tb\nc\td\na = 3\nb = 4\nc = 5\nd = 6\nm[0][0] = 3\nm[0][1] = 4\nm[1][0] = 5\nm[1][1] = 6"
        self.assertTrue(TestCodeGen.test(input,expect,502))