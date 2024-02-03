from contextlib import contextmanager
import time

@contextmanager
deftimer(label):
 start = time.time()
try:
 yield
finally:
 end = time.time()
print(f'{label}: {end - start} seconds')

# Usage:
# with timer('Model training'):
#   Your code block here, e.g.: train your model