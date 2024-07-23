def count_less_equal(x, M, N):
    count = 0
    for i in range(1, M + 1):
        count += min(x // i, N)
    return count

def find_kth_smallest(M, N, K):
    low, high = 1, M * N
    while low < high:
        mid = (low + high) // 2
        if count_less_equal(mid, M, N) < K:
            low = mid + 1
        else:
            high = mid
    return low

print(find_kth_smallest(3, 3, 5))  
print(find_kth_smallest(2, 3, 6)) 
