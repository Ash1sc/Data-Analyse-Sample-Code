import __init__
import util.setup

a, b, c = 1, 2, util.setup.c(3)
t = (a, b, c)
print(t)
print(t[2].get_attr())

c.set_attr(4)
print(t)
print(t[2].get_attr())
