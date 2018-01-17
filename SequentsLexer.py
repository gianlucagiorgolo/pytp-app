# Generated from Sequents.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("H\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\6\f\65")
        buf.write("\n\f\r\f\16\f\66\3\f\3\f\3\r\3\r\7\r=\n\r\f\r\16\r@\13")
        buf.write("\r\3\16\3\16\7\16D\n\16\f\16\16\16G\13\16\2\2\17\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\3\2\6\4\2\13\f\"\"\3\2c|\6\2\62;C\\aac|\3\2C\\\2J")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\3\35\3\2\2\2\5 \3\2\2\2\7\"\3\2\2\2\t$\3\2\2\2\13")
        buf.write("&\3\2\2\2\r(\3\2\2\2\17+\3\2\2\2\21-\3\2\2\2\23/\3\2\2")
        buf.write("\2\25\61\3\2\2\2\27\64\3\2\2\2\31:\3\2\2\2\33A\3\2\2\2")
        buf.write("\35\36\7~\2\2\36\37\7/\2\2\37\4\3\2\2\2 !\7.\2\2!\6\3")
        buf.write("\2\2\2\"#\7>\2\2#\b\3\2\2\2$%\7@\2\2%\n\3\2\2\2&\'\7,")
        buf.write("\2\2\'\f\3\2\2\2()\7/\2\2)*\7q\2\2*\16\3\2\2\2+,\7\60")
        buf.write("\2\2,\20\3\2\2\2-.\7*\2\2.\22\3\2\2\2/\60\7+\2\2\60\24")
        buf.write("\3\2\2\2\61\62\7<\2\2\62\26\3\2\2\2\63\65\t\2\2\2\64\63")
        buf.write("\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("8\3\2\2\289\b\f\2\29\30\3\2\2\2:>\t\3\2\2;=\t\4\2\2<;")
        buf.write("\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\32\3\2\2\2@>\3")
        buf.write("\2\2\2AE\t\5\2\2BD\t\4\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2")
        buf.write("\2EF\3\2\2\2F\34\3\2\2\2GE\3\2\2\2\6\2\66>E\3\b\2\2")
        return buf.getvalue()


class SequentsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    WS = 11
    ATOM = 12
    VARIABLE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|-'", "','", "'<'", "'>'", "'*'", "'-o'", "'.'", "'('", "')'", 
            "':'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "ATOM", "VARIABLE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "WS", "ATOM", "VARIABLE" ]

    grammarFileName = "Sequents.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


