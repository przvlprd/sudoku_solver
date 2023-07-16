#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sudoku_model import ClingoModel
from sudoku_view import SudokuGUI


class SudokuController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.subgrid_size = 3  # ToDo: hardcoded?

    def main(self):
        # Run the GUI to get the user input (partially filled Sudoko)
        user_input = self.view()
        values = user_input.values
        print('Values:\n', values)

        # pass values to internal formatting method
        initials = self.format_to_initials(values)

        # Pass formatted input as initials to model, run model, return solution
        solution = self.model(initials, self.subgrid_size).solve()

        # use for output window together with initial input
        # add color or bold font?

        # Debug
        print(solution)

        output = self.format_to_array(solution)

        # Debug
        print(output)

        solved_sudoku = self.view(mode='out', output=output)
        solved_sudoku.display_numbers(output)

    def format_to_initials(self, values: list[[str]]):
        # ToDo: use as int instead of str
        #   make sure input is valid?
        #    otherwise run again
        #  make sure output is valid as well!
        # Initials will be formatted strings as atoms for clingo
        initials = """"""
        # They look like this: 'initial(1,1,5).'
        for row in range(self.subgrid_size**2):
            for element in range(self.subgrid_size**2):
                # Element is not empty if there is a user input
                if values[row][element] != '':
                    initials += f"initial({row + 1},{element + 1}," \
                                f"{values[row][element]}). "
        print(initials)
        return initials

    def format_to_array(self, solution: list[str]):
        # Number of rows and columns in output
        rws_cls = self.subgrid_size**2
        sudoku_out = [["" for _ in range(rws_cls)] for _ in range(rws_cls)]
        # Single value in solution looks like this: 'sudoku(1,1,1)'
        for value in solution:
            sudoku_out[int(value[7])-1][int(value[9])-1] = int(value[11])

        return sudoku_out


if __name__ == '__main__':
    # Create an instance of the SudokuController
    controller = SudokuController(model=ClingoModel, view=SudokuGUI)
    controller.main()
