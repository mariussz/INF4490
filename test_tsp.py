#!/usr/bin/env python
try:
    import tsp, random
except ImportError as err:
    print(err)


sol1 = tsp.Traveling_salesman("european_cities.csv")

#result1 = sol1.exhaustive_search(8)
#print("R1= {}".format(result1))


#result2 = sol1.hill_climbing(number_of_cities = 24, number_of_generations = 1000)
#print("R2= {}".format(result2))


#result3 = sol1.genetic_algorithm(population_size = 8, number_of_cities= 24, number_of_generations =100)
#print("R3= {}".format(result3))

#hybrid_algorithm
result4 = sol1.hybrid_algorithm(population_size = 8, number_of_cities= 24, number_of_generations =100)
print("R4= {}".format(result4))

#R2= [23682.269999999997, [14, 19, 18, 13, 7, 6, 8, 20, 3, 11, 16, 12, 0, 9, 21, 22, 5, 1, 17, 15, 4, 23, 2, 10]]
#[14533.96, [18, 0, 12, 7, 11, 6, 21, 19, 14, 23, 17, 2, 8, 3, 16, 15, 13, 22, 5, 10, 4, 9, 20, 1]]
#R3= [14533.96, [18, 0, 12, 7, 11, 6, 21, 19, 14, 23, 17, 2, 8, 3, 16, 15, 13, 22, 5, 10, 4, 9, 20, 1]]
#[14992.37, [21, 15, 18, 13, 0, 12, 16, 11, 7, 3, 22, 1, 5, 17, 2, 8, 6, 23, 4, 9, 20, 10, 14, 19]]
#Better: 0, worse: 8
#R4= [14992.37, [21, 15, 18, 13, 0, 12, 16, 11, 7, 3, 22, 1, 5, 17, 2, 8, 6, 23, 4, 9, 20, 10, 14, 19]]



#Lowest distance for 24 cities is 12287.070000
#11219.87 and 11712.03

#my [11159.980000000001, [9, 4, 20, 1, 5, 22, 15, 17, 2, 23, 10, 14, 19, 21, 6, 8, 3, 11, 7, 16, 13, 18, 0, 12]]


#['Stockholm', 'Saint Petersburg', 'Moscow', 'Kiev', 'Bucharest', 'Istanbul', 'Sofia', 'Belgrade', 'Budapest', 'Vienna', 'Munich', 'Milan', 'Rome', 'Barcelona', 'Madrid', 'Paris', 'Dublin', 'London', 'Brussels', 'Hamburg', 'Copenhagen', 'Berlin', 'Prague', 'Warsaw']


#ids = sol1._citi_names_to_id(list(['Stockholm', 'Saint Petersburg', 'Moscow', 'Kiev', 'Bucharest', 'Istanbul', 'Sofia', 'Belgrade', 'Budapest', 'Vienna', 'Munich', 'Milan', 'Rome', 'Barcelona', 'Madrid', 'Paris', 'Dublin', 'London', 'Brussels', 'Hamburg', 'Copenhagen', 'Berlin', 'Prague', 'Warsaw']))
#dist = sol1._calculate_the_distance(ids)
#print(ids)
#print(dist)




#...
#New shortest distance found = 6185.94 
#for path = [4, 1, 2, 6, 5, 3, 7, 0]

#New shortest distance found = 5023.2 
#for path = [4, 1, 5, 6, 2, 3, 7, 0]

#New shortest distance found = 4816.0 
#for path = [0, 7, 3, 6, 2, 5, 1, 4]

#Hill climbing search result: [4816.0, [0, 4, 7, 5, 1, 6, 2, 3]]