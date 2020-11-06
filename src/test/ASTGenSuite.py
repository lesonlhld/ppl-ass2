import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x;"""
    #     expect = Program([VarDecl(Id("x"),[],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,300))

    # def test_simple_program1(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x =5 ;"""
    #     expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,301))
    
    # def test_simple_program2(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x[12];"""
    #     expect = Program([VarDecl(Id("x"),[IntLiteral(12)],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,302))
    
    # def test_simple_program3(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x[0x13];"""
    #     expect = Program([VarDecl(Id("x"),[IntLiteral(0x13)],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,303))
    
    # def test_simple_program4(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x[0x12][13]=5;"""
    #     expect = Program([VarDecl(Id("x"),[IntLiteral(0x12),IntLiteral(13)],IntLiteral(5))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,304))
 
    # def test_simple_program5(self):
    #     """Simple program: int main() {} """
    #     input = """Var:x;
    #     Var: x=12;"""
    #     expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(12))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    # def test_simple_program6(self):
    #     """Simple program: int main() {} """
    #     input = """Var: x[12]={12};"""
    #     expect = Program([VarDecl(Id("x"),[IntLiteral(12)],ArrayLiteral([IntLiteral(12)]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,306))
    
    # def test_simple_program7(self):
    #     """Simple program: int main() {} """
    #     input = """Var: arr[5][6] = {1,2}, y[1];"""
    #     expect = Program([VarDecl(Id("arr"),[IntLiteral(5),IntLiteral(6)],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[IntLiteral(1)],None)])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,307))

    # def test_simple_program8(self):
    #     """Simple program: int main() {} """
    #     input = """Function: foo 
    #     Parameter: n 
    #     Body: 
    #         Var: x[12]={12};
    #     EndBody."""
    #     expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[IntLiteral(12)],ArrayLiteral([IntLiteral(12)]))],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,308))
        
    # def test_simple_program9(self):
    #     """Simple program: int main() {} """
    #     input = """Var: b = True, c = False;"""
    #     expect = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
    #     print(expect)
    #     self.assertTrue(TestAST.checkASTGen(input,expect,309))

    # def test_func_declare(self):
    #     """Simple program: int main() {} """
    #     input = """ Function: foo
    #                     Parameter: a
    #                     Body:
    #                     Var: x = 2;
    #                     EndBody.
    #             """
    #     expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],(([VarDecl(Id("x"),[],IntLiteral(2))],[])))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,310))    
    
    def test_func_declare1(self):
        """Simple program: int main() {} """
        input = """ Function: foo
                        Parameter: a
                        Body:
                        x = 3;
                        EndBody.
                """
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],(([VarDecl(Id("x"),[],IntLiteral(2))],[])))])
        # expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([Assign(Id(x),IntLiteral(2))][]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
        
    # def test_none_program(self):
    #     input = """Function: foo
    #                 Body:
    #                 EndBody."""
    #     expect = Program([FuncDecl(Id("foo"),[],([],[]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,312))

    # def test_simple_7(self):
    #     """Simple program: int main() {} """
    #     input = """Var: arr[2] = {1,2};"""
    #     expect = Program([VarDecl(Id("arr"),[IntLiteral(2)],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
    #     self.assertTrue(TestAST.checkASTGen(input,expect,313))