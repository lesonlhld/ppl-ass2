# Generate automatically
from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *

class ASTGeneration(BKITVisitor):
    # program  : SKIP_* variable_decl* SKIP_* body_decl* SKIP_* EOF;
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        return None

    # var_list: variable_decl var_list | variable_decl |;
    def visitVariable_decl(self,ctx:BKITParser.Variable_declContext):
        return None

    # variable_list: variable (ASSIGN init_value)? COMMA variable_list | variable (ASSIGN init_value)?;
    def visitVariable_list(self,ctx:BKITParser.Variable_listContext):
        return None

    # array_decl: ID dimension;
    def visitArray_decl(self,ctx:BKITParser.Array_declContext):
        return None

    # dimension: LEFT_BRACKET integer RIGHT_BRACKET dimension | LEFT_BRACKET integer RIGHT_BRACKET;
    def visitDimension(self,ctx:BKITParser.DimensionContext):
        return None

    # init_value: literal COMMA init_value | literal;
    def visitInit_value(self,ctx:BKITParser.Init_valueContext):
        return None

    # operands: ID | literal | element_exp;
    def visitLiteral(self,ctx:BKITParser.LiteralContext):
        return None

    # integer: DECIMAL_INTEGER | HEX_INTEGER | OCT_INTEGER;
    def visitInteger(self,ctx:BKITParser.IntegerContext):
        return None

    # boolean_literal: TRUE | FALSE ;
    def visitBoolean_literal(self,ctx:BKITParser.Boolean_literalContext):
        return None

    # array_list: literal COMMA array_list | literal;
    def visitArray(self,ctx:BKITParser.ArrayContext):
        return None

    # array_list: literal COMMA array_list | literal;
    def visitArray_list(self,ctx:BKITParser.Array_listContext):
        return None

    # body_decl: init_body body;
    def visitBody_decl(self,ctx:BKITParser.Body_declContext):
        return None

    # init_body: FUNCTION COLON ID parameter;
    def visitInit_body(self,ctx:BKITParser.Init_bodyContext):
        return None

    # parameter_list: variable COMMA parameter_list | variable;
    def visitParameter(self,ctx:BKITParser.ParameterContext):
        return None

    # body: BODY COLON var_list stmt_list ENDBODY DOT;
    def visitBody(self,ctx:BKITParser.BodyContext):
        return None

    # return_stmt: RETURN exp? SEMI;
    def visitStmt(self,ctx:BKITParser.StmtContext):
        return None

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitStmt_list(self,ctx:BKITParser.Stmt_listContext):
        return None

    # assign_stmt: ID index_operators? ASSIGN exp SEMI;
    def visitAssign_stmt(self,ctx:BKITParser.Assign_stmtContext):
        return None

    # if_stmt: IF exp THEN stmt_list else_if (ELSE stmt_list)? ENDIF DOT;
    def visitIf_stmt(self,ctx:BKITParser.If_stmtContext):
        return None

    # for_stmt: FOR LEFT_PAREN for_condition RIGHT_PAREN DO stmt_list ENDFOR DOT;
    def visitFor_stmt(self,ctx:BKITParser.For_stmtContext):
        return None

    # for_condition: ID ASSIGN exp COMMA exp COMMA exp;
    def visitFor_condition(self,ctx:BKITParser.For_conditionContext):
        return None

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitWhile_stmt(self,ctx:BKITParser.While_stmtContext):
        return None

    # do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;
    def visitDo_while_stmt(self,ctx:BKITParser.Do_while_stmtContext):
        return None

    # break_stmt: BREAK SEMI;
    def visitBreak_stmt(self,ctx:BKITParser.Break_stmtContext):
        return None

    # continue_stmt: CONTINUE SEMI;
    def visitContinue_stmt(self,ctx:BKITParser.Continue_stmtContext):
        return None

    # call_stmt: ID LEFT_PAREN exp_list? RIGHT_PAREN SEMI;
    def visitCall_stmt(self,ctx:BKITParser.Call_stmtContext):
        return None

    # return_stmt: RETURN exp? SEMI;
    def visitReturn_stmt(self,ctx:BKITParser.Return_stmtContext):
        return None

    # expr_index: ID | function_call;
    def visitFunction_call(self,ctx:BKITParser.Function_callContext):
        return None

    # expr_index: ID | function_call;
    def visitExp(self,ctx:BKITParser.ExpContext):
        return None

    # exp1: exp1 boolean_operators exp2 | exp2;
    def visitExp1(self,ctx:BKITParser.Exp1Context):
        return None

    # exp2: exp2 adding_operators exp3 | exp3;
    def visitExp2(self,ctx:BKITParser.Exp2Context):
        return None

    # exp3: exp3 multiplying_operators exp4 | exp4;
    def visitExp3(self,ctx:BKITParser.Exp3Context):
        return None

    # exp4: NOT exp4 | exp5;
    def visitExp4(self,ctx:BKITParser.Exp4Context):
        return None

    # exp5: sign_operators exp5 | exp6;
    def visitExp5(self,ctx:BKITParser.Exp5Context):
        return None

    # exp6: exp6 index_operators | exp7;
    def visitExp6(self,ctx:BKITParser.Exp6Context):
        return None

    # exp7: function_call | LEFT_PAREN exp RIGHT_PAREN | operands;
    def visitExp7(self,ctx:BKITParser.Exp7Context):
        return None

    # exp_list: exp COMMA exp_list | exp;
    def visitExp_list(self,ctx:BKITParser.Exp_listContext):
        return None

    # operands: ID | literal | element_exp;
    def visitOperands(self,ctx:BKITParser.OperandsContext):
        return None

    # multiplying_operators: MULTI | MULTI_F | DIV | DIV_F | MOD;
    def visitMultiplying_operators(self,ctx:BKITParser.Multiplying_operatorsContext):
        return None

    # adding_operators: ADD | ADD_F | SUB | SUB_F;
    def visitAdding_operators(self,ctx:BKITParser.Adding_operatorsContext):
        return None

    # sign_operators: SUB| SUB_F;
    def visitSign_operators(self,ctx:BKITParser.Sign_operatorsContext):
        return None

    # boolean_operators: ANDAND | OROR;
    def visitBoolean_operators(self,ctx:BKITParser.Boolean_operatorsContext):
        return None

    # relational_operators: EQUAL | NOT_EQUAL | LESS_THAN | GREATER_THAN | GREATER_EQUAL | LESS_EQUAL | NOT_EQUAL_F | LESS_THAN_F | GREATER_THAN_F | GREATER_EQUAL_F | LESS_EQUAL_F;
    def visitRelational_operators(self,ctx:BKITParser.Relational_operatorsContext):
        return None

    # element_exp: expr_index index_operators;
    def visitElement_exp(self,ctx:BKITParser.Element_expContext):
        return None

    # index_operators: LEFT_BRACKET exp RIGHT_BRACKET | LEFT_BRACKET exp RIGHT_BRACKET index_operators;
    def visitIndex_operators(self,ctx:BKITParser.Index_operatorsContext):
        return None

    # expr_index: ID | function_call;
    def visitExpr_index(self,ctx:BKITParser.Expr_indexContext):
        return None

