#gradient_simplenet
import numpy as np
from lesson3 import softmax,sigmoid,cross_entropy_error
from lesson6 import numerical_gradient
class Simplenet:
    def __init__(self):
        self.W = np.random.randn(3,3)
    def predict(self,x):
        return np.dot(x,self.W)
    def loss(self,x,t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y,t)
        return loss


net = Simplenet()
print("网络权重为：",net.W)
x = np.array([0.6,0.9,0.5])
p = net.predict(x)
print("网络推理结果为：",p)
t = np.array([0,0,1])
loss = net.loss(x,t)
print("损失函数为：",loss)


def f(W):
    return net.loss(x,t)
dw = numerical_gradient(f,net.W)
print("梯度为：",dw)
