import numpy as np
'''Cox-Ross_Rubenstein method'''
def discounted_price(price, rate):
  return price/(1+rate)

def initial_price_european_one_step(K, S_0, rate, X_u, X_d):
"""Returns discounted price of the expected value of a one step option with strike price K"""
  u = S_0/X_u
  d = S_0/X_d
  p = (1+rate-d)/(u-d)
  exptd = p*X_u + (1-p)*X_d
  return discounted_price(exptd)

initial_price_european_one_step(21, 20, .01, 25, 17)
#replicating needs correcting
def replicating_strat_one_step_european(S_0, rate, X_u, X_d):
  """Returns a tuple of (a, b), where a represents the number of stocks you should hold, and b the number of bonds"""
  u = S_0/X_u
  d = S_0/X_d
  a = (X_u-X_d)/((u-d)*S_0)
  b = (1+rate)**(-1)*(uX_d-dX_u)/(u-d)
# A = np.array([[S_0, 1+rate], [S_0, 1+rate]])
# v = np.array([X_u, X_d])
# Av = np.linalg.solve(A,v) """This returns the same thing as the code above just in matrix form"""
  return np.array([a,b])
