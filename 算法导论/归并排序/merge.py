def merge(A, p, q, r):
    # if type(A) is list:
    #     L = A[p:q+1]
    #     R = A[q+1 :r + 1]
    # else:
    #     L = list(A[p:q+1])
    #     R = list(A[q+1:r + 1])
    L = A[p:q+1]
    R = A[q+1 :r + 1]

    i = 0
    j = 0
    k = p


    # for k in range(p,r):
    #     print('k', k)
    #     if L[i] <= R[j]:
    #         A[k] = L[i]
    #         i += 1
    #     elif A[k] == R[j]:
    #         j += 1

    # # for i in range()
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1


    if i < len(L):
        A[k:r+1] = L[i:]
    if j < len(R):
        A[k:r+1] = R[j:]

def merge_sort(A,p,r):
    if r is None:
        r = len(A) - 1
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p , q)
        print('1111')
        merge_sort(A, q + 1 , r)
        print('2222')
        merge(A, p, q, r)


A = [2,4,5,7,1,2,3,6]
print(A)

merge_sort(A, 0, len(A))
print(A)




    