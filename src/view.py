"""
View
"""


class View:
    """
    Abstract class for different view types.
    """

    def __init__(self, low_inner_display_limit, high_inner_display_limit, max_display_limit):
        self.lowest_value = self.low_inner_display_limit = low_inner_display_limit
        self.highest_value = self.high_inner_display_limit = high_inner_display_limit
        self.max_display_limit = max_display_limit
        self.scale = 1

    def reframe_display(self, lowest_value, highest_value):
        """
        Base method to reframe display according to values.
        Intended to be implemented in child.
        """
        self.lowest_value, self.highest_value = lowest_value, highest_value

    def display(self, array):
        """
        Virtual method to be implemented in child.
        Method used to display.
        """
        raise NotImplementedError

    def ask_input(self):
        """
        Virtual method to be implemented in child.
        Method getting user input.
        """
        raise NotImplementedError


class ConsoleView(View):
    """
    Method to display with console.
    """

    def __init__(self):
        """
        Constructor. Takes in the character to display in console.
        """
        # different console characters : █ ▓ ▒ ░ | — ⟸ ⟹ ▐ ▌

        super().__init__(-4, 5, 165)
        self.display_char = '█'
        self.zero_char = '|'
        self.is_centered = True

    def reframe_display(self, lowest_value, highest_value):
        """
        Reframe display to fit console.

        (This console display only cares about the lowest value.)
        """
        self.scale = self.max_display_limit / (highest_value - lowest_value)
        if self.scale > 1:
            self.scale = 1

        # adapt scale then center around values

        if (highest_value < self.low_inner_display_limit or
                lowest_value > self.high_inner_display_limit):  # if values are all not centered
            self.is_centered = False
            self.highest_value = highest_value if lowest_value > 0 else int((101 * highest_value - lowest_value) / 100)
            self.lowest_value = lowest_value if lowest_value < 0 else int((101 * lowest_value - highest_value) / 100)
            # +/- other extreme to show the lowest value in display
            self.zero_char = '⟸' if lowest_value < 0 else '⟹'
        elif lowest_value < self.lowest_value:  # else, lowest value
            self.lowest_value = lowest_value

    def display(self, array):
        """
        Method displaying the array in console.
        """
        print('')
        print('')
        for i in array:
            displayed_number_len = len(str(i))
            if self.is_centered:
                if i > 0:
                    print(
                        ' ' * int((abs(self.lowest_value) * self.scale) - displayed_number_len + 1)
                        + str(i)
                        + self.zero_char
                        + self.display_char * int(i * self.scale)
                        + self.last_display_char(i))
                else:
                    print(
                        ' ' * int((abs(self.lowest_value - i) * self.scale).__ceil__())
                        + self.last_display_char(i)
                        + self.display_char * int(abs(i) * self.scale)
                        + self.zero_char
                        + str(i))
            elif i > 0:
                print(
                    self.zero_char
                    + ' ' * (5 - displayed_number_len)
                    + str(i)
                    + ' '
                    + self.display_char * int((i - self.lowest_value) * self.scale)
                    + self.last_display_char(i))
            else:
                print(
                    ' ' * int((abs(self.lowest_value - i) * self.scale).__ceil__())
                    + self.last_display_char(i)
                    + self.display_char * int(abs(i - self.highest_value) * self.scale)
                    + ' ' * (6 - displayed_number_len)
                    + str(i)
                    + ' '
                    + self.zero_char)

    def last_display_char(self, number):
        """
        Returns a character relative to how close it is to 1. (with small scale)
        """
        if self.scale >= 1:
            return ' '
        remainder = (abs(number) % self.scale) / self.scale
        if remainder > .5:
            return '▌' if number > 0 else '▐'
        else:
            return ' '

    def ask_sort(self):
        pass

    def ask_input(self):
        """
        Method getting user input
        """
        array_int = []
        array_str = input('Input whole numbers of the array (-9999 to 9999) : ').split(',')
        # todo Gets the user input (go get regex) if I want better handling of data

        for x in array_str:
            x = int(x)
            array_int.append(x)

        return array_int
