digits = [
    None,
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
decades = [
    None,
    "ten",
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
centuries = [
    None,
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
]
exceptions = {
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}


def format_decade(n):
    t = decades[n // 10]
    o = digits[n % 10]
    return exceptions.get(
        n,
        (t or "")
        + ("-" if t and o else "")
        + (o or "")
    )


def format_century(n):
    h = digits[n // 100]
    t = format_decade(n % 100)
    return (
        (h + " hundred" if h else "")
        + (" " if h and t else "")
        + t
    )


def iter_centuries(n):
    n = abs(n)
    while n:
        yield format_century(n % 1000)
        n //= 1000


def name_from_integer(n):
    return (
               ("negative " if n < 0 else "")
               + " ".join(reversed(list(
                num + (" " if num and name else "") + (name or "")
                for num, name in zip(iter_centuries(n), centuries) if num
                ))) or "zero"
    )
