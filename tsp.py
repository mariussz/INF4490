#!/usr/bin/env python
from csv import reader
import itertools as itt
import time

#the itertools module provides a permutations function that returns successive permutations, this is useful for exhaustive search
try:
    with open("european_cities.csv", "r") as f:
        data = list(reader(f, delimiter=';'))
        f.close()
except IOError as err:
    print(err)

cities = tuple(data[0])         #saveing cities' names into tuple
data.remove(data[0])            #removing the first columnt from data
traces = data                   #saving data to global varaible traces


def calculate_the_path(path=[]):
    total_distance = 0.0
    
    for x in range(0,len(path)-1):    #2,3,4,5,6
        city_from = path[x]
        city_to = path[x+1]
        total_distance += float(traces[city_from][city_to])
        #print(str(city_from)+" do "+str(city_to)+ " = " + traces[city_from][city_to])
        
    return total_distance


start = time.time()
#calculate_the_path([3,5,7,4])
shortest_path = 0
paths = itt.permutations(range(0,8),8)
for path in paths:
    calculated_path = calculate_the_path(path)
    print("The path for: {} = {}".format(list(path),calculated_path))
    if calculated_path < shortest_path or shortest_path == 0:
        shortest_path = calculated_path

end = time.time()
print("Calculating time = {}".format(end - start))
print("The shortest path = {}".format(shortest_path))





