def test_open_string():
    from proper_parenthetics import proper_parens
    test_input = "()()(DJKLSJDF"
    assert proper_parens(test_input) == 1


def test_balanced_string():
    from proper_parenthetics import proper_parens
    test_input = "()()(DJKLSJDF)(((())))"
    assert proper_parens(test_input) == 0


def test_broken_string():
    from proper_parenthetics import proper_parens
    test_input = "()())DJKLSJDF("
    assert proper_parens(test_input) == -1
