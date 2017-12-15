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
        return None;S




class SimulatedAnnealingAlgorithm:
    def __init__(self,problem,Tmax=2500,Tmin=2.5,iteration_number=5000):
        self.problem=problem;
        self.Tmax=Tmax;
        self.Tmin=Tmin;
        self.iteration_number=iteration_number;
        self.step=(Tmax-Tmin)/iteration_number;
        self.current_state=None;
        self.solution=[];
        self.visited_nodes=0;


    def begin(self):
        self.current_state=self.problem.random_node();
        self.solution.append(self.current_state);
        for i in range(1,self.iteration_number):
            if(self.problem.Goal_test(self.current_state)==True):
                return self.solution;
            neighbers_list=random.shuffle(self.problem.create_neighbers(self.current_state));
            self.visited_nodes+=len(neighbers_list);
            if (neighbers_list[0].utility>=self.current_state.utility):
                self.current_state=neighbers_list[0];
                self.solution.append(self.current_state);
            elif(random.randint(0,self.Tmax)<=(self.Tmax-(i*self.step))):
                self.current_state = neighbers_list[0];
                self.solution.append(self.current_state);


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
            if(self.mode=="simple"):
                neighbers_list = self.problem.create_neighbers(self.current_state);
                self.visited_nodes+=len(neighbers_list);
                neighbers_list.sort(key=lambda node: node.utility);
                if (neighbers_list[-1].utility < self.current_state.utility): break;
                self.current_state=neighbers_list[-1];
                temp_solution_list.append(self.current_state);
                if (self.problem.Goal_test(self.current_state)==True):
                    break;
            elif(self.mode=="stochastic"):
                neighbers_list = self.problem.create_neighbers(self.current_state);
                self.visited_nodes+=len(neighbers_list);
                neighbers_list.sort(key=lambda node: node.utility);
                if (neighbers_list[-1].utility < self.current_state.utility): break;
                rand_var=random.randomint(0,len(neighbers_list)-1)
                while(neighbers_list[rand_var].utility<self.current_state.utility):
                    rand_var = random.randomint(0, len(neighbers_list) - 1);
                self.current_state = neighbers_list[rand_var];
                temp_solution_list.append(self.current_state);
                if (self.problem.Goal_test(self.current_state) == True):
                    break;
            elif (self.mode=="first-choice"):
                random_neighber = self.problem.create_random_neighber(self.current_state);
                self.visited_nodes+=1;
                while(random_neighber.utility<self.current_state):
                    random_neighber = self.problem.create_random_neighber(self.current_state);
                    self.visited_nodes += 1;
                self.current_state =random_neighber;
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
            elif(self.solution[-1].utility<temp_solution_list[-1].utility):
                self.solution = list(temp_solution_list);
                if (self.problem.Gaol_test(self.solution[-1]) == True):
                    return self.solution;
                else:
                    self.begin();
            else:
                self.begin();
