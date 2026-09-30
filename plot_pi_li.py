"""Plot the prime-counting function pi(x) and logarithmic integral Li(x)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expi
from sympy import primerange

# Integer x values for the prime-counting function.
x = np.arange(2, 1001)
primes = np.fromiter(primerange(1, x[-1] + 1), dtype=int)
pi_x = np.searchsorted(primes, x, side="right")

# Li(x) = Ei(log(x)), the standard offset logarithmic integral.
li_x = expi(np.log(x))

plt.figure(figsize=(9, 5.5))
plt.plot(x, pi_x, label=r"$\pi(x)$", linewidth=2)
plt.plot(x, li_x, label=r"$\mathrm{Li}(x)$", linewidth=2)
plt.xlabel("x")
plt.ylabel("value")
plt.title(r"Prime-counting function $\pi(x)$ and logarithmic integral $\mathrm{Li}(x)$")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("pi_li.png", dpi=160)
plt.show()
