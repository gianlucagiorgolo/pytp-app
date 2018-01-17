import antlr4

import SequentsVisitor
import lambda_calc as lc
import tp
from SequentsLexer import SequentsLexer
from SequentsParser import SequentsParser


class Visitor(SequentsVisitor.SequentsVisitor):
    """
    Subclassing it just to keep in changes in between ANTLR iteration
    """

    def visitAtomFormula(self, ctx: SequentsParser.AtomFormulaContext):
        sym = ctx.body.text
        if ctx.c_type:
            typ = ctx.c_type.text
        else:
            typ = tp.universal_type
        return tp.Atom(symbol=sym, typ=typ)

    def visitVariableFormula(self, ctx: SequentsParser.VariableFormulaContext):
        ident = ctx.body.text
        if ctx.v_type:
            typ = ctx.v_type.text
        else:
            typ = tp.universal_type
        return tp.Variable(identifier=ident, typ=typ)

    def visitTensorFormula(self, ctx: SequentsParser.TensorFormulaContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return tp.Tensor(left, right)

    def visitImplicationFormula(self, ctx: SequentsParser.ImplicationFormulaContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        return tp.Implication(left, right)

    def visitParensFormula(self, ctx: SequentsParser.ParensFormulaContext):
        return self.visit(ctx.body)

    def visitMonadFormula(self, ctx: SequentsParser.MonadFormulaContext):
        body = self.visit(ctx.body)
        if ctx.monadtype:
            typ = ctx.monadtype.text
        else:
            typ = ''
        return tp.Monad(body, typ)

    def visitSimpleSequent(self, ctx: SequentsParser.SimpleSequentContext):
        return self.visit(ctx.seq)

    def visitDecoratedSequent(self, ctx: SequentsParser.DecoratedSequentContext):
        return self.visit(ctx.seq)

    def visitSimple_sequent(self, ctx: SequentsParser.Simple_sequentContext):
        hyps = self.visit(ctx.hyps)
        cons = self.visit(ctx.cons)
        return tp.Sequent(hyps, cons)

    def visitHypotheses(self, ctx: SequentsParser.HypothesesContext):
        hyps = list()
        if ctx.first:
            hyps.append(self.visit(ctx.first))
        for h in ctx.rest:
            hyps.append(self.visit(h))
        return hyps

    def visitConsequence(self, ctx: SequentsParser.ConsequenceContext):
        return self.visit(ctx.form)

    def visitDecorated_sequent(self, ctx: SequentsParser.Decorated_sequentContext):
        dec_hyps = self.visit(ctx.hyps)
        cons = self.visit(ctx.cons)
        return tp.DecoratedSequent(dec_hyps[1], cons, dec_hyps[0])

    def visitDecorated_hypotheses(self, ctx: SequentsParser.Decorated_hypothesesContext):
        hyps = list()
        terms = list()
        if ctx.first:
            tmp = self.visit(ctx.first)
            hyps.append(tmp[1])
            terms.append(tmp[0])
        for h in ctx.rest:
            tmp = self.visit(h)
            hyps.append(tmp[1])
            terms.append(tmp[0])
        return (terms, hyps)

    def visitDecorated_formula(self, ctx: SequentsParser.Decorated_formulaContext):
        term = lc.Const(ctx.term.text)
        form = self.visit(ctx.form)
        return (term, form)


def parse(input_text):
    input = antlr4.InputStream(input_text)
    lexer = SequentsLexer(input)
    stream = antlr4.CommonTokenStream(lexer)
    parser = SequentsParser(stream)
    cst = parser.sequent()
    visitor = Visitor()
    return visitor.visit(cst)


import unittest


class TestParser(unittest.TestCase):
    def test_parsing(self):
        seq = tp.Sequent
        a = tp.Atom
        m = tp.Monad
        i = tp.Implication
        t = tp.Tensor
        ut = tp.universal_type
        s1 = 'atom |- a'
        r1 = seq([a('atom', ut)], a('a', ut))
        s2 = '<>a |- a'
        r2 = seq([m(a('a', ut), '')], a('a', ut))
        s3 = '<c>a |- a'
        r3 = seq([m(a('a', ut), 'c')], a('a', ut))
        s4 = '|- a.a'
        r4 = seq([], a('a', 'a'))
        s5 = 'a : a |- b'
        r5 = tp.DecoratedSequent([a('a', ut)], a('b', ut), [lc.Const('a')])
        s6 = 'a -o b -o c |- d'
        r6 = seq([i(a('a', ut), i(a('b', ut), a('c', ut)))], a('d', ut))
        s7 = 'a * b * c |- d'
        r7 = seq([t(t(a('a', ut), a('b', ut)), a('c', ut))], a('d', ut))
        s = [s1, s2, s3, s4, s5, s6, s7]
        r = [r1, r2, r3, r4, r5, r6, r7]

        for i in range(len(s)):
            self.assertEqual(parse(s[i]), r[i])


if __name__ == '__main__':
    unittest.main()
