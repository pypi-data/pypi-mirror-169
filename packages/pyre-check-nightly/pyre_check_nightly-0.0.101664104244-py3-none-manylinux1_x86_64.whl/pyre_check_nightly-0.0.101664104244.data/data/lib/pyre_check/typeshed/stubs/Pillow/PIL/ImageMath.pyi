from typing import Any

class _Operand:
    im: Any
    def __init__(self, im) -> None: ...
    def apply(self, op, im1, im2: Any | None = ..., mode: Any | None = ...): ...
    def __bool__(self): ...
    def __abs__(self): ...
    def __pos__(self): ...
    def __neg__(self): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    def __mod__(self, other): ...
    def __rmod__(self, other): ...
    def __pow__(self, other): ...
    def __rpow__(self, other): ...
    def __invert__(self): ...
    def __and__(self, other): ...
    def __rand__(self, other): ...
    def __or__(self, other): ...
    def __ror__(self, other): ...
    def __xor__(self, other): ...
    def __rxor__(self, other): ...
    def __lshift__(self, other): ...
    def __rshift__(self, other): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...

def imagemath_int(self): ...
def imagemath_float(self): ...
def imagemath_equal(self, other): ...
def imagemath_notequal(self, other): ...
def imagemath_min(self, other): ...
def imagemath_max(self, other): ...
def imagemath_convert(self, mode): ...

ops: Any

def eval(expression, _dict=..., **kw): ...
