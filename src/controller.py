"""
Controller module
"""

import time
import model
import view


class Controller:
    """
    Controller
    """
    def __init__(self):
        """
        Constructor taking in the model and view modules
        """
        self.model = model.BubbleSort([1, 30, 10, 5, 2 * 3])
        self.view = view.ConsoleView('▀', '▄')

    def run(self):
        """
        Function that runs the program
        """
        while not self.model.is_sorted():
            self.view.display(self.model.array)
            time.sleep(1)
            self.model.next_step()
