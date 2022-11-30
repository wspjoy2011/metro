from types import MappingProxyType
from collections import namedtuple
from prettytable import PrettyTable


Month = namedtuple('Month', 'number name')

SEASONS = MappingProxyType(
    {
        'winter': (
            Month(12, 'December'),
            Month(1,  'January'),
            Month(2,  'February'),
        ),
        'spring': (
            Month(3, 'March'),
            Month(4, 'April'),
            Month(5, 'May')
        ),
        'summer': (
            Month(6, 'June'),
            Month(7, 'July'),
            Month(8, 'August')
        ),
        'fall': (
            Month(9, 'September'),
            Month(10, 'October'),
            Month(11, 'November')
        )
    }
)


if __name__ == '__main__':
    user_month = input('Enter number or name of month: ')

    if user_month.isdigit():
        user_month = int(user_month)
    else:
        user_month = user_month.capitalize()

    for season in SEASONS:
        for month in SEASONS[season]:
            if user_month in month:
                print(f'Your choice "{month.name}" refers to the season "{season}"')
                exit()

    print(f'Your choice "{user_month}" is not correct')
    print(f'Use next values')

    cli_table = PrettyTable()
    cli_table.field_names = ['Season', 'Number', 'Name']

    for season, months in SEASONS.items():
        for month in months:
            cli_table.add_row([season, month.number, month.name])
    print(cli_table)
