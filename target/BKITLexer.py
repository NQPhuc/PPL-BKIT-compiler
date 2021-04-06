# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u01fe\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\7")
        buf.write("\2\u0098\n\2\f\2\16\2\u009b\13\2\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3#\3$\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3)\3*\3*\3*\3+")
        buf.write("\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3:\7:\u0178")
        buf.write("\n:\f:\16:\u017b\13:\5:\u017d\n:\3;\3;\3;\3;\7;\u0183")
        buf.write("\n;\f;\16;\u0186\13;\3<\3<\3<\3<\7<\u018c\n<\f<\16<\u018f")
        buf.write("\13<\3=\3=\7=\u0193\n=\f=\16=\u0196\13=\3>\6>\u0199\n")
        buf.write(">\r>\16>\u019a\3?\3?\5?\u019f\n?\3?\3?\3@\3@\3@\5@\u01a6")
        buf.write("\n@\3@\5@\u01a9\n@\3A\3A\5A\u01ad\nA\3B\3B\3C\3C\3C\3")
        buf.write("C\3C\5C\u01b6\nC\3D\3D\7D\u01ba\nD\fD\16D\u01bd\13D\3")
        buf.write("D\3D\3D\3E\6E\u01c3\nE\rE\16E\u01c4\3E\3E\3F\3F\3F\3F")
        buf.write("\7F\u01cd\nF\fF\16F\u01d0\13F\3F\3F\3F\3F\3F\3G\3G\7G")
        buf.write("\u01d9\nG\fG\16G\u01dc\13G\3G\5G\u01df\nG\3G\3G\3H\3H")
        buf.write("\7H\u01e5\nH\fH\16H\u01e8\13H\3H\3H\3H\3H\5H\u01ee\nH")
        buf.write("\3H\3H\3I\3I\3I\3I\3I\3I\7I\u01f8\nI\fI\16I\u01fb\13I")
        buf.write("\3J\3J\3\u01ce\2K\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\2+\2-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36?\37")
        buf.write("A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64")
        buf.write("k\65m\66o\67q8s9u:w;y\2{\2}\2\177<\u0081=\u0083\2\u0085")
        buf.write("\2\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093D\3")
        buf.write("\2\26\3\2c|\6\2\62;C\\aac|\3\2\63;\3\2\62;\4\2ZZzz\4\2")
        buf.write("\63;CH\4\2\62;CH\4\2QQqq\3\2\639\3\2\629\4\2GGgg\4\2-")
        buf.write("-//\t\2))^^ddhhppttvv\3\2^^\7\2\f\f\17\17$$))^^\5\2\13")
        buf.write("\f\17\17\"\"\4\3\f\f\17\17\3\2))\3\2$$\3\2,,\2\u020b\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\3\u0095")
        buf.write("\3\2\2\2\5\u009c\3\2\2\2\7\u00a1\3\2\2\2\t\u00a7\3\2\2")
        buf.write("\2\13\u00b0\3\2\2\2\r\u00b3\3\2\2\2\17\u00b8\3\2\2\2\21")
        buf.write("\u00bf\3\2\2\2\23\u00c7\3\2\2\2\25\u00cd\3\2\2\2\27\u00d4")
        buf.write("\3\2\2\2\31\u00dd\3\2\2\2\33\u00e1\3\2\2\2\35\u00ea\3")
        buf.write("\2\2\2\37\u00ed\3\2\2\2!\u00f7\3\2\2\2#\u00fe\3\2\2\2")
        buf.write("%\u0103\3\2\2\2\'\u0107\3\2\2\2)\u010d\3\2\2\2+\u0112")
        buf.write("\3\2\2\2-\u0118\3\2\2\2/\u011e\3\2\2\2\61\u0120\3\2\2")
        buf.write("\2\63\u0123\3\2\2\2\65\u0125\3\2\2\2\67\u0128\3\2\2\2")
        buf.write("9\u012a\3\2\2\2;\u012d\3\2\2\2=\u012f\3\2\2\2?\u0132\3")
        buf.write("\2\2\2A\u0134\3\2\2\2C\u0136\3\2\2\2E\u0138\3\2\2\2G\u013b")
        buf.write("\3\2\2\2I\u013e\3\2\2\2K\u0141\3\2\2\2M\u0144\3\2\2\2")
        buf.write("O\u0146\3\2\2\2Q\u0148\3\2\2\2S\u014b\3\2\2\2U\u014e\3")
        buf.write("\2\2\2W\u0152\3\2\2\2Y\u0155\3\2\2\2[\u0158\3\2\2\2]\u015c")
        buf.write("\3\2\2\2_\u0160\3\2\2\2a\u0162\3\2\2\2c\u0164\3\2\2\2")
        buf.write("e\u0166\3\2\2\2g\u0168\3\2\2\2i\u016a\3\2\2\2k\u016c\3")
        buf.write("\2\2\2m\u016e\3\2\2\2o\u0170\3\2\2\2q\u0172\3\2\2\2s\u017c")
        buf.write("\3\2\2\2u\u017e\3\2\2\2w\u0187\3\2\2\2y\u0190\3\2\2\2")
        buf.write("{\u0198\3\2\2\2}\u019c\3\2\2\2\177\u01a2\3\2\2\2\u0081")
        buf.write("\u01ac\3\2\2\2\u0083\u01ae\3\2\2\2\u0085\u01b5\3\2\2\2")
        buf.write("\u0087\u01b7\3\2\2\2\u0089\u01c2\3\2\2\2\u008b\u01c8\3")
        buf.write("\2\2\2\u008d\u01d6\3\2\2\2\u008f\u01e2\3\2\2\2\u0091\u01f1")
        buf.write("\3\2\2\2\u0093\u01fc\3\2\2\2\u0095\u0099\t\2\2\2\u0096")
        buf.write("\u0098\t\3\2\2\u0097\u0096\3\2\2\2\u0098\u009b\3\2\2\2")
        buf.write("\u0099\u0097\3\2\2\2\u0099\u009a\3\2\2\2\u009a\4\3\2\2")
        buf.write("\2\u009b\u0099\3\2\2\2\u009c\u009d\7D\2\2\u009d\u009e")
        buf.write("\7q\2\2\u009e\u009f\7f\2\2\u009f\u00a0\7{\2\2\u00a0\6")
        buf.write("\3\2\2\2\u00a1\u00a2\7D\2\2\u00a2\u00a3\7t\2\2\u00a3\u00a4")
        buf.write("\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6\7m\2\2\u00a6\b")
        buf.write("\3\2\2\2\u00a7\u00a8\7E\2\2\u00a8\u00a9\7q\2\2\u00a9\u00aa")
        buf.write("\7p\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac\7k\2\2\u00ac\u00ad")
        buf.write("\7p\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af\7g\2\2\u00af\n")
        buf.write("\3\2\2\2\u00b0\u00b1\7F\2\2\u00b1\u00b2\7q\2\2\u00b2\f")
        buf.write("\3\2\2\2\u00b3\u00b4\7G\2\2\u00b4\u00b5\7n\2\2\u00b5\u00b6")
        buf.write("\7u\2\2\u00b6\u00b7\7g\2\2\u00b7\16\3\2\2\2\u00b8\u00b9")
        buf.write("\7G\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\u00bd\7K\2\2\u00bd\u00be\7h\2\2\u00be\20")
        buf.write("\3\2\2\2\u00bf\u00c0\7G\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2")
        buf.write("\7f\2\2\u00c2\u00c3\7D\2\2\u00c3\u00c4\7q\2\2\u00c4\u00c5")
        buf.write("\7f\2\2\u00c5\u00c6\7{\2\2\u00c6\22\3\2\2\2\u00c7\u00c8")
        buf.write("\7G\2\2\u00c8\u00c9\7p\2\2\u00c9\u00ca\7f\2\2\u00ca\u00cb")
        buf.write("\7K\2\2\u00cb\u00cc\7h\2\2\u00cc\24\3\2\2\2\u00cd\u00ce")
        buf.write("\7G\2\2\u00ce\u00cf\7p\2\2\u00cf\u00d0\7f\2\2\u00d0\u00d1")
        buf.write("\7H\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7t\2\2\u00d3\26")
        buf.write("\3\2\2\2\u00d4\u00d5\7G\2\2\u00d5\u00d6\7p\2\2\u00d6\u00d7")
        buf.write("\7f\2\2\u00d7\u00d8\7Y\2\2\u00d8\u00d9\7j\2\2\u00d9\u00da")
        buf.write("\7k\2\2\u00da\u00db\7n\2\2\u00db\u00dc\7g\2\2\u00dc\30")
        buf.write("\3\2\2\2\u00dd\u00de\7H\2\2\u00de\u00df\7q\2\2\u00df\u00e0")
        buf.write("\7t\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7H\2\2\u00e2\u00e3")
        buf.write("\7w\2\2\u00e3\u00e4\7p\2\2\u00e4\u00e5\7e\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\u00e7\7k\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7p\2\2\u00e9\34\3\2\2\2\u00ea\u00eb\7K\2\2\u00eb\u00ec")
        buf.write("\7h\2\2\u00ec\36\3\2\2\2\u00ed\u00ee\7R\2\2\u00ee\u00ef")
        buf.write("\7c\2\2\u00ef\u00f0\7t\2\2\u00f0\u00f1\7c\2\2\u00f1\u00f2")
        buf.write("\7o\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7v\2\2\u00f4\u00f5")
        buf.write("\7g\2\2\u00f5\u00f6\7t\2\2\u00f6 \3\2\2\2\u00f7\u00f8")
        buf.write("\7T\2\2\u00f8\u00f9\7g\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7w\2\2\u00fb\u00fc\7t\2\2\u00fc\u00fd\7p\2\2\u00fd\"")
        buf.write("\3\2\2\2\u00fe\u00ff\7V\2\2\u00ff\u0100\7j\2\2\u0100\u0101")
        buf.write("\7g\2\2\u0101\u0102\7p\2\2\u0102$\3\2\2\2\u0103\u0104")
        buf.write("\7X\2\2\u0104\u0105\7c\2\2\u0105\u0106\7t\2\2\u0106&\3")
        buf.write("\2\2\2\u0107\u0108\7Y\2\2\u0108\u0109\7j\2\2\u0109\u010a")
        buf.write("\7k\2\2\u010a\u010b\7n\2\2\u010b\u010c\7g\2\2\u010c(\3")
        buf.write("\2\2\2\u010d\u010e\7V\2\2\u010e\u010f\7t\2\2\u010f\u0110")
        buf.write("\7w\2\2\u0110\u0111\7g\2\2\u0111*\3\2\2\2\u0112\u0113")
        buf.write("\7H\2\2\u0113\u0114\7c\2\2\u0114\u0115\7n\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7g\2\2\u0117,\3\2\2\2\u0118\u0119")
        buf.write("\7G\2\2\u0119\u011a\7p\2\2\u011a\u011b\7f\2\2\u011b\u011c")
        buf.write("\7F\2\2\u011c\u011d\7q\2\2\u011d.\3\2\2\2\u011e\u011f")
        buf.write("\7-\2\2\u011f\60\3\2\2\2\u0120\u0121\7-\2\2\u0121\u0122")
        buf.write("\7\60\2\2\u0122\62\3\2\2\2\u0123\u0124\7/\2\2\u0124\64")
        buf.write("\3\2\2\2\u0125\u0126\7/\2\2\u0126\u0127\7\60\2\2\u0127")
        buf.write("\66\3\2\2\2\u0128\u0129\7,\2\2\u01298\3\2\2\2\u012a\u012b")
        buf.write("\7,\2\2\u012b\u012c\7\60\2\2\u012c:\3\2\2\2\u012d\u012e")
        buf.write("\7^\2\2\u012e<\3\2\2\2\u012f\u0130\7^\2\2\u0130\u0131")
        buf.write("\7\60\2\2\u0131>\3\2\2\2\u0132\u0133\7\'\2\2\u0133@\3")
        buf.write("\2\2\2\u0134\u0135\7?\2\2\u0135B\3\2\2\2\u0136\u0137\7")
        buf.write("#\2\2\u0137D\3\2\2\2\u0138\u0139\7(\2\2\u0139\u013a\7")
        buf.write("(\2\2\u013aF\3\2\2\2\u013b\u013c\7~\2\2\u013c\u013d\7")
        buf.write("~\2\2\u013dH\3\2\2\2\u013e\u013f\7?\2\2\u013f\u0140\7")
        buf.write("?\2\2\u0140J\3\2\2\2\u0141\u0142\7#\2\2\u0142\u0143\7")
        buf.write("?\2\2\u0143L\3\2\2\2\u0144\u0145\7>\2\2\u0145N\3\2\2\2")
        buf.write("\u0146\u0147\7@\2\2\u0147P\3\2\2\2\u0148\u0149\7>\2\2")
        buf.write("\u0149\u014a\7?\2\2\u014aR\3\2\2\2\u014b\u014c\7@\2\2")
        buf.write("\u014c\u014d\7?\2\2\u014dT\3\2\2\2\u014e\u014f\7?\2\2")
        buf.write("\u014f\u0150\7\61\2\2\u0150\u0151\7?\2\2\u0151V\3\2\2")
        buf.write("\2\u0152\u0153\7>\2\2\u0153\u0154\7\60\2\2\u0154X\3\2")
        buf.write("\2\2\u0155\u0156\7@\2\2\u0156\u0157\7\60\2\2\u0157Z\3")
        buf.write("\2\2\2\u0158\u0159\7>\2\2\u0159\u015a\7?\2\2\u015a\u015b")
        buf.write("\7\60\2\2\u015b\\\3\2\2\2\u015c\u015d\7@\2\2\u015d\u015e")
        buf.write("\7?\2\2\u015e\u015f\7\60\2\2\u015f^\3\2\2\2\u0160\u0161")
        buf.write("\7*\2\2\u0161`\3\2\2\2\u0162\u0163\7+\2\2\u0163b\3\2\2")
        buf.write("\2\u0164\u0165\7]\2\2\u0165d\3\2\2\2\u0166\u0167\7_\2")
        buf.write("\2\u0167f\3\2\2\2\u0168\u0169\7}\2\2\u0169h\3\2\2\2\u016a")
        buf.write("\u016b\7\177\2\2\u016bj\3\2\2\2\u016c\u016d\7=\2\2\u016d")
        buf.write("l\3\2\2\2\u016e\u016f\7\60\2\2\u016fn\3\2\2\2\u0170\u0171")
        buf.write("\7.\2\2\u0171p\3\2\2\2\u0172\u0173\7<\2\2\u0173r\3\2\2")
        buf.write("\2\u0174\u017d\7\62\2\2\u0175\u0179\t\4\2\2\u0176\u0178")
        buf.write("\t\5\2\2\u0177\u0176\3\2\2\2\u0178\u017b\3\2\2\2\u0179")
        buf.write("\u0177\3\2\2\2\u0179\u017a\3\2\2\2\u017a\u017d\3\2\2\2")
        buf.write("\u017b\u0179\3\2\2\2\u017c\u0174\3\2\2\2\u017c\u0175\3")
        buf.write("\2\2\2\u017dt\3\2\2\2\u017e\u017f\7\62\2\2\u017f\u0180")
        buf.write("\t\6\2\2\u0180\u0184\t\7\2\2\u0181\u0183\t\b\2\2\u0182")
        buf.write("\u0181\3\2\2\2\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2")
        buf.write("\u0184\u0185\3\2\2\2\u0185v\3\2\2\2\u0186\u0184\3\2\2")
        buf.write("\2\u0187\u0188\7\62\2\2\u0188\u0189\t\t\2\2\u0189\u018d")
        buf.write("\t\n\2\2\u018a\u018c\t\13\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018ex\3\2\2\2\u018f\u018d\3\2\2\2\u0190\u0194\7\60\2")
        buf.write("\2\u0191\u0193\t\5\2\2\u0192\u0191\3\2\2\2\u0193\u0196")
        buf.write("\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195")
        buf.write("z\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u0199\t\5\2\2\u0198")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b|\3\2\2\2\u019c\u019e\t\f\2")
        buf.write("\2\u019d\u019f\t\r\2\2\u019e\u019d\3\2\2\2\u019e\u019f")
        buf.write("\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\5{>\2\u01a1~")
        buf.write("\3\2\2\2\u01a2\u01a8\5{>\2\u01a3\u01a5\5y=\2\u01a4\u01a6")
        buf.write("\5}?\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01a9")
        buf.write("\3\2\2\2\u01a7\u01a9\5}?\2\u01a8\u01a3\3\2\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u0080\3\2\2\2\u01aa\u01ad\5)\25\2\u01ab")
        buf.write("\u01ad\5+\26\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2")
        buf.write("\u01ad\u0082\3\2\2\2\u01ae\u01af\t\16\2\2\u01af\u0084")
        buf.write("\3\2\2\2\u01b0\u01b1\7)\2\2\u01b1\u01b6\7$\2\2\u01b2\u01b3")
        buf.write("\t\17\2\2\u01b3\u01b6\5\u0083B\2\u01b4\u01b6\n\20\2\2")
        buf.write("\u01b5\u01b0\3\2\2\2\u01b5\u01b2\3\2\2\2\u01b5\u01b4\3")
        buf.write("\2\2\2\u01b6\u0086\3\2\2\2\u01b7\u01bb\7$\2\2\u01b8\u01ba")
        buf.write("\5\u0085C\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2\u01bb")
        buf.write("\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01be\3\2\2\2")
        buf.write("\u01bd\u01bb\3\2\2\2\u01be\u01bf\7$\2\2\u01bf\u01c0\b")
        buf.write("D\2\2\u01c0\u0088\3\2\2\2\u01c1\u01c3\t\21\2\2\u01c2\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c5\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\bE\3\2")
        buf.write("\u01c7\u008a\3\2\2\2\u01c8\u01c9\7,\2\2\u01c9\u01ca\7")
        buf.write(",\2\2\u01ca\u01ce\3\2\2\2\u01cb\u01cd\13\2\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cf\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d2\7,\2\2\u01d2\u01d3\7,\2\2\u01d3\u01d4\3\2")
        buf.write("\2\2\u01d4\u01d5\bF\3\2\u01d5\u008c\3\2\2\2\u01d6\u01da")
        buf.write("\7$\2\2\u01d7\u01d9\5\u0085C\2\u01d8\u01d7\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01db\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01df\t")
        buf.write("\22\2\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0")
        buf.write("\u01e1\bG\4\2\u01e1\u008e\3\2\2\2\u01e2\u01e6\7$\2\2\u01e3")
        buf.write("\u01e5\5\u0085C\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2")
        buf.write("\2\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01ed")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01ea\t\17\2\2\u01ea")
        buf.write("\u01ee\n\16\2\2\u01eb\u01ec\t\23\2\2\u01ec\u01ee\n\24")
        buf.write("\2\2\u01ed\u01e9\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f0\bH\5\2\u01f0\u0090\3\2\2\2\u01f1")
        buf.write("\u01f2\7,\2\2\u01f2\u01f3\7,\2\2\u01f3\u01f9\3\2\2\2\u01f4")
        buf.write("\u01f8\n\25\2\2\u01f5\u01f6\7,\2\2\u01f6\u01f8\n\25\2")
        buf.write("\2\u01f7\u01f4\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f8\u01fb")
        buf.write("\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u0092\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fc\u01fd\13\2\2")
        buf.write("\2\u01fd\u0094\3\2\2\2\30\2\u0099\u0179\u017c\u0184\u018d")
        buf.write("\u0194\u019a\u019e\u01a5\u01a8\u01ac\u01b5\u01bb\u01c4")
        buf.write("\u01ce\u01da\u01de\u01e6\u01ed\u01f7\u01f9\6\3D\2\b\2")
        buf.write("\2\3G\3\3H\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    BODY = 2
    BREAK = 3
    CONT = 4
    DO = 5
    ELSE = 6
    ELSEIF = 7
    ENDBODY = 8
    ENDIF = 9
    ENDFOR = 10
    ENDWHILE = 11
    FOR = 12
    FUNC = 13
    IF = 14
    PARA = 15
    RETURN = 16
    THEN = 17
    VAR = 18
    WHILE = 19
    ENDDO = 20
    ADD = 21
    ADDF = 22
    SUB = 23
    SUBF = 24
    MUL = 25
    MULF = 26
    DIV = 27
    DIVF = 28
    MOD = 29
    ASS = 30
    NOT = 31
    AND = 32
    OR = 33
    EQUAL = 34
    NEQUAL = 35
    SMALLER = 36
    LARGER = 37
    SEQUAL = 38
    LEQUAL = 39
    NEQUALF = 40
    SMALLERF = 41
    LARGERF = 42
    SEQUALF = 43
    LEQUALF = 44
    RBRACKET_L = 45
    RBRACKET_R = 46
    SBRACKET_L = 47
    SBRACKET_R = 48
    CBRACKET_L = 49
    CBRACKET_R = 50
    SEMI = 51
    DOT = 52
    COMMA = 53
    COLON = 54
    INT_LIT = 55
    HEX_LIT = 56
    OCT_LIT = 57
    FLOAT_LIT = 58
    BOOL_LIT = 59
    STRING_LIT = 60
    WS = 61
    CMT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Body'", "'Break'", "'Continue'", "'Do'", "'Else'", "'ElseIf'", 
            "'EndBody'", "'EndIf'", "'EndFor'", "'EndWhile'", "'For'", "'Function'", 
            "'If'", "'Parameter'", "'Return'", "'Then'", "'Var'", "'While'", 
            "'EndDo'", "'+'", "'+.'", "'-'", "'-.'", "'*'", "'*.'", "'\\'", 
            "'\\.'", "'%'", "'='", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'<'", "'>'", "'<='", "'>='", "'=/='", "'<.'", "'>.'", "'<=.'", 
            "'>=.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "'.'", 
            "','", "':'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "BODY", "BREAK", "CONT", "DO", "ELSE", "ELSEIF", "ENDBODY", 
            "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNC", "IF", "PARA", 
            "RETURN", "THEN", "VAR", "WHILE", "ENDDO", "ADD", "ADDF", "SUB", 
            "SUBF", "MUL", "MULF", "DIV", "DIVF", "MOD", "ASS", "NOT", "AND", 
            "OR", "EQUAL", "NEQUAL", "SMALLER", "LARGER", "SEQUAL", "LEQUAL", 
            "NEQUALF", "SMALLERF", "LARGERF", "SEQUALF", "LEQUALF", "RBRACKET_L", 
            "RBRACKET_R", "SBRACKET_L", "SBRACKET_R", "CBRACKET_L", "CBRACKET_R", 
            "SEMI", "DOT", "COMMA", "COLON", "INT_LIT", "HEX_LIT", "OCT_LIT", 
            "FLOAT_LIT", "BOOL_LIT", "STRING_LIT", "WS", "CMT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "ID", "BODY", "BREAK", "CONT", "DO", "ELSE", "ELSEIF", 
                  "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNC", 
                  "IF", "PARA", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "ADD", "ADDF", "SUB", "SUBF", "MUL", 
                  "MULF", "DIV", "DIVF", "MOD", "ASS", "NOT", "AND", "OR", 
                  "EQUAL", "NEQUAL", "SMALLER", "LARGER", "SEQUAL", "LEQUAL", 
                  "NEQUALF", "SMALLERF", "LARGERF", "SEQUALF", "LEQUALF", 
                  "RBRACKET_L", "RBRACKET_R", "SBRACKET_L", "SBRACKET_R", 
                  "CBRACKET_L", "CBRACKET_R", "SEMI", "DOT", "COMMA", "COLON", 
                  "INT_LIT", "HEX_LIT", "OCT_LIT", "DecimalPart", "Digits", 
                  "SciNotation", "FLOAT_LIT", "BOOL_LIT", "LegalEscape", 
                  "StringElement", "STRING_LIT", "WS", "CMT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.STRING_LIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text[1:]
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:]
     


