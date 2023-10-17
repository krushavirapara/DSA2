def generate_grammar(N,K):
    if N==1 and K==1:
        return 0
    length = pow(2,N-1)
    mid = length//2
    if K<=mid:
        return generate_grammar(N-1,K)
    elif K>mid:
        return 1 -  generate_grammar(N-1,K-mid)
    
print(generate_grammar(4,6))

    