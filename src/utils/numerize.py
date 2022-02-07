import math

positive_suffixes: list[list[str]] = [
    [''],
    ['k', 'K'],
    ['M'],
    ['G'],
    ['T'],
    ['P']
]

negative_suffixes: list[list[str]] = [
    ['m'],
    ['μ', 'u'],
    ['n'],
    ['p']
]


def format(
    number: float, *,
    precision: int = 2,
    unit=''
) -> str:
    suffixes_options = positive_suffixes + negative_suffixes[::-1]
    if number == 0:
        return '0'
    magnitude = int(math.floor(math.log(abs(number), 1e3)))
    if magnitude <= len(positive_suffixes) - 1 and magnitude >= -len(negative_suffixes):
        number_str = f'{number/1e3**magnitude:.{precision}f}'
        number_str = number_str.strip('0').strip('.')
        suffix = suffixes_options[magnitude][0]
        number_str = f'{number_str}{suffix}{unit}'
    else:
        number_str = f'{number:.{precision}e}{unit}'
    return number_str.replace('.', ',')


def revert(
    number_str: str,
    unit: str = ''
) -> float:
    suffixes_options = positive_suffixes + negative_suffixes[::-1]
    number_str = number_str.replace(',', '.')
    number_str = number_str.replace(' ', '')
    if len(unit) > 0 and number_str.endswith(unit):
        number_str = number_str[:-len(unit)]

    sorted_sufixes_options = negative_suffixes[::-1] + positive_suffixes
    for suffix_options in suffixes_options:
        for suffix in suffix_options:
            if number_str.endswith(suffix):
                magnitude = sorted_sufixes_options.index(
                    suffix_options) - len(negative_suffixes)
                if magnitude != 0:
                    return float(number_str[:-len(suffix)]) * 1e3**magnitude
    return float(number_str)
