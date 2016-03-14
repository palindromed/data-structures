import pytest


TEST_OPTIONS = [("()()(DJKLSJDF", 1),
                ("()()(DJKLSJDF)(((())))", 0),
                ("()())DJKLSJDF(", -1)]


@pytest.mark.parametrize("test_input, expected", TEST_OPTIONS)
def test_proper_parens(test_input, expected):
    from proper_parenthetics import proper_parens
    assert proper_parens(test_input) == expected
