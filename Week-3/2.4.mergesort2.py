from typing import List

def merge2(low: int, mid: int, high: int, S: List[int]) -> None:
    U = [0] * (high - low + 1)
    i, j, k = low, mid + 1, 0
    #S에서 U로 비교하며 U에 정렬
    while i <= mid and j <= high:
        if S[i] < S[j]:
            U[k] = S[i]
            i += 1
        else:
            U[k] = S[j]
            j += 1
        k += 1    

    # 정렬후 남은 요소들 처리
    while i <= mid:
        U[k] = S[i]
        i += 1
        k += 1
        
    while j <= high:
        U[k] = S[j]
        j += 1
        k += 1
    
    # 완성된 임시 배열의 값을 원래 배열로 복사
    for i in range(high - low + 1):
        S[low + i] = U[i]

def mergesort2(low: int, high: int, S: List[int]) -> None:
    if low < high:
        mid = (low + high) // 2
        mergesort2(low, mid, S)
        mergesort2(mid + 1, high, S)
        merge2(low, mid, high, S)