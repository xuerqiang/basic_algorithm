#coding=utf-8
#   1. 当N=1，M种
#   2. 当N=2，M(M-1)
#   3. 当N>=3,M(M-1)^(N-1),但第N块与第1块可能会同色（即N-1的情况）
def Iter_func(N,M):
    if N == 1:
        S = M
    elif N == 2:
        S = M * (M - 1)
    else:
        S=M * ((M - 1)**(N-1))-Iter_func(N-1,M)
    return S
M = int(input("M:"))
N = int(input("N:"))
S=Iter_func(N,M)
print(S)
