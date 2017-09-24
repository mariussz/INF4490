#!/usr/bin/env python
try:
    import tsp, random, math
    from numpy import std, mean
    
except ImportError as err:
    print(err)


sol1 = tsp.Traveling_salesman("european_cities.csv")

#for i in range(6,11):
    #result1 = sol1.exhaustive_search(number_of_cities= i, report_file="report_exhaustive_search.txt")
    #print("R1= {}".format(result1))



numbers_of_cities = list([10,24])
report = ""
for cities_number in numbers_of_cities:
    results = []
    best = None
    worst = None
    results_mean = None
    runs_number = 20
    generations = 50
    for i in range(runs_number):
        result2 = sol1.hill_climbing(number_of_cities = cities_number, number_of_generations = generations) #, report_file="report_hill_climbing.txt")
        #print(result2)
        results.append(result2[0])
        if i == 0 or result2[0] > worst:
            worst = result2[0]
        if i == 0 or result2[0] < best:
            best = result2[0]
            
    standard_deviation = std(results)
    results_mean = mean(results)
    report += "Number of cities = {}\nNumber of generations = {}\nNumer of runs = {}\nThe best tour = {}\nThe worst tour = {}\nMean = {}\nStandard deviation = {}\n\n".format(
        cities_number,generations,runs_number,round(best,2),round(worst,2),round(results_mean,2),round(standard_deviation,2))
sol1._save_to_file("report_hill_climbing.txt",report)






population_sizes = list([6,10,20])
report = ""
for size in population_sizes:
    results = []
    best = None
    worst = None
    results_mean = None
    runs_number = 20
    generations = 50
    cities_number = 24
    
    for i in range(runs_number):
        result3 = sol1.genetic_algorithm(population_size = size, number_of_cities= cities_number, 
                                         number_of_generations =generations, report_file="report_genetic_algorithm.txt")
        #print("R3= {}".format(result3))
        results.append(result3[0])
        if i == 0 or result3[0] > worst:
            worst = result3[0]
        if i == 0 or result3[0] < best:
            best = result3[0]        
    standard_deviation = std(results)
    results_mean = mean(results)
    report += "Number of cities = {}\nNumber of generations = {}\nPopulation size = {}\nNumer of runs = {}\nThe best tour = {}\nThe worst tour = {}\nMean = {}\nStandard deviation = {}\n\n".format(
        cities_number,generations,size,runs_number,round(best,2),round(worst,2),round(results_mean,2),round(standard_deviation,2))
sol1._save_to_file("report_genetic_algorithm.txt",report)    






#result1 = sol1.exhaustive_search(number_of_cities=9)
#print("R1= {}".format(result1))

#result2 = sol1.hill_climbing(number_of_cities = 10, number_of_generations = 50)
#print("R2= {}".format(result2))


#result3 = sol1.genetic_algorithm(population_size =4, number_of_cities= 24, number_of_generations =75)
#print("R3= {}".format(result3))

#hybrid_algorithm
#result4 = sol1.hybrid_algorithm(population_size = 4, number_of_cities= 24, number_of_generations =200)
#print("R4= {}".format(result4))



#Lowest distance for 24 cities is 12287.070000
#11219.87 and 11712.03