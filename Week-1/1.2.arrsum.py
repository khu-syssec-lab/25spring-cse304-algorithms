from typing import List

def arrsum(n: int, S: List[int]) -> int:
    # Complete the code here
    
    result = 0
    for i in range (n):
        result += S[i]
    return result