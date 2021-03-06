import unittest
from match import match


class TestMatching(unittest.TestCase):

    def test_literal(self):
        val = match("A")
        self.assertIsNotNone(val)
        [kind, matches] = val
        self.assertEqual(kind, "lit")
        self.assertEqual(matches, "A")

    def test_negation(self):
        # define the test cases
        cases = {
          "~A": "A",
          "~(AvB)": "AvB",
          "~(A^B)": "A^B",
          "~(A->B)": "A->B",
          "~(A<->B)": "A<->B",
          "~(~A^~B)": "~A^~B",
          "~(Av(B^C))": "Av(B^C)"
        }

        for case in cases:
            val = match(case)
            self.assertIsNotNone(val, msg="match(%s) == None" % case)
            [kind, matches] = val
            self.assertEqual(kind, "~")
            self.assertEqual(matches, cases[case])

    def test_disjunction(self):
        cases = {
          "AvB": ("A", "B"),
          "~AvB": ("~A", "B"),
          "Av~B": ("A", "~B"),
          "~Av~B": ("~A", "~B"),
          "Av(B^C)": ("A", "B^C"),
          "Av(BvC)": ("A", "BvC"),
          "Av(B->C)": ("A", "B->C"),
          "Av(B<->C)": ("A", "B<->C"),
          "Av(~B^C)": ("A", "~B^C"),
          "Av~(~B^C)": ("A", "~(~B^C)"),
          "Av~((B^C)->D)": ("A", "~((B^C)->D)")
        }
        for case in cases:
            val = match(case)
            self.assertIsNotNone(val, msg="match(%s) == None" % case)
            [kind, matches] = val
            self.assertEqual(kind, "v")
            self.assertEqual(matches, cases[case])

    def test_conjunction(self):
        cases = {
          "A^B": ("A", "B"),
          "~A^B": ("~A", "B"),
          "A^~B": ("A", "~B"),
          "~A^~B": ("~A", "~B"),
          "A^(B^C)": ("A", "B^C"),
          "A^(BvC)": ("A", "BvC"),
          "A^(B->C)": ("A", "B->C"),
          "A^(B<->C)": ("A", "B<->C"),
          "A^(~B^C)": ("A", "~B^C"),
          "A^~(~B^C)": ("A", "~(~B^C)"),
          "A^~((B^C)->D)": ("A", "~((B^C)->D)")
        }
        for case in cases:
            val = match(case)
            self.assertIsNotNone(val, msg="match(%s) == None" % case)
            [kind, matches] = val
            self.assertEqual(kind, "^")
            self.assertEqual(matches, cases[case])

    def test_implication(self):
        cases = {
          "A->B": ("A", "B"),
          "~A->B": ("~A", "B"),
          "A->~B": ("A", "~B"),
          "~A->~B": ("~A", "~B"),
          "A->(B^C)": ("A", "B^C"),
          "A->(BvC)": ("A", "BvC"),
          "A->(B->C)": ("A", "B->C"),
          "A->(B<->C)": ("A", "B<->C"),
          "A->(~B^C)": ("A", "~B^C"),
          "A->~(~B^C)": ("A", "~(~B^C)"),
          "A->~((B^C)->D)": ("A", "~((B^C)->D)")
        }
        for case in cases:
            val = match(case)
            self.assertIsNotNone(val, msg="match(%s) == None" % case)
            [kind, matches] = val
            self.assertEqual(kind, "->")
            self.assertEqual(matches, cases[case])

    def test_biconditional(self):
        cases = {
          "A<->B": ("A", "B"),
          "~A<->B": ("~A", "B"),
          "A<->~B": ("A", "~B"),
          "~A<->~B": ("~A", "~B"),
          "A<->(B^C)": ("A", "B^C"),
          "A<->(BvC)": ("A", "BvC"),
          "A<->(B->C)": ("A", "B->C"),
          "A<->(B<->C)": ("A", "B<->C"),
          "A<->(~B^C)": ("A", "~B^C"),
          "A<->~(~B^C)": ("A", "~(~B^C)"),
          "A<->~((B^C)->D)": ("A", "~((B^C)->D)")
        }
        for case in cases:
            val = match(case)
            self.assertIsNotNone(val, msg="match(%s) == None" % case)
            [kind, matches] = val
            self.assertEqual(kind, "<->")
            self.assertEqual(matches, cases[case])

    def test_no_match(self):
        vals = []
        vals.append(match("a"))
        vals.append(match("AB"))
        vals.append(match("A B"))

        for val in vals:
            self.assertIsNone(val, msg="Invalid pattern matched!")


if __name__ == '__main__':
    print "Test match():"
    unittest.main()
