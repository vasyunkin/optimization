from math import sqrt
import logging

logging.basicConfig(level=logging.INFO)


def golden_selection(f, a, b, eps=1e-3) -> float:
    k = 0
    q = (3 - sqrt(5)) / 2

    y = a + q * (b - a)
    z = b + a - y

    fy = f(y)
    fz = f(z)

    while True:
        logging.info(f"k: {k}")

        if fy <= fz:
            a_next = a
            b_next = z

            z_next = y
            fz_next = fy

            y_next = a_next + b_next - y
            fy_next = f(y_next)

        else:
            a_next = y
            b_next = b

            y_next = z
            fy_next = fz

            z_next = a_next + b_next - z
            fz_next = f(z_next)

        delta = abs(a_next - b_next)
        
        if delta <= eps:
            x_star = (a_next + b_next) / 2
            return x_star, f(x_star)

        k += 1

        a = a_next
        b = b_next
        y = y_next
        z = z_next
        fy = fy_next
        fz = fz_next


def target_func(x: float) -> float:
    return (x - 5) / sqrt(x**2 + 2)


print(golden_selection(target_func, -10, 10))