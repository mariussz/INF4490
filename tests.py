import itertools as itt
import random as r
from math import factorial



#print(r.randint(0,1))

genotype = list([3,4,5,2,3,1,7])


print(genotype)
print(genotype.index(5))
print(genotype)





#if counter > number_of_generations:
    #gene_a = sample(range(0,number_of_cities),1)[0]
    
    #sorted_distances_list = []
    #for idd, distance in enumerate(list(self.traces[gene_a])):
        #sorted_distances_list.append(list([distance,idd]))
    #sorted_distances_list.sort()
    
    #id_close_city = sample(range(0,3),1)[0]      
    #gene_b = sorted_distances_list[id_close_city][1]    #will get oryginal id of one of the 3 closest cities for gene_a

    #if gene_a > 0:
        #gene_c = genotype[gene_a-1]
    #else:
        #gene_c = genotype[gene_a+1]
    ##id_far_city = sample(range(len(sorted_distances_list)-3,len(sorted_distances_list)),1)[0]
    ##gene_c = sorted_distances_list[id_far_city][1]      #will get oryginal id of one of the 3 farest cities for gene_a
    
    #genes_ab = list([gene_b,gene_c])
    #genotype[genes_ab[0]], genotype[genes_ab[1]] = genotype[genes_ab[1]], genotype[genes_ab[0]]     #swap genes                          






