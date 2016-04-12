"""
Project Euler problem 1

Solution by Charlotte Aten (caten2@u.rochester.edu) 2016

Problem statement:
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
"""

class MultiplesUpTo:
    """
    A collection of multiples of some natural numbers.

    Attributes:
        multiples_of (set): Multiples of the natural numbers in this set are considered.
        list_multiples_of (lis): Sorted list of the natural numbers in the set `multiples_of`.
        maximum (int): No multiples of elements of `multiples_of` greater than or equal to `maximum` are considered.
    """

    def __init__(self, nums, maximum):
        """
        Args:
            nums (list): A list of natural numbers.
            maximum (int): The maximum number up to which to consider multiples of the integers in `nums`.
        """

        assert len(nums) > 0
        self.multiples_of = frozenset(nums)
        self.list_multiples_of = sorted(list(self.multiples_of))
        self.maximum = maximum

    def __repr__(self):
        """
        Examples:
            >>> m = MultiplesUpTo([3,5],10); m
            'Multiples of 3 and 5 strictly less than 10.'
            >>> n = MultiplesUpTo([3,5,7,5,3,7],50); n
            'Multiples of 3, 5, and 7 strictly less than 50.'
        """

        if len(self.multiples_of) == 1:
            return 'Multiples of {} strictly less than {}.'.format(self.list_multiples_of[0],self.maximum)
        if len(self.multiples_of) == 2:
            lis = self.list_multiples_of
            return 'Multiples of {} and {} strictly less than {}.'.format(lis[0],lis[1],self.maximum)
        if len(self.multiples_of) > 2:
            lis = self.list_multiples_of
            parsed_lis = ', '.join([str(num) for num in lis[:-1]])+', '
            return 'Multiples of ' + parsed_lis + 'and {} strictly less than {}.'.format(lis[-1],self.maximum)

    def elements(self):
        """
        Generate numbers below `maximum` which are multiples of elements of `multiples_of`.

        Yields:
            int: The next number which is a multiple of an element of `nums`.
        """

        for i in range(1,self.maximum):
            for n in self.multiples_of:
                # Check whether `i` is a multiple of `n` by noting that n divides `i` iff `i` is congruent to 0 modulo `n`.
                if i % n == 0:
                    yield i

    def list_elements(self):
        """
        List all the numbers yielded by the generator ``elements``.

        Returns:
            list: All numbers yielded by ``elements`` in numerical order.
        """

        return list(self.elements())

    def total(self):
        """
        Sum all numbers yielded by ``elements``.

        Returns:
            int: The sum of all natural multiples of elements of `multiples_of` less than `maximum`.
        """

        return sum(self.elements())

print('Create an object for the multiples of 3 and 5 below 10 and have it give its name.')
m = MultiplesUpTo([3,5],10)
print(m)
print()

print('List all of the multiples of 3 and 5 below 10.')
print(m.list_elements())
print()

print('Give the sum of those values.')
print(m.total())
print()

print('Create an object for the multiples of 3 and 5 below 1000 and have it give its name.')
n = MultiplesUpTo([3,5],1000)
print(n)
print()

print('List all of the multiples of 3 and 5 below 1000.')
print(n.list_elements())
print()

print('Give the sum of those values.')
print(n.total())