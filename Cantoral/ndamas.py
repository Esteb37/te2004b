
def isValid(row: int, col: int, positions: list, n: int):

    for row2 in range(n):
        col2 = positions[row2]

        if col2 is not None and (col2 == col or abs(row-row2) == abs(col-col2)):
            return False

    return True


def print_positions(positions: list):
    for col in positions:
        for i in range(n):
            if col == i:
                print("O", end=" ")
            else:
                print("_", end=" ")
        print("\n")

    print("\n----------------\n")


def check(queen: int, positions: list):

    for col in range(n):

        if isValid(queen, col, positions, n):

            positions[queen] = col

            if(queen == n-1):
                print_positions(positions)

            else:
                check(queen + 1, positions)

        if col == n - 1:
            positions[queen] = None


def solve(n: int):
    check(0, [None]*n)


if __name__ == "__main__":
    n = int(input("N: "))
    solve(n)
