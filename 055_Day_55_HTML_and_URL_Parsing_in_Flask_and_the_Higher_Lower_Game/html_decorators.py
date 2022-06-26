def make_bold(function):
    def add_b_tags():
        bold_html = f"<b>{function()}</b>"
        return bold_html
    return add_b_tags


def make_emphasis(function):
    def add_em_tags():
        emphasis_html = f"<em>{function()}</em>"
        return emphasis_html
    return add_em_tags


def make_underlined(function):
    def add_u_tags():
        underline_html = f"<u>{function()}</u>"
        return underline_html
    return add_u_tags