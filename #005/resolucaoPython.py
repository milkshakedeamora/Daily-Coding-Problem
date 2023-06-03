def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
def car(pair):
    def returnValue(a,b):
        return a
    return pair(returnValue)
def cdr(pair):
    def returnValue(a,b):
      return b
    return pair(returnValue)
print(car(cons(3,4)))
print(cdr(cons(3,4)))
