def isStringPermutation(s1: str, s2: str) -> bool:
    return False




#Test Cases
print(isStringPermutation('asdf', 'fsda') == True)
print(isStringPermutation('asdf', 'fsa') == False)
print(isStringPermutation('asdf', 'fsax') == False)