
def proper_parens(string):
    """Take a string and evaluate if parens are open, broken or balanced."""
    open_count = 0
    close_count = 0

    for thing in string:
        if thing == "(":
            open_count += 1
        elif thing == ")":
            close_count += 1
        if close_count > open_count:
            return -1
    if open_count == close_count:
        return 0
    return 1
