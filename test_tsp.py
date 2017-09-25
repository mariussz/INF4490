#!/usr/bin/env python
try:
    import tsp, random, math
    from numpy import std, mean
    
except ImportError as err:
    print(err)


sol1 = tsp.Traveling_salesman("european_cities.csv")

#---------------------------EXHAUSTIVE SEARCH------------------------------------------------------------------------------
#for i in range(6,11):
    #result1 = sol1.exhaustive_search(number_of_cities= i, report_file="report_exhaustive_search.txt")
    #print("R1= {}".format(result1))


#---------------------------HILL CLIMBING------------------------------------------------------------------------------
#numbers_of_cities = list([10,24])
#report = ""
#for cities_number in numbers_of_cities:
    #results = []
    #running_times = []
    #best = None
    #worst = None
    #results_mean = None
    #runs_number = 20
    #generations = 50
    #for i in range(runs_number):
        #result2 = sol1.hill_climbing(number_of_cities = cities_number, number_of_generations = generations)
        #results.append(result2[0])
        #running_times.append(result2[3])
        #if i == 0 or result2[0] > worst:
            #worst = result2[0]
        #if i == 0 or result2[0] < best:
            #best = result2[0]
            
    #standard_deviation = std(results)
    #results_mean = mean(results)
    #report += "Number of cities = {}\nNumber of generations = {}\nNumer of runs = {}\nAverage running time = {}\nThe best tour = {}\nThe worst tour = {}\nMean = {}\nStandard deviation = {}\n\n".format(
        #cities_number,generations,runs_number,round(mean(running_times),3),round(best,2),round(worst,2),round(results_mean,2),round(standard_deviation,2))
#sol1._save_to_file("report_hill_climbing.txt",report)




#---------------------------GENETIC ALGORITHM------------------------------------------------------------------------------
population_sizes = list([6,10,20])
report = ""
for size in population_sizes:
    results = []
    running_times = []
    best = None
    worst = None
    runs_number = 20
    generations = 50
    cities_number = 24
    avg_bar = []   #average of bests across runs "...the average fitness of the best fit individual in each generation (average across runs)"
    
    for i in range(runs_number):
        result3 = sol1.genetic_algorithm(population_size = size, number_of_cities= cities_number, 
                                         number_of_generations =generations)
        #print("R3= {}".format(result3))
        results.append(result3[0])
        avg_bar.append(result3[2])
        running_times.append(result3[3])
        if i == 0 or result3[0] > worst:
            worst = result3[0]
        if i == 0 or result3[0] < best:
            best = result3[0]        
    standard_deviation = std(results)
    report += "Number of cities = {}\nNumber of generations = {}\nPopulation size = {}\nNumer of runs = {}\nAverage running time = {}\nThe best tour = {}\nThe worst tour = {}\nMean = {}\nAverage of best in each generation = {}\nStandard deviation = {}\n\n".format(
        cities_number,generations,size,runs_number,round(mean(running_times),3),round(best,2),round(worst,2),round(mean(results),2),round(mean(avg_bar),2), round(standard_deviation,2))
sol1._save_to_file("report_genetic_algorithm.txt",report)




#---------------------------HYBRID ALGORITHM------------------------------------------------------------------------------
#learning_models = list(["L","B"]) #L- Lamarckian, B- Baldwinian
#report = ""
#for model in learning_models:
    #results = []
    #running_times = []
    #best = None
    #worst = None
    #runs_number = 20
    #generations = 50
    #cities_number = 24
    #population = 6
    #avg_bar = []   #average of best across runs "...the average fitness of the best fit individual in each generation (average across runs)"

    #for i in range(runs_number):
        #result4 = sol1.hybrid_algorithm(population_size= population, number_of_cities= cities_number, 
                                        #number_of_generations= generations, generations_in_hill_climbing = 20, 
                                        #learning_model= model)
        #results.append(result4[0])
        #avg_bar.append(result4[2])
        #running_times.append(result4[3])
        #if i == 0 or result4[0] > worst:
            #worst = result4[0]
        #if i == 0 or result4[0] < best:
            #best = result4[0]
    #standard_deviation = std(results)
    #report += "Learning model = {}\nNumber of cities = {}\nNumber of generations = {}\nPopulation size = {}\nNumer of runs = {}\nAverage running time = {}\nThe best tour = {}\nThe worst tour = {}\nMean = {}\nAverage of best in each generation = {}\nStandard deviation = {}\n\n".format(
        #model,cities_number,generations,population,runs_number,round(mean(running_times),3),round(best,2),round(worst,2),round(mean(results),2),round(mean(avg_bar),2), round(standard_deviation,2))
#sol1._save_to_file("report_hybrid_algorithm.txt",report)