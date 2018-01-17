# Generated from Sequents.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\3\3")
        buf.write("\3\3\3\3\3\3\4\5\4 \n\4\3\4\3\4\7\4$\n\4\f\4\16\4\'\13")
        buf.write("\4\3\5\3\5\3\6\3\6\3\6\5\6.\n\6\3\6\3\6\3\6\3\6\3\6\5")
        buf.write("\6\65\n\6\3\6\3\6\3\6\5\6:\n\6\3\6\3\6\3\6\3\6\5\6@\n")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6H\n\6\f\6\16\6K\13\6\3\7")
        buf.write("\3\7\3\7\3\7\3\b\5\bR\n\b\3\b\3\b\7\bV\n\b\f\b\16\bY\13")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\2\3\n\n\2\4\6\b\n\f\16\20\2\2\2")
        buf.write("c\2\30\3\2\2\2\4\32\3\2\2\2\6\37\3\2\2\2\b(\3\2\2\2\n")
        buf.write("?\3\2\2\2\fL\3\2\2\2\16Q\3\2\2\2\20Z\3\2\2\2\22\23\5\f")
        buf.write("\7\2\23\24\7\2\2\3\24\31\3\2\2\2\25\26\5\4\3\2\26\27\7")
        buf.write("\2\2\3\27\31\3\2\2\2\30\22\3\2\2\2\30\25\3\2\2\2\31\3")
        buf.write("\3\2\2\2\32\33\5\6\4\2\33\34\7\3\2\2\34\35\5\b\5\2\35")
        buf.write("\5\3\2\2\2\36 \5\n\6\2\37\36\3\2\2\2\37 \3\2\2\2 %\3\2")
        buf.write("\2\2!\"\7\4\2\2\"$\5\n\6\2#!\3\2\2\2$\'\3\2\2\2%#\3\2")
        buf.write("\2\2%&\3\2\2\2&\7\3\2\2\2\'%\3\2\2\2()\5\n\6\2)\t\3\2")
        buf.write("\2\2*+\b\6\1\2+-\7\5\2\2,.\7\16\2\2-,\3\2\2\2-.\3\2\2")
        buf.write("\2./\3\2\2\2/\60\7\6\2\2\60@\5\n\6\b\61\64\7\16\2\2\62")
        buf.write("\63\7\t\2\2\63\65\7\16\2\2\64\62\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65@\3\2\2\2\669\7\17\2\2\678\7\t\2\28:\7\16\2\29\67\3")
        buf.write("\2\2\29:\3\2\2\2:@\3\2\2\2;<\7\n\2\2<=\5\n\6\2=>\7\13")
        buf.write("\2\2>@\3\2\2\2?*\3\2\2\2?\61\3\2\2\2?\66\3\2\2\2?;\3\2")
        buf.write("\2\2@I\3\2\2\2AB\f\7\2\2BC\7\7\2\2CH\5\n\6\bDE\f\6\2\2")
        buf.write("EF\7\b\2\2FH\5\n\6\6GA\3\2\2\2GD\3\2\2\2HK\3\2\2\2IG\3")
        buf.write("\2\2\2IJ\3\2\2\2J\13\3\2\2\2KI\3\2\2\2LM\5\16\b\2MN\7")
        buf.write("\3\2\2NO\5\b\5\2O\r\3\2\2\2PR\5\20\t\2QP\3\2\2\2QR\3\2")
        buf.write("\2\2RW\3\2\2\2ST\7\4\2\2TV\5\20\t\2US\3\2\2\2VY\3\2\2")
        buf.write("\2WU\3\2\2\2WX\3\2\2\2X\17\3\2\2\2YW\3\2\2\2Z[\7\16\2")
        buf.write("\2[\\\7\f\2\2\\]\5\n\6\2]\21\3\2\2\2\r\30\37%-\649?GI")
        buf.write("QW")
        return buf.getvalue()


class SequentsParser ( Parser ):

    grammarFileName = "Sequents.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|-'", "','", "'<'", "'>'", "'*'", "'-o'", 
                     "'.'", "'('", "')'", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WS", "ATOM", 
                      "VARIABLE" ]

    RULE_sequent = 0
    RULE_simple_sequent = 1
    RULE_hypotheses = 2
    RULE_consequence = 3
    RULE_formula = 4
    RULE_decorated_sequent = 5
    RULE_decorated_hypotheses = 6
    RULE_decorated_formula = 7

    ruleNames =  [ "sequent", "simple_sequent", "hypotheses", "consequence", 
                   "formula", "decorated_sequent", "decorated_hypotheses", 
                   "decorated_formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    WS=11
    ATOM=12
    VARIABLE=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class SequentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SequentsParser.RULE_sequent

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DecoratedSequentContext(SequentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.SequentContext
            super().__init__(parser)
            self.seq = None # Decorated_sequentContext
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(SequentsParser.EOF, 0)
        def decorated_sequent(self):
            return self.getTypedRuleContext(SequentsParser.Decorated_sequentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecoratedSequent" ):
                listener.enterDecoratedSequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecoratedSequent" ):
                listener.exitDecoratedSequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecoratedSequent" ):
                return visitor.visitDecoratedSequent(self)
            else:
                return visitor.visitChildren(self)


    class SimpleSequentContext(SequentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.SequentContext
            super().__init__(parser)
            self.seq = None # Simple_sequentContext
            self.copyFrom(ctx)

        def EOF(self):
            return self.getToken(SequentsParser.EOF, 0)
        def simple_sequent(self):
            return self.getTypedRuleContext(SequentsParser.Simple_sequentContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimpleSequent" ):
                listener.enterSimpleSequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimpleSequent" ):
                listener.exitSimpleSequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleSequent" ):
                return visitor.visitSimpleSequent(self)
            else:
                return visitor.visitChildren(self)



    def sequent(self):

        localctx = SequentsParser.SequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sequent)
        try:
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = SequentsParser.DecoratedSequentContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                localctx.seq = self.decorated_sequent()
                self.state = 17
                self.match(SequentsParser.EOF)
                pass

            elif la_ == 2:
                localctx = SequentsParser.SimpleSequentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                localctx.seq = self.simple_sequent()
                self.state = 20
                self.match(SequentsParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_sequentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.hyps = None # HypothesesContext
            self.cons = None # ConsequenceContext

        def hypotheses(self):
            return self.getTypedRuleContext(SequentsParser.HypothesesContext,0)


        def consequence(self):
            return self.getTypedRuleContext(SequentsParser.ConsequenceContext,0)


        def getRuleIndex(self):
            return SequentsParser.RULE_simple_sequent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_sequent" ):
                listener.enterSimple_sequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_sequent" ):
                listener.exitSimple_sequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_sequent" ):
                return visitor.visitSimple_sequent(self)
            else:
                return visitor.visitChildren(self)




    def simple_sequent(self):

        localctx = SequentsParser.Simple_sequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_simple_sequent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            localctx.hyps = self.hypotheses()
            self.state = 25
            self.match(SequentsParser.T__0)
            self.state = 26
            localctx.cons = self.consequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class HypothesesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # FormulaContext
            self._formula = None # FormulaContext
            self.rest = list() # of FormulaContexts

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SequentsParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SequentsParser.FormulaContext,i)


        def getRuleIndex(self):
            return SequentsParser.RULE_hypotheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHypotheses" ):
                listener.enterHypotheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHypotheses" ):
                listener.exitHypotheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHypotheses" ):
                return visitor.visitHypotheses(self)
            else:
                return visitor.visitChildren(self)




    def hypotheses(self):

        localctx = SequentsParser.HypothesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_hypotheses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SequentsParser.T__2) | (1 << SequentsParser.T__7) | (1 << SequentsParser.ATOM) | (1 << SequentsParser.VARIABLE))) != 0):
                self.state = 28
                localctx.first = self.formula(0)


            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SequentsParser.T__1:
                self.state = 31
                self.match(SequentsParser.T__1)
                self.state = 32
                localctx._formula = self.formula(0)
                localctx.rest.append(localctx._formula)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConsequenceContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.form = None # FormulaContext

        def formula(self):
            return self.getTypedRuleContext(SequentsParser.FormulaContext,0)


        def getRuleIndex(self):
            return SequentsParser.RULE_consequence

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsequence" ):
                listener.enterConsequence(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsequence" ):
                listener.exitConsequence(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConsequence" ):
                return visitor.visitConsequence(self)
            else:
                return visitor.visitChildren(self)




    def consequence(self):

        localctx = SequentsParser.ConsequenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_consequence)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            localctx.form = self.formula(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SequentsParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.body = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(SequentsParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensFormula" ):
                listener.enterParensFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensFormula" ):
                listener.exitParensFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensFormula" ):
                return visitor.visitParensFormula(self)
            else:
                return visitor.visitChildren(self)


    class MonadFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.monadtype = None # Token
            self.body = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(SequentsParser.FormulaContext,0)

        def ATOM(self):
            return self.getToken(SequentsParser.ATOM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonadFormula" ):
                listener.enterMonadFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonadFormula" ):
                listener.exitMonadFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonadFormula" ):
                return visitor.visitMonadFormula(self)
            else:
                return visitor.visitChildren(self)


    class AtomFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.body = None # Token
            self.c_type = None # Token
            self.copyFrom(ctx)

        def ATOM(self, i:int=None):
            if i is None:
                return self.getTokens(SequentsParser.ATOM)
            else:
                return self.getToken(SequentsParser.ATOM, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomFormula" ):
                listener.enterAtomFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomFormula" ):
                listener.exitAtomFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomFormula" ):
                return visitor.visitAtomFormula(self)
            else:
                return visitor.visitChildren(self)


    class TensorFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SequentsParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SequentsParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensorFormula" ):
                listener.enterTensorFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensorFormula" ):
                listener.exitTensorFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTensorFormula" ):
                return visitor.visitTensorFormula(self)
            else:
                return visitor.visitChildren(self)


    class ImplicationFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SequentsParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SequentsParser.FormulaContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicationFormula" ):
                listener.enterImplicationFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicationFormula" ):
                listener.exitImplicationFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicationFormula" ):
                return visitor.visitImplicationFormula(self)
            else:
                return visitor.visitChildren(self)


    class VariableFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SequentsParser.FormulaContext
            super().__init__(parser)
            self.body = None # Token
            self.v_type = None # Token
            self.copyFrom(ctx)

        def VARIABLE(self):
            return self.getToken(SequentsParser.VARIABLE, 0)
        def ATOM(self):
            return self.getToken(SequentsParser.ATOM, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableFormula" ):
                listener.enterVariableFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableFormula" ):
                listener.exitVariableFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableFormula" ):
                return visitor.visitVariableFormula(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SequentsParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SequentsParser.T__2]:
                localctx = SequentsParser.MonadFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 41
                self.match(SequentsParser.T__2)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SequentsParser.ATOM:
                    self.state = 42
                    localctx.monadtype = self.match(SequentsParser.ATOM)


                self.state = 45
                self.match(SequentsParser.T__3)
                self.state = 46
                localctx.body = self.formula(6)
                pass
            elif token in [SequentsParser.ATOM]:
                localctx = SequentsParser.AtomFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                localctx.body = self.match(SequentsParser.ATOM)
                self.state = 50
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 48
                    self.match(SequentsParser.T__6)
                    self.state = 49
                    localctx.c_type = self.match(SequentsParser.ATOM)


                pass
            elif token in [SequentsParser.VARIABLE]:
                localctx = SequentsParser.VariableFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                localctx.body = self.match(SequentsParser.VARIABLE)
                self.state = 55
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 53
                    self.match(SequentsParser.T__6)
                    self.state = 54
                    localctx.v_type = self.match(SequentsParser.ATOM)


                pass
            elif token in [SequentsParser.T__7]:
                localctx = SequentsParser.ParensFormulaContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                self.match(SequentsParser.T__7)
                self.state = 58
                localctx.body = self.formula(0)
                self.state = 59
                self.match(SequentsParser.T__8)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 71
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 69
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SequentsParser.TensorFormulaContext(self, SequentsParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 63
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 64
                        self.match(SequentsParser.T__4)
                        self.state = 65
                        localctx.right = self.formula(6)
                        pass

                    elif la_ == 2:
                        localctx = SequentsParser.ImplicationFormulaContext(self, SequentsParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 66
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 67
                        self.match(SequentsParser.T__5)
                        self.state = 68
                        localctx.right = self.formula(4)
                        pass

             
                self.state = 73
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class Decorated_sequentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.hyps = None # Decorated_hypothesesContext
            self.cons = None # ConsequenceContext

        def decorated_hypotheses(self):
            return self.getTypedRuleContext(SequentsParser.Decorated_hypothesesContext,0)


        def consequence(self):
            return self.getTypedRuleContext(SequentsParser.ConsequenceContext,0)


        def getRuleIndex(self):
            return SequentsParser.RULE_decorated_sequent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorated_sequent" ):
                listener.enterDecorated_sequent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorated_sequent" ):
                listener.exitDecorated_sequent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorated_sequent" ):
                return visitor.visitDecorated_sequent(self)
            else:
                return visitor.visitChildren(self)




    def decorated_sequent(self):

        localctx = SequentsParser.Decorated_sequentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_decorated_sequent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            localctx.hyps = self.decorated_hypotheses()
            self.state = 75
            self.match(SequentsParser.T__0)
            self.state = 76
            localctx.cons = self.consequence()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decorated_hypothesesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.first = None # Decorated_formulaContext
            self._decorated_formula = None # Decorated_formulaContext
            self.rest = list() # of Decorated_formulaContexts

        def decorated_formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SequentsParser.Decorated_formulaContext)
            else:
                return self.getTypedRuleContext(SequentsParser.Decorated_formulaContext,i)


        def getRuleIndex(self):
            return SequentsParser.RULE_decorated_hypotheses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorated_hypotheses" ):
                listener.enterDecorated_hypotheses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorated_hypotheses" ):
                listener.exitDecorated_hypotheses(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorated_hypotheses" ):
                return visitor.visitDecorated_hypotheses(self)
            else:
                return visitor.visitChildren(self)




    def decorated_hypotheses(self):

        localctx = SequentsParser.Decorated_hypothesesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_decorated_hypotheses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SequentsParser.ATOM:
                self.state = 78
                localctx.first = self.decorated_formula()


            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SequentsParser.T__1:
                self.state = 81
                self.match(SequentsParser.T__1)
                self.state = 82
                localctx._decorated_formula = self.decorated_formula()
                localctx.rest.append(localctx._decorated_formula)
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Decorated_formulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.term = None # Token
            self.form = None # FormulaContext

        def ATOM(self):
            return self.getToken(SequentsParser.ATOM, 0)

        def formula(self):
            return self.getTypedRuleContext(SequentsParser.FormulaContext,0)


        def getRuleIndex(self):
            return SequentsParser.RULE_decorated_formula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecorated_formula" ):
                listener.enterDecorated_formula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecorated_formula" ):
                listener.exitDecorated_formula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecorated_formula" ):
                return visitor.visitDecorated_formula(self)
            else:
                return visitor.visitChildren(self)




    def decorated_formula(self):

        localctx = SequentsParser.Decorated_formulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_decorated_formula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            localctx.term = self.match(SequentsParser.ATOM)
            self.state = 89
            self.match(SequentsParser.T__9)
            self.state = 90
            localctx.form = self.formula(0)
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
        self._predicates[4] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




