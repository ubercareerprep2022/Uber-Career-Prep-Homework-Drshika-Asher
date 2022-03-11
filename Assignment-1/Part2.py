# # 2.1
# def isStringPermutation(s1: str, s2: str) -> bool:
#     return sorted(s1) == sorted(s2)


# #Runtime O(log n) as sorted takes O(log n) time to sort an array of chars
# #Space time O(n) since this is in place

# #Test Cases
# print(isStringPermutation('asdf', 'fsda') == True)
# print(isStringPermutation('asdf', 'fsa') == False)
# print(isStringPermutation('asdf', 'fsax') == False)

#2.2
def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    solution = []
    for i in inputArray:
        for j in inputArray[1::]:
            int_sum = i+j
            if int_sum == targetSum:
                res = sorted((i, j))
                res = tuple(res) #i had to google this but now i know lol
                print(res)
                if res not in solution:
                    solution.append(res)
                print(solution)
    return solution
#Test Cases
print(pairsThatEqualSum([1, 2, 3, 4, 5], 5) == [(1, 4), (2, 3)])
print(pairsThatEqualSum([1, 2, 3, 4, 5], 1) == [])
print(pairsThatEqualSum([1, 2, 3, 4, 5], 7) == [(2, 5), (3, 4)])