def find_leaders(A):
    leaders = []
    max_right = float('-inf') 
    for i in range(len(arr)-1, -1, -1):
        if A[i] > max_right:
            leaders.append(A[i])  
            max_right = A[i] 

    leaders.reverse() 
    return leaders
