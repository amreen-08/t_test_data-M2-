import numpy as np
import pandas as pd
from scipy.stats import norm, t, binom
from statistics import stdev

data = [52, 55, 49, 50, 58, 54, 53, 51]

def One_Sample_T_Test_with_data(x,Mu,alternative):
  n = len(x)
  x_bar = np.mean(x)
  sd = stdev(x)
  alpha = 0.05
  df = n-1
  sd_error = sd/np.sqrt(n)
  t_cal = (x_bar - Mu)/sd_error
  print("t_cal = ",t_cal)

  if (alternative == "less"):
    p_vlaue = t.cdf(t_cal,df)
    t_left = t.ppf(alpha,df)
    print("p_value = ",p_vlaue)
    print("t_left = ",t_left)

    if(t_cal < t_left):
      print("Hypothesis rejected")
    else:
      print("Hypothesis not rejected")

  elif (alternative == "greater"):
    p_value = 1-t.cdf(t_cal,df)
    t_right = t.ppf(1-alpha,df)
    print("p_value = ",p_value)
    print("t_right = ",t_right)

    if(t_cal > t_right):
      print("Hypothesis rejected")
    else:
      print("Hypothesis not rejected")

  elif (alternative == "two-sided"):
    p_value = 2*(1-t_cal(t_cal,df))
    t_left = t.ppf(alpha/2,df)
    t_right = t.ppf(1-alpha/2,df)
    print("p_value = ",p_value)
    print("t_left = ",t_left)
    print("t_right = ",t_right)

    if(t_cal < t_left or t_cal > t_right):
      print("Hypothesis rejected")
    else:
      print("Hypothesis not rejected")

  else:
    print("Invalid alternative hypothesis")

One_Sample_T_Test_with_data(data,50,'greater')