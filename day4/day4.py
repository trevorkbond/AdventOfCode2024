WORD = "XMAS"


def read_file(file_name):
    file = open(file_name, "r")
    lines = file.readlines()
    return [line.strip() for line in lines]


class Solution:
    def __init__(self):
        self.puzzle = read_file("input.txt")
        self.num_valid_word_encountered = 0
        self.width = len(self.puzzle[0])
        self.height = len(self.puzzle)
        self.num_x_mas = 0

    def is_in_bounds(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height


    def build_word(self, start_x, start_y, move_x, move_y):
        coordinates = [(start_x, start_y)]
        current_x = start_x
        current_y = start_y
        word = self.puzzle[start_x][start_y]
        for i in range(len(WORD) - 1):
            current_x += move_x
            current_y += move_y
            if not self.is_in_bounds(current_x, current_y):
                continue
            coordinates.append((current_x, current_y))
            word += self.puzzle[current_x][current_y]
        if word == WORD:
            self.num_valid_word_encountered += 1

    def build_words(self, start_x, start_y):
        move_possibilities = [-1, 0, 1]
        for i in range(len(move_possibilities)):
            for j in range(len(move_possibilities)):
                self.build_word(start_x, start_y, move_possibilities[i], move_possibilities[j])

    def find_x_mas(self, start_x, start_y):
        if self.puzzle[start_x][start_y] != "A":
            return
        word_1 = self.puzzle[start_x - 1][start_y - 1] + self.puzzle[start_x][start_y] + self.puzzle[start_x + 1][start_y + 1]
        word_2 = self.puzzle[start_x - 1][start_y + 1] + self.puzzle[start_x][start_y] + self.puzzle[start_x + 1][start_y - 1]
        if (word_1 == "MAS" or word_1 == "SAM") and (word_2 == "MAS" or word_2 == "SAM"):
            self.num_x_mas += 1

    def run(self):
        for i in range(self.width):
            for j in range(self.height):
                self.build_words(i, j)

        print(self.num_valid_word_encountered)

    def run_part2(self):
        for i in range(1, self.width - 1):
            for j in range(1, self.height - 1):
                self.find_x_mas(i, j)

        print(self.num_x_mas)



solution = Solution()
solution.run()
solution.run_part2()
