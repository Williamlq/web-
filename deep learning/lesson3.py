#function

import matplotlib.pyplot as plt
import numpy as np



def relu(x):
    return np.maximum(0,x)


def sigmoid(x):
    return 1/(1+np.exp(-x))


def step_function(x):
    return (x>0).astype(int)

def identity_function(x):
    return x

#交叉熵函数
def cross_entropy_error(y, t):
    # 处理维度，确保是二维（批量数据）
    if y.ndim == 1:
        y = y.reshape(1, y.size)
    if t.ndim == 1:
        t = t.reshape(1, t.size)

    delta = 1e-7  # 防止log(0)
    batch_size = y.shape[0]  # 批量大小

    # 处理标签格式：单值标签 → one-hot 编码
    if t.size == y.size:  # t是one-hot编码（每个样本的长度等于类别数）
        pass  # 已经是one-hot，直接用
    else:  # t是单值标签（如 [2, 0, 1]），转换为one-hot
        t_one_hot = np.zeros_like(y)
        t = t.astype(int)  # 确保标签是整数
        t_one_hot[np.arange(batch_size), t] = 1
        t = t_one_hot

    # 计算每个样本的交叉熵，再求平均
    return -np.sum(t * np.log(y + delta)) / batch_size

#均方误差损失函数
def mean_squared_error(y,t):
    return 0.5 * np.sum((y-t)**2)

def softmax(x):
    x = x - np.max(x, axis=1, keepdims=True)  # 数值稳定
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)

class Relu():
    def __init__(self):
        self.mask = None
    def forward(self,x):
        self.mask = (x<=0)
        out = x.copy()
        out[self.mask] = 0
        return out
    def backward(self,dout):
        dout[self.mask] = 0
        dx = 1*dout
        return dx

class Sigmoid():
    def __init__(self):
        self.out = None
    def forward(self,x):
        out = 1 / (1+np.exp(-x))
        self.out = out
        return out
    def backward(self,dout):
        dx = dout*self.out*(1-self.out)
        return dx

class Affine():
    def __init__(self,W,b):
        self.W = W
        self.b = b
        self.x = None
        self.dw = None
        self.db = None
    def forward(self,x):
        self.x = x
        out = np.dot(x,self.W)+self.b
        return out
    def backward(self,dout):
        dx = np.dot(dout,self.W.T)
        self.dw = np.dot(self.x.T,dout)
        self.db = np.sum(dout,axis = 0)
        return dx

class Softmax_with_loss():
    def __init__(self):
        self.loss = None
        self.y = None
        self.t = None
    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y,self.t)
        return self.loss
    def backward(self,dout = 1):
        batch_size = self.t.shape[0]
        dx = (self.y-self.t)/batch_size
        return dx