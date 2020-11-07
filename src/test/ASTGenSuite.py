import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    
    def test_test_404(self):
        """Created automatically"""
        input = r"""Function: indexop
        Parameter: n
        Body: 
            a[b[4 + foo(2)][b||True]][b[b[1+0x469]]] = a[b[2][b[12E-9]*4]] + 4;
        EndBody.""" 
        expect = Program([FuncDecl(Id("indexop"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("a"),[ArrayCell(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(4),CallExpr(Id("foo"),[IntLiteral(2)]))]),[BinaryOp("||",Id("b"),BooleanLiteral(True))]),ArrayCell(Id("b"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(1),IntLiteral(874))])])]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(ArrayCell(Id("b"),[IntLiteral(2)]),[BinaryOp("*",ArrayCell(Id("b"),[FloatLiteral(12E-9)]),IntLiteral(4))])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_test_401243(self):
        """Created automatically"""
        input = r"""Function: arr
        Body: 
            arr[1][2][3] = 4;
        EndBody.""" 
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    # def test_test_405(self):
    #     """Created automatically"""
    #     input = r"""Function: stmtcallinindex 
    #     Parameter: n
    #     Body: 
    #         a = 4*.4.5\0e-2+arr[4-function("call")];
    #     EndBody.""" 
    #     expect = Program([FuncDecl(Id("stmtcallinindex"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("a"),BinaryOp("+",BinaryOp("\\",BinaryOp("*.",IntLiteral(4),FloatLiteral(4.5)),FloatLiteral(0e-2)),ArrayCell(Id("arr"),[BinaryOp("-",IntLiteral(4),CallExpr(Id("function"),[StringLiteral("call")]))])))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,405))
    # def test_test_407(self):
    #     """Created automatically"""
    #     input = r"""Function: iFElseIFNotElse 
    #     Parameter: n
    #     Body: 
    #         If bool_of_string("True") Then
    #             a = int_of_string (read ());
    #         ElseIf n =/= 1.08 Then
    #             b = float_of_int (a) +. 2.0;
    #         ElseIf False Then
    #             Return n;
    #         EndIf.
    #     EndBody.""" 
    #     expect = 
    # def test_test_407(self):
    #     """Created automatically"""
    #     input = r"""Function: mmmmm
    #     Body: 
    #         Do
    #             While(1) Do
    #             foo (2 + x, 4. \. y);goo ();
    #         EndWhile.
    #         While(1)
    #         EndDo.
    #     EndBody.""" 
    #     expect = ""

    # def test_test_410(self):
    #     """Created automatically"""
    #     input = r"""Function: complexarray
    #         Body: x[124]={"duwat74\r \t", "@#&\n rwFEW54",54412,10.e14, 0.124, 544.0e-6  ,{"xe mau xanh"},"xe mau do"};
    #     EndBody.""" 
    #     expect = Program([FuncDecl(Id("complexarray"),[],([],[Assign(ArrayCell(Id("x"),[IntLiteral(124)]),ArrayLiteral([StringLiteral("duwat74\r \t"),StringLiteral("@#&\n rwFEW54"),IntLiteral(54412),FloatLiteral(10.e14),FloatLiteral(0.124),FloatLiteral(544.0e-6),ArrayLiteral([StringLiteral("xe mau xanh")]),StringLiteral("xe mau do")]))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,410))
    # def test_test_411(self):
    #     """Created automatically"""
    #     input = r"""Function: returnstring
    #         Body:
    #             Return "String'"";
    #         EndBody.""" 
    #     expect = Program([FuncDecl(Id("returnstring"),[],([],[Return(StringLiteral("String'""))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,411))
    # def test_test_412(self):
    #     """Created automatically"""
    #     input = r"""Function: iflongnhau
    #     Parameter: a, b
    #     Body:
    #     Var: id[4412][867][9856][867], stringID[108] = "day la \\ 1 chuoi !!",literal = 120000e-1,  array[2][4] = {{867,445,987},{76,12,744}};
    #         If n > 10 Then
    #             If n <. 20.5 Then Return x;
    #             EndIf.
    #             printStrLn(arg);
    #         Else fact(x);
    #         EndIf.
    #     EndBody.""" 
    #     expect = Program([FuncDecl(Id("iflongnhau"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("id"),[4412,867,9856,867],None),VarDecl(Id("stringID"),[108],StringLiteral("day la \\ 1 chuoi !!")),VarDecl(Id("literal"),[],FloatLiteral(120000e-1)),VarDecl(Id("array"),[2,4],ArrayLiteral([ArrayLiteral([IntLiteral(867),IntLiteral(445),IntLiteral(987)]),ArrayLiteral([IntLiteral(76),IntLiteral(12),IntLiteral(744)])]))],[If([(BinaryOp(">",Id("n"),IntLiteral(10)),[],[If([(BinaryOp("<.",Id("n"),FloatLiteral(20.5)),[],[Return(Id("x"))])],()),CallStmt(Id("printStrLn"),[Id("arg")])])],([],[CallStmt(Id("fact"),[Id("x")])]))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,412))
    # def test_test_417(self):
    #     """Created automatically"""
    #     input = r"""Function: callmore
    #     Body: 
    #         call(var*a,876,.65e-1,arr[4],True,"chuoi~~\n");
    #     EndBody.""" 
    #     expect = Program([FuncDecl(Id("callmore"),[],([],[CallStmt(Id("call"),[BinaryOp("*",Id("var"),Id("a")),IntLiteral(876),FloatLiteral(65e-1),ArrayCell(Id("arr"),[IntLiteral(4)]),BooleanLiteral(True),StringLiteral("chuoi~~\n")])]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,417))
    # def test_test_418(self):
    #     """Created automatically"""
    #     input = r"""Function: precedence 
    #     Body: 
    #         x = -(-15.e-1+(-.45.1*.2.4)*(45+108+a[4]));
    #     EndBody.""" 
    #     expect = Program([FuncDecl(Id("precedence"),[],([],[Assign(Id("x"),UnaryOp("-",BinaryOp("+",UnaryOp("-",FloatLiteral(15.e-1)),BinaryOp("*",BinaryOp("*.",UnaryOp("-.",FloatLiteral(45.1)),FloatLiteral(2.4)),BinaryOp("+",BinaryOp("+",IntLiteral(45),IntLiteral(108)),ArrayCell(Id("a"),[IntLiteral(4)]))))))]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,418))