from scipy.interpolate import lagrange, CubicSpline
from numpy import array, linspace
from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt

pH = array([1.58, 1.62, 1.68, 1.76, 1.79, 1.87,
            1.91, 1.96, 2.03, 2.03, 2.11, 2.09,
            2.23, 2.23, 2.40, 2.51, 2.55, 2.88,
            2.92, 3.10, 3.57, 7.47, 8.04, 8.38,
            8.57, 8.72, 8.79, 8.95, 9.00, 9.15,
            9.19, 9.35, 9.50, 9.52, 9.68, 10.00,
            10.24, 10.64, 11.02, 11.19, 11.41,
            11.51, 11.51, 11.65, 11.66, 11.68,
            11.77, 11.82, 11.87, 11.88, 11.91,
            11.95, 11.92, 11.92, 11.92, 11.92,
            11.92, 11.92
           ])

concentracao = array([0.125/1000 * n for n in range(0, 58)])

poly0 = lagrange(concentracao[5:15], pH[5:15])
poly1 = lagrange(concentracao[19:23], pH[19:23])
poly2 = lagrange(concentracao[24:35], pH[24:35])
poly3 = lagrange(concentracao[46:53], pH[46:53])

pI = 6.34
pKa1 = 2.72
pKa2 = 10.18
pKa3 = 12.01

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('[OH-] (mol/L)')
fig.suptitle('Arginina', fontsize=14, fontweight='bold')
ax.set_ylabel('pH')
ax.text(0.005, 5.5, "pI = 5.52\nPka1 = 2.07\npKa2=9.14\npKa3=11.90")

plt.plot(concentracao, pH, "-o")
plt.plot(linspace(concentracao[5], concentracao[14], 30), poly0(linspace(concentracao[5], concentracao[14], 30)), "--")
plt.plot(linspace(concentracao[19], concentracao[22], 30), poly1(linspace(concentracao[19], concentracao[22], 30)), "--")
plt.plot(linspace(concentracao[24], concentracao[34], 30), poly2(linspace(concentracao[24], concentracao[34], 30)), "--")
plt.plot(linspace(concentracao[46], concentracao[53], 30), poly3(linspace(concentracao[46], concentracao[53], 30)), "--")

plt.show()
