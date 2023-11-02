import itertools


def equilateral(sides):
    return all_positive_values(sides) and all_equal_values(sides)


def isosceles(sides):
    return all_positive_values(sides) and first_triangle_inequality(sides) and any_equal_values(sides)


def scalene(sides):
    pass


def all_positive_values(xs):
    return all(x > 0 for x in xs)


def first_triangle_inequality(sides):
    pairs = itertools.combinations(enumerate(sides), 2)

    for pair in pairs:
        third_side = set(enumerate(sides)).difference(pair)
        if sum(pair[1]) < min(third_side)[1]:
            return False

    return True


def all_equal_values(l):
    return min(l) == max(l)


def any_equal_values(l):
    pairs = itertools.combinations(l, 2)
    return any(a == b for (a, b) in pairs)
