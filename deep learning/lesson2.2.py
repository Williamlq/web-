import numpy as np
import matplotlib.pyplot as plt
def AND(x1,x2):
    w1,w2,b=0.5,0.5,-0.7
    tmp =x1*w1 +x2 * w2 + b
    return 1 if tmp>0 else 0
# 验证真值表
print("与门真值表验证:")
for x1,x2 in[(0,0),(1,0),(0,1),(1,1)]:
    print(f"AND({x1},{x2})={AND(x1,x2)}")
# 绘制线性分割边界
x1=np.linspace(-0.5,1.5,100)
x2=-(0.5*x1-0.7)/0.5 # 分割边界公式

plt.scatter([0,1,0,1],[0,0,1,1],c=[0,0,0,1],cmap="gray") # 4个输入点
plt.plot(x1,x2,'r--')
# 关键修改:设置坐标轴范围，确保所有点可见
plt.xlim(-0.1,1.1)# x轴范围:略小于0到略大于1plt.ylim(*args:-0.1，1.1)# y轴范围:同上plt.xlabel("x1")
plt.ylabel("x2")
plt.title("AND Gate Linear Separation")
plt.show()
def NAND(x1,x2):
    w1,w2,b=-0.5,-0.5,0.7
    tmp =x1 *w1+x2 * w2 + b
    return 1 if tmp>0 else 0

print("与非门真值表验证:")
for x1,x2 in[(0,0),(1,0),(0,1),(1,1)]:
    print(f"NAND({x1},{x2})= {NAND(x1,x2)}")
# 绘制线性分割边界
x1 =np.linspace(-0.5,1.5,100)
x2=-(-0.5*x1+0.7)/(-0.5)
plt.scatter([0,1,0,1],[0,0,1,1],c=[1,1,1,0],cmap="gray")
plt.plot(x1,x2,'b--')

plt.xlim(-0.1,1.1)
plt.ylim(-0.1,1.1)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("NAND Gate Linear Separation")
plt.show()
def OR(x1,x2):
    w1,w2,b=0.5,0.5,-0.2
    tmp =x1*w1+ x2*w2 + b
    return 1 if tmp>0 else 0

print("或门真值表验证:")
for x1,x2 in[(0,0),(1,0),(0,1),(1,1)]:
    print(f"0R({x1},{x2})= {OR(x1,x2)}")

x1=np.linspace(-0.5,1.5,100)
x2=-(0.5*x1-0.2)/0.5

plt.scatter([0,1,0,1],[0,0,1,1],c=[0,1,1,1],cmap="gray")
plt.plot(x1,x2,'g--')

plt.xlim(-0.1,1.1)
plt.ylim(-.1,1.1)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("OR Gate Linear separation")
plt.show()
def XOR(x1,x2):
    s1 =NAND(x1,x2)
    s2 =OR(x1,x2)
    return AND(s1,s2)

print("异或门真值表验证:")
for x1,x2 in[(0,0),(1,0),(0,1),(1,1)]:
    print(f"XOR({x1},{x2})={XOR(x1,x2)}")

x1 = np.linspace(-0.5,1.5,100)
x2_nand=(-0.5*x1-0.7)/(-0.5)
x2_or=-(0.5*x1-0.2)/0.5
plt.scatter([0,1,0,1],[0,0,1,1],c=[0,1,1,0],cmap="gray")
plt.plot(x1,x2_nand,'g--',label="NAND Boundary")
plt.plot(x1,x2_or,'b--',label="OR Boundary")
plt.xlim( -1.1,1.1)
plt.ylim( -1.1,1.1)
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("XoR Gate(combination of NAND and OR)")
plt.legend()
plt.show()
