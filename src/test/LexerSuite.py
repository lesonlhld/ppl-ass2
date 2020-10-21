import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_101(self):
        """Created automatically"""
        input = r"""abc""" 
        output = r"""abc,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,101))
    def test_102(self):
        """Created automatically"""
        input = r"""Var""" 
        output = r"""Var,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,102))
    def test_103(self):
        """Created automatically"""
        input = r"""day la 1 test""" 
        output = r"""day,la,1,test,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,103))
    def test_104(self):
        """Created automatically"""
        input = r"""xin chao cac ban""" 
        output = r"""xin,chao,cac,ban,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,104))
    def test_105(self):
        """Created automatically"""
        input = r"""co so dau tien 108NVH""" 
        output = r"""co,so,dau,tien,108,Error Token N"""
        self.assertTrue(TestLexer.checkLexeme(input,output,105))
    def test_106(self):
        """Created automatically"""
        input = r"""viet hoa IDENTIFIERS""" 
        output = r"""viet,hoa,Error Token I"""
        self.assertTrue(TestLexer.checkLexeme(input,output,106))
    def test_107(self):
        """Created automatically"""
        input = r"""vIet Lon XOn nE""" 
        output = r"""vIet,Error Token L"""
        self.assertTrue(TestLexer.checkLexeme(input,output,107))
    def test_108(self):
        """Created automatically"""
        input = r"""co ky tu dac biet @@""" 
        output = r"""co,ky,tu,dac,biet,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(input,output,108))
    def test_109(self):
        """Created automatically"""
        input = r"""Var: x""" 
        output = r"""Var,:,x,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,109))
    def test_110(self):
        """Created automatically"""
        input = r"""tu1 1a` le^ trun9 son!!!""" 
        output = r"""tu1,1,a,Error Token `"""
        self.assertTrue(TestLexer.checkLexeme(input,output,110))
    def test_111(self):
        """Created automatically"""
        input = r"""0X54J54""" 
        output = r"""0X54,Error Token J"""
        self.assertTrue(TestLexer.checkLexeme(input,output,111))
    def test_112(self):
        """Created automatically"""
        input = r"""0X5456A 0x205F 0XBCD 0X0 0X567 0x2""" 
        output = r"""0X5456A,0x205F,0XBCD,0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(input,output,112))
    def test_113(self):
        """Created automatically"""
        input = r"""01 8 0108 2000 000""" 
        output = r"""0,1,8,0,108,2000,0,0,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,113))
    def test_114(self):
        """Created automatically"""
        input = r"""0o1 0o413215 0O0""" 
        output = r"""0o1,0o413215,0,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(input,output,114))
    def test_115(self):
        """Created automatically"""
        input = r"""0B2005""" 
        output = r"""0,Error Token B"""
        self.assertTrue(TestLexer.checkLexeme(input,output,115))
    def test_116(self):
        """Created automatically"""
        input = r"""20.e5 18.E9 9.e+3 33.e-3 0.e """ 
        output = r"""20.e5,18.E9,9.e+3,33.e-3,0.,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,116))
    def test_117(self):
        """Created automatically"""
        input = r"""0.0 52.. 43124. 120000e-1""" 
        output = r"""0.0,52.,.,43124.,120000e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,117))
    def test_118(self):
        """Created automatically"""
        input = r"""0.4254 654.321 .7582 87867. .""" 
        output = r"""0.4254,654.321,.,7582,87867.,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,118))
    def test_119(self):
        """Created automatically"""
        input = r"""4.e.6 -0 -404 -.e3 -10.e -10.e3""" 
        output = r"""4.,e,.,6,-,0,-,404,-.,e3,-,10.,e,-,10.e3,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,119))
    def test_120(self):
        """Created automatically"""
        input = r"""e97 E-66 16e 30E4 12.0e3""" 
        output = r"""e97,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,120))
    def test_121(self):
        """Created automatically"""
        input = r""" "abc\h def"  """ 
        output = r"""Illegal Escape In String: abc\h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,121))
    def test_122(self):
        """Created automatically"""
        input = r""" "hello\'\myfriend" """ 
        output = r"""Illegal Escape In String: hello\'\m"""
        self.assertTrue(TestLexer.checkLexeme(input,output,122))
    def test_123(self):
        """Created automatically"""
        input = r""" "chao cac ban nhaaa \Hom\nay cac ban the nao" """ 
        output = r"""Illegal Escape In String: chao cac ban nhaaa \H"""
        self.assertTrue(TestLexer.checkLexeme(input,output,123))
    def test_124(self):
        """Created automatically"""
        input = r""" "24 naif ^%$^% cdasjh\Fncueyew" """ 
        output = r"""Illegal Escape In String: 24 naif ^%$^% cdasjh\F"""
        self.assertTrue(TestLexer.checkLexeme(input,output,124))
    def test_125(self):
        """Created automatically"""
        input = r""" "To la Chung Xon \Ne" """ 
        output = r"""Illegal Escape In String: To la Chung Xon \N"""
        self.assertTrue(TestLexer.checkLexeme(input,output,125))
    def test_126(self):
        """Created automatically"""
        input = r""" xin chao "phan thanh truong'haha" 456""" 
        output = r"""xin,chao,Illegal Escape In String: phan thanh truong'h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,126))
    def test_127(self):
        """Created automatically"""
        input = r""" "ahihi do ngoc\\" """ 
        output = r"""ahihi do ngoc\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,127))
    def test_128(self):
        """Created automatically"""
        input = r""" "Day la ' illegal" """ 
        output = r"""Illegal Escape In String: Day la ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,128))
    def test_129(self):
        """Created automatically"""
        input = r""" "Test met qua troi '"\Wa dat luon ne""" 
        output = r"""Illegal Escape In String: Test met qua troi '"\W"""
        self.assertTrue(TestLexer.checkLexeme(input,output,129))
    def test_130(self):
        """Created automatically"""
        input = r""" "ngoi TAo \\tESt eScapE '" ne ' \r" """ 
        output = r"""Illegal Escape In String: ngoi TAo \\tESt eScapE '" ne ' """
        self.assertTrue(TestLexer.checkLexeme(input,output,130))
    def test_131(self):
        """Created automatically"""
        input = r""" "abc def  """ 
        output = r"""Unclosed String: abc def  """
        self.assertTrue(TestLexer.checkLexeme(input,output,131))
    def test_132(self):
        """Created automatically"""
        input = r""" "Hi Chau Thanh""Tan """ 
        output = r"""Hi Chau Thanh,Unclosed String: Tan """
        self.assertTrue(TestLexer.checkLexeme(input,output,132))
    def test_133(self):
        """Created automatically"""
        input = r""" "vi su nghiep qua PPL \n" """ 
        output = r"""vi su nghiep qua PPL \n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,133))
    def test_134(self):
        """Created automatically"""
        input = r""" "String ket thuc bang '" """ 
        output = r"""Unclosed String: String ket thuc bang '" """
        self.assertTrue(TestLexer.checkLexeme(input,output,134))
    def test_135(self):
        """Created automatically"""
        input = r""" "abc\n """ 
        output = r"""Unclosed String: abc\n """
        self.assertTrue(TestLexer.checkLexeme(input,output,135))
    def test_136(self):
        """Created automatically"""
        input = r""" "khok '" 1" "dong song~~~ 
        newline" " """ 
        output = r"""khok '" 1,Unclosed String: dong song~~~ 
"""
        self.assertTrue(TestLexer.checkLexeme(input,output,136))
    def test_137(self):
        """Created automatically"""
        input = r""" "" " """ 
        output = r""",Unclosed String:  """
        self.assertTrue(TestLexer.checkLexeme(input,output,137))
    def test_138(self):
        """Created automatically"""
        input = r"""Function: assignment Body: str = "Hello World!!! \" Endbody.""" 
        output = r"""Function,:,assignment,Body,:,str,=,Unclosed String: Hello World!!! \" Endbody."""
        self.assertTrue(TestLexer.checkLexeme(input,output,138))
    def test_139(self):
        """Created automatically"""
        input = r""" "8n[#F*`~.~+C_D""" 
        output = r"""Unclosed String: 8n[#F*`~.~+C_D"""
        self.assertTrue(TestLexer.checkLexeme(input,output,139))
    def test_140(self):
        """Created automatically"""
        input = r""""fe23%$.81r " {"abc"} 123"abc""" 
        output = r"""fe23%$.81r ,{,abc,},123,Unclosed String: abc"""
        self.assertTrue(TestLexer.checkLexeme(input,output,140))
    def test_141(self):
        """Created automatically"""
        input = r""" "Day la 1 string nha Dang Huynh Minh Tri"  """ 
        output = r"""Day la 1 string nha Dang Huynh Minh Tri,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,141))
    def test_142(self):
        """Created automatically"""
        input = r""" "This is a string containing tab \t"  """ 
        output = r"""This is a string containing tab \t,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,142))
    def test_143(self):
        """Created automatically"""
        input = r""" "He asked me: '"Where is John?'""  """ 
        output = r"""He asked me: '"Where is John?'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,143))
    def test_144(self):
        """Created automatically"""
        input = r""" "String nay chua cac ky tu dac biet !@#$%^^&*()?/|~!%>:P{}<> :)))"  """ 
        output = r"""String nay chua cac ky tu dac biet !@#$%^^&*()?/|~!%>:P{}<> :))),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,144))
    def test_145(self):
        """Created automatically"""
        input = r""" "ab'"c\n def"  """ 
        output = r"""ab'"c\n def,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,145))
    def test_146(self):
        """Created automatically"""
        input = r""" "Sau day la 1 string rong" ""  """ 
        output = r"""Sau day la 1 string rong,,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,146))
    def test_147(self):
        """Created automatically"""
        input = r""" "bool_of_string ('"True'")"  """ 
        output = r"""bool_of_string ('"True'"),<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,147))
    def test_148(self):
        """Created automatically"""
        input = r""" "** cai nay hong phai comment nha **"  """ 
        output = r"""** cai nay hong phai comment nha **,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,148))
    def test_149(self):
        """Created automatically"""
        input = r"""" This is a test 0925919727 \' PHONE" abc 
"YKYUUD '" \f fsgre " """ 
        output = r""" This is a test 0925919727 \' PHONE,abc,YKYUUD '" \f fsgre ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,149))
    def test_150(self):
        """Created automatically"""
        input = r""" "\b\f\r\n\t\'\\"  """ 
        output = r"""\b\f\r\n\t\'\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,150))
    def test_151(self):
        """Created automatically"""
        input = r"""Body Break  Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False EndDo""" 
        output = r"""Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,151))
    def test_152(self):
        """Created automatically"""
        input = r"""if thEn ElsE Then """ 
        output = r"""if,thEn,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,152))
    def test_153(self):
        """Created automatically"""
        input = r"""EndFor EndIff EndDoOO EndGame""" 
        output = r"""EndFor,EndIf,f,EndDo,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(input,output,153))
    def test_154(self):
        """Created automatically"""
        input = r"""Parameter: x[123],n""" 
        output = r"""Parameter,:,x,[,123,],,,n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,154))
    def test_155(self):
        """Created automatically"""
        input = r""" int var_ =. int(1.12)*1.0 12and""" 
        output = r"""int,var_,=,.,int,(,1.12,),*,1.0,12,and,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,155))
    def test_156(self):
        """Created automatically"""
        input = r"""x oR y assign !k""" 
        output = r"""x,oR,y,assign,!,k,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,156))
    def test_157(self):
        """Created automatically"""
        input = r"""If a == true then Return 1. elseIf a = False Returnn 0""" 
        output = r"""If,a,==,true,then,Return,1.,elseIf,a,=,False,Return,n,0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,157))
    def test_158(self):
        """Created automatically"""
        input = r"""If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf.""" 
        output = r"""If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,158))
    def test_159(self):
        """Created automatically"""
        input = r"""Function: foo
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5)
a[i] = b +. 1.0;
i = i + 1;
EndWhile.
EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,159))
    def test_160(self):
        """Created automatically"""
        input = r"""If!aThenbElseWhile(x>0)Thena++EndWhileEndIF""" 
        output = r"""If,!,aThenbElseWhile,(,x,>,0,),Then,a,+,+,EndWhile,Error Token E"""
        self.assertTrue(TestLexer.checkLexeme(input,output,160))
    def test_161(self):
        """Created automatically"""
        input = r"""25+6-.2.5%3\100""" 
        output = r"""25,+,6,-.,2.5,%,3,\,100,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,161))
    def test_162(self):
        """Created automatically"""
        input = r"""2e-5*.41+-18""" 
        output = r"""2e-5,*.,41,+,-,18,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,162))
    def test_163(self):
        """Created automatically"""
        input = r"""test&&lexer||parser&h=4/5""" 
        output = r"""test,&&,lexer,||,parser,Error Token &"""
        self.assertTrue(TestLexer.checkLexeme(input,output,163))
    def test_164(self):
        """Created automatically"""
        input = r"""=<=<>>=>=.=/===>.<<.!=""" 
        output = r"""=,<=,<,>,>=,>=.,=/=,==,>.,<,<.,!=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,164))
    def test_165(self):
        """Created automatically"""
        input = r"""!x&&a<=.b\.d*""" 
        output = r"""!,x,&&,a,<=.,b,\.,d,*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,165))
    def test_166(self):
        """Created automatically"""
        input = r"""** This is a single-line comment. **""" 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,166))
    def test_167(self):
        """Created automatically"""
        input = r"""***** *** **""" 
        output = r"""*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,167))
    def test_168(self):
        """Created automatically"""
        input = r"""** This is a
* multi-line
* comment.
** """ 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,168))
    def test_169(self):
        """Created automatically"""
        input = r"""* * **** * *""" 
        output = r"""*,*,*,*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,169))
    def test_170(self):
        """Created automatically"""
        input = r"""**Tui SaP Bj LAG luon r =.= (T.T) :v 2654^$$%!{><>~}{5}[789]!@#$%^&* \v \n   **""" 
        output = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,170))
    def test_171(self):
        """Created automatically"""
        input = r"""hello **"be mo"** **cUG wa tr wa dat lun""" 
        output = r"""hello,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input,output,171))
    def test_172(self):
        """Created automatically"""
        input = r"""**met xiu luon a* kok tie9 con bo""" 
        output = r"""Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input,output,172))
    def test_173(self):
        """Created automatically"""
        input = r"""**VI DU CO EOF TRONG CMT** "\\den day la oke\n" """ 
        output = r"""\\den day la oke\n,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,173))
    def test_174(self):
        """Created automatically"""
        input = r""" "**comment trong string nha \haha**" oke hem???""" 
        output = r"""Illegal Escape In String: **comment trong string nha \h"""
        self.assertTrue(TestLexer.checkLexeme(input,output,174))
    def test_175(self):
        """Created automatically"""
        input = r"""**sau day
        *la
        * **comment trong cmt**
        *
        **""" 
        output = r"""comment,trong,cmt,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,175))
    def test_176(self):
        """Created automatically"""
        input = r"""fjiwef883_Fef_GRWE4324 r3fe 23728DFRfdw""" 
        output = r"""fjiwef883_Fef_GRWE4324,r3fe,23728,Error Token D"""
        self.assertTrue(TestLexer.checkLexeme(input,output,176))
    def test_177(self):
        """Created automatically"""
        input = r"""__count in function""" 
        output = r"""Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input,output,177))
    def test_178(self):
        """Created automatically"""
        input = r"""iwqoue9432@#$8(!/da""" 
        output = r"""iwqoue9432,Error Token @"""
        self.assertTrue(TestLexer.checkLexeme(input,output,178))
    def test_179(self):
        """Created automatically"""
        input = r"""!!=x/y""" 
        output = r"""!,!=,x,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input,output,179))
    def test_180(self):
        """Created automatically"""
        input = r""""string nay co 2 \' nha qui vi ^.^"' """ 
        output = r"""string nay co 2 \' nha qui vi ^.^,Error Token '"""
        self.assertTrue(TestLexer.checkLexeme(input,output,180))
    def test_181(self):
        """Created automatically"""
        input = r"""{996,712,216}""" 
        output = r"""{,996,,,712,,,216,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,181))
    def test_182(self):
        """Created automatically"""
        input = r"""{{867,345,987},{76,12,744}}""" 
        output = r"""{,{,867,,,345,,,987,},,,{,76,,,12,,,744,},},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,182))
    def test_183(self):
        """Created automatically"""
        input = r"""{y65,de3DEF,ca_rFE245_2E23}""" 
        output = r"""{,y65,,,de3DEF,,,ca_rFE245_2E23,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,183))
    def test_184(self):
        """Created automatically"""
        input = r"""{"STRING","aRraY1","Array2"}""" 
        output = r"""{,STRING,,,aRraY1,,,Array2,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,184))
    def test_185(self):
        """Created automatically"""
        input = r"""{   20, 2   ,108  }""" 
        output = r"""{,20,,,2,,,108,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,185))
    def test_186(self):
        """Created automatically"""
        input = r"""{10.e13, 0.123, 543.0e-6  }""" 
        output = r"""{,10.e13,,,0.123,,,543.0e-6,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,186))
    def test_187(self):
        """Created automatically"""
        input = r"""{{"xe mau xanh"},"xe mau do"}""" 
        output = r"""{,{,xe mau xanh,},,,xe mau do,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,187))
    def test_188(self):
        """Created automatically"""
        input = r""" {"duwat73\r \t", "@#&\n rwFEW54", 54312}  """ 
        output = r"""{,duwat73\r \t,,,@#&\n rwFEW54,,,54312,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,188))
    def test_189(self):
        """Created automatically"""
        input = r""" {**comment trong array**}  """ 
        output = r"""{,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,189))
    def test_190(self):
        """Created automatically"""
        input = r""" {True,False}  """ 
        output = r"""{,True,,,False,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,190))
    def test_191(self):
        """Created automatically"""
        input = r"""** comment nha **
    Function: foo 
        Parameter: n 
        Body: 
            For (i == 0, i != 5, i*1) Do x=6; EndFor.
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,For,(,i,==,0,,,i,!=,5,,,i,*,1,),Do,x,=,6,;,EndFor,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,191))
    def test_192(self):
        """Created automatically"""
        input = r"""Var: someid[0][1][123][999], mor3Id[1000] = "SomeSTRING",
some_more_id[987],muchmoreID = 123.321e-2,  lots_m0rE_1D[123][123] = {12,3};""" 
        output = r"""Var,:,someid,[,0,],[,1,],[,123,],[,999,],,,mor3Id,[,1000,],=,SomeSTRING,,,some_more_id,[,987,],,,muchmoreID,=,123.321e-2,,,lots_m0rE_1D,[,123,],[,123,],=,{,12,,,3,},;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,192))
    def test_193(self):
        """Created automatically"""
        input = r"""Function: foo
        Parameter: a[5], b
        Body:
        Var: i = 0;
        While (i < 5)
        a[i] = b +. 1.0;
        i = i + 1;
        EndWhile.
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,193))
    def test_194(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            While i < 5 
                Var: k = 10;
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,While,i,<,5,Var,:,k,=,10,;,a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,194))
    def test_195(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,Var,:,r,=,10.,,,v,;,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,195))
    def test_196(self):
        """Created automatically"""
        input = r"""Function: foo
    Parameter: abc;
    Body:
    Var **COMMENT**: ****id = 465632
        **dsfhfsdhjnc^#%#@@~!**
    vAr: sss;
    EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,abc,;,Body,:,Var,:,id,=,465632,vAr,:,sss,;,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,196))
    def test_197(self):
        """Created automatically"""
        input = r"""Function:fooParameter:nBody:Ifn==0ThenReturn1;ElseReturnn*fact(n-1);ElseReturnn;EndIf.EndBody.""" 
        output = r"""Function,:,fooParameter,:,nBody,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,Else,Return,n,;,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,197))
    def test_198(self):
        """Created automatically"""
        input = r"""Function: foo 
        Parameter: n
        Body: 
            If n == 0 Then
                If n!=0 Then
                    c =a && b;
                Else 
                    Do
                        x= x+1;
                        iF x==5 tHEN Break;
                    While x>1 
                    EndDo.
            EndIf.
        EndBody.""" 
        output = r"""Function,:,foo,Parameter,:,n,Body,:,If,n,==,0,Then,If,n,!=,0,Then,c,=,a,&&,b,;,Else,Do,x,=,x,+,1,;,iF,x,==,5,tHEN,Break,;,While,x,>,1,EndDo,.,EndIf,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,198))
    def test_199(self):
        """Created automatically"""
        input = r""" **global declaration**  Var: a = 5;
        Varr: b[2][3] = {{2,3,4},{4,5,6}};
        Varrr: c, d = 6, e, f;
        Var: m, n[10];""" 
        output = r"""Var,:,a,=,5,;,Var,r,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},;,Var,rr,:,c,,,d,=,6,,,e,,,f,;,Var,:,m,,,n,[,10,],;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,199))
    def test_200(self):
        """Created automatically"""
        input = r"""Function:testdjiDEW__214__wsaParameter:ne23Body:x1 = a[3-foo(3)];Var:x,y[1][3]={{{12,1}, {12., 12e3}},{23}, {13,32}};WhileTrueprint("Hello_World\n");EndWhile.EndBody.""" 
        output = r"""Function,:,testdjiDEW__214__wsaParameter,:,ne23Body,:,x1,=,a,[,3,-,foo,(,3,),],;,Var,:,x,,,y,[,1,],[,3,],=,{,{,{,12,,,1,},,,{,12.,,,12e3,},},,,{,23,},,,{,13,,,32,},},;,While,True,print,(,Hello_World\n,),;,EndWhile,.,EndBody,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input,output,200))