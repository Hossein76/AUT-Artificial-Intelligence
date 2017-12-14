import random


class GeneticAlgorithm:
    def __init__(self,problem,population_size=35,parents_number=7,offspring_number=21,iteration_number=50,sampling_mode="default"
                 ):
        self.problem = problem;
        self.population_size=population_size;
        self.parents_number=parents_number;
        self.iteration_number=iteration_number;
        self.offspring_number=offspring_number;
        self.sampling_mode=sampling_mode;
        self.generation=[];
        self.generation_params=[];

    def begin(self):
        for i in range(0,self.population_size):
            self.generation.append(self.problem.random_node())
        self.evaluate_generation();
        for i in range(0,self.iteration_number):
            parents_list=self.chose_parents();
            offspring_list=self.create_offspring(parents_list);
            mutated_list=self.mutate_offspring(offspring_list);
            temp_list=[];
            for j in range(0,len(mutated_list)):
                for k in self.generation:
                    if (self.problem.check_state(k,mutated_list[j])):
                        temp_list.append(j);
            mutated_list.reverse();
            for j in temp_list:
                mutated_list.pop(j);
            self.generation=self.evolve(mutated_list);
            supreme=self.evaluate_generation();
            if (supreme!=None):
                return supreme;


    def chose_parents(self):
        random.shuffle(self.generation);
        temp_list=[];
        for i in range(0,self.parents_number):
            temp_list.append(i);
        return temp_list;

    def create_offspring(self,parents_list):
        return [];

    def mutate_offspring(self,offspring_list):
        return [];

    def evolve(self,mutated_list):
        return [];

    def evaluate_generation(self):
        self.generation.sort(key=lambda node: node.utility);
        temp_var=0;
        for i in self.generation:
            temp_var+=i.utility;
        temp_var= temp_var/self.population_size;
        self.generation_params.append([self.generation[0],self.generation[self.population_size-1],temp_var]);
        if (self.problem.Goal_test(self.generation[self.population_size-1])==True):
            return [len(self.generation),self.generation[self.population_size-1]];
        return None;



