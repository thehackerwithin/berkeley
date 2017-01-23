def mean(numlist):
  try : 
    tot = float(sum(numlist))
    n = len(numlist)
  except TypeError : 
    raise TypeError("This is not a list of numbers")

  return tot/n
