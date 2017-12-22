import random
import math
from Equation import *




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
            temp_var1=random.randint(0,len(parents_list)-1);
            temp_var2=random.randint(0,len(parents_list)-1);
            if (temp_var1==temp_var2):
                continue;
            flag=False;
            temp_node=self.problem.mix(parents_list[temp_var2],parents_list[temp_var1]);
            for i in temp_list:
                if (self.problem.check_state(i,temp_node)==True):
                    flag=True;
                    break;
            if (flag==True):
                continue;
            temp_list.append(temp_node);

        return temp_list;

    def mutate_offspring(self,offspring_list):
        temp_list=list(offspring_list);
        for i in range(0,len(temp_list)-1):
            temp_list[i]=self.problem.mutate(temp_list[i]);
        return temp_list;

    def evolve(self,mutated_list):
        temp_list=(list(mutated_list)).extend(self.generation);
        self.generation=[];
        util_sum=0;
        for i in temp_list:
            util_sum+=i.utility;
        while(len(self.generation)<self.population_size):
            temp_var=random.randint(0,len(temp_list)-1);
            util_var = random.randint(0, util_sum);
            if(temp_list[temp_var].utility>=util_var):
                self.generation.append(temp_list.pop(temp_var));
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
    def __init__(self,problem,Tmax=2500,Tmin=2.5,iteration_number=150,annealing_mode="simple"):
        self.problem=problem;
        self.Tmax=Tmax;
        self.Tmin=Tmin;
        self.iteration_number=iteration_number;
        self.tempreture=Tmax-Tmin;
        self.step=(Tmax-Tmin)/iteration_number;
        self.current_state=None;
        self.solution=[];
        self.visited_nodes=0;
        self.annealing_mode=annealing_mode;

    def anneal(self,i):
        if(self.annealing_mode=="simple"):
            self.tempreture-=self.step;
        elif(self.annealing_mode=="log"):
            self.tempreture=(self.Tmax-self.Tmin)/(math.log(i)+1);
        elif(self.annealing_mode=="exp"):
            self.tempreture = (self.Tmax - self.Tmin) /(math.exp(i));

    def begin(self):
        self.current_state=self.problem.random_node();
        self.solution.append(self.current_state);
        for i in range(1,self.iteration_number):
            if(self.problem.Goal_test(self.current_state)==True):
                return self.solution;
            neighbors_list=list(self.problem.create_neighbors(self.current_state));
            random.shuffle(neighbors_list);
            self.anneal(i);
            random.shuffle(neighbors_list);
            self.visited_nodes+=len(neighbors_list);
            if (neighbors_list[0].utility>=self.current_state.utility):
                self.current_state=neighbors_list[0];
                self.solution.append(self.current_state);
            elif(random.randint(0,self.Tmax)<=(self.tempreture+self.Tmin)):
                self.current_state = neighbors_list[0];
                self.solution.append(self.current_state);
        return self.solution;


class HillClimbingAlgorithm:
    def __init__(self,problem,mode="simple",random_restart=False):
        self.problem=problem;
        self.current_state=None;
        self.solution=[];
        self.mode=mode;
        self.visited_nodes=0;
        self.random_restart=random_restart;

    def begin(self):
        self.current_state=self.problem.random_node();
        temp_solution_list=[self.current_state];
        while(True):
            print (self.current_state.utility,"one step \n")
            if(self.mode == "simple"):
                neighbors_list = list(self.problem.create_neighbors(self.current_state));
                random.shuffle(neighbors_list);
                self.visited_nodes+=len(neighbors_list);
                neighbors_list.sort(key=lambda node: node.utility);
                if (neighbors_list[0].utility >self.current_state.utility): break;
                self.current_state=neighbors_list[0];
                temp_solution_list.append(self.current_state);
                if (self.problem.Goal_test(self.current_state)==True):
                    break;
            elif(self.mode == "stochastic"):
                neighbors_list = list(self.problem.create_neighbors(self.current_state));
                random.shuffle(neighbors_list);
                self.visited_nodes+=len(neighbors_list);
                neighbors_list.sort(key=lambda node: node.utility);
                if (neighbors_list[0].utility >self.current_state.utility): break;
                rand_var=random.randint(0,len(neighbors_list)-1)
                while(neighbors_list[rand_var].utility>self.current_state.utility):
                    rand_var = random.randint(0, len(neighbors_list) - 1);
                self.current_state = neighbors_list[rand_var];
                temp_solution_list.append(self.current_state);
                if (self.problem.Goal_test(self.current_state) == True):
                    break;
            elif (self.mode == "first-choice"):
                random_neighbor = self.problem.create_random_neighbor(self.current_state);
                self.visited_nodes+=1;
                while(random_neighbor.utility>self.current_state.utility):
                    random_neighbor = self.problem.create_random_neighbor(self.current_state);
                    self.visited_nodes += 1;
                self.current_state =random_neighbor;
                temp_solution_list.append(self.current_state);
                if (self.problem.Goal_test(self.current_state) == True):
                    break;

        if(self.random_restart==False):
            self.solution=list(temp_solution_list);
            return self.solution;
        elif(self.random_restart==True):
            if(len(self.solution)==0):
                self.solution=list(temp_solution_list);
                if(self.problem.Gaol_test(self.solution[-1])==True):
                    return self.solution;
                else:
                    self.begin();
            elif(self.solution[-1].utility>temp_solution_list[-1].utility):
                self.solution = list(temp_solution_list);
                if (self.problem.Gaol_test(self.solution[-1]) == True):
                    return self.solution;
                else:
                    self.begin();
            else:
                self.begin();


class GeneticAlgorithmPaper:
    def __init__(self,problem,population_size=35,iteration_number=50,pc=0.25,pm=0.2
                 ):
        self.problem = problem;
        self.population_size=population_size;
        self.iteration_number=iteration_number;
        self.pc=pc;
        self.pm=pm;
        self.generation=[];
        self.generation_params=[];

    def begin(self):
        for i in range(0,self.population_size):
            self.generation.append(self.problem.random_node())
        self.evaluate_generation();
        for i in range(0,self.iteration_number):
            self.generation=self.create_new_generation();
            parents_list=self.chose_parents();
            self.create_offspring(parents_list);
            self.mutate_offspring();
            supreme=self.evaluate_generation();
            if (supreme!=None):
                pass;
                #return supreme;
        return supreme;

    def create_new_generation(self):
        fitness=[];
        total_fitness=0;
        probability=[];
        new_generation=[];
        r=[];
        for i in self.generation:
            temp_var=1/(1+i.utility);
            total_fitness+=temp_var;
            fitness.append(temp_var);
            r.append(random.random());

        for i in fitness:
            probability.append(i/total_fitness);

        for i in range(1,len(probability)):
            probability[i]+=probability[i-1];

        for i in range(0,len(r)):
            for j in range(0,len(probability)):
                if (r[i]<probability[j]):
                    new_generation.append(self.generation[j]);
                    break;
        return list(new_generation);

    def chose_parents(self):
        parent_list=[];
        for i in range(0,len(self.generation)):
            temp_var=random.random();
            if(temp_var<self.pc):
                parent_list.append(i);
        return parent_list;

    def create_offspring(self,parents_list):
        c_list=[]
        for i in range(0,len(parents_list)):
            c_list.append(random.randint(0,len(self.generation[0].state_list)));

        temp_list=[];
        for i in range(0,len(parents_list)):
            if(i==len(parents_list)-1):
                temp_list.append(self.problem.mix(self.generation[parents_list[i]],self.generation[parents_list[0]],c_list[i]));
            else:
                temp_list.append(self.problem.mix(self.generation[parents_list[i]],self.generation[parents_list[i+1]],c_list[i]));

        for i in range(0,len(parents_list)):
            self.generation[parents_list[i]]=temp_list[i];
        return list(temp_list);

    def mutate_offspring(self):
        temp_var=int(self.pm*len(self.generation[0].state_list)*len(self.generation));
        for i in range (0,temp_var):
            rand_var=random.randint(0,len(self.generation)-1);
            self.generation[rand_var]=self.problem.mutate(self.generation[rand_var]);

    def evaluate_generation(self):
        self.generation.sort(key=lambda node: node.utility);
        temp_var=0;
        for i in self.generation:
            temp_var+=i.utility;
        temp_var= temp_var/self.population_size;
        self.generation_params.append([self.generation[0].utility,self.generation[self.population_size-1].utility,temp_var]);
        if (self.problem.Goal_test(self.generation[0])==True):
            return [len(self.generation),self.generation[self.population_size-1]];
        return None;

matrix=[[0,1,1,0,1,0,0,0,0,0,0,0],[1,0,1,0,0,0,0,0,0,0,0,0],[1,1,0,1,0,0,0,0,1,0,0,0],[0,0,1,0,1,0,1,0,0,0,0,0],[1,0,0,1,0,1,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,0,0,0,0]
    , [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],[0,0,0,0,0,0,1,0,1,1,1,0],[0,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,1,0],[0,0,0,0,0,0,0,1,0,1,0,1],[0,0,0,0,0,0,1,0,0,0,1,0]];


temp_list1=[];
for k in range(1,99,2):
    temp_list2 = [0, 0, 0];
    for j in range(0,50):
        print(k,"---",j)
        a=GeneticAlgorithmPaper(problem=Problem(),population_size=k,iteration_number=200,pc=0.25,pm=0.2);
        b=a.begin();
        for i in a.generation_params:
            temp_list2[0]+=i[0]/len(a.generation_params);
            temp_list2[1]+=i[1]/len(a.generation_params);
            temp_list2[2]+=i[2]/len(a.generation_params);
    temp_list2[0]/=50;
    temp_list2[1]/=50;
    temp_list2[2]/=50;
    temp_list1.append(list(temp_list2));

print ("[",end="");

for i in temp_list1:
    print(i[0],",",i[1],",",i[2],"; ...");




