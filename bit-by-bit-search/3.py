from math import sqrt


def bit_by_bit_search(f, a, b, eps=1e-3):
    x = a
    h = (b - a) / 4

    fx = f(x)
    k = 1

    while True:
        x_next = x + h

        if x_next < a or x_next > b:
            h = -h / 4
            continue

        if abs(h) <= eps:
            break

        fx_next = f(x_next)
        k += 1

        if fx_next < fx:
            x = x_next
            fx = fx_next

        else:
            h = -h / 4



    return x, fx, k


def target_func(x: float) -> float:
    return (x - 5) / sqrt(x**2 + 2)


print(bit_by_bit_search(target_func, -10, 10))