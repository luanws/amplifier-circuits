import math


def format(
    number: float, *,
    precision: int = 2,
    positive_suffixes: list[str] = ['', 'K', 'M', 'G', 'T', 'P'],
    negative_suffixes: list[str] = ['m', 'u', 'n', 'p'],
    unit=''
) -> str:
    suffixes = positive_suffixes + negative_suffixes[::-1]
    if number == 0:
        return '0'
    magnitude = int(math.floor(math.log(abs(number), 1e3)))
    if magnitude <= len(positive_suffixes) - 1 and magnitude >= -len(negative_suffixes):
        number_str = f'{number/1e3**magnitude:.{precision}f}'
        number_str = number_str.strip('0').strip('.')
        number_str = f'{number_str}{suffixes[magnitude]}{unit}'
    else:
        number_str = f'{number:.{precision}e}{unit}'
    return number_str.replace('.', ',')


def revert(
    number_str: str,
    positive_suffixes: list[str] = ['', 'K', 'M', 'G', 'T', 'P'],
    negative_suffixes: list[str] = ['m', 'u', 'n', 'p'],
    unit: str = ''
) -> float:
    suffixes = positive_suffixes + negative_suffixes[::-1]
    number_str = number_str.replace(',', '.')
    number_str = number_str.replace(' ', '')
    if len(unit) > 0 and number_str.endswith(unit):
        number_str = number_str[:-len(unit)]
    for i, suffix in enumerate(suffixes):
        if number_str.endswith(suffix):
            sorted_sufixes = negative_suffixes[::-1] + positive_suffixes
            magnitude = sorted_sufixes.index(suffix) - len(negative_suffixes)
            if magnitude != 0:
                return float(number_str[:-len(suffix)]) * 1e3**magnitude
    return float(number_str)