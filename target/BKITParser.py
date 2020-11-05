# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3I")
        buf.write("\u01ba\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\3\2\7\2`\n\2\f\2\16\2c\13\2\3\2\7\2f\n\2\f\2\16\2")
        buf.write("i\13\2\3\2\7\2l\n\2\f\2\16\2o\13\2\3\2\7\2r\n\2\f\2\16")
        buf.write("\2u\13\2\3\2\7\2x\n\2\f\2\16\2{\13\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u0084\n\3\3\3\3\3\3\3\3\3\5\3\u008a\n\3")
        buf.write("\7\3\u008c\n\3\f\3\16\3\u008f\13\3\3\3\3\3\3\4\3\4\5\4")
        buf.write("\u0095\n\4\3\4\3\4\3\4\3\4\5\4\u009b\n\4\3\5\3\5\6\5\u009f")
        buf.write("\n\5\r\5\16\5\u00a0\3\6\3\6\3\6\3\6\3\7\3\7\3\7\7\7\u00aa")
        buf.write("\n\7\f\7\16\7\u00ad\13\7\3\b\3\b\3\b\3\b\3\b\5\b\u00b4")
        buf.write("\n\b\3\t\3\t\3\n\3\n\3\13\3\13\5\13\u00bc\n\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\7\f\u00c3\n\f\f\f\16\f\u00c6\13\f\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00cf\n\16\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\7\20\u00d8\n\20\f\20\16\20\u00db")
        buf.write("\13\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\5\21\u00ea\n\21\3\22\7\22\u00ed\n\22")
        buf.write("\f\22\16\22\u00f0\13\22\3\23\3\23\5\23\u00f4\n\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\7\24\u0103\n\24\f\24\16\24\u0106\13\24\3\24\3\24")
        buf.write("\5\24\u010a\n\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\5\33\u0137\n\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\5\34\u013e\n\34\3\34\3\34\3\35\3\35\3\35\5\35\u0145")
        buf.write("\n\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\5\36\u014e\n")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37\u0157\n\37")
        buf.write("\f\37\16\37\u015a\13\37\3 \3 \3 \3 \3 \3 \3 \7 \u0163")
        buf.write("\n \f \16 \u0166\13 \3!\3!\3!\3!\3!\3!\3!\7!\u016f\n!")
        buf.write("\f!\16!\u0172\13!\3\"\3\"\3\"\5\"\u0177\n\"\3#\3#\3#\3")
        buf.write("#\5#\u017d\n#\3$\3$\3$\3$\3$\7$\u0184\n$\f$\16$\u0187")
        buf.write("\13$\3%\3%\3%\3%\3%\3%\5%\u018f\n%\3&\3&\3&\7&\u0194\n")
        buf.write("&\f&\16&\u0197\13&\3\'\3\'\3\'\5\'\u019c\n\'\3(\3(\3)")
        buf.write("\3)\3*\3*\3+\3+\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\5.\u01b4\n.\3/\3/\5/\u01b8\n/\3/\2\6<>@F\60\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\\2\t\3\2?A\3\2\26\27\3\2!%\3\2\35")
        buf.write(" \3\2\37 \3\2\'(\3\2)\63\2\u01bd\2a\3\2\2\2\4~\3\2\2\2")
        buf.write("\6\u009a\3\2\2\2\b\u009c\3\2\2\2\n\u00a2\3\2\2\2\f\u00a6")
        buf.write("\3\2\2\2\16\u00b3\3\2\2\2\20\u00b5\3\2\2\2\22\u00b7\3")
        buf.write("\2\2\2\24\u00b9\3\2\2\2\26\u00bf\3\2\2\2\30\u00c7\3\2")
        buf.write("\2\2\32\u00ca\3\2\2\2\34\u00d0\3\2\2\2\36\u00d4\3\2\2")
        buf.write("\2 \u00e9\3\2\2\2\"\u00ee\3\2\2\2$\u00f1\3\2\2\2&\u00f9")
        buf.write("\3\2\2\2(\u010e\3\2\2\2*\u0117\3\2\2\2,\u011f\3\2\2\2")
        buf.write(".\u0126\3\2\2\2\60\u012d\3\2\2\2\62\u0130\3\2\2\2\64\u0133")
        buf.write("\3\2\2\2\66\u013b\3\2\2\28\u0141\3\2\2\2:\u014d\3\2\2")
        buf.write("\2<\u014f\3\2\2\2>\u015b\3\2\2\2@\u0167\3\2\2\2B\u0176")
        buf.write("\3\2\2\2D\u017c\3\2\2\2F\u017e\3\2\2\2H\u018e\3\2\2\2")
        buf.write("J\u0190\3\2\2\2L\u019b\3\2\2\2N\u019d\3\2\2\2P\u019f\3")
        buf.write("\2\2\2R\u01a1\3\2\2\2T\u01a3\3\2\2\2V\u01a5\3\2\2\2X\u01a7")
        buf.write("\3\2\2\2Z\u01b3\3\2\2\2\\\u01b7\3\2\2\2^`\7E\2\2_^\3\2")
        buf.write("\2\2`c\3\2\2\2a_\3\2\2\2ab\3\2\2\2bg\3\2\2\2ca\3\2\2\2")
        buf.write("df\5\4\3\2ed\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh\3\2\2\2hm\3")
        buf.write("\2\2\2ig\3\2\2\2jl\7E\2\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2")
        buf.write("\2mn\3\2\2\2ns\3\2\2\2om\3\2\2\2pr\5\30\r\2qp\3\2\2\2")
        buf.write("ru\3\2\2\2sq\3\2\2\2st\3\2\2\2ty\3\2\2\2us\3\2\2\2vx\7")
        buf.write("E\2\2wv\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z|\3\2\2")
        buf.write("\2{y\3\2\2\2|}\7\2\2\3}\3\3\2\2\2~\177\7\4\2\2\177\u0080")
        buf.write("\7\65\2\2\u0080\u0083\5\6\4\2\u0081\u0082\7>\2\2\u0082")
        buf.write("\u0084\5\f\7\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\u008d\3\2\2\2\u0085\u0086\7\67\2\2\u0086\u0089")
        buf.write("\5\6\4\2\u0087\u0088\7>\2\2\u0088\u008a\5\f\7\2\u0089")
        buf.write("\u0087\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008c\3\2\2\2")
        buf.write("\u008b\u0085\3\2\2\2\u008c\u008f\3\2\2\2\u008d\u008b\3")
        buf.write("\2\2\2\u008d\u008e\3\2\2\2\u008e\u0090\3\2\2\2\u008f\u008d")
        buf.write("\3\2\2\2\u0090\u0091\7\64\2\2\u0091\5\3\2\2\2\u0092\u0095")
        buf.write("\7\3\2\2\u0093\u0095\5\b\5\2\u0094\u0092\3\2\2\2\u0094")
        buf.write("\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0097\7\67\2")
        buf.write("\2\u0097\u009b\5\6\4\2\u0098\u009b\7\3\2\2\u0099\u009b")
        buf.write("\5\b\5\2\u009a\u0094\3\2\2\2\u009a\u0098\3\2\2\2\u009a")
        buf.write("\u0099\3\2\2\2\u009b\7\3\2\2\2\u009c\u009e\7\3\2\2\u009d")
        buf.write("\u009f\5\n\6\2\u009e\u009d\3\2\2\2\u009f\u00a0\3\2\2\2")
        buf.write("\u00a0\u009e\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\t\3\2\2")
        buf.write("\2\u00a2\u00a3\7:\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5")
        buf.write("\7;\2\2\u00a5\13\3\2\2\2\u00a6\u00ab\5\16\b\2\u00a7\u00a8")
        buf.write("\7\67\2\2\u00a8\u00aa\5\16\b\2\u00a9\u00a7\3\2\2\2\u00aa")
        buf.write("\u00ad\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00ac\3\2\2\2")
        buf.write("\u00ac\r\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ae\u00b4\5\24")
        buf.write("\13\2\u00af\u00b4\5\20\t\2\u00b0\u00b4\7B\2\2\u00b1\u00b4")
        buf.write("\5\22\n\2\u00b2\u00b4\7D\2\2\u00b3\u00ae\3\2\2\2\u00b3")
        buf.write("\u00af\3\2\2\2\u00b3\u00b0\3\2\2\2\u00b3\u00b1\3\2\2\2")
        buf.write("\u00b3\u00b2\3\2\2\2\u00b4\17\3\2\2\2\u00b5\u00b6\t\2")
        buf.write("\2\2\u00b6\21\3\2\2\2\u00b7\u00b8\t\3\2\2\u00b8\23\3\2")
        buf.write("\2\2\u00b9\u00bb\7<\2\2\u00ba\u00bc\5\26\f\2\u00bb\u00ba")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd")
        buf.write("\u00be\7=\2\2\u00be\25\3\2\2\2\u00bf\u00c4\5\16\b\2\u00c0")
        buf.write("\u00c1\7\67\2\2\u00c1\u00c3\5\16\b\2\u00c2\u00c0\3\2\2")
        buf.write("\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\27\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c8")
        buf.write("\5\32\16\2\u00c8\u00c9\5\36\20\2\u00c9\31\3\2\2\2\u00ca")
        buf.write("\u00cb\7\20\2\2\u00cb\u00cc\7\65\2\2\u00cc\u00ce\7\3\2")
        buf.write("\2\u00cd\u00cf\5\34\17\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf")
        buf.write("\3\2\2\2\u00cf\33\3\2\2\2\u00d0\u00d1\7\22\2\2\u00d1\u00d2")
        buf.write("\7\65\2\2\u00d2\u00d3\5\6\4\2\u00d3\35\3\2\2\2\u00d4\u00d5")
        buf.write("\7\5\2\2\u00d5\u00d9\7\65\2\2\u00d6\u00d8\5\4\3\2\u00d7")
        buf.write("\u00d6\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00dd\5\"\22\2\u00dd\u00de\7\13\2\2\u00de")
        buf.write("\u00df\7\66\2\2\u00df\37\3\2\2\2\u00e0\u00ea\5$\23\2\u00e1")
        buf.write("\u00ea\5&\24\2\u00e2\u00ea\5(\25\2\u00e3\u00ea\5,\27\2")
        buf.write("\u00e4\u00ea\5.\30\2\u00e5\u00ea\5\60\31\2\u00e6\u00ea")
        buf.write("\5\62\32\2\u00e7\u00ea\5\64\33\2\u00e8\u00ea\5\66\34\2")
        buf.write("\u00e9\u00e0\3\2\2\2\u00e9\u00e1\3\2\2\2\u00e9\u00e2\3")
        buf.write("\2\2\2\u00e9\u00e3\3\2\2\2\u00e9\u00e4\3\2\2\2\u00e9\u00e5")
        buf.write("\3\2\2\2\u00e9\u00e6\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea!\3\2\2\2\u00eb\u00ed\5 \21\2\u00ec")
        buf.write("\u00eb\3\2\2\2\u00ed\u00f0\3\2\2\2\u00ee\u00ec\3\2\2\2")
        buf.write("\u00ee\u00ef\3\2\2\2\u00ef#\3\2\2\2\u00f0\u00ee\3\2\2")
        buf.write("\2\u00f1\u00f3\7\3\2\2\u00f2\u00f4\5Z.\2\u00f3\u00f2\3")
        buf.write("\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6")
        buf.write("\7>\2\2\u00f6\u00f7\5:\36\2\u00f7\u00f8\7\64\2\2\u00f8")
        buf.write("%\3\2\2\2\u00f9\u00fa\7\21\2\2\u00fa\u00fb\5:\36\2\u00fb")
        buf.write("\u00fc\7\24\2\2\u00fc\u0104\5\"\22\2\u00fd\u00fe\7\n\2")
        buf.write("\2\u00fe\u00ff\5:\36\2\u00ff\u0100\7\24\2\2\u0100\u0101")
        buf.write("\5\"\22\2\u0101\u0103\3\2\2\2\u0102\u00fd\3\2\2\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0109\3\2\2\2\u0106\u0104\3\2\2\2\u0107\u0108\7")
        buf.write("\t\2\2\u0108\u010a\5\"\22\2\u0109\u0107\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\7\f\2\2")
        buf.write("\u010c\u010d\7\66\2\2\u010d\'\3\2\2\2\u010e\u010f\7\17")
        buf.write("\2\2\u010f\u0110\78\2\2\u0110\u0111\5*\26\2\u0111\u0112")
        buf.write("\79\2\2\u0112\u0113\7\b\2\2\u0113\u0114\5\"\22\2\u0114")
        buf.write("\u0115\7\r\2\2\u0115\u0116\7\66\2\2\u0116)\3\2\2\2\u0117")
        buf.write("\u0118\7\3\2\2\u0118\u0119\7>\2\2\u0119\u011a\5:\36\2")
        buf.write("\u011a\u011b\7\67\2\2\u011b\u011c\5:\36\2\u011c\u011d")
        buf.write("\7\67\2\2\u011d\u011e\5:\36\2\u011e+\3\2\2\2\u011f\u0120")
        buf.write("\7\25\2\2\u0120\u0121\5:\36\2\u0121\u0122\7\b\2\2\u0122")
        buf.write("\u0123\5\"\22\2\u0123\u0124\7\16\2\2\u0124\u0125\7\66")
        buf.write("\2\2\u0125-\3\2\2\2\u0126\u0127\7\b\2\2\u0127\u0128\5")
        buf.write("\"\22\2\u0128\u0129\7\25\2\2\u0129\u012a\5:\36\2\u012a")
        buf.write("\u012b\7\30\2\2\u012b\u012c\7\66\2\2\u012c/\3\2\2\2\u012d")
        buf.write("\u012e\7\6\2\2\u012e\u012f\7\64\2\2\u012f\61\3\2\2\2\u0130")
        buf.write("\u0131\7\7\2\2\u0131\u0132\7\64\2\2\u0132\63\3\2\2\2\u0133")
        buf.write("\u0134\7\3\2\2\u0134\u0136\78\2\2\u0135\u0137\5J&\2\u0136")
        buf.write("\u0135\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\3\2\2\2")
        buf.write("\u0138\u0139\79\2\2\u0139\u013a\7\64\2\2\u013a\65\3\2")
        buf.write("\2\2\u013b\u013d\7\23\2\2\u013c\u013e\5:\36\2\u013d\u013c")
        buf.write("\3\2\2\2\u013d\u013e\3\2\2\2\u013e\u013f\3\2\2\2\u013f")
        buf.write("\u0140\7\64\2\2\u0140\67\3\2\2\2\u0141\u0142\7\3\2\2\u0142")
        buf.write("\u0144\78\2\2\u0143\u0145\5J&\2\u0144\u0143\3\2\2\2\u0144")
        buf.write("\u0145\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0147\79\2\2")
        buf.write("\u01479\3\2\2\2\u0148\u0149\5<\37\2\u0149\u014a\5V,\2")
        buf.write("\u014a\u014b\5<\37\2\u014b\u014e\3\2\2\2\u014c\u014e\5")
        buf.write("<\37\2\u014d\u0148\3\2\2\2\u014d\u014c\3\2\2\2\u014e;")
        buf.write("\3\2\2\2\u014f\u0150\b\37\1\2\u0150\u0151\5> \2\u0151")
        buf.write("\u0158\3\2\2\2\u0152\u0153\f\4\2\2\u0153\u0154\5T+\2\u0154")
        buf.write("\u0155\5> \2\u0155\u0157\3\2\2\2\u0156\u0152\3\2\2\2\u0157")
        buf.write("\u015a\3\2\2\2\u0158\u0156\3\2\2\2\u0158\u0159\3\2\2\2")
        buf.write("\u0159=\3\2\2\2\u015a\u0158\3\2\2\2\u015b\u015c\b \1\2")
        buf.write("\u015c\u015d\5@!\2\u015d\u0164\3\2\2\2\u015e\u015f\f\4")
        buf.write("\2\2\u015f\u0160\5P)\2\u0160\u0161\5@!\2\u0161\u0163\3")
        buf.write("\2\2\2\u0162\u015e\3\2\2\2\u0163\u0166\3\2\2\2\u0164\u0162")
        buf.write("\3\2\2\2\u0164\u0165\3\2\2\2\u0165?\3\2\2\2\u0166\u0164")
        buf.write("\3\2\2\2\u0167\u0168\b!\1\2\u0168\u0169\5B\"\2\u0169\u0170")
        buf.write("\3\2\2\2\u016a\u016b\f\4\2\2\u016b\u016c\5N(\2\u016c\u016d")
        buf.write("\5B\"\2\u016d\u016f\3\2\2\2\u016e\u016a\3\2\2\2\u016f")
        buf.write("\u0172\3\2\2\2\u0170\u016e\3\2\2\2\u0170\u0171\3\2\2\2")
        buf.write("\u0171A\3\2\2\2\u0172\u0170\3\2\2\2\u0173\u0174\7&\2\2")
        buf.write("\u0174\u0177\5B\"\2\u0175\u0177\5D#\2\u0176\u0173\3\2")
        buf.write("\2\2\u0176\u0175\3\2\2\2\u0177C\3\2\2\2\u0178\u0179\5")
        buf.write("R*\2\u0179\u017a\5D#\2\u017a\u017d\3\2\2\2\u017b\u017d")
        buf.write("\5F$\2\u017c\u0178\3\2\2\2\u017c\u017b\3\2\2\2\u017dE")
        buf.write("\3\2\2\2\u017e\u017f\b$\1\2\u017f\u0180\5H%\2\u0180\u0185")
        buf.write("\3\2\2\2\u0181\u0182\f\4\2\2\u0182\u0184\5Z.\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u0187\3\2\2\2\u0185\u0183\3\2\2\2\u0185")
        buf.write("\u0186\3\2\2\2\u0186G\3\2\2\2\u0187\u0185\3\2\2\2\u0188")
        buf.write("\u018f\58\35\2\u0189\u018a\78\2\2\u018a\u018b\5:\36\2")
        buf.write("\u018b\u018c\79\2\2\u018c\u018f\3\2\2\2\u018d\u018f\5")
        buf.write("L\'\2\u018e\u0188\3\2\2\2\u018e\u0189\3\2\2\2\u018e\u018d")
        buf.write("\3\2\2\2\u018fI\3\2\2\2\u0190\u0195\5:\36\2\u0191\u0192")
        buf.write("\7\67\2\2\u0192\u0194\5:\36\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196K\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019c\7\3\2")
        buf.write("\2\u0199\u019c\5\16\b\2\u019a\u019c\5X-\2\u019b\u0198")
        buf.write("\3\2\2\2\u019b\u0199\3\2\2\2\u019b\u019a\3\2\2\2\u019c")
        buf.write("M\3\2\2\2\u019d\u019e\t\4\2\2\u019eO\3\2\2\2\u019f\u01a0")
        buf.write("\t\5\2\2\u01a0Q\3\2\2\2\u01a1\u01a2\t\6\2\2\u01a2S\3\2")
        buf.write("\2\2\u01a3\u01a4\t\7\2\2\u01a4U\3\2\2\2\u01a5\u01a6\t")
        buf.write("\b\2\2\u01a6W\3\2\2\2\u01a7\u01a8\5\\/\2\u01a8\u01a9\5")
        buf.write("Z.\2\u01a9Y\3\2\2\2\u01aa\u01ab\7:\2\2\u01ab\u01ac\5:")
        buf.write("\36\2\u01ac\u01ad\7;\2\2\u01ad\u01b4\3\2\2\2\u01ae\u01af")
        buf.write("\7:\2\2\u01af\u01b0\5:\36\2\u01b0\u01b1\7;\2\2\u01b1\u01b2")
        buf.write("\5Z.\2\u01b2\u01b4\3\2\2\2\u01b3\u01aa\3\2\2\2\u01b3\u01ae")
        buf.write("\3\2\2\2\u01b4[\3\2\2\2\u01b5\u01b8\7\3\2\2\u01b6\u01b8")
        buf.write("\58\35\2\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8")
        buf.write("]\3\2\2\2\'agmsy\u0083\u0089\u008d\u0094\u009a\u00a0\u00ab")
        buf.write("\u00b3\u00bb\u00c4\u00ce\u00d9\u00e9\u00ee\u00f3\u0104")
        buf.write("\u0109\u0136\u013d\u0144\u014d\u0158\u0164\u0170\u0176")
        buf.write("\u017c\u0185\u018e\u0195\u019b\u01b3\u01b7")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Var'", "'Body'", "'Break'", 
                     "'Continue'", "'Do'", "'Else'", "'ElseIf'", "'EndBody'", 
                     "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
                     "'If'", "'Parameter'", "'Return'", "'Then'", "'While'", 
                     "'True'", "'False'", "'EndDo'", "'int'", "'float'", 
                     "'boolean'", "'string'", "'+'", "'+.'", "'-'", "'-.'", 
                     "'*'", "'*.'", "'\\'", "'\\.'", "'%'", "'!'", "'&&'", 
                     "'||'", "'=='", "'!='", "'<'", "'>'", "'>='", "'<='", 
                     "'=/='", "'<.'", "'>.'", "'>=.'", "'<=.'", "';'", "':'", 
                     "'.'", "','", "'('", "')'", "'['", "']'", "'{'", "'}'", 
                     "'='" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR", "BODY", "BREAK", "CONTINUE", 
                      "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", 
                      "ENDWHILE", "FOR", "FUNCTION", "IF", "PARAMETER", 
                      "RETURN", "THEN", "WHILE", "TRUE", "FALSE", "ENDDO", 
                      "INT_TYPE", "FLOAT_TYPE", "BOOLEAN_TYPE", "STRING_TYPE", 
                      "ADD", "ADD_F", "SUB", "SUB_F", "MULTI", "MULTI_F", 
                      "DIV", "DIV_F", "MOD", "NOT", "ANDAND", "OROR", "EQUAL", 
                      "NOT_EQUAL", "LESS_THAN", "GREATER_THAN", "GREATER_EQUAL", 
                      "LESS_EQUAL", "NOT_EQUAL_F", "LESS_THAN_F", "GREATER_THAN_F", 
                      "GREATER_EQUAL_F", "LESS_EQUAL_F", "SEMI", "COLON", 
                      "DOT", "COMMA", "LEFT_PAREN", "RIGHT_PAREN", "LEFT_BRACKET", 
                      "RIGHT_BRACKET", "LEFT_BRACE", "RIGHT_BRACE", "ASSIGN", 
                      "DECIMAL_INTEGER", "HEX_INTEGER", "OCT_INTEGER", "FLOAT", 
                      "BOOLEAN", "STRING", "SKIP_", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_variable_decl = 1
    RULE_variable_list = 2
    RULE_array_decl = 3
    RULE_dimension = 4
    RULE_init_value = 5
    RULE_literal = 6
    RULE_integer = 7
    RULE_boolean_literal = 8
    RULE_array = 9
    RULE_array_list = 10
    RULE_body_decl = 11
    RULE_init_body = 12
    RULE_parameter = 13
    RULE_body = 14
    RULE_stmt = 15
    RULE_stmt_list = 16
    RULE_assign_stmt = 17
    RULE_if_stmt = 18
    RULE_for_stmt = 19
    RULE_for_condition = 20
    RULE_while_stmt = 21
    RULE_do_while_stmt = 22
    RULE_break_stmt = 23
    RULE_continue_stmt = 24
    RULE_call_stmt = 25
    RULE_return_stmt = 26
    RULE_function_call = 27
    RULE_exp = 28
    RULE_exp1 = 29
    RULE_exp2 = 30
    RULE_exp3 = 31
    RULE_exp4 = 32
    RULE_exp5 = 33
    RULE_exp6 = 34
    RULE_exp7 = 35
    RULE_exp_list = 36
    RULE_operands = 37
    RULE_multiplying_operators = 38
    RULE_adding_operators = 39
    RULE_sign_operators = 40
    RULE_boolean_operators = 41
    RULE_relational_operators = 42
    RULE_element_exp = 43
    RULE_index_operators = 44
    RULE_expr_index = 45

    ruleNames =  [ "program", "variable_decl", "variable_list", "array_decl", 
                   "dimension", "init_value", "literal", "integer", "boolean_literal", 
                   "array", "array_list", "body_decl", "init_body", "parameter", 
                   "body", "stmt", "stmt_list", "assign_stmt", "if_stmt", 
                   "for_stmt", "for_condition", "while_stmt", "do_while_stmt", 
                   "break_stmt", "continue_stmt", "call_stmt", "return_stmt", 
                   "function_call", "exp", "exp1", "exp2", "exp3", "exp4", 
                   "exp5", "exp6", "exp7", "exp_list", "operands", "multiplying_operators", 
                   "adding_operators", "sign_operators", "boolean_operators", 
                   "relational_operators", "element_exp", "index_operators", 
                   "expr_index" ]

    EOF = Token.EOF
    ID=1
    VAR=2
    BODY=3
    BREAK=4
    CONTINUE=5
    DO=6
    ELSE=7
    ELSEIF=8
    ENDBODY=9
    ENDIF=10
    ENDFOR=11
    ENDWHILE=12
    FOR=13
    FUNCTION=14
    IF=15
    PARAMETER=16
    RETURN=17
    THEN=18
    WHILE=19
    TRUE=20
    FALSE=21
    ENDDO=22
    INT_TYPE=23
    FLOAT_TYPE=24
    BOOLEAN_TYPE=25
    STRING_TYPE=26
    ADD=27
    ADD_F=28
    SUB=29
    SUB_F=30
    MULTI=31
    MULTI_F=32
    DIV=33
    DIV_F=34
    MOD=35
    NOT=36
    ANDAND=37
    OROR=38
    EQUAL=39
    NOT_EQUAL=40
    LESS_THAN=41
    GREATER_THAN=42
    GREATER_EQUAL=43
    LESS_EQUAL=44
    NOT_EQUAL_F=45
    LESS_THAN_F=46
    GREATER_THAN_F=47
    GREATER_EQUAL_F=48
    LESS_EQUAL_F=49
    SEMI=50
    COLON=51
    DOT=52
    COMMA=53
    LEFT_PAREN=54
    RIGHT_PAREN=55
    LEFT_BRACKET=56
    RIGHT_BRACKET=57
    LEFT_BRACE=58
    RIGHT_BRACE=59
    ASSIGN=60
    DECIMAL_INTEGER=61
    HEX_INTEGER=62
    OCT_INTEGER=63
    FLOAT=64
    BOOLEAN=65
    STRING=66
    SKIP_=67
    ERROR_CHAR=68
    UNCLOSE_STRING=69
    ILLEGAL_ESCAPE=70
    UNTERMINATED_COMMENT=71

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def SKIP_(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.SKIP_)
            else:
                return self.getToken(BKITParser.SKIP_, i)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def body_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Body_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Body_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 92
                    self.match(BKITParser.SKIP_) 
                self.state = 97
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 98
                self.variable_decl()
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 104
                    self.match(BKITParser.SKIP_) 
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 110
                self.body_decl()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.SKIP_:
                self.state = 116
                self.match(BKITParser.SKIP_)
                self.state = 121
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 122
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_listContext,i)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ASSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ASSIGN)
            else:
                return self.getToken(BKITParser.ASSIGN, i)

        def init_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Init_valueContext)
            else:
                return self.getTypedRuleContext(BKITParser.Init_valueContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_decl" ):
                return visitor.visitVariable_decl(self)
            else:
                return visitor.visitChildren(self)




    def variable_decl(self):

        localctx = BKITParser.Variable_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_variable_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(BKITParser.VAR)
            self.state = 125
            self.match(BKITParser.COLON)
            self.state = 126
            self.variable_list()
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 127
                self.match(BKITParser.ASSIGN)
                self.state = 128
                self.init_value()


            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 131
                self.match(BKITParser.COMMA)
                self.state = 132
                self.variable_list()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==BKITParser.ASSIGN:
                    self.state = 133
                    self.match(BKITParser.ASSIGN)
                    self.state = 134
                    self.init_value()


                self.state = 141
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 142
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKITParser.COMMA, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def array_decl(self):
            return self.getTypedRuleContext(BKITParser.Array_declContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_list" ):
                return visitor.visitVariable_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_list(self):

        localctx = BKITParser.Variable_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_list)
        try:
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 144
                    self.match(BKITParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 145
                    self.array_decl()
                    pass


                self.state = 148
                self.match(BKITParser.COMMA)
                self.state = 149
                self.variable_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 151
                self.array_decl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def dimension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.DimensionContext)
            else:
                return self.getTypedRuleContext(BKITParser.DimensionContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_array_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_decl" ):
                return visitor.visitArray_decl(self)
            else:
                return visitor.visitChildren(self)




    def array_decl(self):

        localctx = BKITParser.Array_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(BKITParser.ID)
            self.state = 156 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 155
                self.dimension()
                self.state = 158 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LEFT_BRACKET):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimensionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def integer(self):
            return self.getTypedRuleContext(BKITParser.IntegerContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_dimension

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimension" ):
                return visitor.visitDimension(self)
            else:
                return visitor.visitChildren(self)




    def dimension(self):

        localctx = BKITParser.DimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.match(BKITParser.LEFT_BRACKET)
            self.state = 161
            self.integer()
            self.state = 162
            self.match(BKITParser.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_init_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.literal()
            self.state = 169
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 165
                    self.match(BKITParser.COMMA)
                    self.state = 166
                    self.literal() 
                self.state = 171
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(BKITParser.ArrayContext,0)


        def integer(self):
            return self.getTypedRuleContext(BKITParser.IntegerContext,0)


        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def boolean_literal(self):
            return self.getTypedRuleContext(BKITParser.Boolean_literalContext,0)


        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_literal)
        try:
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LEFT_BRACE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.array()
                pass
            elif token in [BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.integer()
                pass
            elif token in [BKITParser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 174
                self.match(BKITParser.FLOAT)
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 175
                self.boolean_literal()
                pass
            elif token in [BKITParser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 176
                self.match(BKITParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL_INTEGER(self):
            return self.getToken(BKITParser.DECIMAL_INTEGER, 0)

        def HEX_INTEGER(self):
            return self.getToken(BKITParser.HEX_INTEGER, 0)

        def OCT_INTEGER(self):
            return self.getToken(BKITParser.OCT_INTEGER, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInteger" ):
                return visitor.visitInteger(self)
            else:
                return visitor.visitChildren(self)




    def integer(self):

        localctx = BKITParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_literal" ):
                return visitor.visitBoolean_literal(self)
            else:
                return visitor.visitChildren(self)




    def boolean_literal(self):

        localctx = BKITParser.Boolean_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_boolean_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==BKITParser.TRUE or _la==BKITParser.FALSE):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACE(self):
            return self.getToken(BKITParser.LEFT_BRACE, 0)

        def RIGHT_BRACE(self):
            return self.getToken(BKITParser.RIGHT_BRACE, 0)

        def array_list(self):
            return self.getTypedRuleContext(BKITParser.Array_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = BKITParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(BKITParser.LEFT_BRACE)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & ((1 << (BKITParser.TRUE - 20)) | (1 << (BKITParser.FALSE - 20)) | (1 << (BKITParser.LEFT_BRACE - 20)) | (1 << (BKITParser.DECIMAL_INTEGER - 20)) | (1 << (BKITParser.HEX_INTEGER - 20)) | (1 << (BKITParser.OCT_INTEGER - 20)) | (1 << (BKITParser.FLOAT - 20)) | (1 << (BKITParser.STRING - 20)))) != 0):
                self.state = 184
                self.array_list()


            self.state = 187
            self.match(BKITParser.RIGHT_BRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_list" ):
                return visitor.visitArray_list(self)
            else:
                return visitor.visitChildren(self)




    def array_list(self):

        localctx = BKITParser.Array_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_array_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.literal()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 190
                self.match(BKITParser.COMMA)
                self.state = 191
                self.literal()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def init_body(self):
            return self.getTypedRuleContext(BKITParser.Init_bodyContext,0)


        def body(self):
            return self.getTypedRuleContext(BKITParser.BodyContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_body_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_decl" ):
                return visitor.visitBody_decl(self)
            else:
                return visitor.visitChildren(self)




    def body_decl(self):

        localctx = BKITParser.Body_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.init_body()
            self.state = 198
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def parameter(self):
            return self.getTypedRuleContext(BKITParser.ParameterContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_init_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_body" ):
                return visitor.visitInit_body(self)
            else:
                return visitor.visitChildren(self)




    def init_body(self):

        localctx = BKITParser.Init_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_init_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(BKITParser.FUNCTION)
            self.state = 201
            self.match(BKITParser.COLON)
            self.state = 202
            self.match(BKITParser.ID)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 203
                self.parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def variable_list(self):
            return self.getTypedRuleContext(BKITParser.Variable_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = BKITParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(BKITParser.PARAMETER)
            self.state = 207
            self.match(BKITParser.COLON)
            self.state = 208
            self.variable_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def variable_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKITParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(BKITParser.BODY)
            self.state = 211
            self.match(BKITParser.COLON)
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 212
                self.variable_decl()
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 218
            self.stmt_list()
            self.state = 219
            self.match(BKITParser.ENDBODY)
            self.state = 220
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def do_while_stmt(self):
            return self.getTypedRuleContext(BKITParser.Do_while_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_stmt)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.assign_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.if_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.for_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.while_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 226
                self.do_while_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 227
                self.break_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 228
                self.continue_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 229
                self.call_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 230
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_list" ):
                return visitor.visitStmt_list(self)
            else:
                return visitor.visitChildren(self)




    def stmt_list(self):

        localctx = BKITParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_stmt_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 233
                    self.stmt() 
                self.state = 238
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKITParser.ID)
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.LEFT_BRACKET:
                self.state = 240
                self.index_operators()


            self.state = 243
            self.match(BKITParser.ASSIGN)
            self.state = 244
            self.exp()
            self.state = 245
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def THEN(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.THEN)
            else:
                return self.getToken(BKITParser.THEN, i)

        def stmt_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_listContext,i)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ELSEIF)
            else:
                return self.getToken(BKITParser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(BKITParser.IF)
            self.state = 248
            self.exp()
            self.state = 249
            self.match(BKITParser.THEN)
            self.state = 250
            self.stmt_list()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 251
                self.match(BKITParser.ELSEIF)
                self.state = 252
                self.exp()
                self.state = 253
                self.match(BKITParser.THEN)
                self.state = 254
                self.stmt_list()
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 261
                self.match(BKITParser.ELSE)
                self.state = 262
                self.stmt_list()


            self.state = 265
            self.match(BKITParser.ENDIF)
            self.state = 266
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def for_condition(self):
            return self.getTypedRuleContext(BKITParser.For_conditionContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(BKITParser.FOR)
            self.state = 269
            self.match(BKITParser.LEFT_PAREN)
            self.state = 270
            self.for_condition()
            self.state = 271
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 272
            self.match(BKITParser.DO)
            self.state = 273
            self.stmt_list()
            self.state = 274
            self.match(BKITParser.ENDFOR)
            self.state = 275
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_conditionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_for_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_condition" ):
                return visitor.visitFor_condition(self)
            else:
                return visitor.visitChildren(self)




    def for_condition(self):

        localctx = BKITParser.For_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_for_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(BKITParser.ID)
            self.state = 278
            self.match(BKITParser.ASSIGN)
            self.state = 279
            self.exp()
            self.state = 280
            self.match(BKITParser.COMMA)
            self.state = 281
            self.exp()
            self.state = 282
            self.match(BKITParser.COMMA)
            self.state = 283
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(BKITParser.WHILE)
            self.state = 286
            self.exp()
            self.state = 287
            self.match(BKITParser.DO)
            self.state = 288
            self.stmt_list()
            self.state = 289
            self.match(BKITParser.ENDWHILE)
            self.state = 290
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmt_list(self):
            return self.getTypedRuleContext(BKITParser.Stmt_listContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_do_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while_stmt" ):
                return visitor.visitDo_while_stmt(self)
            else:
                return visitor.visitChildren(self)




    def do_while_stmt(self):

        localctx = BKITParser.Do_while_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_do_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BKITParser.DO)
            self.state = 293
            self.stmt_list()
            self.state = 294
            self.match(BKITParser.WHILE)
            self.state = 295
            self.exp()
            self.state = 296
            self.match(BKITParser.ENDDO)
            self.state = 297
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(BKITParser.BREAK)
            self.state = 300
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(BKITParser.CONTINUE)
            self.state = 303
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_call_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(BKITParser.ID)
            self.state = 306
            self.match(BKITParser.LEFT_PAREN)
            self.state = 308
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 307
                self.exp_list()


            self.state = 310
            self.match(BKITParser.RIGHT_PAREN)
            self.state = 311
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(BKITParser.RETURN)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 314
                self.exp()


            self.state = 317
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def exp_list(self):
            return self.getTypedRuleContext(BKITParser.Exp_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = BKITParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(BKITParser.ID)
            self.state = 320
            self.match(BKITParser.LEFT_PAREN)
            self.state = 322
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ID) | (1 << BKITParser.TRUE) | (1 << BKITParser.FALSE) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F) | (1 << BKITParser.NOT) | (1 << BKITParser.LEFT_PAREN) | (1 << BKITParser.LEFT_BRACE) | (1 << BKITParser.DECIMAL_INTEGER) | (1 << BKITParser.HEX_INTEGER) | (1 << BKITParser.OCT_INTEGER))) != 0) or _la==BKITParser.FLOAT or _la==BKITParser.STRING:
                self.state = 321
                self.exp_list()


            self.state = 324
            self.match(BKITParser.RIGHT_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def relational_operators(self):
            return self.getTypedRuleContext(BKITParser.Relational_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp)
        try:
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.exp1(0)
                self.state = 327
                self.relational_operators()
                self.state = 328
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def boolean_operators(self):
            return self.getTypedRuleContext(BKITParser.Boolean_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exp1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 342
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 336
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 337
                    self.boolean_operators()
                    self.state = 338
                    self.exp2(0) 
                self.state = 344
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def adding_operators(self):
            return self.getTypedRuleContext(BKITParser.Adding_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 354
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 349
                    self.adding_operators()
                    self.state = 350
                    self.exp3(0) 
                self.state = 356
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def multiplying_operators(self):
            return self.getTypedRuleContext(BKITParser.Multiplying_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp3, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 366
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 360
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 361
                    self.multiplying_operators()
                    self.state = 362
                    self.exp4() 
                self.state = 368
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_exp4)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(BKITParser.NOT)
                self.state = 370
                self.exp4()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUB_F, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE, BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_operators(self):
            return self.getTypedRuleContext(BKITParser.Sign_operatorsContext,0)


        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp5)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUB_F]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.sign_operators()
                self.state = 375
                self.exp5()
                pass
            elif token in [BKITParser.ID, BKITParser.TRUE, BKITParser.FALSE, BKITParser.LEFT_PAREN, BKITParser.LEFT_BRACE, BKITParser.DECIMAL_INTEGER, BKITParser.HEX_INTEGER, BKITParser.OCT_INTEGER, BKITParser.FLOAT, BKITParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.exp6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exp7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 387
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.index_operators() 
                self.state = 389
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def LEFT_PAREN(self):
            return self.getToken(BKITParser.LEFT_PAREN, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(BKITParser.RIGHT_PAREN, 0)

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp7" ):
                return visitor.visitExp7(self)
            else:
                return visitor.visitChildren(self)




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_exp7)
        try:
            self.state = 396
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.function_call()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 391
                self.match(BKITParser.LEFT_PAREN)
                self.state = 392
                self.exp()
                self.state = 393
                self.match(BKITParser.RIGHT_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 395
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_exp_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_list" ):
                return visitor.visitExp_list(self)
            else:
                return visitor.visitChildren(self)




    def exp_list(self):

        localctx = BKITParser.Exp_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_exp_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp()
            self.state = 403
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 399
                self.match(BKITParser.COMMA)
                self.state = 400
                self.exp()
                self.state = 405
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def element_exp(self):
            return self.getTypedRuleContext(BKITParser.Element_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operands)
        try:
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 406
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 407
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 408
                self.element_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multiplying_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(BKITParser.MULTI, 0)

        def MULTI_F(self):
            return self.getToken(BKITParser.MULTI_F, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def DIV_F(self):
            return self.getToken(BKITParser.DIV_F, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multiplying_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplying_operators" ):
                return visitor.visitMultiplying_operators(self)
            else:
                return visitor.visitChildren(self)




    def multiplying_operators(self):

        localctx = BKITParser.Multiplying_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_multiplying_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MULTI) | (1 << BKITParser.MULTI_F) | (1 << BKITParser.DIV) | (1 << BKITParser.DIV_F) | (1 << BKITParser.MOD))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Adding_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def ADD_F(self):
            return self.getToken(BKITParser.ADD_F, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_adding_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdding_operators" ):
                return visitor.visitAdding_operators(self)
            else:
                return visitor.visitChildren(self)




    def adding_operators(self):

        localctx = BKITParser.Adding_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_adding_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.ADD_F) | (1 << BKITParser.SUB) | (1 << BKITParser.SUB_F))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUB_F(self):
            return self.getToken(BKITParser.SUB_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_sign_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_operators" ):
                return visitor.visitSign_operators(self)
            else:
                return visitor.visitChildren(self)




    def sign_operators(self):

        localctx = BKITParser.Sign_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_sign_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            _la = self._input.LA(1)
            if not(_la==BKITParser.SUB or _la==BKITParser.SUB_F):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ANDAND(self):
            return self.getToken(BKITParser.ANDAND, 0)

        def OROR(self):
            return self.getToken(BKITParser.OROR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_boolean_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_operators" ):
                return visitor.visitBoolean_operators(self)
            else:
                return visitor.visitChildren(self)




    def boolean_operators(self):

        localctx = BKITParser.Boolean_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_boolean_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            _la = self._input.LA(1)
            if not(_la==BKITParser.ANDAND or _la==BKITParser.OROR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Relational_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(BKITParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(BKITParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(BKITParser.LESS_THAN, 0)

        def GREATER_THAN(self):
            return self.getToken(BKITParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(BKITParser.GREATER_EQUAL, 0)

        def LESS_EQUAL(self):
            return self.getToken(BKITParser.LESS_EQUAL, 0)

        def NOT_EQUAL_F(self):
            return self.getToken(BKITParser.NOT_EQUAL_F, 0)

        def LESS_THAN_F(self):
            return self.getToken(BKITParser.LESS_THAN_F, 0)

        def GREATER_THAN_F(self):
            return self.getToken(BKITParser.GREATER_THAN_F, 0)

        def GREATER_EQUAL_F(self):
            return self.getToken(BKITParser.GREATER_EQUAL_F, 0)

        def LESS_EQUAL_F(self):
            return self.getToken(BKITParser.LESS_EQUAL_F, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_relational_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelational_operators" ):
                return visitor.visitRelational_operators(self)
            else:
                return visitor.visitChildren(self)




    def relational_operators(self):

        localctx = BKITParser.Relational_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_relational_operators)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.EQUAL) | (1 << BKITParser.NOT_EQUAL) | (1 << BKITParser.LESS_THAN) | (1 << BKITParser.GREATER_THAN) | (1 << BKITParser.GREATER_EQUAL) | (1 << BKITParser.LESS_EQUAL) | (1 << BKITParser.NOT_EQUAL_F) | (1 << BKITParser.LESS_THAN_F) | (1 << BKITParser.GREATER_THAN_F) | (1 << BKITParser.GREATER_EQUAL_F) | (1 << BKITParser.LESS_EQUAL_F))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Element_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_index(self):
            return self.getTypedRuleContext(BKITParser.Expr_indexContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_element_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement_exp" ):
                return visitor.visitElement_exp(self)
            else:
                return visitor.visitChildren(self)




    def element_exp(self):

        localctx = BKITParser.Element_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_element_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.expr_index()
            self.state = 422
            self.index_operators()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_BRACKET(self):
            return self.getToken(BKITParser.LEFT_BRACKET, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RIGHT_BRACKET(self):
            return self.getToken(BKITParser.RIGHT_BRACKET, 0)

        def index_operators(self):
            return self.getTypedRuleContext(BKITParser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)




    def index_operators(self):

        localctx = BKITParser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_index_operators)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 425
                self.exp()
                self.state = 426
                self.match(BKITParser.RIGHT_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.match(BKITParser.LEFT_BRACKET)
                self.state = 429
                self.exp()
                self.state = 430
                self.match(BKITParser.RIGHT_BRACKET)
                self.state = 431
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def function_call(self):
            return self.getTypedRuleContext(BKITParser.Function_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expr_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_index" ):
                return visitor.visitExpr_index(self)
            else:
                return visitor.visitChildren(self)




    def expr_index(self):

        localctx = BKITParser.Expr_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr_index)
        try:
            self.state = 437
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.function_call()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[29] = self.exp1_sempred
        self._predicates[30] = self.exp2_sempred
        self._predicates[31] = self.exp3_sempred
        self._predicates[34] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




