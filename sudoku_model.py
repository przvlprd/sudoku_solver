#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from clingo import Control


class ClingoModel:

    def __init__(self, initials: str, subgrid_size: int = 3):
        self.ctl = Control()  # Create a Control object
        self.subgrid_size = subgrid_size  # default = 3 for 9x9 Sudoku field
        self.initials = initials

    def solve(self):
        # Add the ASP code
        self.ctl.add("base", [], f"""

                % initials
                {self.initials}

                % size of subgrids, e.g., '3' will result in 9x9 square
                subgrid_size({self.subgrid_size}).

                % there are (1-9) nums
                num(1..S*S) :- subgrid_size(S).

                % there are (1-9) cols
                col(1..S*S) :- subgrid_size(S).

                % there are (1-9) rows
                row(1..S*S) :- subgrid_size(S).

                % include initials as sudokus
                sudoku(X,Y,N) :- initial(X,Y,N).

                % there are (1-9) subgrids with (1-9) cells each
                subgrid(X,Y,Q,P) :- col(X), row(Y), col(Q), row(P), 
                                    ((X-1)/S)*S == ((Q-1)/S)*S, 
                                    (Y-1)/S == (P-1)/S, 
                                    subgrid_size(S).

                % Generator: there must be exactly 1 num for each cell (X,Y) 
                % where no initial is given
                {{ sudoku(X,Y,N) : num(N) }} = 1 :- col(X), row(Y), 
                                                    not initial(X,Y,_).

                % Constraints: no same num for each col and each row
                :- sudoku(X,Y,N), sudoku(X',Y,N), X != X'.
                :- sudoku(X,Y,N), sudoku(X,Y',N), Y != Y'.

                % Constraint: no same num twice in same subgrid
                :- sudoku(X,Y,V), sudoku(Q,P,V), subgrid(X,Y,Q,P), 
                   X != Q, Y != P.
                :- sudoku(X,Y,V), initial(Q,P,V), subgrid(X,Y,Q,P), 
                   X != Q, Y != P.

                % only show sudokus
                #show sudoku/3.

            """)

        # Ground the program
        self.ctl.ground([("base", [])])

        output = []

        # Solve the program and retrieve the first model
        with self.ctl.solve(yield_=True) as solved:
            for solution in solved:
                output = str(solution).split()

        return output


if __name__ == '__main__':
    # Insert the initials of the Sudoku (given values)
    # --> implement GUI to do this (KB+mouse)
    # use CNN and OCR to automate this
    example = """
        initial(1,1,5). initial(1,2,3). initial(1,5,7).
        initial(2,1,6). initial(2,4,1). initial(2,5,9). initial(2,6,5).
        initial(3,2,9). initial(3,3,8). initial(3,8,6).
        initial(4,1,8). initial(4,5,6). initial(4,9,3).
        initial(5,1,4). initial(5,4,8). initial(5,6,3). initial(5,9,1).
        initial(6,1,7). initial(6,5,2). initial(6,9,6).
        initial(7,2,6). initial(7,7,2). initial(7,8,8).
        initial(8,4,4). initial(8,5,1). initial(8,6,9). initial(8,9,5).
        initial(9,5,8). initial(9,8,7). initial(9,9,9).
        """

    # Insert size of of subgrid (e.g., Default 9x9 Sudoku = 3)
    a = ClingoModel(subgrid_size=3, initials=example).solve()
    print(a)
