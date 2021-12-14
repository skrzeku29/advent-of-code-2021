def gen_array_of_data():
    with open("data.txt") as data:
        data = list(filter(len, data.read().split("\n")))

    return data


class Board:
    def __init__(self, values_array):
        self.values_array = values_array
        self.winner = False

    def check_score(self):
        for i in range(len(self.values_array)):
            if self.values_array[i] == '1000' and self.values_array[i][1] == '1000' and self.values_array[i][2] == '1000' and self.values_array[i][3] == '1000' and self.values_array[i][4] == '1000':
                self.winner = True

        for j in range(5):
            if self.values_array[0][j] == '1000' and self.values_array[1][j] == '1000' and self.values_array[2][j] == '1000' and self.values_array[3][j] == '1000' and self.values_array[4][j] == '1000':
                self.winner = True

    def add_number_to_board(self, num):
        for i in range(len(self.values_array)):
            for j in range(len(self.values_array)):
                if int(self.values_array[i][j]) == int(num):
                    self.values_array[i][j] = "1000"
    
    def calculate_remaining(self, num):
        total=0
        for i in range(len(self.values_array)):
            for j in range(len(self.values_array)):
                if int(self.values_array[i][j]) != 1000:
                    total+=int(self.values_array[i][j])
        return total*int(num)

def run_the_game(dib_array, boards):
    for dib in dib_array:
        for board in boards:
            board.add_number_to_board(dib)
        for board in boards:
            board.check_score()
            if board.winner:
                return board.calculate_remaining(dib)

    return "no bingo :("

def run_the_game_until_last(dib_array, boards):
    last_winner = Board(None)
    for dib in dib_array:
        for board in boards:
            board.add_number_to_board(dib)
        for board in boards:
            board.check_score()
            if not board.winner:
                last_winner = board
        if all(board.winner == True for board in boards):
            return last_winner.calculate_remaining(dib)
    return "no bingo :("

data = gen_array_of_data()

dib_array = data[0].split(",")


chunks = []
boards = []

for chunk in data[1:]:
    chunks.append(list(filter(None, chunk.split(' '))))

for i in range(0, len(chunks), 5):
    boards.append(Board(chunks[i:i+5]))


print("part1: "+str(run_the_game(dib_array, boards)))
print("part2: "+str(run_the_game_until_last(dib_array, boards)))