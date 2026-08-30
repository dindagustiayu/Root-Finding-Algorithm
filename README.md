---
title: "A Root-Finding Algorithms"
date: "2026-08-27"
---

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1_Smn3XOiIKVI4S9Yp9WUsywi0FIn4OoD?usp=sharing)

# What are root-finding algorithms?

A root-finding algorithm is an iterative calculation scheme to approximate a single, isolated root of a function ($f$). Root-finding algorithms are tools used in mathematics and computer science to locate the solutions or "roots," of equations. These algorithms help us find solutions to equations where the function equals zero. 

For example, if we have an equation like $f(x) = 0$, a root-finding algorithm will help us determine the value of $x$ that makes this equation equal to zero. But this can be tricky, especially with complicated functions. That's where numerical methods come to the rescue. These methods include strategies like the _Bisection, Brent's Algorithm, and the Newton-Raphson method, each with its own strengths and use cases.

# Why do we use numerical root-finding algorithms?
This topic is introduced with the goal of easing us into numerical solutions to mathematical problems. In the real world, equations can represent everything from engineering problems to scientific mysteries. These methods are like problem-solving superpowers, making it possible to optimize designs, predict behaviors, and analyze data more effectively. 

Learning Numerical Root-Finding methods is essential because it equips us with problem-solving skills that are valuable in various fields. They are important because they allow us to find solutions to equations that might not have straightforward answers. Imagine trying to pinpoint the exact location where a function crosses the zero line.

# Prerequisite

- Polynomial

# Preliminaries

- `scipy.optimize` containts package that implementions of algorithms to find the roots of arbitary univariative and multivariate functions.
- `scipy.optimization.root_scalar` is a package to find the roots of a univariate (scalar) function, $f(x)$.

# Case study

Here, we will demonstrate three commonly used root-finding methods to determine the positions of the radial nodes in the orbital. For atomic orbitals, the wavefunction can be separated into a radial part and an angular part so that it has the form.

$$\Psi(r, \ \theta, \ \psi) = R(r) Y(\theta, \ \phi) \quad (1)$$

The positions of radial nodes in the 4s atomic orbital ($n = 4, \ l=0, \ ml = 0$), which may be written:

$$\Psi(r, \ \theta, \ \psi) = R(r) Y(\theta, \ \phi) =N(24 -36 \rho +12 \rho^{2} - \rho^{3})e^{- \rho/2} \quad (2)$$

where $\rho = 2Zr/n = Zr/2$ and $N = (Z^3 /pi)^{1/2} /192$ combines the spherical harmonic $y_{00}$ and a normalization constant. Z is the nuclear charge in multiples of the electron charge, $e$, and the units of $r$ are bohr, $a_0 \approx 52.9$ pm; for simplicity, we have assumed the nucleus to be infinitely heavy.

## Available solvers

`scipy.optimize` provides several methods for obtaining the roots of both univariate and multivariate functions. The algorithms relation to functions of a single variable:

- `bisect`: Bisection;
- `brenth`: Brent's algorithm;
- `newton`: Newton-Raphson

## Bisection
The bisection method introduces a simple idea to hone in on the root. This method requires a bracketing interval $[a, \ b]$: $x=a$ and $x=b$ such that the desired root is known to lie between $a$ and $b$. Start with an interval $[a, \ b]$ that brackets the root. The interval should only bracket one root, so that $f(a) \times f(b) < 0$. The bisection algorithm divides this interval each iteration, successively refining the approximation for the root:

$x_{n+1} = (a + b) /2$$

$$ \mbox{If} f(x_{n+1} \times f(a) > 1 \mbox{then let} a = x_{n+1})$$

If $f(x_{n+1} \times f(b) >1)$ then let $a =x_{n+1}$. Thus the new $[a, \ b]$ is a smaller interval that brackets the root.

Each step halves the interval size. Convergence is guaranteed (you can't lose the root). This method has "linear" convergence, that is, the log of the error decreases linearly with the number of iterations.

In this case, root finding for orbital 4s used Bisection method with $\rho =6$ and $\rho = 8$: 

```python
# import package
import numpy as np 
from scipy.optimize import root_scalar

# A grid of distance from the nucleus, in atomic units (bohr)
r = np.linspace(0, 60, 100)

# Nuclear charge
Z = 1

# Factor for the 4s orbital
N = np.sqrt(Z**1.5 /np.pi) / 192

rho = Z * r /2
def psi(rho):
    return N * (24 - 36 * rho + 12 * rho**2 - rho**3) * np.exp(-rho /2)

root_scalar(psi, method='bisect', bracket=(6,8))
```
```
converged: True
           flag: converged
 function_calls: 42
     iterations: 40
           root: 7.758770483143962
         method: bisect
```

## Brent's Algorithm

Brent's method is a root-finding algorithm which combines root bracketing, bisection, and inverse quadratic interpolation. It has the reliability of bisection, but it can be as quick as some of the less reliable methods. The idea is to use the secant method or inverse quadratic interpolation if possible, because they converge faster, but to fall back to the more robust bisection method if necessary.

The basic version is referred to as method = `brentq`:

```python
root_scalar(psi, method ='brentq', bracket=(6, 8))
```
```
converged: True
           flag: converged
 function_calls: 7
     iterations: 6
           root: 7.758770483143634
         method: brentq
```


The returned object summarizes how the algorithm proceeded. The most important information in this object is as follows:
<br>

|Key | Description|
|--|--|
|`converged` | `True/False', the algorithm found the root successfully |
|`flag` | `converged`, confirming a valid root 
|`function_calls`| The number of times the algorithm evaluated $f(x)$ during search the root|
|`iteration` | The number of steps to estimate the root|

<br>

The returned object has a flag, `converged`, indicating the algorithm was succesfully, some statistics on how the algorithm proceeded, and the value of the root: here $\rho = 7.759$. 

- The bisection method can be slow (it required 42 function calls here), but it has the merit that for well-behaved functions, it cannot fail.
- Brent's method returned the same root, but faster than the bisection method. It takes only seven function calls.
  

## Newton-Raphson

Instead of bracketing the root, the Newton-Raphson method (finding one root) makes a linear approximation to the function each iteration to get a better guess at the root. Start with an $x_1$ near the root. Iterate using the formula:

$$x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$$

This formula can be easily derived from a Taylor expansion about $X_n$

Example - Calculate the Square Root of 5

$$\begin{aligned}f(x) &= x^2 - 5 \\
f'(x) &= 2x \\
x_{k+1} &= x_k - \frac{x^2 -5}{2x} 
\end{aligned}$$

|k | $x_k$|
|--|---|
|1 | 2|
|2| 2.25|
|3| 2.2361111|
|4| 2.2360798|
|infinity | 2.2360798|

This method converges much faster than bisection (superlinear). But this method can head to other roots, go to infinity, or get trapped in cycles. Not guaranteed to converge.

In this case, it is easy to code a function to return the first derivative.  In fact, since $e^{- \rho /2}$ is not zero at the nodes, we can divide $\psi$ by this factor and find the roots of its polynomial pre-exponential function. Consider the starting guess, $\rho = 6$.

```python
# import package
from scipy.optimize import root_scalar

# A grid of distance from the nucleus, in atomic units (bohr)
r = np.linspace(0, 60, 100)

# Nuclear charge
Z = 1

# Factor for the 4s orbital
N = np.sqrt(Z**1.5 /np.pi) / 192

rho = Z * r /2

# function and first derivative

def func(rho):
    """4s orbital wavefunction:pre-exponential function"""
    return 24 - 36* rho + 12*rho**2 - rho**3

def funcp(rho):
    return -36 + 24*rho - 3*rho**2

# root-finding

root_scalar(func, method='newton', fprime=funcp, x0 = 6)
```
```
converged: False
           flag: convergence error
 function_calls: 2
     iterations: 1
           root: 6.0
         method: newton
```

```python
root_scalar(func, method='newton', fprime=funcp, x0 = 8)
```
```
 converged: True
           flag: converged
 function_calls: 8
     iterations: 4
           root: 7.758770483143632
         method: newton
```

It is important to be aware of the circumstances under which the Newton-Raphson method can fail to find its root (initial guess $\rho = 6$. As indicated in the warning report, this failed because the function's first derivative was zero at the initial guess:  We started the algorithm at a maximum in $f(x)$. Without a notion of how to construct an extrapolation from this point back to $f =0$

# Conclusion

Table. The result of finding the root using different methods
|Algorithm | Root | Function calls | Iterations|
|--|--|--|--|
|Bisection | 7.758770483143962 | 42 | 40|
|Brent's Algorithm | 7.758770483143634 | 7 | 6|
|Newton-Raphson (x0 = 8) |7.758770483143632 |8 |4 |

From the Table above, all three methods find the same root ($\approx 7.7588$), confirming accuracy. Newton-Raphson is the fastest method (4 iterations and 8 function calls), Brent's Algorithm is nearly as fast (6 iterations and 7 function calls), while Bisection is the slowest (40 iterations and 42 function calls). 

Overall, Brent's Algorithm offers a good balance of speed; Newton-Raphson is fastest but needs a good initial guess ($\rho = 6$, convergence error), and Bisection is average but least efficient.
