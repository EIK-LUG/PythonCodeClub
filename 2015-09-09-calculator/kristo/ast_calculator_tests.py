import unittest
import ast_calculator as ast_calc


class TestAstCalculator(unittest.TestCase):

    def test_get_priority_operation(self):
        self.assertEqual(ast_calc.get_priority_operation("1+2+3/4"), "/")
        self.assertEqual(ast_calc.get_priority_operation("1+2+3*4"), "*")
        self.assertEqual(ast_calc.get_priority_operation("1+2+3+4"), "+")
        self.assertEqual(ast_calc.get_priority_operation("1-2+3+4"), "-")

    def test_get_priority_scope(self):
        self.assertEqual(ast_calc.get_priority_scope("(1+(2+(3+4))+(5+6))"), "(3+4)")
        self.assertEqual(ast_calc.get_priority_scope("(1+(2+(3+4))+(5+6)+(7+(8+(9+(10+11))))"), "(10+11)")
        self.assertEqual(ast_calc.get_priority_scope("(1+9.0+(5+6)+(7+(8+30.0))"), "(8+30.0)")

    def test_get_priority_simple_expr(self):
        self.assertEqual(ast_calc.get_priority_simple_expr("(1+2+3/4)"), "3/4")
        self.assertEqual(ast_calc.get_priority_simple_expr("(1+2+3*4)"), "3*4")
        self.assertEqual(ast_calc.get_priority_simple_expr("(1+2+3+4)"), "1+2")
        self.assertEqual(ast_calc.get_priority_simple_expr("(1-2+3+4)"), "1-2")

    def test_eval_basic_expr(self):
        self.assertEqual(ast_calc.eval_basic_expr("3/4"), 0.75)
        self.assertEqual(ast_calc.eval_basic_expr("3*4"), 12)
        self.assertEqual(ast_calc.eval_basic_expr("3+4"), 7)
        self.assertEqual(ast_calc.eval_basic_expr("1-2"), -1)
        self.assertEqual(ast_calc.eval_basic_expr("0.6666666666666666-4"), -3.3333333333333335)

    def test_calc_eval(self):
        expressions = ["(2+3)",
                       "(2*(2/3)-4)",
                       "(1+1+2-3-3-3)",
                       "(2+2-4*(8-7))",
                       "(1+(2+(3+4))+(5+6)+(7+(8+(9+(10+11))))"]

        for expr in expressions:
            print(ast_calc.calc_eval(expr))
            self.assertEqual(ast_calc.calc_eval(expr), eval(expr))


if __name__ == "__main__":
    unittest.main()
