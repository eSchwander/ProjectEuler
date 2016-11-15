"""
The Fibonacci numbers {fn, n ≥ 0} are defined recursively as fn = fn-1 + fn-2 with base cases f0 = 0 and f1 = 1.

Define the polynomials {Fn, n ≥ 0} as Fn(x) = ∑fixi for 0 ≤ i ≤ n.

For example, F7(x) = x + x2 + 2x3 + 3x4 + 5x5 + 8x6 + 13x7, and F7(11) = 268357683.

Let n = 1015. Find the sum [∑0≤x≤100 Fn(x)] mod 1307674368000 (= 15!).
"""

class PolyFib():

    class FibList():
        def __init__(self):
            self.list = [1,1,2]
            self.digit = 3

    def __init__(self):
        self.fibList = [1,1,2]

    def getFib(self, x):
        if len(self.fibList) < x:
            self.populateToX(x)
        return self.fibList[x-1]

    def populateToDigit(self, digit):
        while len(self.fibList) < digit:
            self.fibList.append(self.fibList[-1] + self.fibList[-2])

    def poly(self, x, n):
        self.populateToDigit(n)
        total = 0
        for i, number in enumerate(self.fibList):
            if i == n:
                break
            total += x**(i+1) * number
        return total

def recursiveFib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return recursiveFib(x-1) + recursiveFib(x-2)

fibber = PolyFib()

total = 0
n = 10**15
for x in range(101):
    total += fibber.poly(x, n)

with open("435Answer.txt", "w") as answerText:
    answerText.writelines(str(total % 1307674368000))