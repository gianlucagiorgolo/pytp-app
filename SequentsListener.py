# Generated from Sequents.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SequentsParser import SequentsParser
else:
    from SequentsParser import SequentsParser

# This class defines a complete listener for a parse tree produced by SequentsParser.
class SequentsListener(ParseTreeListener):

    # Enter a parse tree produced by SequentsParser#DecoratedSequent.
    def enterDecoratedSequent(self, ctx:SequentsParser.DecoratedSequentContext):
        pass

    # Exit a parse tree produced by SequentsParser#DecoratedSequent.
    def exitDecoratedSequent(self, ctx:SequentsParser.DecoratedSequentContext):
        pass


    # Enter a parse tree produced by SequentsParser#SimpleSequent.
    def enterSimpleSequent(self, ctx:SequentsParser.SimpleSequentContext):
        pass

    # Exit a parse tree produced by SequentsParser#SimpleSequent.
    def exitSimpleSequent(self, ctx:SequentsParser.SimpleSequentContext):
        pass


    # Enter a parse tree produced by SequentsParser#simple_sequent.
    def enterSimple_sequent(self, ctx:SequentsParser.Simple_sequentContext):
        pass

    # Exit a parse tree produced by SequentsParser#simple_sequent.
    def exitSimple_sequent(self, ctx:SequentsParser.Simple_sequentContext):
        pass


    # Enter a parse tree produced by SequentsParser#hypotheses.
    def enterHypotheses(self, ctx:SequentsParser.HypothesesContext):
        pass

    # Exit a parse tree produced by SequentsParser#hypotheses.
    def exitHypotheses(self, ctx:SequentsParser.HypothesesContext):
        pass


    # Enter a parse tree produced by SequentsParser#consequence.
    def enterConsequence(self, ctx:SequentsParser.ConsequenceContext):
        pass

    # Exit a parse tree produced by SequentsParser#consequence.
    def exitConsequence(self, ctx:SequentsParser.ConsequenceContext):
        pass


    # Enter a parse tree produced by SequentsParser#ParensFormula.
    def enterParensFormula(self, ctx:SequentsParser.ParensFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#ParensFormula.
    def exitParensFormula(self, ctx:SequentsParser.ParensFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#MonadFormula.
    def enterMonadFormula(self, ctx:SequentsParser.MonadFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#MonadFormula.
    def exitMonadFormula(self, ctx:SequentsParser.MonadFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#AtomFormula.
    def enterAtomFormula(self, ctx:SequentsParser.AtomFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#AtomFormula.
    def exitAtomFormula(self, ctx:SequentsParser.AtomFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#TensorFormula.
    def enterTensorFormula(self, ctx:SequentsParser.TensorFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#TensorFormula.
    def exitTensorFormula(self, ctx:SequentsParser.TensorFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#ImplicationFormula.
    def enterImplicationFormula(self, ctx:SequentsParser.ImplicationFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#ImplicationFormula.
    def exitImplicationFormula(self, ctx:SequentsParser.ImplicationFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#VariableFormula.
    def enterVariableFormula(self, ctx:SequentsParser.VariableFormulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#VariableFormula.
    def exitVariableFormula(self, ctx:SequentsParser.VariableFormulaContext):
        pass


    # Enter a parse tree produced by SequentsParser#decorated_sequent.
    def enterDecorated_sequent(self, ctx:SequentsParser.Decorated_sequentContext):
        pass

    # Exit a parse tree produced by SequentsParser#decorated_sequent.
    def exitDecorated_sequent(self, ctx:SequentsParser.Decorated_sequentContext):
        pass


    # Enter a parse tree produced by SequentsParser#decorated_hypotheses.
    def enterDecorated_hypotheses(self, ctx:SequentsParser.Decorated_hypothesesContext):
        pass

    # Exit a parse tree produced by SequentsParser#decorated_hypotheses.
    def exitDecorated_hypotheses(self, ctx:SequentsParser.Decorated_hypothesesContext):
        pass


    # Enter a parse tree produced by SequentsParser#decorated_formula.
    def enterDecorated_formula(self, ctx:SequentsParser.Decorated_formulaContext):
        pass

    # Exit a parse tree produced by SequentsParser#decorated_formula.
    def exitDecorated_formula(self, ctx:SequentsParser.Decorated_formulaContext):
        pass


