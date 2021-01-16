

'''
string --> list of strings
returns a list of strings where each string represents a permutation of the input string
'''

def perm_gen_lex(a):
    all_perms = []
    if a == "": #base case
        return [a]
    for i in range(len(a)): #reduction
        first = a[i]
        rest = a[:i] + a[i+1:] #all chars except for ith
        temp_perm = perm_gen_lex(rest) #gives all permutations of last values
        for x in range(len(temp_perm)): #for each permutation
            all_perms.append(first + temp_perm[x]) #combine
    return all_perms







