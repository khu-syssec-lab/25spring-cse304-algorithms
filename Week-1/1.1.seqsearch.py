from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    location = 0

    if n == 0:
        return location
    for i in range (n):
        if S[i] == x :
            location = i
            break

    return location