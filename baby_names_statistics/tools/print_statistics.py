from prettytable import PrettyTable

from baby_names_statistics.tools.find_min_max_numbers_of_names import find_min_max_names


def print_table(names, gender, ban_names, reverse=False):
    """Print result console table"""
    names_table = PrettyTable()
    names_table.field_names = ['Year', f'Most {gender}', 'Most QTY', f'Least {gender}', 'Least QTY']
    for year, name in sorted(names.items(), reverse=reverse):
        most_name = name[0][0]
        most_name_qty = name[0][-1]
        least_name = name[1][0]
        least_name_qty = name[1][-1]
        names_table.add_row([year, most_name, most_name_qty, least_name,  least_name_qty])
    least_name_ever, most_name_ever = find_min_max_names(names)
    print(names_table)
    print(f"""
Least name: 
Name: {least_name_ever[1]} 
Numbers of names: {least_name_ever[0]} 
Year: {least_name_ever[2]}""")

    print(f"""
Most name: 
Name: {most_name_ever[1]} 
Numbers of names: {most_name_ever[0]} 
Year: {most_name_ever[2]}""")

