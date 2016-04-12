"""
Project Euler problem 3

Solution by Charlotte Aten (caten2@u.rochester.edu) 2016

Problem statement:
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143?
"""

class PrimeFactors:
    """
    The collection of natural prime factors of a specified integer.

    Attributes:
        integer (int): The integer for which prime factors are determined.
        factors (list): The factors of `integer` greater than 1.
        prime_factors (list): The prime factors of `integer`.
        largest_prime_factor (int): The largest prime factor of `integer`.
    """

    def __init__(self,i):
        """
        Args:
            i (int): The integer for which prime factors are determined.
        """

        self.integer = i
        self.factors = list(self.factors())
        self.prime_factors = list(self.prime_factors())
        self.largest_prime_factor = self.prime_factors[-1]

    def __repr__(self):
        return 'Prime factorization of {}.'.format(self.integer)

    def factors(self):
        """
        Generate those positive integers greater than 1 which are factors of `integer`.

        Yields:
            int: The next factor of `integer`.
        """

        for n in range(2,self.integer//2):
            if self.integer%n == 0:
                yield n
        yield self.integer

    def prime_factors(self):
        """
        Generate those positive integers which are prime factors of `integer`.

        Yields:
            int: The next prime factor of `integer`.
        """

        lis = self.factors[:]
        while lis != []:
            p = lis.pop(0)
            lis = [r for r in lis if r%p!=0]
            yield p

print('Create an object for the prime factorization of 13195 and have it give its name.')
f = PrimeFactors(13195)
print(f)
print()

print('List the prime factors of 13195.')
print(f.prime_factors)
print()

print('Give the largest prime factor of 13195.')
print(f.largest_prime_factor)
print()

print('Create an object for the prime factorization of 600851475143 and have it give its name.')
g = PrimeFactors(600851475143)
print(g)
print()

print('List the prime factors of 600851475143.')
print(g.prime_factors)
print()

print('Give the largest prime factor of 600851475143.')
print(g.largest_prime_factor)