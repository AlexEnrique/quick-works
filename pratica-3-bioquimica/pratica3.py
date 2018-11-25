import matplotlib.pyplot as plt
from numpy import array

# the curve is of the form y = a * x
# 'a' is the coeficiente and '__a' the error of 'a'
def regression(x, y):
    __y = .01 # Error of y[i], for each i

    a = sum(x * y) / sum(x**2)
    __a = (sum( (__y * x)**2 ))**(1/2) / sum(x**2)

    return a, __a

concentr = array([.125, .25, .50, .75, 1.0, 1.25, 1.75])
A = array([.06, .11, .21, .31, .42, .47, .48])

n = len(A)
a, __a = regression(concentr[:n-2], A[:n-2])

# print(f"a = ({a} +/- {__a})")

func = lambda x: a * x

plt.xlabel("Solução padrão de albumina % (m/v)")
plt.ylabel("Absorbância")
plt.text(.9, .25, ("absortividade = %.2f +/- %.2f" % (a, __a)))
plt.plot(concentr[:n-2], A[:n-2], "ok")
plt.plot(concentr[n-2:], A[n-2:], "or")
plt.plot(concentr[:n-2], func(concentr[:n-2]), "--b")

plt.savefig("pratica3.png")
plt.show()
