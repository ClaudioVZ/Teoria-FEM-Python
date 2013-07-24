import numpy as np
from sympy import Matrix, Transpose, expand, latex

def expandir_matriz(matriz):
    fila = matriz.shape[0]
    for i in range(fila):
        for j in range(fila):
            matriz[i, j] = expand(matriz[i, j])
    return matriz

def lagrangiana_1D(x, n):
    puntos = np.linspace(-1, 1, n)
    resultado = []
    for i in range(np.size(puntos)):
        b = puntos[puntos != puntos[i]]
        polinomio = 1.0
        for j in range(np.size(b)):
            polinomio *= (x - b[j]) / (puntos[i] - b[j])
        resultado.append(expand(polinomio))
    return resultado

def lagrangiana_2D(x, y, n):
    Lx = Matrix(lagrangiana_1D(x, n))
    Ly = Transpose(Matrix(lagrangiana_1D(y, n)))
    Lxy = expandir_matriz((Lx*Ly))
    return Lxy

def lagrangiana_3D(x, y, z, n):
    Lx = Matrix(lagrangiana_1D(x, n))
    Ly = Transpose(Matrix(lagrangiana_1D(y, n)))
    Lz = Transpose(Matrix(lagrangiana_1D(z, n)))
    Lxy = expandir_matriz((Lx*Ly))
    filas = Lxy.shape[0]
    Lxyz = []
    for i in range(filas):
        resultado = expandir_matriz((Lxy[:, i]*Lz))
        Lxyz = np.append(Lxyz, resultado)
    return Lxyz.reshape(filas, filas, filas)

def recorrer_matriz_espiral(M):
    filas_M = M.shape[0]
    iteraciones = filas_M - (filas_M/2)
    for i in range(iteraciones):
        m = M[i:filas_M-i, i:filas_M-i]
        filas_m = m.shape[0]
        n = filas_m - 1
        if n == 0:
            print m[0,0]
        else:
            for j in range(n):
                print m[j,0]
            for j in range(n):
                print m[n,j]
            for j in range(n,0,-1):
                print m[j,n]
            for j in range(n,0,-1):
                print m[0,j]

def guardar_matriz_espiral(M):
    resultado = []
    filas_M = M.shape[0]
    iteraciones = filas_M - (filas_M/2)
    for i in range(iteraciones):
        m = M[i:filas_M-i, i:filas_M-i]
        filas_m = m.shape[0]
        n = filas_m - 1
        if n == 0:
            resultado.append(m[0,0])
        else:
            for j in range(n):
                resultado.append(m[j,0])
            for j in range(n):
                resultado.append(m[n,j])
            for j in range(n,0,-1):
                resultado.append(m[j,n])
            for j in range(n,0,-1):
                resultado.append(m[0,j])
    return resultado

def recorrer_matriz_3d_espiral(N):
    filas = N.shape[0]
    for i in range(filas):
        recorrer_matriz_espiral(N[i])

def guardar_matriz_3d_espiral(N):
    resultado1 = []
    filas = N.shape[0]
    for i in range(filas):
        resultado1.append(guardar_matriz_espiral(N[i]))
    return reduce(lambda x,y: x+y,resultado1)
