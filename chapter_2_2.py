import numpy as np
'''Cox-Ross_Rubenstein method'''
def discounted_price(price, rate):
  return price/(1+rate)

def initial_price_european_one_step(K, S_0, rate, S_1_u, S_1_d):
    """Returns discounted price of the expected value of a one step option with strike price K"""
    u = S_1_u/S_0
    d = S_1_d/S_0
    p = (1+rate-d)/(u-d)
    high_pay_out = S_1_u - K
    low_pay_out = 0
    exptd = p*high_pay_out + (1-p)*low_pay_out
    return discounted_price(exptd, rate)

# example
print(initial_price_european_one_step(21, 20, .01, 25, 17)

def replicating_strat_one_step_european(K, S_0, rate, S_1_u, S_1_d):
    """Returns a tuple of (a, b), where a represents the number of stocks you should hold, and b the number of bonds"""
    u = S_1_u/S_0
    d = S_1_d/S_0
    X_u = S_1_u - K
    X_d = 0
    a = (X_u-X_d)/((u-d)*S_0)
    b = (1+rate)**(-1)*(u*X_d-d*X_u)/(u-d)
    return np.array([a,b])

#example
print(replicating_strat_one_step_european(21, 20, .01, 25, 17))
