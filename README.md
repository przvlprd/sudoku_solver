# Sudoku-Solver GUI

Working prototype of interface for solving Sudokus. 

- currently only working for 9x9 Sudokus, preferably on Windows


### Usage

- requires `potassco clingo` on Python 3.10
  -  `conda install -c potassco clingo`
- run `python sudoku_controller.py`, insert the given numbers in the grid, 
  click on `OK` and get the solution for your (now completely filled) Sudoku

### ToDos

#### Concrete tasks:
- add `requirements.txt`
  - use `conda` env instead of `pip`?
- use `numpy` arrays instead of nested lists for in- and output
- remove hard-coding for Sudoku- / subgrid-size (currently only 9x9)
- check input validity and how to handle invalid input (abort, restart?)
  - restrict input to single `int` (0-9)?
  - check for invalid input per grid, row, col (Sudoku rules)
- check output and display error message if no solution could be found

#### General roadmap:
- clean and update code
- separate and fix responsibilities for MVC modules
- fix clingo backend logic, no need for explicit string names passed to solver
- check/fix OS independent compatibility
  - rendering `tkinter` on Linux slow, cell background colors do not match
- use `PyQT` instead of `tkinter` 
   - possible reimplementation of view? all 
     parts should be modular anyway!
- when all is working:
  - web server implementation using `cherrypy`, later possibly `Django`
  - test image as input + CNN OCR to get input instead of manual user input
    - when this is working:
      - Android app
