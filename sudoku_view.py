#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.font import Font


class SudokuGUI:

    def __init__(self, mode: str = 'in', output=None):
        # Create a window
        self.window = tk.Tk()  # ToDo: use PyQt instead of tkinter
        # Create a 2D list to store the entry fields
        self.entry_fields = []
        # Create a 2D list to store the user input
        self.values = []  # ToDo: use NP array
        # Create the "OK" button
        ok_button = tk.Button(self.window, text="OK", command=self.on_ok_click)
        ok_button.grid(row=20, column=9, pady=10)
        self.mode = mode
        self.output = output
        self.subgrid_size = 3  # FixMe hardcode!
        self.numbers_out = list(list())
        if mode == 'in':
            self.main()
            # Start the Tkinter event loop
            self.window.mainloop()

        # ToDo: use logic for grid for input (user) and output (result)
        #  input: as right now with empty fields to fill in
        #  output: with filled fields (from input + from solution)
        #  use highlighting, colors, bold fonts, etc. for visuals

    def main(self):
        if self.mode == 'out':
            numbers_out = [
                [tk.StringVar() for value in range(self.subgrid_size**2)]
                for value in range(self.subgrid_size**2)
            ]  # FixMe: use array
        # Create the 9x9 grid of entry fields with additional empty cells
        for row in range(19):
            row_fields = []
            for col in range(19):
                if row % 2 == 0 and col % 2 == 0:
                    # Create empty cells
                    label = tk.Label(self.window, width=1)
                    label.grid(row=row, column=col)
                    row_fields.append(None)
                elif row % 2 == 0:
                    # Create vertical grid lines
                    separator = ttk.Separator(self.window, orient="vertical")
                    separator.grid(row=row, column=col, sticky="ns")
                    separator.lift()  # Lower the grid lines below the labels
                    row_fields.append(None)
                elif col % 2 == 0:
                    # Create horizontal grid lines
                    separator = ttk.Separator(self.window, orient="horizontal")
                    separator.grid(row=row, column=col, sticky="ew")
                    separator.lift()  # Lower the grid lines below the labels
                    row_fields.append(None)
                else:
                    if self.mode == 'out':
                        placeholder = tk.StringVar()
                        entry = tk.Entry(self.window, width=5,
                                         textvariable=placeholder)

                        i = int((row - 1) / 2)
                        j = int((col - 1) / 2)

                        placeholder.set(self.numbers_out[i][j])
                    else:
                        entry = tk.Entry(self.window, width=5)
                    entry.grid(row=row, column=col)

                    # row_fields.append(entry)  # FixMe: here
                    # Assign different background colors to fields
                    if row in [1, 3, 5, 13, 15, 17]:
                        if col in [1, 3, 5, 13, 15, 17]:
                            entry.config(bg="lightgray")
                        else:
                            entry.config(bg="white")
                    else:
                        if col in [7, 9, 11]:
                            entry.config(bg="lightgray")
                        else:
                            entry.config(bg="white")
                    row_fields.append(entry)

            self.entry_fields.append(row_fields)

        # Create labels for axes
        bold_font = Font(weight="bold")
        i = 1
        for row in range(1, 19, 2):
            label_text = i
            label_col = tk.Label(self.window, text=label_text, bg="white",
                                 width=1, font=bold_font)
            label_col.grid(row=row, column=0, sticky="e")
            label_row = tk.Label(self.window, text=label_text, bg="white",
                                 width=1, font=bold_font)
            label_row.grid(row=0, column=row, sticky="s")
            i += 1

    def display_numbers(self, numbers):
        self.numbers_out = numbers
        self.main()
        # Start the Tkinter event loop
        self.window.mainloop()

    def on_ok_click(self):
        # Retrieve the values from the entry fields
        values = []
        for row in range(1, 19, 2):
            row_values = []
            for col in range(1, 19, 2):
                entry = self.entry_fields[row][col]
                value = entry.get()
                row_values.append(value)
            values.append(row_values)

        # Set the user input to internal state values
        self.values = values
        # Exit the window
        self.window.destroy()
