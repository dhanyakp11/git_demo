import time
from functools import wraps
def my_decorator(func):
  @wraps(func)
  def wrapper(*args,**kwargs):
    print(func(*args,**kwargs))
  return wrapper

def timer(func):
  @wraps(func)
  def wrapper(*args,**kwargs):
    t1=time.time()
    func(*args,**kwargs)
    t2=time.time()-t1
    print('{} ran in {} sec'.format(func.__name__,t2))
  return wrapper

@timer
@my_decorator
def calc(num):
  return num**3

calc(5)
