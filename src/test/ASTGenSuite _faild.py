import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    # def fewfe(self):
    #     """Created automatically"""
    #     input = r"""Function: calculate 
    #     Parameter: n
    #     Body: 
    #         Var: a = {1,2,3}, b[2][3] = 5, c[2] = {{1,3},{3,5,7}};
    #         a[3+foo(3)] = a[b[2][3]] + 4;
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,7855647))
    # def fewf(self):
    #     """Created automatically"""
    #     input = r"""Function: stmtcallinindex 
    #     Parameter: n
    #     Body: 
    #         a = 3*.4.5\0e-2+arr[3-function("call")];
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,1324))
    # def wefde(self):
    #     """Created automatically"""
    #     input = r"""Function: precedence 
    #     Body: 
    #         x = -(-15.e-1+(-.45.1*.2.3)*(35+108+a[4]));
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,431))
    # def gre(self):
    #     """Created automatically"""
    #     input = r"""Function: array 
    #     Parameter: i , j, arr[1001]
    #     Body: 
    #         a[i] = arr[c[2+j][b[i]*3]] + 4;
    #         i = i + 1;
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,7234))
    # def effe(self):
    #     """Created automatically"""
    #     input = r"""Function: indexop
    #     Parameter: n
    #     Body: 
    #         a[a[3 + foo(2)][b||True]][b[b[1+0x369]]] = a[b[2][b[12E-9]*3]] + 4;
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,743213))
    # def fewwe(self):
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
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,976))
    # def kuty(self):
    #     """Created automatically"""
    #     input = r"""Function: fullIf 
    #     Body: 
    #         If (x == (b!=c && (a > b + c))) Then Return;
    #         ElseIf (x=="Chung Xon@@") Then Break;
    #         Else 
    #         x="successful";
    #         EndIf.
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,24872))
    # def test_3ee24240(self):
    #     """Created automatically"""
    #     input = r"""Function: iflongnhau
    #     Parameter: a, b
    #     Body:
    #     Var: id[4312][867][9856][867], stringID[108] = "day la \\ 1 chuoi !!",literal = 120000e-1,  array[2][3] = {{867,345,987},{76,12,744}};
    #         If n > 10 Then
    #             If n <. 20.5 Then Return x;
    #             EndIf.
    #             printStrLn(arg);
    #         Else fact(x);
    #         EndIf.
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,8652652))
    # # def qawszfcas(self):
    # #     """Created automatically"""
    # #     input = r"""Function: nothen
    # #     Body:
    # #         If e==True Then
    # #             print("Hello cac cau\n");
    # #         EndIf.
    # #     EndBody.""" 
    # #     expect = "" 
    # #     self.assertTrue(TestAST.checkASTGen(input,expect,75454))
    # # def dsadcas(self):
    # #     """Created automatically"""
    # #     input = r"""Function: whileoke
    # #     Body: 
    # #         Var: i = 0,k=10;
    # #         While i !=k Do
    # #             a[i] = b + i +. 15.0;
    # #             i = i + 1;
    # #         EndWhile.
    # #     EndBody.""" 
    # #     expect = "" 
    # #     self.assertTrue(TestAST.checkASTGen(input,expect,1245))
    # # def jythr(self):
    # #     """Created automatically"""
    # #     input = r"""Function: continue 
    # #     Body: 
    # #         For (i=0, i!=9, i) Do
    # #             If i==10 Then Continue;
    # #             EndIf.
    # #             foo();
    # #         EndFor.
    # #     EndBody.""" 
    # #     expect = "" 
    # #     self.assertTrue(TestAST.checkASTGen(input,expect,7647332))
    # # def wadretj(self):
    # #     """Created automatically"""
    # #     input = r"""Function: callstmt 
    # #     Parameter: x,y
    # #     Body:
    # #         foo(2 + x, 4. \. y);
    # #         goo();
    # #     EndBody.""" 
    # #     expect = "" 
    # #     self.assertTrue(TestAST.checkASTGen(input,expect,142657))
    # def testwesfhdr_327(self):
    #     """Created automatically"""
    #     input = r"""Function: callmore
    #     Body: 
    #         call(var*a,876,.65e-1,arr[3],True,"chuoi~~\n");
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,21563))
    def edfew2413(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body: 
            call(a);
        EndBody.""" 
        expect = "" 
        self.assertTrue(TestAST.checkASTGen(input,expect,234142))
    # def safere(self):
    #     """Created automatically"""
    #     input = r"""Function: returnstring
    #         Body:
    #             Return "String'"";
    #         EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,5325345))
    # def dwaewtre(self):
    #     """Created automatically"""
    #     input = r"""
    #         Function: returnboolean
    #         Body:
    #         If str == "Chung Xon" Then
    #             Return True;
    #         Else
    #             Return False;
    #             EndIf.
    #         EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,5346361))
    def test_kuljryseg328(self):
        """Created automatically"""
        input = r"""Function: array
        Parameter: x[123]
        Body:
            Var: i = 0;
            x[123]={996,712,216};
        EndBody.""" 
        expect = "" 
        self.assertTrue(TestAST.checkASTGen(input,expect,12426436))
    # def wfeehrhtr(self):
    #     """Created automatically"""
    #     input = r"""Function: arrayinarray 
    #             Parameter: x[2][3]
    #     Body:
    #         Var: i = 0;
    #         x[2][3]={{867,345,987},{76,12,744}};
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,1535646))
    # def test_cw33dw328(self):
    #     """Created automatically"""
    #     input = r"""
    #     Var: stringinarray, x[123]={"STRING","aRraY1","Array2"};""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,32526))
    # def r2tr(self):
    #     """Created automatically"""
    #     input = r"""Function: complexarray
    #         Body: x[123]={"duwat73\r \t", "@#&\n rwFEW54",54312,10.e13, 0.123, 543.0e-6  ,{"xe mau xanh"},"xe mau do"};
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,856653))
    # def fec(self):
    #     """Created automatically"""
    #     input = r"""Function: arraynull
    #     Body: 
    #         a[12] = {  };
    #         x[45]={{{{{}}}}};

    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,876845))
    def test_3fewgt29(self):
        """Created automatically"""
        input = r"""Function: multicallstmt
        Body:
            a =-((func1(a)+23) * -func2(4)+arr[3])\. 0.5;
        EndBody.""" 
        expect = "" 
        self.assertTrue(TestAST.checkASTGen(input,expect,8343))
    # def fgwge(self):
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
    #     self.assertTrue(TestAST.checkASTGen(input,expect,76583242))
    # def testfrqewrfwe_332(self):
    #     """Created automatically"""
    #     input = r"""Function: more1
    #     Parameter: a[5], b
    #     Body:
    #     Var: x = {{1,2,3}, **Comment here** "abc"};
    #     Var: i = 0;
    #     While (i < 5) Do
    #     If i == 3 ThenReturn 1;EndIf.
    #     i = i + 1;
    #     EndWhile.
    #     EndBody.""" 
    #     expect = "" 
    #     self.assertTrue(TestAST.checkASTGen(input,expect,1245772))
    # def g4ewe4w(self):
    #     """Created automatically"""
    #     input = r"""Function: fibo
    #     Parameter: n
    #     Body:
    #         Var: n, t1 = 0, t2 = 1, nextTerm = 0;
    #         print("Enter the number of terms: ");
    #         getline(n);
    #         print("Fibonacci Series: ");
    #         For (i = 1, i <= n, 1) Do
    #             If(i == 1) Then
    #             print(" " + t1);
    #             Continue;
    #             EndIf.
    #         If(i == 2) Then
    #             print( t2+" ");
    #     Continue;
    #     EndIf.
    #     nextTerm = t1 + t2;
    #     t1 = t2;
    #     t2 = nextTerm;
        
    #     print(nextTerm + " ");
    # EndFor.
    # Return 0;
    # EndBody.""" 
    #     expect = ""
    #     self.assertTrue(TestAST.checkASTGen(input,expect,214534))
    