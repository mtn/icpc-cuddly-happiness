
def insertQueen(x, y, board):
    for offset in range(-8, 8):
        if (x + offset, y) in board:
            return False
        if (x, y + offset) in board:
            return False
        if (x + offset, y + offset) in board:
            return False
    board.add((x, y))
    return True

board = set()
failed = False

for y in range(8):
    x = input().find("*")
    if not insertQueen(x, y, board):
        failed = True
        break

if failed:
    print("invalid")
else:
    print('valid')
