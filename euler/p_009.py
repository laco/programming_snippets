# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def abc_1000():
    for a in range(1, 500):
        for b in range(1, 1000-a):
            yield a, b, 1000 - a - b

options = list(abc_1000())
for o in options:
    assert o[0] + o[1] + o[2] == 1000


for a, b, c in abc_1000():
    if a < b and b < c and a*a + b*b == c*c:
        print(a, b, c, a*b*c)
