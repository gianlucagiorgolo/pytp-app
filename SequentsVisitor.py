# Generated from Sequents.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SequentsParser import SequentsParser
else:
    from SequentsParser import SequentsParser

# This class defines a complete generic visitor for a parse tree produced by SequentsParser.

class SequentsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SequentsParser#DecoratedSequent.
    def visitDecoratedSequent(self, ctx:SequentsParser.DecoratedSequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#SimpleSequent.
    def visitSimpleSequent(self, ctx:SequentsParser.SimpleSequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#simple_sequent.
    def visitSimple_sequent(self, ctx:SequentsParser.Simple_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#hypotheses.
    def visitHypotheses(self, ctx:SequentsParser.HypothesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#consequence.
    def visitConsequence(self, ctx:SequentsParser.ConsequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#ParensFormula.
    def visitParensFormula(self, ctx:SequentsParser.ParensFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#MonadFormula.
    def visitMonadFormula(self, ctx:SequentsParser.MonadFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#AtomFormula.
    def visitAtomFormula(self, ctx:SequentsParser.AtomFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#TensorFormula.
    def visitTensorFormula(self, ctx:SequentsParser.TensorFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#ImplicationFormula.
    def visitImplicationFormula(self, ctx:SequentsParser.ImplicationFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#VariableFormula.
    def visitVariableFormula(self, ctx:SequentsParser.VariableFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#decorated_sequent.
    def visitDecorated_sequent(self, ctx:SequentsParser.Decorated_sequentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#decorated_hypotheses.
    def visitDecorated_hypotheses(self, ctx:SequentsParser.Decorated_hypothesesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SequentsParser#decorated_formula.
    def visitDecorated_formula(self, ctx:SequentsParser.Decorated_formulaContext):
        return self.visitChildren(ctx)



del SequentsParser