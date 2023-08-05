class ABC_CSA:
    '''
    Antibodies is the population of antibodies. Each row of Antibodies matrix is a vector holding D parameters to be optimized. The number of rows of Antibodies matrix equals to the P
    clones: New solution (neighbour) produced by v_{ij}=x_{ij}+\phi_{ij}*(x_{kj}-x_{ij}) j is a randomly chosen parameter and k is a randomly chosen solution different from i
    solution: New solution (neighbour) produced by v_{ij}=x_{ij}+\phi_{ij}*(x_{kj}-x_{ij}) j is a randomly chosen parameter and k is a randomlu chosen solution different from i
    f; %f is a vector holding objective function values associated with food sources
    fitness; %fitness is a vector holding fitness (quality) values associated with food sources
    trial; %trial is a vector holding trial numbers through which solutions can not be improved
    cloneF;
    cloneFitness;
    GlobalMin; %Optimum solution obtained by ABC algorithm
    GlobalParams; %Parameters of the optimum solution
    GlobalMinIndex; %%
    prob; %prob is a vector holding probabilities of food sources (solutions) to be chosen
    tmpID;
    '''

    def __init__(self, inputX, target, P, B, lb, ub, alpha, MR, L2, parallelType):
        self.parT = parallelType
        self.X = inputX
        self.FVS = inputX.shape[1]
        # self.XwithBias = self.parT.append(self.parT.ones((self.X.shape[0], 1)), self.X, axis=1)
        self.y = target.reshape(-1, 1)
        self.P = P  # P is population size
        self.alpha = alpha  # the number of clones for each antibody
        self.B = B  # eliminate worst %B number of antibodies in the population
        # The number of parameters to be optimized (FVS: Feature Vector Size)
        self.D = self.FVS + 1
        self.lb = lb  # lower bound for parameters
        self.ub = ub  # upper bound for parameters
        self.MR = MR  # modification rate
        self.L2 = L2
        self.evaluationNumber = 0
        self.tmpID = [-1] * self.P
        self.inds = self.parT.arange(self.P) * self.alpha

        self.Antibodies = self.lb + \
            self.parT.random.rand(self.P, self.D) * (self.ub - self.lb)
        self.solution = self.parT.copy(self.Antibodies)
        self.f = self.calculateF(self.Antibodies)
        self.fitness = 1 / (1 + self.f)

    def findBestAntibody(self):
        index = self.parT.argmin(self.f)
        self.globalMin = self.f[index, 0]
        self.globalParams = self.parT.copy(self.Antibodies[index: index + 1])

    def cloning(self):
        self.clones = self.parT.repeat(self.Antibodies, self.alpha, axis=0)
        # self.cloneF = self.parT.repeat(self.f, self.alpha, axis = 0)
        # self.cloneFitness = 1 / (1 + self.cloneF)

    def sendEmployedBees(self):
        for i in range(self.P * self.alpha):  # for each clone
            ar = self.parT.random.rand(self.D)
            param2change = self.parT.where(ar < self.MR)[0]
            # param2change = ar < self.MR

            # neighbour = self.parT.random.randint(self.P * self.alpha)
            # while neighbour == i:
            #   neighbour = self.parT.random.randint(self.P * self.alpha)

            start_indis = (i // self.alpha) * self.alpha
            valid_choices = self.parT.append(self.parT.arange(
                0, start_indis), self.parT.arange(start_indis + self.alpha, self.P * self.alpha))
            neighbour = self.parT.random.choice(valid_choices, 1)
            # random number generation between -1 and 1 values
            r = -1 + (1 + 1) * self.parT.random.rand()
            arr = self.clones[i, param2change]
            arr = arr + r * (arr - self.clones[neighbour, param2change])
            arr[arr < self.lb] = self.lb
            arr[arr > self.ub] = self.ub
            self.clones[i, param2change] = arr
            # self.clones[i, param2change] = self.clones[i, param2change] + r * (self.clones[i, param2change] - self.clones[neighbour, param2change])
            # self.clones[i, param2change] = self.parT.where(self.clones[i, param2change] < self.lb, self.lb, self.clones[i, param2change])
            # self.clones[i, param2change] = self.parT.where(self.clones[i, param2change] > self.ub, self.ub, self.clones[i, param2change])
        self.cloneF = self.calculateF(self.clones)
        self.cloneFitness = 1 / (1 + self.cloneF)

    # def selection(self):
    #   clone_reshape = self.cloneFitness.reshape(self.P, self.alpha)
    #   max_idxs = self.parT.argmax(clone_reshape, axis=1)
    #   idxs = self.parT.arange(self.P) * self.alpha + max_idxs
    #   bestIdxs = (self.cloneFitness[idxs] > self.fitness).flatten()
    #   self.Antibodies[bestIdxs, :] = self.clones[idxs,:][bestIdxs, :]
    #   self.f[bestIdxs] = self.cloneF[idxs][bestIdxs]
    #   self.fitness[bestIdxs] = self.cloneFitness[idxs][bestIdxs]

    def selection(self):
        clone_reshape = self.cloneFitness.reshape(self.P, self.alpha)
        max_idxs = self.parT.argmax(clone_reshape, axis=1)
        idxs = self.inds + max_idxs
        bestIdxs = (self.cloneFitness[idxs] > self.fitness).flatten()
        self.Antibodies[bestIdxs, :] = self.clones[idxs, :][bestIdxs, :]
        self.f[bestIdxs] = self.cloneF[idxs][bestIdxs]
        self.fitness[bestIdxs] = self.cloneFitness[idxs][bestIdxs]

    def sendOnLookerBees(self):
        i = 0
        t = 0
        while t < self.P:
            if self.parT.random.rand() < self.prob[i, 0]:
                ar = self.parT.random.rand(self.D)
                param2change = self.parT.where(ar < self.MR)[0]

                neighbour = self.parT.random.randint(self.P)
                while neighbour == i:
                    neighbour = self.parT.random.randint(self.P)

                self.solution[t, :] = self.Antibodies[i, :]
                # v_{ij} = x_{ij} + phi_{ij}*(x_{kj}-x_{ij})
                # random number generation between -1 and 1 values
                r = -1 + (1 + 1) * self.parT.random.rand()
                # self.solution[t, param2change] = self.Antibodies[i, param2change] + r * (self.Antibodies[i, param2change] - self.Antibodies[neighbour, param2change])
                arr = self.Antibodies[i, param2change] + r * (
                    self.Antibodies[i, param2change] - self.Antibodies[neighbour, param2change])
                self.tmpID[t] = i
                # arr = self.solution[t, param2change]
                arr[arr < self.lb] = self.lb
                arr[arr > self.ub] = self.ub
                self.solution[t, param2change] = arr
                # self.solution[t, param2change] = self.parT.where(self.solution[t, param2change] < self.lb, self.lb, self.solution[t, param2change])
                # self.solution[t, param2change] = self.parT.where(self.solution[t, param2change] > self.ub, self.ub, self.solution[t, param2change])
                t += 1
            i += 1
            if i >= self.P:
                i = 0

    def calculateProbabilities(self):
        maxfit = self.parT.max(self.fitness)
        self.prob = 0.9 * (self.fitness / maxfit) + 0.1

    def receptorEditing(self):
        fIndex = self.parT.argsort(self.fitness, axis=0)
        N = round(self.P * self.B)
        worstNindex = fIndex[:N, 0]
        new_N_Antibodies = self.lb + \
            self.parT.random.rand(N, self.D) * (self.ub - self.lb)
        new_N_f = self.calculateF(new_N_Antibodies)
        new_N_fitness = 1 / (1 + new_N_f)
        # self.Antibodies[worstNindex, :] = self.parT.copy(new_N_Antibodies)
        self.Antibodies[worstNindex, :] = new_N_Antibodies
        self.f[worstNindex] = new_N_f
        self.fitness[worstNindex] = new_N_fitness

    def calculateF(self, foods):
        W = foods[:, 1:]
        b = foods[:, 0]
        A = self.sig(self.X.dot(W.T) + b)
        # Mean Absolute Error - MAE
        f = self.parT.mean(self.parT.absolute(
            A-self.y), axis=0, keepdims=True).T
        self.evaluationNumber += len(f)
        return f

    def sig(self, n):  # Sigmoid function
        return 1 / (1 + self.parT.exp(-n))


class LearnABC_CSA:
    def __init__(self, inputX, target, P, B, lb, ub, alpha, MR, L2, parallelType, evaluationNumber):
        self.parT = parallelType
        self.abc_csa = ABC_CSA(inputX, target, P, B, lb,
                               ub, alpha, MR, L2, parallelType)
        self.total_numberof_evaluation = evaluationNumber

    def learn(self):
        self.f_values = []
        self.f_values.append(self.parT.min(self.abc_csa.f))

        sayac = 0
        while self.abc_csa.evaluationNumber <= self.total_numberof_evaluation:
            self.abc_csa.cloning()
            self.abc_csa.sendEmployedBees()
            self.abc_csa.selection()
            self.abc_csa.calculateProbabilities()
            self.abc_csa.sendOnLookerBees()

            objValSol = self.abc_csa.calculateF(self.abc_csa.solution)
            fitnessSol = 1 / (1 + objValSol)

            for i in range(self.abc_csa.P):
                t = self.abc_csa.tmpID[i]
                if fitnessSol[i] > self.abc_csa.fitness[t]:
                    self.abc_csa.Antibodies[t, :] = self.abc_csa.solution[i, :]
                    self.abc_csa.f[t] = objValSol[i]
                    self.abc_csa.fitness[t] = fitnessSol[i]

            sayac += 1
            if sayac % 50 == 0:
                self.abc_csa.receptorEditing()

            self.f_values.append(self.parT.min(self.abc_csa.f))

        self.abc_csa.findBestAntibody()
        self.net = self.abc_csa.globalParams
        self.globalMin = self.abc_csa.globalMin
        # print(f"Evaluation Number: {self.abc_csa.evaluationNumber}"); #


class ABC_CSA_LR_Model():
    def __init__(self, lb=-32, ub=32, evaluationNumber=60000, P=40, B=0.1, alpha=2, MR=0.1, L2=0, parallelType=None):
        '''
        lb is lower bound for parameters to be learned
        ub is upper bound for parameters to be learned
        '''
        self.lb = lb
        self.ub = ub
        self.evaluationNumber = evaluationNumber
        self.P = P
        self.B = B
        self.alpha = alpha
        self.MR = MR
        self.L2 = L2
        self.parallelType = parallelType

    def fit(self, trainX, trainY):
        learn = LearnABC_CSA(trainX, trainY, self.P, self.B, self.lb, self.ub,
                             self.alpha, self.MR, self.L2, self.parallelType, self.evaluationNumber)
        learn.learn()
        self.net = learn.net

    def sig(self, x):
        return 1 / (1 + self.parallelType.exp(-x))

    def __str__(self):
        return f"lb={self.lb}, ub={self.ub}, evaNumber={self.evaluationNumber}, P={self.P}, alpha={self.alpha}, B={self.B}, MR={self.MR}, L2={self.L2}"

    def f1_score(self, actual, predicted):
        tp = self.parallelType.sum(predicted * actual, axis=0)
        fp = self.parallelType.sum(predicted, axis=0) - tp
        fn = self.parallelType.sum(actual) - tp
        f1 = self.parallelType.zeros(tp.shape)
        ind = tp != 0
        precision = tp[ind] / (tp[ind] + fp[ind])
        recall = tp[ind] / (tp[ind] + fn[ind])
        f1[ind] = 2*precision*recall / (precision+recall)
        return f1

    def score(self, X, y):
        W = self.net[:, 1:]
        b = self.net[:, 0]
        A = self.sig(X.dot(W.T) + b)
        p = self.parallelType.rint(A)
        # prediction = self.logsig(self.parallelType.dot(self.parallelType.append(self.parallelType.ones((X.shape[0], 1)), X, axis=1), self.net.T))
        # prediction = self.parallelType.where(prediction >= 0.5, 1, 0)
        y = y.reshape(-1, 1)
        f1 = self.f1_score(y, p)
        acc = self.parallelType.average(y == p)
        return [acc, f1, p]
