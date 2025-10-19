def AND(x1 , x2):
    w1 , w2, theta = 0.5,0.5,0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    if tmp >theta:
        return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))

def NAND(x1,x2):
    w1,w2,b = -0.5,-0.5,0.7
    tmp = x1*w1 + x2*w2 +b
    if tmp <= 0:
        return 0
    if tmp > 0:
        return 1
print(NAND(0,0))
print(NAND(1,0))
print(NAND(0,1))
print(NAND(1,1))

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w1 + x2*w2
    if tmp >theta:
        return 0
    elif tmp <= theta:
        return 1

def XOR (x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y
print(XOR(0,0))
print(XOR(1,0))
print(XOR(0,1))
print(XOR(1,1))

