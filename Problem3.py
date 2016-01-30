"""
Project Euler problem 3

Solution by Charlotte Aten (caten2@u.rochester.edu) 2015

Problem statement:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
"""

class PrimeFactors():
    """
    The collection of natural prime factors of a specified integer.
    """

    def __init__(self,i):
        self.integer = i # Return the integer in question.
        self.primeFactors = list(self.PrimeFactors()) # Return a list of the prime factors of i.

    def PrimeFactors(self):
        for n in range(1,self.integer):
            if self.integer%n == 0:
                