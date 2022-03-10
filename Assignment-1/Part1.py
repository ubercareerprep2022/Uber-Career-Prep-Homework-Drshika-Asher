# 2.1
def isStringPermutation(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


#Runtime O(log n) as sorted takes O(log n) time to sort an array of chars
#Space time O(n) since this is in place

#Test Cases
print(isStringPermutation('asdf', 'fsda') == True)
print(isStringPermutation('asdf', 'fsa') == False)
print(isStringPermutation('asdf', 'fsax') == False)
