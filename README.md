# P5640ex00
See the full description of this exercise in the assigned reading and on the course web site.


## C++ starter code

The starter code here (projGSL.cpp) demonstrates very basic usage of the gsl for solving a problem of coupled differential equations.  An 8th order R-K solver with fixed step size is used.  You are encouraged to try other solvers as you explore the problem.  See here for the gsl docs: https://www.gnu.org/software/gsl/doc/html/ode-initval.html

This example solves the 2D projectile motion problem with a simple model for air resistance.  After each step, data are stored in ROOT TGraphs, which are then displayed at the conclusion of the calculation.  These are the basic pieces you will need to address the Duffing Oscillator problem.

----
## Python starter code

Two examples are given for using ODE solvers from the scipy.integrate sub-package in Python.  In these examples graphs are made using matplotlib.

1) Solution (projScPY2.py[ipynb]) using a more modern interface [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/reference/generated/scipy.integrate.solve_ivp.html#scipy.integrate.solve_ivp).  See also: https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html  and https://www.programcreek.com/python/example/119375/scipy.integrate.solve_ivp

2) Solution (projScPY.py[ipynb]) using an older interface [scipy.integrate.odeint¶](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html) (see comments here: https://docs.scipy.org/doc/scipy/reference/integrate.html).

The notebook versions contain additional comments on using the integrators.

----

Give the computing IDs for team members here:  UVA_ID1  UVA_ID2 ...

Push your solution code and PDF reports to this repo.
