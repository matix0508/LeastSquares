import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([2.2, 3.8, 6.1, 7.9, 9.9])
y1 = np.array([1, 2, 3, 4, 5])


def least_square(x, y):
    S = len(x)
    Sx = x.sum()
    Sy = y.sum()
    Sxx = np.square(x).sum()
    Sxy = (x * y).sum()
    Syy = np.square(y).sum()
    det = S * Sxx - Sx ** 2
    a = (S * Sxy - Sx * Sy) / det
    b = (Sxx * Sy - Sx * Sxy) / det

    uy = Syy - a * Sxy - b * Sy
    ua = uy / (S-2) * S / det
    ub = ua * Sxx / S
    return a, b, ua, ub


a, b, _, _ = least_square(x1, y1)
plt.scatter(x1, y1)
plt.plot(range(10), [a * i + b for i in range(10)])
plt.show()
