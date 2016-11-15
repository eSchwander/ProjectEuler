"""
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
"""

#This does not succeed at completing the problem, but it is a permutations algorithm.


def listSum(aList):
    if len(aList) <= 1:
        return 0
    sum = 0
    for x in aList:
        sum += x
    return sum

def listProd(aList):
    if len(aList) <= 1:
        return 0
    prod = 1
    for x in aList:
        prod *= x
    return prod

def permutations(k):
    '''
    Finds all permutations of a list size k
    '''
    firstList = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
    options = firstList.copy()
    permList = []
    permList.append(firstList)
    for i in range(k):
        permList.append(permHelper(permList[i], options))
        print(i)
    return permList

def permHelper(prevList, options):
    optionsCopy = options.copy()
    toAppend = []
    for i, x in enumerate(optionsCopy):
        for y in prevList:
            subList = x.copy()
            subList.extend(y)
            toAppend.append(subList)
    return toAppend

# def comboNoReplacements(k):
#     options = [[1], [2], [3], [4], [5], [6], [7], [8], [9]]
#     combList = [[]]
#     for i in range(k):
#         combList.append(kSizeCombos(i+1, options.copy(), combList[i]))
#     return combList
#
# def kSizeCombos(size, options, prevCombos):
#     newList = []
#     if size == 1:
#         newList = firstCombo(options)
#     else:
#         for i, o in enumerate(options):
#             for x in prevCombos:
#                 test = x.copy
#                 test.extend(x)
#                 newList.append(test)
#     return newList
#
# def firstCombo(options):
#     return options

permList = permutations(12000)

totalSum = 0

for perms in permList:
    for perm in perms:
        if listProd(perm) == listSum(perm):
            totalSum += listSum(perm)

print(totalSum)





"""
answerList = []

for k in range(2, 12000):
    kList = [1]*k
    for
    if listProd(kList) == listSum(kList):
        answerList.append(listSum(kList))

answerList.sort()
prevAnswer = -1
totalSum = 0

for answer in answerList:
    if answer != prevAnswer:
        totalSum += answer
    prevAnswer = answer

print(totalSum)
"""
