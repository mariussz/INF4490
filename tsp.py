#!/usr/bin/env python
from csv import reader
import itertools as itt
import time
from random import sample


class Traveling_salesman:

    def __init__(self):
        try:
            with open("european_cities.csv", "r") as f:
                data = list(reader(f, delimiter=';'))
                f.close()
        except IOError as err:
            print(err)
        
        self.cities = tuple(data[0])         #saveing cities' names into tuple
        data.remove(data[0])                 #removing the first columnt from data
        self.traces = data                   #saving data to global varaible traces


    def _calculate_the_distance(self, path=[]):
        total_distance = 0.0
        
        for x in range(0,len(path)-1):       #2,3,4,5,6
            city_from = path[x]
            city_to = path[x+1]
            total_distance += float(self.traces[city_from][city_to])
            #print(str(city_from)+" do "+str(city_to)+ " = " + self.traces[city_from][city_to])
            
        return total_distance

    def exhaustive_search(self, number_of_cities= 10, show_details=0):
        shortest_distance = 0
        shortest_path = ()
        
        all_possible_paths = itt.permutations(range(0,number_of_cities),number_of_cities)
        
        for path in all_possible_paths:
            calculated_distance = self._calculate_the_distance(path)
            if calculated_distance < shortest_distance or shortest_distance == 0:
                shortest_distance = calculated_distance
                shortest_path = path[:]
                
            if show_details == 2:
                print("The distance for: {} = {}".format(list(path),calculated_distance))
        if show_details >= 1:
            print("The shortest distance = {}\nfor path = {} ".format(shortest_distance,shortest_path))
        
        return list([shortest_distance,shortest_path])
    
    
    def hill_climbing(self, number_of_cities= 10, iterations= 1000, show_details=1):
        
        path = sample(range(0,number_of_cities), number_of_cities)                          #initialise a genotype
        
        
        if show_details >=1:    #show extra information if necessery
            print("Initial path: {}\n".format(path))
        
        shortest_distance = self._calculate_the_distance(list(path))
        shortest_path = path
        
        while iterations > 0:
            genes_ab = sample(range(0,number_of_cities),2)                                #generate two random genes to swap
            path[genes_ab[0]], path[genes_ab[1]] = path[genes_ab[1]], path[genes_ab[0]]     #swap the given genes
            new_distance = self._calculate_the_distance(path)
            if new_distance < shortest_distance:
                shortest_distance = new_distance
                shortest_path = path[:]
                if show_details == 2:
                    print("New shortest distance found = {} \nfor path = {}\n".format(shortest_distance, path))
            iterations -= 1
        return list([shortest_distance,shortest_path])





















#if __name__ == "__main__":
    #start = time.time()
    #shortest_path = 0
    #paths = itt.permutations(range(0,9),9)
    #for path in paths:
        #calculated_path = calculate_the_path(path)
        #print("The path for: {} = {}".format(list(path),calculated_path))
        #if calculated_path < shortest_path or shortest_path == 0:
            #shortest_path = calculated_path
    #end = time.time()
    #print("Calculating time = {}".format(end - start))
    #print("The shortest path = {}".format(shortest_path))





