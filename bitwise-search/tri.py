from math import sqrt


def bitwise_search(f, a, b, eps=1e-3):
    h = (b - a) / 4

    x = a
    fx = f(x)

    while h > eps:
        x_next = x + h
        fx_next = f(x_next)

        if fx_next < fx:
            x = x_next
            fx = fx_next

        else:
            h = -h / 4
            x_next = x + h
            if x_next > a:
                fx_next = f(x_next)
                if fx_next < fx:
                    x = x_next
                    fx = fx_next
            h = -h / 4

    return x


def bitwise_search(f, a, b, eps=1e-3):
    h = (b - a) / 4

    x = a
    fx = f(x)

    while abs(h) > eps:
        x_next = x + h

        if x_next < a or x_next > b:
            h = -h / 2
            continue

        fx_next = f(x_next)

        if fx_next < fx:
            x = x_next
            fx = fx_next
        else:
            h = -h / 2

    return x


def bitwise_search(f, a, b, eps=1e-3):
    h = (b - a) / 4

    x = a
    x_next = x + h

    fx = f(x)
    fxn = f(x_next)

    while True:
        if fx > fxn:
            if x_next < a or x_next > b:
                if abs(h) <= eps:
                    return x_next
                else: h = -h / 4

        if fx <= fxn:
            if abs(h) <= eps:
                return x_next
            else:
                h = -h / 4

        x = x_next
        fx = fxn

        x_next = x + h
        fxn = f(x_next)


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