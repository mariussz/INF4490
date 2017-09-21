import itertools as itt
import random as r


number_of_cities = 3
path = r.sample(range(0,number_of_cities), number_of_cities)

spath = path[:]
print("spath1: {}".format(spath))
print("path1: {}".format(path))
print("\n")

path[0] = 9
print("spath2: {}".format(spath))
print("path2: {}".format(path))
print("\n")
