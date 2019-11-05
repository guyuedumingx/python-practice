
def minSwap(A,B):
    g = 0
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            if B[i] > B[i+1]:
                A[i+1],B[i+1] = B[i+1],A[i+1]
                g = g + 1
        elif A[i]==A[i+1] and A[i]>B[i]:
            A[i],B[i] = B[i],A[i]
            g = g +1
        else:
            A[i+1],B[i+1] = B[i+1],A[i+1]
            g = g +1
    print(g)
A = [3,3,8,9,10]
B = [1,7,4,6,8]

minSwap(A,B)