#!/usr/bin/env python
from csv import reader
import itertools as itt
import time
from random import sample, randint
from math import factorial


class Traveling_salesman:

    def __init__(self, file_path):
        try:
            with open(file_path, "r") as f:
                data = list(reader(f, delimiter=';'))
                f.close()
        except IOError as err:
            print(err)
        
        self.cities = tuple(data[0])         #saveing cities' names into tuple
        data.remove(data[0])                 #removing the first columnt from data
        self.traces = data                   #saving data to global variable traces


    def _calculate_the_distance(self, path=[]):
        total_distance = 0.0
        
        for x in range(len(path)-1):
            city_from = path[x]
            city_to = path[x+1]
            total_distance += float(self.traces[city_from][city_to])
        total_distance += float(self.traces[path[len(path)-1]][path[0]])        
            
        return total_distance
    
    def _select_parents(self, population_size):
        ret_pairs = []
        while len(ret_pairs) < population_size:
            new_pair = sample(range(0,population_size),2)       #generate a new pair of genotypes' id
            if new_pair not in ret_pairs:                       #check if unique
                ret_pairs.append(new_pair)  
                    
        return ret_pairs
    
    def _recombine_pairs(self, start, stop, parent1, parent2):
        offspring = [None]*len(parent1)
        offspring[start:stop] = parent1[start:stop]                 #copy a slice from first parent
        
        # Map the same slice in parent2 to offspring using indices from parent a:
        for ind,x in enumerate(parent2[start:stop]):
            ind += start
            if x not in offspring:
                while offspring[ind] != None:
                    ind = parent2.index(parent1[ind])
                offspring[ind] = x

        # Copy over the rest from parent 1
        for ind,x in enumerate(offspring):
            if x == None:
                offspring[ind] = parent2[ind]            
        
        return offspring
    def _citi_names_to_id(self, names):
        ret_list = []
        for name in names:
            if name in self.cities:
                citi_id = self.cities.index(name)
                ret_list.append(citi_id)
            else:
                print("The city {} not exists in the list".format(name))
        return ret_list
    
    def _get_random_subset(self, input_list):
        if len(input_list) >= 5:
            point_a = sample(range(0,len(input_list)-3), 1)[0]
            point_b = sample(range(point_a + 2,len(input_list)+1), 1)[0]
            outList = list([input_list[point_a:point_b],point_a,point_b-1])
        else:
            outList = list([input_list,0,len(input_list)])
            #raise ValueError('The input_list paramether must be at least 5 elements length')
        return outList


    
    
    
    def _mutate(self, genotype, mutation_type = 0):
        return_genotype = genotype[:]
        
        if mutation_type == 0:
            rand_id = randint(0,len(return_genotype)-1)
            l_neigh_id = None
            r_neigh_id = None
            
            
            city = return_genotype[rand_id]
            
            if rand_id == 0:
                l_neigh_id = len(return_genotype)-1
                r_neigh_id = rand_id + 1
            elif rand_id == (len(return_genotype)-1):
                l_neigh_id = rand_id -1
                r_neigh_id = 0
            else:
                l_neigh_id = rand_id -1
                r_neigh_id = rand_id + 1
            
            citys_paths = self.traces[city][:]
            l_neigh_distance = citys_paths[return_genotype[l_neigh_id]]
            r_neigh_distance = citys_paths[return_genotype[r_neigh_id]]
            
            sorted_distances_list = []
            for idd, distance in enumerate(list(citys_paths)):
                sorted_distances_list.append(list([distance,idd]))
            sorted_distances_list.sort()
            
            closest_city = None
            for distance in sorted_distances_list:
                if distance[1] != city and distance[1] != return_genotype[l_neigh_id] and distance[1] != return_genotype[r_neigh_id]:
                    closest_city = distance[1]
                    break
                
            
            #closest_city = sorted_distances_list[0][1]
            closest_city_id = return_genotype.index(closest_city)
            if float(l_neigh_distance) > float(r_neigh_distance):
                return_genotype[l_neigh_id], return_genotype[closest_city_id] = return_genotype[closest_city_id], return_genotype[l_neigh_id]
            else:
                return_genotype[r_neigh_id], return_genotype[closest_city_id] = return_genotype[closest_city_id], return_genotype[r_neigh_id]
            
        else:
            genes_ab = sample(range(0,len(return_genotype)),2)               #generate two random genes to swap
            return_genotype[genes_ab[0]], return_genotype[genes_ab[1]] = return_genotype[genes_ab[1]], return_genotype[genes_ab[0]]     #swap genes
          
        return return_genotype
        
    
    def exhaustive_search(self, number_of_cities= 10):
        shortest_distance = 0
        shortest_path = ()
        
        all_possible_paths = itt.permutations(range(0,number_of_cities),number_of_cities)
        
        for path in all_possible_paths:
            calculated_distance = self._calculate_the_distance(path)
            if calculated_distance < shortest_distance or shortest_distance == 0:
                shortest_distance = calculated_distance
                shortest_path = path[:]
        
        return list([shortest_distance,shortest_path])
    
    
    
    def hill_climbing(self, number_of_cities= 24, number_of_generations= 100, genotype = None):
        
        if genotype is None:
            genotype = sample(range(0,number_of_cities), number_of_cities)
        
        shortest_distance = self._calculate_the_distance(genotype)
        best_genotype = genotype[:]
        counter = number_of_generations
        
        while counter > 0:
            new_genotype = self._mutate(best_genotype, mutation_type = 1)
            new_distance = self._calculate_the_distance(new_genotype)
            
            if new_distance < shortest_distance:
                counter = number_of_generations         #reset the counter after sucess and continue 
                shortest_distance = new_distance
                best_genotype[:] = new_genotype[:]
            counter -= 1
            
        return list([shortest_distance,best_genotype])




    def genetic_algorithm(self, population_size = 10, number_of_cities= 24, 
                          number_of_generations = 100, couple_with_hill_climbing = False):
        """Description"""
        population = []
        distances = []
        all_sol = factorial(number_of_cities)                                       #number of all possible solutions- permutation
        population_size = population_size - (population_size%2)                     #to make sure the population size is an even number
        start = randint(0, number_of_cities - (number_of_cities // 2))              #slice starting point. Genotype's length is the same as the number_of_cities
        stop = start + (number_of_cities // 2)                                      #the length of a slice
        
        
        #initialise population
        while len(population) < population_size and len(population) < all_sol:      #..and prevent infinite loop
            path = sample(range(0,number_of_cities), number_of_cities)
            if path not in population:
                population.append(path)
                
                
        #evaluate each candidate
        for genotype in population:
            distance = self._calculate_the_distance(genotype)
            distances.append(distance)
            
        #repeat until termination condition is reached
        while number_of_generations > 0:
            #select parents (ids)          
            parents_pairs = self._select_parents(population_size)
            offsprings = []
            offsprings_distances = []
            
            #recombine pairs- crossover
            for pair in parents_pairs:
                parent1 = population[pair[0]][:]
                parent2 = population[pair[1]][:]                
                
                #print("parent 1 = {}".format(parent1))
                #print("parent 2 = {}".format(parent2))
                
                new_offspring = self._recombine_pairs(start,stop,parent1,parent2)
                offsprings.append(new_offspring)
                #print("new_offspring from p1 and p2 = {}".format(new_offspring))
                
                new_offspring = self._recombine_pairs(start,stop,parent2,parent1)
                offsprings.append(new_offspring)
                #print("new_offspring from p2 and p1 = {}".format(new_offspring))
            
            #print(new_offspring)
            
            
            #Mutation of offspring
            for genotype in offsprings:
                genes_ab = sample(range(0,len(genotype)),2)                                     #generate two random gene ids to swap
                genotype[genes_ab[0]], genotype[genes_ab[1]] = genotype[genes_ab[1]], genotype[genes_ab[0]]     #swap the given genes            
            
            #Hybrid Algorithm if necessery
            if couple_with_hill_climbing:
                better = 0
                bet_dis = 0
                worse = 0
                wor_dis = 0
                for idg, genotype in enumerate(population):
                    current_distance = distances[idg]
                    improved_genotype = self.hill_climbing(number_of_cities, number_of_generations, 
                                                           genotype = genotype)
                    if improved_genotype[0] < current_distance:
                        #print(improved_genotype)
                        wor_dis = distances[idg]
                        bet_dis = improved_genotype[0]
                        distances[idg] = improved_genotype[0]
                        population[idg] = improved_genotype[1]
                        better += 1                        
                    else:
                        worse += 1
                #print("dist: {} to {} \t Better: {}, worse: {}".format(wor_dis, bet_dis, better, worse))            
            
            #evaluate new candidates
            for genotype in offsprings:
                distance = self._calculate_the_distance(genotype)
                offsprings_distances.append(distance)                
            
            #select individuals for the next generation
            for ido, offspring_distance in enumerate(offsprings_distances):
                for idp, parent_distance in enumerate(distances):
                    if parent_distance > offspring_distance:        #look for the first worse solution in population and override it
                        distances[idp] = offspring_distance
                        population[idp] = offsprings[ido][:]
                        break
                        
            number_of_generations -= 1
        
              
        
        
        #evaluate the best genotype
        shortest_distance = None
        shortest_path = None
        for idd, distance in enumerate(distances):
            if shortest_distance is None or idd == 0:
                shortest_distance = distance
                shortest_path = population[idd]
            
        print(list([shortest_distance,shortest_path]))

        return list([shortest_distance,shortest_path])
        
        

    def hybrid_algorithm(self, population_size = 10, number_of_cities= 24, number_of_generations = 100):
        return self.genetic_algorithm(population_size, number_of_cities, number_of_generations, couple_with_hill_climbing= True)
        




















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





