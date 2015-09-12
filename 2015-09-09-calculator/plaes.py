#!/usr/bin/env python3
"""
    calc.py
    ~~~~~~~

    Simple mathematical expression parser for infix syntax.

    Caveats:
        - only supports +-/* and ()
        - fails with prefix syntax: -1
        - doesn't support ^ or ** operations
        - probably something else... :)

    author: Priit Laes
    license: WTFPL
"""
import collections
import operator
import unittest
import re


class Calculator():
    token_map = {
        '+': 'ADD',
        '-': 'SUB',
        '*': 'MUL',
        '/': 'DIV',
        '(': 'LPAR',
        ')': 'RPAR',
    }

    Symbol = collections.namedtuple('Symbol', ['id', 'pr', 'op'])
    t_map = {
        'ADD': Symbol('ADD', '2', operator.add),
        'SUB': Symbol('ADD', '2', operator.sub),
        'MUL': Symbol('MUL', '3', operator.mul),
        'DIV': Symbol('DIV', '3', operator.div),
    }

    def tokenize(self, expr):
        """Tokenizes input into atom list"""
        Atom = collections.namedtuple('Atom', ['tok', 'val'])
        for i in re.findall('[\d.]+|[%s]' % ''.join(self.token_map), expr):
            yield Atom(self.token_map.get(i, 'NUM'), i)
        yield None

    def calculate(self, expr):
        """"
        https://en.wikipedia.org/wiki/Shunting-yard_algorithm
        """
        out = []
        ops = []
        iter = self.tokenize(expr)
        # Read token
        t = iter.next()
        # While there are tokens to read
        while t:
            # if operator o1, then:
            if t.tok in self.t_map:
                # while there is an operator o2 at the top of stack and
                    # o1 is left-assoc and its prec is <= o2.prec or
                    # o1 is right-assoc and o1.prec < o2
                while len(ops) and ops[-1].tok in self.t_map and \
                        self.t_map[t.tok].pr <= self.t_map[ops[-1].tok].pr:
                    # then pop off o2 to stack
                    out.append(ops.pop())
                ops.append(t)
            # if token is left paren, then push to stack
            elif t.tok == 'LPAR':
                ops.append(t)
            # if token is right parenthesis:
            elif t.tok == 'RPAR':
                # until token at the top of the stack is left paren
                while len(ops) and ops[-1].tok != 'LPAR':
                    # pop operators off the stack onto the output queue
                    out.append(ops.pop())
                # if stack runs out without finding left paren,
                # then there are mismatched parens
                if not len(ops):
                    raise SyntaxError("Mismatched parenthesis")
                # pop left paren from the stack (but not onto output queue)
                if ops[-1].tok == 'LPAR':
                    ops.pop()
            # if number - add to output queue
            elif t.tok == 'NUM':
                out.append(t)
            # Read next token
            t = iter.next()
            # print ('WHILE: ', [x.val for x in out], [x.val for x in ops])
        # When there are no more tokens to read:
        # while there are still operator tokens in the stack
        while len(ops):
            # if operator token on the top is paren, then paren mismatch
            if ops[-1].tok in ('LPAR', 'RPAR'):
                raise SyntaxError("Mismatched parenthesis")
            # pop operator onto the output queue
            out.append(ops.pop())
        # print ('RPN: ', [t.val for t in out])
        # Do the RPN dance
        stack = []
        for token in out:
            if token.tok not in self.t_map:
                stack.append(float(token.val))
            elif token.tok in self.t_map:
                if len(stack) < 2:
                    raise SyntaxError("Invalid RPN input")
                a = stack.pop()
                stack.append(self.t_map[token.tok].op(stack.pop(), a))
            else:
                raise RuntimeError("Shouldn't happen!")

        if len(stack) > 1:
            raise SyntaxError("Calculator error.")
        return float(stack.pop())


class TestEvilCalculator(unittest.TestCase):

    def setUp(self):
        self.c = Calculator()

    def calc(self, expr):
        self.assertEqual(self.c.calculate(expr), float(eval(expr)))

    def test(self):
        self.calc("1+1")
        self.calc("5+5-3")
        self.calc("55+5-3")
        self.calc("5/5+5-3*2")
        self.calc("5+(10-3)*2")
        self.calc("5.5+(5-3)*2")

    def test_fail_lparen(self):
        with self.assertRaises(SyntaxError):
            self.c.calculate("(")
        with self.assertRaises(SyntaxError):
            self.c.calculate(")")
        with self.assertRaises(SyntaxError):
            self.c.calculate("1 + (1 * (1 / 2)")

if __name__ == "__main__":
    c = Calculator()
    while True:
        try:
            print (c.calculate(raw_input("> ")))
        except SyntaxError as e:
            print (e)
        except EOFError, KeyboardInterrupt:
            print ("Exciting..")  # I know
            break
