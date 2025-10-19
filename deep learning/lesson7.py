import sys,os
sys.path.append(os.pardir)
from lesson3 import *
from lesson6 import numerical_gradient
import numpy as np
class Twolayernet:
    def __init__(self,input_size,hidden_size,output_size):
        self.params = {}
        self.params ['W1'] = np.random.rand(input_size,hidden_size)
        self.params ['b1'] = np.zeros(hidden_size)
        self.params ['W2'] = np.random.rand(hidden_size,output_size)
        self.params ['b2'] = np.zeros(output_size)
        
    def predict(self,x):
        W1,W2 = self.params ['W1'],self.params ['W2']
        b1,b2 = self.params ['b1'],self.params ['b2']
        a1 = np.dot(x,W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1,W2) + b2
        y = softmax(a2)
        return y

    def loss(self,x,t):
        y = self.predict(x)
        return cross_entropy_error(y,t)
    
    def accuracy(self,x,t):
        y = self.predict(x)
        y = np.argmax(y,axis=1)
        t = np.argmax(t,axis=1)
        accuracy = np.sum( y == t / float(x.shape[0]))
        return accuracy

    def numrical_gradient(self,x,t):
        loss_W = lambda W:self.loss(x,t)
        grads = {}
        grads ['W1'] = numerical_gradient(loss_W ,self.params['W1'])
        grads ['b1'] = numerical_gradient(loss_W,self.params['b1'])
        grads ['W2'] = numerical_gradient(loss_W,self.params['W2'])
        grads ['b2'] = numerical_gradient(loss_W,self.params['b2'])
        return grads

class Mullayer:
    def __init__(self):
        self.x = None
        self.y = None
    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x*y
        return out
    def backward(self,dout):
        dx = dout*self.y
        dy = dout*self.x
        return dx,dy

class AddLayer:
    def __init__(self):
        pass
    def forward(self,x,y):
        out = x+y
        return out
    def backward(self,dout):
        dx = dout *1
        dy = dout *1
        return dx,dy



