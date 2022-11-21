from prettytable import PrettyTable


def make_pretty_table(qty_words: dict[str: int], col_name) -> PrettyTable:
    """Make pretty better result table"""
    result_table = PrettyTable()
    result_table.field_names = ['word', col_name]
    for word, qty in qty_words.items():
        result_table.add_row([word, qty])
    return result_table
