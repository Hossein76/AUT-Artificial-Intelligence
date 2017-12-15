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
        temp_list=[];
        for i in range(len(self.generation)-self.parents_number,len(self.generation)):
            temp_list.append(i);
        return temp_list;

    def create_offspring(self,parents_list):
        temp_list=[];
        while(len(temp_list)<self.offspring_number):
            temp_var1=random.randint(0, len(parents_list) - 1);
            temp_var2=random.randint(0, len(parents_list) - 1);
            if (temp_var2==temp_var1):
                continue;
            temp_node=self.problem.mix(parents_list[temp_var1],parents_list[temp_var2]);
            flag=False;
            for i in temp_list:
                if (self.problem.check_state(i,temp_node)==True):
                    flag=True;
                    break;
            if (flag==True):continue;
            temp_list.append(temp_node);
        return temp_list;

    def mutate_offspring(self,offspring_list):
        temp_list=list(offspring_list);
        for i in range(0,temp_list):
            temp_list[i]=self.problem.mutate(temp_list[i]);

        return temp_list;

    def evolve(self,mutated_list):
        temp_list=(list(mutated_list)).extend(self.generation);
        self.generation=[];
        utility_sum=0;
        for i in temp_list:
            utility_sum+=i.utility;
        while(len(self.generation)<self.population_size):
            temp_var=random.randint(0, len(temp_list)-1)
            if(temp_list[temp_var].utility<=(utility_sum*random.random())):
                self.generation.append(temp_list[temp_var]);
                temp_list.pop(temp_var);
        return temp_list;

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






class SimulatedAnnealingAlgorithm:

    def __init__(self,problem,Tmax = 25000.0 ,Tmin = 2.5  ,iteration_number = 50000 ):
        self.problem=problem;
        self.Tmax=Tmax;
        self.Tmin=Tmin;
        self.iteration_number=iteration_number;
        self.step=(Tmax-Tmin)/iteration_number;
        self.current_state=None;
        self.solutaion=[];

    def begin(self):
        self.current_state=self.problem.random_node();
        self.solutaion.append(self.current_state);
        for i in range(0,self.iteration_number):
            neighbers_list=self.problem.create_neighbers(self.current_state);
            random.shuffle(neighbers_list);



