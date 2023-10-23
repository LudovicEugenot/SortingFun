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
        self.view = view.ConsoleView()

    def run(self):
        """
        Function that runs the program
        """
        sorting = model.BubbleSort(self.view.ask_input())
        self.view.reframe_display(
            sorting.get_lowest_value(),
            sorting.get_highest_value())
        while not sorting.is_sorted():
            self.view.display(sorting.array)
            time.sleep(0.5)
            sorting.next_step()
