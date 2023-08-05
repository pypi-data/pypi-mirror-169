from pynary import PYNOpt

with open("/home/myu/files/dev/python/ygodraft/ygod/data/ext/cards.pyn", "rb") as file:
    d = file.read()

pyn = PYNOpt()

pyn.add_none()
pyn.add_bool()
pyn.add_int()
pyn.add_float()
pyn.add_str()
pyn.add_list()
pyn.add_tuple()
pyn.add_set()
pyn.add_dict()

from timeit import timeit

print(timeit(lambda: pyn.load(d), number=1))
from pynary import pyn

print(timeit(lambda: pyn.load(d), number=1))
