g = (
    "twelve lords a-leaping,",
    "eleven ladies dancing,",
    "ten pipers piping,",
    "nine drummers drumming,",
    "eight maids a-milking,",
    "seven swans a-swimming,",
    "six geese a-laying,",
    "five gold rings,",
    "four calling birds,",
    "three French hens,",
    "two turtle-doves,",
    "and a partridge in a pear tree.",
)
d = (
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
    "twelfth",
)
song = "\n\n".join(
    f"On the {d[n]} day of Christmas my true love gave to me\n"
    + (
        g[-1][4:]
        if n == 0
        else "\n".join([g[-2][:-1], g[-1]])
        if n == 1
        else "\n".join(g[-(n + 1) :])
    )
    for n in range(12)
)
