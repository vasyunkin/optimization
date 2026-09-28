from math import sqrt


def bitwise_search(f, a, b, eps=1e-3):
    h = (b - a) / 4

    x = a
    fx = f(x)

    while True:
        x_next = x + h

        if x_next < a or x_next > b:
            if abs(h) <= eps:
                return x

            h = -h / 4
            continue

        fx_next = f(x_next)

        if fx > fx_next:
            x = x_next
            fx = fx_next

            if a < x < b:
                continue

        if abs(h) <= eps:
            return x

        x = x_next
        fx = fx_next
        h = -h / 4


def target_func(x: float) -> float:
    return (x - 5) / sqrt(x**2 + 2)


print(bitwise_search(target_func, -10, 10))