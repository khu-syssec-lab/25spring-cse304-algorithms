from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    # Complete the code here

    buffer = 0

    for i in range (n):
        for k in range (i+1,n):
            if S[i] > S[k]:
                S[i], S[k] = S[k], S[i]
    
    return S
