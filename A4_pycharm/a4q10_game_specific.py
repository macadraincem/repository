# Michael Angelo C. Adraincem
# 11208422 MCA655
# game_specific.py


class Game(object):
    def __init__(self, board, size, nqueen):
        self.board = board
        self.size = size
        self.nqueen = []

    def __str__(self):
        for x in range(0, self.size):
            for y in range(0, self.size):
                print(self.board[x][y], end=" ")
            print("\n")

    def createBoard(self):
        temp = []
        new = []
        for x in range(0, self.size):
            for y in range(0, self.size):
                new.append("_")
            temp.append(new)
            new = []
        self.board = temp
        return self

    def putQueen(self, x, y):
        if self.board[x][y] == "Q":
            print("A Queen is already in position ", "(", x, ",",  y, ")")
        else:
            self.board[x][y] = "Q"
            self.nqueen.append([x, y])

    def removeQueen(self, x, y):
        self.board[x][y] = "_"
        self.nqueen.remove([x, y])

    def checkHorizontal(self, x, y):
        ctr = 0
        for z in range(0,self.size):
            if self.board[x][z] == "Q":
                ctr = ctr + 1
        if ctr <= 1:
            return True
        else:
            return False

    def checkVertical(self, x, y):
        ctr = 0
        for z in range(0, self.size):
            if self.board[z][y] == "Q":
                ctr = ctr + 1

        if ctr <= 1:
            return True
        else:
            return False

    def checkDiagonal(self, x, y):
        ctr1 = 0
        ctr = 1
        a = x
        b = y
        c = 1
        while ctr1 <= 4:
            if a+c < 4 and b+c < 4:
                if self.board[a+c][b+c] == "Q":
                    ctr = ctr + 1
            if a-c >= 0 and b-c >= 0:
                if self.board[a-c][b-c] == "Q":
                    ctr = ctr + 1
            if a+c < 4 and b-c >= 0:
                if self.board[a+c][b-c] == "Q":
                    ctr = ctr + 1
            if a-c >= 0 and b+c < 4:
                if self.board[a-c][b+c] == "Q":
                    ctr = ctr + 1
            c = c + 1
            ctr1 = ctr1 + 1

        if ctr <= 1:
            return True
        else:
            return False

    def isNqueen(self):
        if len(self.nqueen) != self.size:
            return False

        ctr = 0
        for a in range(0, self.size):
            if self.checkHorizontal(self.nqueen[a][0], self.nqueen[a][1]):
                if self.checkVertical(self.nqueen[a][0], self.nqueen[a][1]):
                    if self.checkDiagonal(self.nqueen[a][0], self.nqueen[a][1]):
                        ctr = ctr + 1

        if ctr == self.size:
            return True
        else:
            return False


def main():
    test = Game("", 5,0)
    test.createBoard()

    test.putQueen(0,0)
    test.putQueen(2,1)
    test.putQueen(4,2)
    test.putQueen(1,3)
    test.putQueen(3,4)
    test.__str__()
    print(test.isNqueen())

main()