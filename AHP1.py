import numpy as np
from fractions import Fraction

def load_units(file):
    units = []
    with open(file) as fp:
        for line in fp:
            units.append(line.split()[0]) # Used to deal with '\n'
        return units

def cross_compare(units):
    n = len(units)
    A = np.zeros((n, n))
    for i in range(0, n):
        for j in range(i, n):
            if i == j:
                scale = 1
            else:
                scale = float(Fraction(input(units[i]+' to '+units[j]+':')))
            A[i][j] = scale
            A[j][i] = float(1/scale)
    return A

def get_weight(A, getfrom):
    '''
    A: input matrix
    getfrom: 0 = criterions, 1 = alternatives
    '''
    n = A.shape[0]
    B = np.array(A)
    print("The matrix:")
    print(A)
    sumCols = np.array([sum(B[:,i]) for i in range(len(B[0]))])
    for i in range(len(B)):
        for j in range(len(B[i])):
            B[i][j] /= sumCols[j]
    print("Normalized matrix:")
    print(B)
    #print()
    priority = np.array([sum(B[i,:]/len(B[i])) for i in range(len(B))])
    print("Priority(Row avg):")
    print(priority)
    weightedSum = A.dot(priority.T)
    print("Weighted sum:")
    print(weightedSum)
    lamb = sum([weightedSum[i]/priority[i] for i in range(len(weightedSum))])/n
    if (getfrom == 1):
        return priority
    #print(lamb)

    # Consistency Checking
    RI = {1: 0, 2: 0, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49, 11: 1.51}
    CI = (lamb - n) / (n - 1)
    CR = CI / RI[n]

    print('CR = %f'%CR)
    if CR >= 0.1:
        print("Failed in Consistency check.")
        exit = input("Enter 'q' to quit.")
        raise
    return priority, CR

if __name__ == '__main__':
    goal = input("Your Goal: ")
    criterions = load_units('criterions.txt')
    alternatives = load_units('alternatives.txt')
    n2 = len(criterions)
    n3 = len(alternatives)
    A = cross_compare(criterions)

    print()
    W2, cr2 = get_weight(A,0)
    B = {}
    W3 = np.zeros((n2, n3))
    for i in range(n2):
        print("######################")
        print("Consider "+criterions[i])
        B[str(i)] = cross_compare(alternatives)
        w3 = get_weight(B[str(i)],1)
        W3[i] = w3
    W = np.dot(W2, W3)

    print("######################")
    print("The final Weight:")
    print(W)
    W = [(W[i],i) for i in range(len(W))]
    print(W)
    sorted(W, reverse = True)
    print("Pick alternative a"+ str(W[0][1]))
