import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_301(self):
        """Created automatically"""
        input = r"""Var: faji342F__324dADS;""" 
        expect = Program([VarDecl(Id("faji342F__324dADS"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,301))
    def test_302(self):
        """Created automatically"""
        input = r""" 
        Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
        """ 
        expect = Program([VarDecl(Id("a"),[],IntLiteral(5)),VarDecl(Id("b"),[2,3],ArrayLiteral([ArrayLiteral([IntLiteral(2),IntLiteral(3),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(6)])])),VarDecl(Id("c"),[],None),VarDecl(Id("d"),[],IntLiteral(6)),VarDecl(Id("e"),[],None),VarDecl(Id("f"),[],None),VarDecl(Id("m"),[],None),VarDecl(Id("n"),[10],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,302))
    def test_303(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body: 
            call(var*a,876,.65e-1,arr[4],True,"chuoi~~\n");
        EndBody.""" 
        expect = Program([FuncDecl(Id("callmore"),[],([],[CallStmt(Id("call"),[BinaryOp("*",Id("var"),Id("a")),IntLiteral(876),FloatLiteral("65e-1"),ArrayCell(Id("arr"),[IntLiteral(4)]),BooleanLiteral(True),StringLiteral("chuoi~~\\n")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,303))
    def test_304(self):
        """Created automatically"""
        input = r""" 
        Var: decimal[108], hexadecimal[0X5456A][0x205F], octdecimal[0o413215][0O123];
        Var: array[5][13456];
        """ 
        expect = Program([VarDecl(Id("decimal"),[108],None),VarDecl(Id("hexadecimal"),[345450,8287],None),VarDecl(Id("octdecimal"),[136845,83],None),VarDecl(Id("array"),[5,13456],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,304))
    def test_305(self):
        """Created automatically"""
        input = r""" 
        Function: test_lan_1 
        Parameter: global_var
        Body: 
            dayLA1_teNbIen = 25+6-.2.5%3\100 ; 
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("test_lan_1"),[VarDecl(Id("global_var"),[],None)],([],[Assign(Id("dayLA1_teNbIen"),BinaryOp("-.",BinaryOp("+",IntLiteral(25),IntLiteral(6)),BinaryOp("\\",BinaryOp("%",FloatLiteral("2.5"),IntLiteral(3)),IntLiteral(100))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    def test_306(self):
        """Created automatically"""
        input = r""" Function: lan2
        Parameter: var
        Body: 
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("lan2"),[VarDecl(Id("var"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,306))
    def test_307(self):
        """Created automatically"""
        input = r"""
        Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody.""" 
        expect = Program([VarDecl(Id("x"),[],None),FuncDecl(Id("fact"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))])),FuncDecl(Id("main"),[],([],[Assign(Id("x"),IntLiteral(10)),CallStmt(Id("fact"),[Id("x")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,307))
    def test_308(self):
        """Created automatically"""
        input = r"""
        Function: parameter 
        Parameter: a, b,c[123] ,d[123][234][0]  ,e
        Body: 
            a=1;
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("parameter"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[123],None),VarDecl(Id("d"),[123,234,0],None),VarDecl(Id("e"),[],None)],([],[Assign(Id("a"),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,308))
    def test_309(self):
        """Created automatically"""
        input = r"""**sau day la 1 ham \\ main\n**
Function:**het y r** main ** test ne;**
**cmt tum lum ~!$()>?:{}**    Body: a=**235**865;
    EndBody **Body**.""" 
        expect = Program([FuncDecl(Id("main"),[],([],[Assign(Id("a"),IntLiteral(865))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,309))
    def test_310(self):
        """Created automatically"""
        input = r"""** This is a single-line comment. **
** This is a
* multi-line
* comment.
**""" 
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    def test_311(self):
        """Created automatically"""
        input = r"""**Function: main 
        Parameter: x, a
        Body: 
            While x>1 Do
                Var: a = 10;
            EndWhile.
        EndBody.**""" 
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input,expect,311))
    def test_312(self):
        """Created automatically"""
        input = r"""Function: multivscmt 
        Body: 
            Var: a = 100, b;
            b = (6\2)*8*b* **b**b*b;
        EndBody.""" 
        expect = Program([FuncDecl(Id("multivscmt"),[],([VarDecl(Id("a"),[],IntLiteral(100)),VarDecl(Id("b"),[],None)],[Assign(Id("b"),BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("*",BinaryOp("\\",IntLiteral(6),IntLiteral(2)),IntLiteral(8)),Id("b")),Id("b")),Id("b")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    def test_313(self):
        """Created automatically"""
        input = r"""Function: iDenTIfier_SS__ 
        Parameter: varrr
        Body: 
            **Do
                x= x+1;
            While x>1 
            EndDo.
            **
        EndBody.""" 
        expect = Program([FuncDecl(Id("iDenTIfier_SS__"),[VarDecl(Id("varrr"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    def test_314(self):
        """Created automatically"""
        input = r"""Function: keyword 
        Body: 
            Dooo=1; While True
            EndDo.
        EndBody.""" 
        expect = Program([FuncDecl(Id("keyword"),[],([],[Dowhile(([],[Assign(Id("oo"),IntLiteral(1))]),BooleanLiteral(True))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,314))
    def test_315(self):
        """Created automatically"""
        input = r"""Function: hellomoinguoi 
        Parameter: n
        Body: 
            If n <=. 1.2E-4 Then
            n=n*.3.3;
            ElseIf n>.100.2 Then
            n=n\.5;
            EndIf.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("hellomoinguoi"),[VarDecl(Id("n"),[],None)],([],[If([(BinaryOp("<=.",Id("n"),FloatLiteral("1.2E-4")),[],[Assign(Id("n"),BinaryOp("*.",Id("n"),FloatLiteral("3.3")))]),(BinaryOp(">.",Id("n"),FloatLiteral("100.2")),[],[Assign(Id("n"),BinaryOp("\.",Id("n"),IntLiteral(5)))])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,315))
    def test_316(self):
        """Created automatically"""
        input = r"""Function: testop 
        Body: 
            If ((k==1)&&(i!=0))||(k==5)||!j Then
                f=f%3;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("testop"),[],([],[If([(BinaryOp("||",BinaryOp("||",BinaryOp("&&",BinaryOp("==",Id("k"),IntLiteral(1)),BinaryOp("!=",Id("i"),IntLiteral(0))),BinaryOp("==",Id("k"),IntLiteral(5))),UnaryOp("!",Id("j"))),[],[Assign(Id("f"),BinaryOp("%",Id("f"),IntLiteral(3)))])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,316))
    def test_317(self):
        """Created automatically"""
        input = r"""Function: signop
        Parameter: n
        Body:
            a = -1082000;
            b = -0X123BCD;
            c = -0o21345;
            d = -a;
            c = -call(a);
            b = -.352.4E-12 ;
        EndBody.""" 
        expect = Program([FuncDecl(Id("signop"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("a"),UnaryOp("-",IntLiteral(1082000))),Assign(Id("b"),UnaryOp("-",IntLiteral(1194957))),Assign(Id("c"),UnaryOp("-",IntLiteral(8933))),Assign(Id("d"),UnaryOp("-",Id("a"))),Assign(Id("c"),UnaryOp("-",CallExpr(Id("call"),[Id("a")]))),Assign(Id("b"),UnaryOp("-.",FloatLiteral("352.4E-12")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,317))
    def test_318(self):
        """Created automatically"""
        input = r"""
        Function: test
        Body:
            Var: x=1;
            If x > 10 Then
                x=25+6-.2.5%3\100*x;
            Else
                x=x+2;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("test"),[],([VarDecl(Id("x"),[],IntLiteral(1))],[If([(BinaryOp(">",Id("x"),IntLiteral(10)),[],[Assign(Id("x"),BinaryOp("-.",BinaryOp("+",IntLiteral(25),IntLiteral(6)),BinaryOp("*",BinaryOp("\\",BinaryOp("%",FloatLiteral("2.5"),IntLiteral(3)),IntLiteral(100)),Id("x"))))])],([],[Assign(Id("x"),BinaryOp("+",Id("x"),IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,318))
    def test_319(self):
        """Created automatically"""
        input = r"""Function: var_decl 
        Parameter: naybingeohuhu
        Body:
Var: r = 10., v;
v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody.""" 
        expect = Program([FuncDecl(Id("var_decl"),[VarDecl(Id("naybingeohuhu"),[],None)],([VarDecl(Id("r"),[],FloatLiteral("10.")),VarDecl(Id("v"),[],None)],[Assign(Id("v"),BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("*.",BinaryOp("\.",FloatLiteral("4."),FloatLiteral("3.")),FloatLiteral("3.14")),Id("r")),Id("r")),Id("r")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,319))
    def test_320(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Return 1;
            Else
                Return n * fact (n - 1);
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("ifOKE"),[],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Return(IntLiteral(1))])],([],[Return(BinaryOp("*",Id("n"),CallExpr(Id("fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,320))
    def test_321(self):
        """Created automatically"""
        input = r"""
        Function: foroke
        Body: 
            For (i = 0, i < 10, 2) Do
                writeln(i);
            EndFor.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foroke"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[CallStmt(Id("writeln"),[Id("i")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,321))
    def test_322(self):
        """Created automatically"""
        input = r"""Function: whileandif 
        Body:
            Var: x=20;
            While True Do
                If x==0 Then Break;
                ElseIf x%2==0 Then
                    x=x\2;
                Else writeln(x);
                EndIf.
            EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("whileandif"),[],([VarDecl(Id("x"),[],IntLiteral(20))],[While(BooleanLiteral(True),([],[If([(BinaryOp("==",Id("x"),IntLiteral(0)),[],[Break()]),(BinaryOp("==",BinaryOp("%",Id("x"),IntLiteral(2)),IntLiteral(0)),[],[Assign(Id("x"),BinaryOp("\\",Id("x"),IntLiteral(2)))])],([],[CallStmt(Id("writeln"),[Id("x")])]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,322))
    def test_323(self):
        """Created automatically"""
        input = r"""Function: whilenullstmt
        Body:
            While i < 5 Do EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("whilenullstmt"),[],([],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,323))
    def test_324(self):
        """Created automatically"""
        input = r"""Function: whileinwhile 
        Parameter: x
        Body: 
            While (True) Do
                While (x>=0) Do
                    x = x+-1;
                EndWhile.
                If ((x<0)) Then Break; EndIf.
            EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("whileinwhile"),[VarDecl(Id("x"),[],None)],([],[While(BooleanLiteral(True),([],[While(BinaryOp(">=",Id("x"),IntLiteral(0)),([],[Assign(Id("x"),BinaryOp("+",Id("x"),UnaryOp("-",IntLiteral(1))))])),If([(BinaryOp("<",Id("x"),IntLiteral(0)),[],[Break()])],())]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,324))
    def test_325(self):
        """Created automatically"""
        input = r"""Function: iflongnhau
        Parameter: a, b
        Body:
        Var: id[4412][867][9856][867], stringID[108] = "day la \\ 1 chuoi !!",literal = 120000e-1,  array[2][4] = {{867,445,987},{76,12,744}};
            If n > 10 Then
                If n <. 20.5 Then Return x;
                EndIf.
                printStrLn(arg);
            Else fact(x);
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("iflongnhau"),[VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("id"),[4412,867,9856,867],None),VarDecl(Id("stringID"),[108],StringLiteral("day la \\\\ 1 chuoi !!")),VarDecl(Id("literal"),[],FloatLiteral("120000e-1")),VarDecl(Id("array"),[2,4],ArrayLiteral([ArrayLiteral([IntLiteral(867),IntLiteral(445),IntLiteral(987)]),ArrayLiteral([IntLiteral(76),IntLiteral(12),IntLiteral(744)])]))],[If([(BinaryOp(">",Id("n"),IntLiteral(10)),[],[If([(BinaryOp("<.",Id("n"),FloatLiteral("20.5")),[],[Return(Id("x"))])],()),CallStmt(Id("printStrLn"),[Id("arg")])])],([],[CallStmt(Id("fact"),[Id("x")])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,325))
    def test_326(self):
        """Created automatically"""
        input = r"""Function: whileindowhile
        Parameter: x
        Body:
            Do
                While a<100 Do
                    a=a-30;
                EndWhile.
            While (a>1)
            EndDo.
        EndBody.""" 
        expect = Program([FuncDecl(Id("whileindowhile"),[VarDecl(Id("x"),[],None)],([],[Dowhile(([],[While(BinaryOp("<",Id("a"),IntLiteral(100)),([],[Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(30)))]))]),BinaryOp(">",Id("a"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,326))
    def test_327(self):
        """Created automatically"""
        input = r"""Function: breaktest 
        Parameter: x
        Body: 
            While x >= 1 Do
                If y<100 Then Break;
                EndIf.
            EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("breaktest"),[VarDecl(Id("x"),[],None)],([],[While(BinaryOp(">=",Id("x"),IntLiteral(1)),([],[If([(BinaryOp("<",Id("y"),IntLiteral(100)),[],[Break()])],())]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,327))
    def test_328(self):
        """Created automatically"""
        input = r"""Function: breakandcontinuealone
        Body: 
            Continue;
            Break;
        EndBody.""" 
        expect = Program([FuncDecl(Id("breakandcontinuealone"),[],([],[Continue(),Break()]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,328))
    def test_329(self):
        """Created automatically"""
        input = r"""Function: testreturn 
        Parameter: n
        Body: 
            Var: t=False;
            If n<100 Then t=True;
            EndIf.
            Return t;
        EndBody.""" 
        expect = Program([FuncDecl(Id("testreturn"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("t"),[],BooleanLiteral(False))],[If([(BinaryOp("<",Id("n"),IntLiteral(100)),[],[Assign(Id("t"),BooleanLiteral(True))])],()),Return(Id("t"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,329))
    def test_330(self):
        """Created automatically"""
        input = r"""Function: arrayhavespace
        Body: 
            Var  : x[123]={   20, 2   ,108  };
        EndBody.""" 
        expect = Program([FuncDecl(Id("arrayhavespace"),[],([VarDecl(Id("x"),[123],ArrayLiteral([IntLiteral(20),IntLiteral(2),IntLiteral(108)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,330))
    def test_331(self):
        """Created automatically"""
        input = r"""Function: callincall
        Body:
            a =func1(foo(3))+23 - func2(goo(foo(a)));
        EndBody.""" 
        expect = Program([FuncDecl(Id("callincall"),[],([],[Assign(Id("a"),BinaryOp("-",BinaryOp("+",CallExpr(Id("func1"),[CallExpr(Id("foo"),[IntLiteral(3)])]),IntLiteral(23)),CallExpr(Id("func2"),[CallExpr(Id("goo"),[CallExpr(Id("foo"),[Id("a")])])])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,331))
    def test_332(self):
        """Created automatically"""
        input = r"""Function: a Parameter: a Body: Var: a=False;EndBody. Function: b Body: EndBody.
Function: d**Here some too**Parameter: d Body: EndBody.""" 
        expect = Program([FuncDecl(Id("a"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("a"),[],BooleanLiteral(False))],[])),FuncDecl(Id("b"),[],([],[])),FuncDecl(Id("d"),[VarDecl(Id("d"),[],None)],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,332))
    def test_333(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body:
            Var: i = 0;
            While i!=423 Do
                fact (i);
                i = i + 3; **cmt**
                If i==212 Then Break;
                a = (!(b && c)||!(a&&b)); 
                EndIf.
            EndWhile.
        EndBody.
        """ 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("!=",Id("i"),IntLiteral(423)),([],[CallStmt(Id("fact"),[Id("i")]),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(3))),If([(BinaryOp("==",Id("i"),IntLiteral(212)),[],[Break(),Assign(Id("a"),BinaryOp("||",UnaryOp("!",BinaryOp("&&",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("&&",Id("a"),Id("b")))))])],())]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,333))
    def test_334(self):
        """Created automatically"""
        input = r"""Function: octalToDecimal
        Parameter: octalNumber
        Body:
        Var: decimalNumber = 0, i = 0, rem;
        While (octalNumber != 0) Do
            rem = octalNumber % 10;
            octalNumber =octalNumber \ 10;
            decimalNumber =decimalNumber  + rem * pow(8,i);
            i=i+1;
        EndWhile.
    Return decimalNumber;
    EndBody.""" 
        expect = Program([FuncDecl(Id("octalToDecimal"),[VarDecl(Id("octalNumber"),[],None)],([VarDecl(Id("decimalNumber"),[],IntLiteral(0)),VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("rem"),[],None)],[While(BinaryOp("!=",Id("octalNumber"),IntLiteral(0)),([],[Assign(Id("rem"),BinaryOp("%",Id("octalNumber"),IntLiteral(10))),Assign(Id("octalNumber"),BinaryOp("\\",Id("octalNumber"),IntLiteral(10))),Assign(Id("decimalNumber"),BinaryOp("+",Id("decimalNumber"),BinaryOp("*",Id("rem"),CallExpr(Id("pow"),[IntLiteral(8),Id("i")])))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])),Return(Id("decimalNumber"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,334))
    def test_335(self):
        """Created automatically"""
        input = r"""Function: precedence 
        Body: 
            x = -(-15.e-1+(-.45.1*.2.4)*(45+108+a[4]));
        EndBody.""" 
        expect = Program([FuncDecl(Id("precedence"),[],([],[Assign(Id("x"),UnaryOp("-",BinaryOp("+",UnaryOp("-",FloatLiteral("15.e-1")),BinaryOp("*",BinaryOp("*.",UnaryOp("-.",FloatLiteral("45.1")),FloatLiteral("2.4")),BinaryOp("+",BinaryOp("+",IntLiteral(45),IntLiteral(108)),ArrayCell(Id("a"),[IntLiteral(4)]))))))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,335))
    def test_336(self):
        """Created automatically"""
        input = r"""
        Function: foroke
        Body: 
            For (i = 0, i < 10, 2) Do
                Break;
            EndFor.
        EndBody.""" 
        expect = Program([FuncDecl(Id("foroke"),[],([],[For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),IntLiteral(2),([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,336))
    def test_337(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        Var: x = 2;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([VarDecl(Id("x"),[],IntLiteral(2))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,337))
    def test_338(self):
        """Created automatically"""
        input = r""" Function: foo
                        Parameter: a
                        Body:
                        x = 3;
                        EndBody.
                """ 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("a"),[],None)],([],[Assign(Id("x"),IntLiteral(3))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,338))
    def test_339(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                Break;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("ifOKE"),[],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Break()])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,339))
    def test_340(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                x = 3;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("ifOKE"),[],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Assign(Id("x"),IntLiteral(3))])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,340))
    def test_341(self):
        """Created automatically"""
        input = r"""Function: ifOKE 
        Body: 
            If n == 0 Then
                x = 3;
            Else
                Break;
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("ifOKE"),[],([],[If([(BinaryOp("==",Id("n"),IntLiteral(0)),[],[Assign(Id("x"),IntLiteral(3))])],([],[Break()]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,341))
    def test_342(self):
        """Created automatically"""
        input = r"""Function: foo
                    Body:
                    EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[],([],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,342))
    def test_343(self):
        """Created automatically"""
        input = r"""Var: x,x;""" 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,343))
    def test_344(self):
        """Created automatically"""
        input = r"""Var: arr[2] = {1,2};""" 
        expect = Program([VarDecl(Id("arr"),[2],ArrayLiteral([IntLiteral(1),IntLiteral(2)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,344))
    def test_345(self):
        """Created automatically"""
        input = r"""Var:x =5 ;""" 
        expect = Program([VarDecl(Id("x"),[],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,345))
    def test_346(self):
        """Created automatically"""
        input = r"""Var:x;""" 
        expect = Program([VarDecl(Id("x"),[],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,346))
    def test_347(self):
        """Created automatically"""
        input = r"""Var:x[12];""" 
        expect = Program([VarDecl(Id("x"),[12],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,347))
    def test_348(self):
        """Created automatically"""
        input = r"""Var:x[0x13];""" 
        expect = Program([VarDecl(Id("x"),[19],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,348))
    def test_349(self):
        """Created automatically"""
        input = r"""Var:x[0x12][13]=5;""" 
        expect = Program([VarDecl(Id("x"),[18,13],IntLiteral(5))])
        self.assertTrue(TestAST.checkASTGen(input,expect,349))
    def test_350(self):
        """Created automatically"""
        input = r"""Var:x;
        Var: x=12;""" 
        expect = Program([VarDecl(Id("x"),[],None),VarDecl(Id("x"),[],IntLiteral(12))])
        self.assertTrue(TestAST.checkASTGen(input,expect,350))
    def test_351(self):
        """Created automatically"""
        input = r"""Var: x[12]={12};""" 
        expect = Program([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,351))
    def test_352(self):
        """Created automatically"""
        input = r"""Var: arr[5][6] = {1,2}, y[1];""" 
        expect = Program([VarDecl(Id("arr"),[5,6],ArrayLiteral([IntLiteral(1),IntLiteral(2)])),VarDecl(Id("y"),[1],None)])
        self.assertTrue(TestAST.checkASTGen(input,expect,352))
    def test_353(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n 
        Body: 
            Var: x[12]={12};
        EndBody.""" 
        expect = Program([FuncDecl(Id("foo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("x"),[12],ArrayLiteral([IntLiteral(12)]))],[]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,353))
    def test_354(self):
        """Created automatically"""
        input = r"""Var: b = True, c = False;""" 
        expect = Program([VarDecl(Id("b"),[],BooleanLiteral(True)),VarDecl(Id("c"),[],BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input,expect,354))
    def test_355(self):
        """Created automatically"""
        input = r"""Function: complexarray
            Body: x[124]={"duwat74\r \t", "@#&\n rwFEW54",54412,10.e14, 0.124, 544.0e-6  ,{"xe mau xanh"},"xe mau do"};
        EndBody.""" 
        expect = Program([FuncDecl(Id("complexarray"),[],([],[Assign(ArrayCell(Id("x"),[IntLiteral(124)]),ArrayLiteral([StringLiteral("duwat74\\r \\t"),StringLiteral("@#&\\n rwFEW54"),IntLiteral(54412),FloatLiteral("10.e14"),FloatLiteral("0.124"),FloatLiteral("544.0e-6"),ArrayLiteral([StringLiteral("xe mau xanh")]),StringLiteral("xe mau do")]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,355))
    def test_356(self):
        """Created automatically"""
        input = r"""Function: stmtcallinindex 
        Parameter: n
        Body: 
            a = 4*.4.5\0e-2+arr[4-function("call")];
        EndBody.""" 
        expect = Program([FuncDecl(Id("stmtcallinindex"),[VarDecl(Id("n"),[],None)],([],[Assign(Id("a"),BinaryOp("+",BinaryOp("\\",BinaryOp("*.",IntLiteral(4),FloatLiteral("4.5")),FloatLiteral("0e-2")),ArrayCell(Id("arr"),[BinaryOp("-",IntLiteral(4),CallExpr(Id("function"),[StringLiteral("call")]))])))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,356))
    def test_357(self):
        """Created automatically"""
        input = r"""Function: mmmmm
        Body: 
            Do
                While(1) Do
                foo (2 + x, 4. \. y);goo ();
            EndWhile.
            While(1)
            EndDo.
        EndBody.""" 
        expect = Program([FuncDecl(Id("mmmmm"),[],([],[Dowhile(([],[While(IntLiteral(1),([],[CallStmt(Id("foo"),[BinaryOp("+",IntLiteral(2),Id("x")),BinaryOp("\.",FloatLiteral("4."),Id("y"))]),CallStmt(Id("goo"),[])]))]),IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,357))
    def test_358(self):
        """Created automatically"""
        input = r"""
            Function: returnboolean
            Body:
            If str == "Chung Xon" Then
                Return True;
            Else
                Return False;
                EndIf.
            EndBody.""" 
        expect = Program([FuncDecl(Id("returnboolean"),[],([],[If([(BinaryOp("==",Id("str"),StringLiteral("Chung Xon")),[],[Return(BooleanLiteral(True))])],([],[Return(BooleanLiteral(False))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,358))
    def test_359(self):
        """Created automatically"""
        input = r"""Function: arr
        Body: 
            arr[1][2][3] = 4;
        EndBody.""" 
        expect = Program([FuncDecl(Id("arr"),[],([],[Assign(ArrayCell(Id("arr"),[IntLiteral(1),IntLiteral(2),IntLiteral(3)]),IntLiteral(4))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,359))
    def test_360(self):
        """Created automatically"""
        input = r"""Function: callmore
        Body: 
            call(a);
        EndBody.""" 
        expect = Program([FuncDecl(Id("callmore"),[],([],[CallStmt(Id("call"),[Id("a")])]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,360))
    def test_361(self):
        """Created automatically"""
        input = r"""Function: arraynull
        Body: 
            a[12] = {  };
            x[45]={{{{{}}}}};

        EndBody.""" 
        expect = Program([FuncDecl(Id("arraynull"),[],([],[Assign(ArrayCell(Id("a"),[IntLiteral(12)]),ArrayLiteral([])),Assign(ArrayCell(Id("x"),[IntLiteral(45)]),ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,361))
    def test_362(self):
        """Created automatically"""
        input = r"""Function: calculate 
        Parameter: n
        Body: 
            Var: a = {1,2,4}, b[2][4] = 5, c[2] = {{1,4},{4,5,7}};
            a[4+foo(4)] = a[b[2][4]] + 4;
        EndBody.""" 
        expect = Program([FuncDecl(Id("calculate"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("a"),[],ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4)])),VarDecl(Id("b"),[2,4],IntLiteral(5)),VarDecl(Id("c"),[2],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(4)]),ArrayLiteral([IntLiteral(4),IntLiteral(5),IntLiteral(7)])]))],[Assign(ArrayCell(Id("a"),[BinaryOp("+",IntLiteral(4),CallExpr(Id("foo"),[IntLiteral(4)]))]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(4)])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,362))
    def test_363(self):
        """Created automatically"""
        input = r"""Function: fibo
        Parameter: n
        Body:
            Var: n, t1 = 0, t2 = 1, nextTerm = 0;
            print("Enter the number of terms: ");
            getline(n);
            print("Fibonacci Series: ");
            For (i = 1, i <= n, 1) Do
                If(i == 1) Then
                print(" " + t1);
                Continue;
                EndIf.
            If(i == 2) Then
                print( t2+" ");
        Continue;
        EndIf.
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
        
        print(nextTerm + " ");
    EndFor.
    Return 0;
    EndBody.""" 
        expect = Program([FuncDecl(Id("fibo"),[VarDecl(Id("n"),[],None)],([VarDecl(Id("n"),[],None),VarDecl(Id("t1"),[],IntLiteral(0)),VarDecl(Id("t2"),[],IntLiteral(1)),VarDecl(Id("nextTerm"),[],IntLiteral(0))],[CallStmt(Id("print"),[StringLiteral("Enter the number of terms: ")]),CallStmt(Id("getline"),[Id("n")]),CallStmt(Id("print"),[StringLiteral("Fibonacci Series: ")]),For(Id("i"),IntLiteral(1),BinaryOp("<=",Id("i"),Id("n")),IntLiteral(1),([],[If([(BinaryOp("==",Id("i"),IntLiteral(1)),[],[CallStmt(Id("print"),[BinaryOp("+",StringLiteral(" "),Id("t1"))]),Continue()])],()),If([(BinaryOp("==",Id("i"),IntLiteral(2)),[],[CallStmt(Id("print"),[BinaryOp("+",Id("t2"),StringLiteral(" "))]),Continue()])],()),Assign(Id("nextTerm"),BinaryOp("+",Id("t1"),Id("t2"))),Assign(Id("t1"),Id("t2")),Assign(Id("t2"),Id("nextTerm")),CallStmt(Id("print"),[BinaryOp("+",Id("nextTerm"),StringLiteral(" "))])])),Return(IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,363))
    def test_364(self):
        """Created automatically"""
        input = r"""Function: iFElseIFNotElse 
        Parameter: n
        Body: 
            If bool_of_string("True") Then
                a = int_of_string (read ());
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("iFElseIFNotElse"),[VarDecl(Id("n"),[],None)],([],[If([(CallExpr(Id("bool_of_string"),[StringLiteral("True")]),[],[Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])]))])],())]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,364))
    def test_365(self):
        """Created automatically"""
        input = r"""Function: array 
        Parameter: i , j, arr[1001]
        Body: 
            a[i] = arr[c[2+j][b[i]*4]] + 4;
            i = i + 1;
        EndBody.""" 
        expect = Program([FuncDecl(Id("array"),[VarDecl(Id("i"),[],None),VarDecl(Id("j"),[],None),VarDecl(Id("arr"),[1001],None)],([],[Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+",ArrayCell(Id("arr"),[ArrayCell(Id("c"),[BinaryOp("+",IntLiteral(2),Id("j")),BinaryOp("*",ArrayCell(Id("b"),[Id("i")]),IntLiteral(4))])]),IntLiteral(4))),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,365))
    def test_366(self):
        """Created automatically"""
        input = r"""Function: fullIf 
        Body: 
            If (x == (b!=c && (a > b + c))) Then Return;
            ElseIf (x=="Chung Xon@@") Then Break;
            Else 
            x="successful";
            EndIf.
        EndBody.""" 
        expect = Program([FuncDecl(Id("fullIf"),[],([],[If([(BinaryOp("==",Id("x"),BinaryOp("!=",Id("b"),BinaryOp("&&",Id("c"),BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),Id("c")))))),[],[Return(None)]),(BinaryOp("==",Id("x"),StringLiteral("Chung Xon@@")),[],[Break()])],([],[Assign(Id("x"),StringLiteral("successful"))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,366))
    def test_367(self):
        """Created automatically"""
        input = r"""
        Var: stringinarray, x[124]={"STRING","aRraY1","Array2"};""" 
        expect = Program([VarDecl(Id("stringinarray"),[],None),VarDecl(Id("x"),[124],ArrayLiteral([StringLiteral("STRING"),StringLiteral("aRraY1"),StringLiteral("Array2")]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,367))
    def test_368(self):
        """Created automatically"""
        input = r"""Function: multicallstmt
        Body:
            a =-((func1(a)+24) * -func2(4)+arr[4])\. 0.5;
        EndBody.""" 
        expect = Program([FuncDecl(Id("multicallstmt"),[],([],[Assign(Id("a"),BinaryOp("\.",UnaryOp("-",BinaryOp("+",BinaryOp("*",BinaryOp("+",CallExpr(Id("func1"),[Id("a")]),IntLiteral(24)),UnaryOp("-",CallExpr(Id("func2"),[IntLiteral(4)]))),ArrayCell(Id("arr"),[IntLiteral(4)]))),FloatLiteral("0.5")))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,368))
    def test_369(self):
        """Created automatically"""
        input = r"""Function: array
        Parameter: x[124]
        Body:
            Var: i = 0;
            x[124]={996,712,216};
        EndBody.""" 
        expect = Program([FuncDecl(Id("array"),[VarDecl(Id("x"),[124],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[Assign(ArrayCell(Id("x"),[IntLiteral(124)]),ArrayLiteral([IntLiteral(996),IntLiteral(712),IntLiteral(216)]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,369))
    def test_370(self):
        """Created automatically"""
        input = r"""Function: more1
        Parameter: a[5], b
        Body:
        Var: x = {{1,2,4}, **Comment here** "abc"};
        Var: i = 0;
        While (i < 5) Do
        If i == 4 ThenReturn 1;EndIf.
        i = i + 1;
        EndWhile.
        EndBody.""" 
        expect = Program([FuncDecl(Id("more1"),[VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],([VarDecl(Id("x"),[],ArrayLiteral([ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(4)]),StringLiteral("abc")])),VarDecl(Id("i"),[],IntLiteral(0))],[While(BinaryOp("<",Id("i"),IntLiteral(5)),([],[If([(BinaryOp("==",Id("i"),IntLiteral(4)),[],[Return(IntLiteral(1))])],()),Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,370))
    def test_371(self):
        """Created automatically"""
        input = r"""Function: arrayinarray 
                Parameter: x[2][4]
        Body:
            Var: i = 0;
            x[2][4]={{867,445,987},{76,12,744}};
        EndBody.""" 
        expect = Program([FuncDecl(Id("arrayinarray"),[VarDecl(Id("x"),[2,4],None)],([VarDecl(Id("i"),[],IntLiteral(0))],[Assign(ArrayCell(Id("x"),[IntLiteral(2),IntLiteral(4)]),ArrayLiteral([ArrayLiteral([IntLiteral(867),IntLiteral(445),IntLiteral(987)]),ArrayLiteral([IntLiteral(76),IntLiteral(12),IntLiteral(744)])]))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,371))
    def test_372(self):
        """Created automatically"""
        input = r"""Function: returnstring
            Body:
                Return "String";
            EndBody.""" 
        expect = Program([FuncDecl(Id("returnstring"),[],([],[Return(StringLiteral("String"))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,372))
    def test_373(self):
        """Created automatically"""
        input = r"""Function: indexop
        Parameter: n
        Body: 
            a[b[4 + foo(2)][b||True]][b[b[1+0x469]]] = a[b[2][b[12E-9]*4]] + 4;
        EndBody.""" 
        expect = Program([FuncDecl(Id("indexop"),[VarDecl(Id("n"),[],None)],([],[Assign(ArrayCell(Id("a"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(4),CallExpr(Id("foo"),[IntLiteral(2)])),BinaryOp("||",Id("b"),BooleanLiteral(True))]),ArrayCell(Id("b"),[ArrayCell(Id("b"),[BinaryOp("+",IntLiteral(1),IntLiteral(1129))])])]),BinaryOp("+",ArrayCell(Id("a"),[ArrayCell(Id("b"),[IntLiteral(2),BinaryOp("*",ArrayCell(Id("b"),[FloatLiteral("12E-9")]),IntLiteral(4))])]),IntLiteral(4)))]))])
        self.assertTrue(TestAST.checkASTGen(input,expect,373))