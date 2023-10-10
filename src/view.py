"""
View
"""


class ConsoleView():
    """
    Method to display with console.
    """
    def __init__(self, pos_display_char, neg_display_char):
        """
        Constructor. Takes in the character to display in console.
        """
        self.pos_display_char = pos_display_char
        self.neg_display_char = neg_display_char

    def display(self, array):
        """
        Method displaying the array in console.
        """
        print('')
        for i in array:
            if i > 0:
                print('|', self.pos_display_char * i)
            else:
                print('|', self.neg_display_char * abs(i))

    def ask_sort(self):
        pass

    def ask_input(self):
        """
        Method getting user input
        """
        array_int = []
        array_str = input('Input numbers of the array : ').split(',')  # todo Gets the user input (go get regex)

        for x in array_str:
            x = int(x)
            array_int.append(x)

        return array_int