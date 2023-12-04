def sort(A):
    # count number of 0's
    zero = A.count(0)
    # put 0's at the beginning
    b = 0
    while zero:
        A[b]=0
        zero =zero - 1
        b= b + 1
        # fill all remaining elements by 1
        for b in range(b, len(A)):
            A[b] = 1
            
A = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 8, 5, 2]
sort(A)
print(A)

    