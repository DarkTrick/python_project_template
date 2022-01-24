
from .submodule_b.b import *
from .submodule_c.c import *

def foo():
  return "foo" + "\n" + b() + "\n" + c()