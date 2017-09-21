#!/usr/bin/env python
try:
    import tsp
except ImportError as err:
    print(err)


sol1 = tsp.Traveling_salesman()
#path = sol1._calculate_the_path((2,7,4,5,6))

result1 = sol1.exhaustive_search(8)
print("Exhaustive search result: {}\n\n".format(result1))

#def hill_climbing(self, number_of_cities= 10, iterations= 1000, show_details=1):
result2 = sol1.hill_climbing(24,100000,0)
print("Hill climbing search result: {}\n\n".format(result2))

result3 = sol1.genetic_algorithm()




#...
#New shortest distance found = 6185.94 
#for path = [4, 1, 2, 6, 5, 3, 7, 0]

#New shortest distance found = 5023.2 
#for path = [4, 1, 5, 6, 2, 3, 7, 0]

#New shortest distance found = 4816.0 
#for path = [0, 7, 3, 6, 2, 5, 1, 4]

#Hill climbing search result: [4816.0, [0, 4, 7, 5, 1, 6, 2, 3]]