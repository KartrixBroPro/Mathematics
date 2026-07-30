def alphabeta(node,depth,alpha,beta,maximizingPlayer,tree):
    if node==0 or node not in tree:
        return node
    
    if maximizingPlayer:
        maxEva=-9999
        for child in tree[node]:
            eva=alphabeta(child,depth-1,alpha,beta,False,tree)
            maxEva=max(maxEva,eva)
            alpha=max(alpha,eva)
            if beta>=alpha:
                break
        return maxEva
    else:
        minEva=9999
        for child in tree[node]:
            eva=alphabeta(child,depth-1,alpha,beta,True,tree)
            minEva=min(minEva,eva)
            beta=min(beta,eva)
            if beta>=alpha:
                break
        return minEva


tree={
    'A':['B','C'],
    'B':[1,2],
    'C':[2,3],
}

leaf_tree={}

for k,v in tree.items():
    if all(type(x)==int for x in v):
        leaf_tree[k]=v
    else:
        leaf_tree[k]=v

print("result: ",alphabeta('A',2,-9999,9999,True,leaf_tree))
