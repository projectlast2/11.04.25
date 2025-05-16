import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

from classes import MyClass

class TicTacToe(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("TicTacToe")
        self.setGeometry(100, 100, 300, 300)

        self.grid = QGridLayout()
        self.buttons = [[QPushButton("")for _ in range(3)]for _ in range(3)]
        self.board = [[None for _ in range(3)]for _ in range(3)]


        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(100, 100)
                self.buttons[i][j].setStyleSheet("font-size: 40px")
                self.buttons[i][j].clicked.connect(
                    lambda _, x=i, y =j: self.round(x,y)
                )
                self.grid.addWidget(self.buttons[i][j], i, j)

        self.setLayout(self.grid)

    def round(self, x , y):
        print(x,y)
        if self.board[x][y] is None:
            self.board[x][y]= "X"
        self.buttons[x][y].setText("X")
        self.check_winner("X")

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                #print(f"{player}won")
                return True
        for i in range(3):
            if all(self.board[j][i] == player for j in range(3)):
                #print(f"{player}won")
                return True

        if all(self.board[i][i] == player for i in range(3)) \
            or all(self.board[i][2-i]== player for i in range(3)):
            #print(f"{player}won")
            return True



        return False



    def is_cell_full(self):
            if all(all(cell is not None for cell in row) for row in self.board):
                return True
            else:
                return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
