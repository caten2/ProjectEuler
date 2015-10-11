# Project Euler problem 1
# Solution by Charlotte Aten (caten2@u.rochester.edu)
# Problem statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

class Multiples():
    """The set of all multiples of the elements in lis strictly less than maximum."""

    def __init__(self, lis, maximum):
        self.multiplesOf = lis # Give the list of numbers of which we will look at multiples.
        self.maximum = maximum # Give the maximum number to be considered.

    # Create a generator for all numbers below self.maximum which are multiples of
    # elements of self.lis.
    def Elements(self):
        for i in range(1,self.maximum):
            for n in self.multiplesOf:
                # Check if i is a multiple of n by noting that n divides i iff i is
                # congruent to 0 modulo n.
                if i % n == 0:
                    yield i

    # Give a list of the numbers yielded by the above generator.
    def ListElements(self):
        return list(self.Elements())

    # Sum all numbers yielded by the above generator.
    def Total(self):
        return sum(self.Elements())

print("Create an object for the multiples of 3 and 5 below 10.")
M = Multiples([3,5],10)

print("List all of the multiples of 3 and 5 below 10.")
print(M.ListElements())

print("Give the sum of those values.")
print(M.Total())
print("")

print("Create an object for the multiples of 3 and 5 below 1000.")
N = Multiples([3,5],1000)

print("List all of the multiples of 3 and 5 below 1000.")
print(N.ListElements())

print("Give the sum of those values.")
print(N.Total())