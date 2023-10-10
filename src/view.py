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
        :param display_char:
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