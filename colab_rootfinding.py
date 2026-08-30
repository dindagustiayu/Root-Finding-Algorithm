{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bbed703e-5538-42eb-a488-4bc2cbfcbafb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      converged: True\n",
       "           flag: converged\n",
       " function_calls: 42\n",
       "     iterations: 40\n",
       "           root: 7.758770483143962\n",
       "         method: bisect"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import package\n",
    "import numpy as np \n",
    "from scipy.optimize import root_scalar\n",
    "\n",
    "# A grid of distance from the nucleus, in atomic units (bohr)\n",
    "r = np.linspace(0, 60, 100)\n",
    "\n",
    "# Nuclear charge\n",
    "Z = 1\n",
    "\n",
    "# Factor for the 4s orbital\n",
    "N = np.sqrt(Z**1.5 /np.pi) / 192\n",
    "\n",
    "rho = Z * r /2\n",
    "def psi(rho):\n",
    "    return N * (24 - 36 * rho + 12 * rho**2 - rho**3) * np.exp(-rho /2)\n",
    "\n",
    "root_scalar(psi, method='bisect', bracket=(6,8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0e63eaf0-f8ca-46df-b53f-7825dd91f9cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      converged: True\n",
       "           flag: converged\n",
       " function_calls: 7\n",
       "     iterations: 6\n",
       "           root: 7.758770483143634\n",
       "         method: brentq"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root_scalar(psi, method ='brentq', bracket=(6, 8))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ac34ece4-f25e-4b6e-a433-0e86d042e6b3",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\ACER\\miniconda3\\envs\\myenv\\Lib\\site-packages\\scipy\\optimize\\_root_scalar.py:327: RuntimeWarning: Derivative was zero.\n",
      "  r, sol = methodc(f, x0, args=args, fprime=fprime, fprime2=None,\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "      converged: False\n",
       "           flag: convergence error\n",
       " function_calls: 2\n",
       "     iterations: 1\n",
       "           root: 6.0\n",
       "         method: newton"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# import package\n",
    "from scipy.optimize import root_scalar\n",
    "\n",
    "# A grid of distance from the nucleus, in atomic units (bohr)\n",
    "r = np.linspace(0, 60, 100)\n",
    "\n",
    "# Nuclear charge\n",
    "Z = 1\n",
    "\n",
    "# Factor for the 4s orbital\n",
    "N = np.sqrt(Z**1.5 /np.pi) / 192\n",
    "\n",
    "rho = Z * r /2\n",
    "\n",
    "# function and first derivative\n",
    "\n",
    "def func(rho):\n",
    "    \"\"\"4s orbital wavefunction:pre-exponential function\"\"\"\n",
    "    return 24 - 36* rho + 12*rho**2 - rho**3\n",
    "\n",
    "def funcp(rho):\n",
    "    return -36 + 24*rho - 3*rho**2\n",
    "\n",
    "# root-finding\n",
    "\n",
    "root_scalar(func, method='newton', fprime=funcp, x0 = 6)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0c8e524a-e0b9-4df3-96b6-8b6651674b61",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "      converged: True\n",
       "           flag: converged\n",
       " function_calls: 8\n",
       "     iterations: 4\n",
       "           root: 7.758770483143632\n",
       "         method: newton"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "root_scalar(func, method='newton', fprime=funcp, x0 = 8)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1486b639-3506-4f91-9654-c7c89798c0ef",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
