"""
Model.
"""


class Sort:
    """
    Abstract class for underlying sorting algorithms.
    """
    def __init__(self, array):
        """
        Constructor taking the list to sort.
        """
        self.array = array

    def is_sorted(self):
        """
        Virtual method to be implemented in child.
        Returns true if array is sorted.
        """
        raise NotImplementedError

    def next_step(self):
        """
        Virtual method to be implemented in child.
        The next step sorting. Returns current step of the sort.
        """
        raise NotImplementedError


class BubbleSort(Sort):
    """
    Bubble sort implementation.
    """
    def __init__(self, array):
        """
        Constructor taking the list to sort.
        """
        Sort.__init__(self, array)

        self.i = 0
        self.j = 0
        self.already_sorted = True
        self.sort_finished = False

    def is_sorted(self):
        """
        Returns true if array is sorted.
        """
        return self.sort_finished

    def next_step(self):
        """
        The next step sorting. Returns current step of the sort.
        """
        assert self.i < len(self.array) and not self.sort_finished, 'incorrect values'

        if self.array[self.j] > self.array[self.j + 1]:
            stored = self.array[self.j]

            self.array[self.j] = self.array[self.j + 1]
            self.array[self.j + 1] = stored
            self.already_sorted = False

        self.j += 1

        if self.j >= len(self.array) - self.i - 1:
            if self.i >= len(self.array) - 1 or self.already_sorted:
                self.sort_finished = True
            else:
                self.j = 0
                self.i += 1
                self.already_sorted = True
