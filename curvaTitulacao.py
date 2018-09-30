from scipy.interpolate import lagrange, CubicSpline
from numpy import array
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

pH = array([1.75, 2.32, 2.37, 2.44, 2.52, 2.62,
            2.71, 2.80, 2.88, 2.98, 3.13, 3.29,
            3.45, 3.78, 4.25, 5.55, 7.64, 8.80,
            9.25, 9.45, 9.60, 9.76, 9.86, 9.95,
            10.04, 10.17, 10.26, 10.35, 10.44,
            10.58, 10.74, 10.90, 11.08, 11.27,
            11.48, 11.65, 11.73, 11.81, 11.87,
            11.91, 11.97, 12.03, 12.05, 12.08,
            12.11, 12.14, 12.16, 12.17, 12.18,
            12.19, 12.19
           ])

concentracao = array([0.125/1000 * n for n in range(0, 51)])

poly = lagrange(concentracao, pH)
coefficients = poly.coef
n = poly.order
CS = CubicSpline(concentracao, pH)
CSp = CS.derivative(1)
CSpp = CS.derivative(2)

plt.plot(concentracao, pH)
# plt.plot(concentracao, CS(concentracao))
# plt.plot(concentracao, CSp(concentracao))
# plt.plot(concentracao, CSpp(concentracao))

plt.show()
