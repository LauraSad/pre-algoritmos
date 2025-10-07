def conectores_logicos(p,q):
    return (p and q, q or p, not p or not q)
resultado=conectores_logicos(True, False) 
print(resultado)           #expected output: (False, True, True)
# The function returns a tuple with the results of the logical operations: