import json
import os
from time import sleep


def print_puzzle(y):
    for i in range(9):
        print(f"{y[i]['c1']}  {y[i]['c2']}  {y[i]['c3']} | {y[i]['c4']}  {y[i]['c5']}  {y[i]['c6']} | {y[i]['c7']}  {y[i]['c8']}  {y[i]['c9']}", end='\n')


def find_empty_cell(xy):
    # empty_cells = [[j if y[i][j] == 0 else y[i][j] for j in y[i].keys()] for i in range(9)]
    # empty_cells = [[cell for cell in cells if not isinstance(cell, int)]for cells in empty_cells]
    # return empty_cells
    for i in range(9):
        for j in xy[i].keys():
            if xy[i][j] == 0:
                return (i, j)


def update_cell(xy):
    cell = find_empty_cell(xy)
    if not cell:
        print_puzzle(xy)
        return True
    else:
        row, col = cell
    
    for i in range(1,10):
        if validator(xy, i, cell):
            xy[row][col] = i
            print_puzzle(xy)
            sleep(0.1)
            os.system('cls')

            if update_cell(xy):
                return True
            
            xy[row][col] = 0
            print_puzzle(xy)
            sleep(0.1)
            os.system('cls')
    return False
                

def validator(xy, k, cell):
    for i in xy[0].keys():
        if xy[cell[0]][i] == k and cell[1] != i:
            return False

    for i in range(9):
        if xy[i][cell[1]] == k and cell[0] != i:
            return False

    x = cell[0] // 3

    for i in range(x * 3, x*3 + 3):
        if cell[1] in ['c1', 'c2', 'c3']:
            for j in ['c1', 'c2', 'c3']:
                if xy[i][j] == k and cell != (i, j):
                    return False
        elif cell[1] in ['c4', 'c5', 'c6']:
            for j in ['c4', 'c5', 'c6']:
                if xy[i][j] == k and cell != (i, j):
                    return False
        else:
            for j in ['c7', 'c8', 'c9']:
                if xy[i][j] == k and cell != (i, j):
                    return False
    return True



with open('puzzle.json', 'r') as f:
    puzzle = json.load(f)

rows = list(puzzle.keys())
columns = list(puzzle.values())
print(columns)

update_cell(columns)