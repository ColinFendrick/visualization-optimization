from .constants import inputs

def objective(*args):
  res = 0
  for x in args:
    res += x**2
  return res

# compute targets
results = objective(inputs)

optima_x = [0.0, 0.0]
optima_y = objective(0.0)
