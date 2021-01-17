from data.constants import inputs
from data.results import results

# create a mapping of inputs to some results
print('A few results:')
for i in range(5):
  print('f(%.3f) = %.3f' % (inputs[i], results[i]))
