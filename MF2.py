import numpy as np

def matrix_factorization(data, K, steps=5000, beta=0.0002, lamda=0.02):
    
    W = np.random.rand(data.shape[0],K)
    H = np.random.rand(data.shape[1],K)
    H = H.T
    for step in range(steps):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 0:
                    eij = data[i][j] - np.dot(W[i,:],H[:,j])
                    W[i,:] += beta*(2*eij*H[:,j] - lamda * W[i,:])
                    H[:,j] += beta*(2*eij*W[i,:] - lamda * H[:,j])
                    
    
    
        edata = np.dot(W,H)
        e = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] > 0:
                    e = e + pow(data[i][j] - np.dot(W[i,:],H[:,j]), 2)
                    for k in range(K):
                        e = e + (lamda/2) * ( pow(W[i][k],2) + pow(H[k][j],2) )
                        
        if e < 0.001:
            break
    return W, H.T

def readFile(fileString):
    return np.loadtxt(fileString, delimiter=" ", dtype = "int").tolist()



if __name__ == "__main__":
    fileString = r'F:\Tut\Sem6\Information System\testData\test1.txt'
    data = readFile(fileString)

    data = np.array(data)

    K = 4

    W,H = matrix_factorization(data, K)
    print("Matrix Factorization")
    fitted = W.dot(H.T)
    for i in fitted:
        print(np.around(i, decimals = 2))
    #print(fitted)
