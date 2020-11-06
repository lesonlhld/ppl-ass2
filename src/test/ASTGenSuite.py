import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """ 
        output = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("x"),[],IntLiteral(2))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,output,301))
    def test_302(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        x = 3;
                        EndBody.
                """ 
        output = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[None]))])
        self.assertTrue(TestAST.checkASTGen(input,output,302))
    def test_303(self):
        """Created automatically"""
        input = r"""Function: foo
                    Body:
                    EndBody.""" 
        output = Program([FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,output,303))
    def test_304(self):
        """Created automatically"""
        input = r"""Var: arr[2] = {1,2};""" 
        output = Program([VarDecl(Id("arr"),[IntLiteral(2)],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,output,304))
    def test_305(self):
        """Created automatically"""
        input = r"""Var:x;""" 
        output = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,output,305))
    def test_306(self):
        """Created automatically"""
        input = r"""Var:x =5 ;""" 
        output = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,output,306))
    def test_307(self):
        """Created automatically"""
        input = r"""Var:x[12];""" 
        output = Program([VarDecl(Id("x"),[IntLiteral(12)],None)])
        self.assertTrue(TestAST.checkASTGen(input,output,307))
    def test_308(self):
        """Created automatically"""
        input = r"""Var:x[0x13];""" 
        output = Program([VarDecl(Id("x"),[IntLiteral(19)],None)])
        self.assertTrue(TestAST.checkASTGen(input,output,308))
    def test_309(self):
        """Created automatically"""
        input = r"""Var:x[0x12][13]=5;""" 
        output = Program([VarDecl(Id("x"),[IntLiteral(18),IntLiteral(13)],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,output,309))
    def test_310(self):
        """Created automatically"""
        input = r"""Var:x;
        Var: x=12;""" 
        output = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(12))])
        self.assertTrue(TestAST.checkASTGen(input,output,310))
    def test_311(self):
        """Created automatically"""
        input = r"""Var: x[12]={12};""" 
        output = Program([VarDecl(Id("x"),[IntLiteral(12)],ArrayLiteral([IntLiteral(12)]))])
        self.assertTrue(TestAST.checkASTGen(input,output,311))
    def test_312(self):
        """Created automatically"""
        input = r"""Var: arr[5][6] = {1,2}, y[1];""" 
        output = Program([VarDecl(Id("arr"),[IntLiteral(5),IntLiteral(6)],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[IntLiteral(1)],None)])
        self.assertTrue(TestAST.checkASTGen(input,output,312))
    def test_313(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
            Var: x[12]={12};
        EndBody.""" 
        output = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[IntLiteral(12)],ArrayLiteral([IntLiteral(12)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,output,313))
    def test_314(self):
        """Created automatically"""
        input = r"""Var: b = True, c = False;""" 
        output = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,output,314))