from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # program  : SKIP_* variable_decl* SKIP_* body_decl* SKIP_* EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return Program([VarDecl(x) for x in ctx.variable_decl()])

    # variable_decl: VAR COLON variable_list SEMI;
    def visitVariable_decl(self,ctx:BKITParser.Variable_declContext):
        return None

