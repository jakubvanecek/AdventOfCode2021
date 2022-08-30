import numpy as np

with open("Source/SourceDay4", "r") as file:
    lines = file.readlines()

calledNumbers = [int(line) for line in lines[0].split(',')]

print (calledNumbers)


numberOfBoard = (len(lines))//6
print (numberOfBoard)

class Board:
    def __init__(self):
        self.board = np.zeros((5, 5), dtype=int)
        self.marked = np.zeros((5, 5))
        self.winner = 0


    def read_from_lines(self, lines):
        for i in range(5):
            line_entries = [int(entry) for entry in lines[i].split(' ') if entry != '']
            self.board[i] = line_entries

    def markNumber(self, number):
        if number in self.board:
            mark = np.where(self.board == number)
            self.marked[mark[0], mark[1]] = 1

    def checkWinner(self):
        return self.marked.all(axis=0).any() or self.marked.all(axis=1).any()

    def countScore(self, calledNumber):
        return (self.board * (self.marked == 0)).sum() * calledNumber

    def alreadyWinner(self):
        if self.winner > 0:
            return False
        else:
            return True



def letsPay(calledNumbers, numberOfBoards):
    x = 1
    for calledNumber in calledNumbers:
         for board in range(numberOfBoards):
            boards[board].markNumber(calledNumber)
            if boards[board].alreadyWinner():
                if boards[board].checkWinner():
                    boards[board].winner = x
                    x = x + 1
                    if boards[board].winner == 1:
                        resultWinner =f'Winner is board number {board} with last taken number {calledNumber} and score {boards[board].countScore(calledNumber)}'
                    if boards[board].winner == 100:
                        resultLooser =f'Looser is board number {board} with last taken number {calledNumber} and score {boards[board].countScore(calledNumber)}'
    return resultWinner, resultLooser

boards = dict()

for b in range(numberOfBoard):
    boards[b] = Board()
    boards[b].read_from_lines(lines[(b*6+2):(b*6+7)])

resultWinner, resultLooser = letsPay(calledNumbers, numberOfBoard)
print(resultWinner+'\n'+resultLooser)



