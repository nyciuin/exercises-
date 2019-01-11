
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# FIRST PRINT loop

def printline0(variable):
    for ix in grid[variable]:
        print(ix, end=' ')
    print()

for iy in range(9):
    printline0(iy)
print()

# prints default grid

# SECOND PRINT loop
def printline1(variable):
    for iy in range(9):
        print(grid[iy][variable], end=' ')  # goes through 0-8, before finishing then 'variable' increases
    print()

for i in range(6):
    printline1(i)

# ALTERNATE, slightly clearer layout
# for i in range(6):
#     for iy in range(9):
#         print(grid[iy][i], end=' ')
#     print()

# prints rotated grid

#SECOND PRINT
    # print(grid[0][0], end=' ')
    # print(grid[1][0], end=' ')
    # print(grid[2][0], end=' ')
    # print(grid[3][0], end=' ')
    # print(grid[4][0], end=' ')
    # print(grid[5][0], end=' ')
    # print(grid[6][0], end=' ')
    # print(grid[7][0], end=' ')
    # print(grid[8][0], end=' ')


# FIRST PRINT
    # length of grid = 9
    # length of grid[0] = 6

    # for ix in grid[0]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[1]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[2]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[3]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[4]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[5]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[6]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[7]:
    #     print(ix, end=' ')
    # print()
    # for ix in grid[8]:
    #     print(ix, end=' ')
    # print()


# def printline0(variable):
#     for ix in grid[variable]:
#         print(ix, end=' ')
#     print()

    # printline(0)
    # printline(1)
    # printline(2)
    # printline(3)
    # printline(4)
    # printline(5)
    # printline(6)
    # printline(7)
    # printline(8)

# for iy in range(9):
#     printline0(iy)