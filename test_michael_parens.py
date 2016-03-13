import pytest

TEST_STRINGS = [
    (u')', -1),
    (u')(', -1),
    (u'()', 0),
    (u'(()', 1),
    (u'((((()', 1),
    (u'()())', -1),
    (u'()()', 0),
    (u'(())', 0),
    (u')))(((', -1),
    (u'(define (square x) (* x x))', 0),
    (u'(define square x) (* x x))', -1),
    (u'(define (square x) (* x x)', 1),
]

@pytest.mark.parametrize(("input", "expected"), TEST_STRINGS)
def test_balanced(input, expected):
    from michael_parens import proper_parenthetics
    assert proper_parenthetics(input) == expected
