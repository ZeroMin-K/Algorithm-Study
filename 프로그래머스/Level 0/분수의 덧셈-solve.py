def solution(numer1, denom1, numer2, denom2):
    res_numer = numer1 * denom2 + numer2 * denom1
    res_denom = denom1 * denom2 
    
    for div in range(min(res_numer, res_denom), 1, -1): 
        if res_numer % div == 0 and res_denom % div == 0:
            res_numer //= div
            res_denom //= div 
    
    return [res_numer, res_denom]