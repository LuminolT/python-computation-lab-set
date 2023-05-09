import math


def compute_pi(precision=1e-15):
    sum_k = 0
    k = 0
    prev_pi = 0
    while True:
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = (math.factorial(k) ** 4) * (396 ** (4 * k))
        sum_k += num / den

        pi_inverse = (2 * math.sqrt(2) / 9801) * sum_k
        pi = 1 / pi_inverse

        if abs(pi - prev_pi) < precision:
            break

        prev_pi = pi
        k += 1

    return pi


if __name__ == "__main__":
    pi = compute_pi()
    print("计算的pi的近似值为：", pi)
    print("math.pi的值为：", math.pi)
