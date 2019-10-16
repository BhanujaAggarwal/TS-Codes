BOARDSIZE = 8

QUIT = "Q"
LIST = "L"
MOVE = "M"
cmds = [QUIT , LIST , MOVE]

WHITE = "W"
BLACK = "B"
EMPTY = "_"
PLAYERS = [WHITE , BLACK]

class othello :
    def __init__(self,position) :
        row = [EMPTY for _ in range(BOARDSIZE)]
        self.board = [row for _ in range(BOARDSIZE)]
    def get_input(self) :
        self.input = []
        inp = input()
        while inp != QUIT :
            self.input.append(inp)
            inp = input()

    def setup(self) :
        for row,data in enumerate(self, input[:BOARDSIZE]) :
            for col,state in enumerate(data) :
                if state in PLAYERS :
                    self.board[row][col] = state
        self.input = self.input[BOARDSIZE:]
        self.player = self.input[0]
        self.other = WHITE if self.player == BLACK else BLACK
        self.input = self.input[1:]
    def process_command(self , commmand) :
        if commmand[0] == LIST :
            self.list_moves()
        elif commmand[0] == MOVE :
            self.move(commmand[1:])

    def list_moves(self) :
