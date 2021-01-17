import numpy as np

def objective(x):
  return x**2

x = 4.0

# define range for input
r_min, r_max = -5.0, 5.0
# sample input range uniformly at 0.1 increments
inputs = np.arange(r_min, r_max, 0.1)
# compute targets
results = objective(inputs)

# create a mapping of inputs to some results
print('A few results:')
for i in range(5):
  print('f(%.3f) = %.3f' % (inputs[i], results[i]))
