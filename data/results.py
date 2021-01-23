from .constants import inputs

def objective(x):
  return x**2

# compute targets
results = objective(inputs)

optima_x = 0.0
optima_y = objective(optima_x)
