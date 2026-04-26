import numpy as np 
import scipy
import matplotlib.pyplot as plt



class Neural_Net():
    def __init__(self):
        self.weights = []
        self.actual = []
        self.predicted = []

    def init_weights(self,hidden_unit_num):
        for i in range(hidden_unit_num):
            random_weight = np.random.randint(1,100)
            self.weights.append(random_weight)

    def init_actual(self,function,low,high):
        for i in range(low,high):
            data = function(i)
            self.actual.append(data)


    def ReLU(self,x):
        if x >= 0:
            return x
        else:
            return 0

    def least_squares(self,actual,predicted):
        loss = 0
        for i in range(len(predicted)):
            difference = actual-predicted
            squared_difference = difference**2
            loss += squared_difference

    def adaptive_step_size(self):
        pass
    
    def update_weights(self,old_weight,step_size,gradient):
        pass


neural = Neural_Net()
neural.init_actual(np.sin,0,20)
neural.init_weights()
print(neural.weights,neural.actual)

