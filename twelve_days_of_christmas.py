gifts = (
    "twelve lords a-leaping,",
    "eleven ladies dancing,",
    "ten pipers piping,",
    "nine drummers drumming,",
    "eight maids a-milking,",
    "seven swans a-swimming,",
    "six geese a-laying,",
    "five golden rings,",
    "four calling birds,",
    "three French hens,",
    "two turtle-doves,",
    "and a partridge in a pear tree."
)

days = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
)


def line(num):
    if num == 0:
        return gifts[-1][4:]
    if num == 1:
        return "\n".join([gifts[-2][:-1], gifts[-1]])
    return "\n".join(gifts[-(num+1):])


song = "\n\n".join(
    f"On the {days[n]} day of Christmas my true love gave to me\n{line(n)}"
    for n in range(12)
)
